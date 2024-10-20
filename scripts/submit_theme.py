import os
import re
import argparse
import json
import time
import uuid
import sys
import requests
import urllib.parse
from enum import StrEnum


class PreferenceFields(StrEnum):
    PROPERTY = "property"
    LABEL = "label"
    TYPE = "type"
    OPTIONS = "options"
    DEFAULT_VALUE = "defaultValue"
    DISABLED_ON = "disabledOn"
    PLACEHOLDER = "placeholder"


class PreferenceTypes(StrEnum):
    CHECKBOX = "checkbox"
    DROPDOWN = "dropdown"
    STRING = "string"

    def valid_types(self) -> list[type]:
        match self:
            case self.CHECKBOX:
                return [bool]

            case self.DROPDOWN:
                return [str, int, float]

            case self.STRING:
                return [str]


STYLES_FILE = "chrome.css"
COLORS_FILE = "colors.json"
README_FILE = "readme.md"
IMAGE_FILE = "image.png"
PREFERENCES_FILE = "preferences.json"

TEMPLATE_STYLES_FILE = "./theme-styles.css"
TEMPLATE_README_FILE = "./theme-readme.md"
TEMPLATE_PREFERENCES_FILE = "./theme-preferences.json"

VALID_OS = set(["linux", "macos", "windows"])
PLACEHOLDER_TYPES = [PreferenceTypes.DROPDOWN, PreferenceTypes.STRING]
REQUIRED_FIELDS = set(
    [PreferenceFields.PROPERTY, PreferenceFields.LABEL, PreferenceFields.TYPE]
)


def panic(string: str, error=None):
    print(string, file=sys.stderr)

    if error:
        print(error, file=sys.stderr)

    exit(1)


def create_theme_id():
    return str(uuid.uuid4())


def get_static_asset(theme_id, asset):
    return f"https://raw.githubusercontent.com/zen-browser/theme-store/main/themes/{theme_id}/{asset}"


def get_styles(is_color_theme, theme_id):
    with open(TEMPLATE_STYLES_FILE, "r") as f:
        content = f.read()
        content = content[len("```css") :]
        content = content[: -len("```")]

        # we actually have a JSON file here that needs to be generated
        if is_color_theme:
            with open(f"themes/{theme_id}/{COLORS_FILE}", "w") as f:
                json.dump(json.loads(content), f, indent=4)
            return "/* This is a color theme. */"
        return content


def get_readme():
    with open(TEMPLATE_README_FILE, "r") as f:
        content = f.read()
        content = content[len("```markdown") :]
        content = content[: -len("```")]
        return content


def validate_url(url, allow_empty=False):
    if allow_empty and len(url) == 0:
        return
    try:
        result = urllib.parse.urlparse(url)
        if result.scheme != "https":
            panic("URL must be HTTPS.")
    except Exception as e:
        panic("URL is invalid.", e)


def get_enum_error(value, Enum: StrEnum):
    return f"Field must be one of {', '.join(Enum._value2member_map_)} but received \"{value}\""


def parse_field_to_enum(key: tuple[str, any]) -> tuple[PreferenceFields, any]:
    try:
        converted_key = re.sub(r"(?<!^)(?=[A-Z])", "_", key[0]).upper()
        return (PreferenceFields[converted_key], key[1])
    except:
        panic(key[0], PreferenceFields)
        exit(1)


def parse_type(value: str) -> PreferenceTypes:
    try:
        converted_value = re.sub(r"(?<!^)(?=[A-Z])", "_", value).upper()
        return PreferenceTypes[converted_value]
    except:
        panic(get_enum_error(value, PreferenceTypes))


def check_value_type(value, arr_types: list[type]):
    return type(value) in arr_types


def is_value_in_enum(value, Enum: StrEnum) -> bool:
    try:
        Enum[value.upper()]

        return True
    except:
        return False


def is_empty_str(value: str) -> bool:
    return not isinstance(value, str) or len(value) == 0


def validate_preferences(preferences):
    for entry in preferences:
        properties = dict(
            map(
                lambda key: parse_field_to_enum(key),
                entry.items(),
            )
        )

        if not len(set(properties).intersection(REQUIRED_FIELDS)) == len(
            REQUIRED_FIELDS
        ):
            panic(f"Required fields ({", ".join(REQUIRED_FIELDS)}) are not in {entry}.")

        current_type = parse_type(properties[PreferenceFields.TYPE])
        valid_type_list = current_type.valid_types()
        current_property = properties[PreferenceFields.PROPERTY]

        for key, value in properties.items():
            match key:
                case PreferenceFields.PROPERTY:
                    if is_empty_str(value) or re.search(r"[^A-z0-9\-_.]", value):
                        panic(
                            f"Property must only contain letters, numbers, periods, dashes, and underscores. Received {current_property}"
                        )

                case PreferenceFields.LABEL:
                    if not isinstance(value, str) or len(value) == 0:
                        panic(f"Label for {current_property} is required.")

                case PreferenceFields.TYPE:
                    if not isinstance(value, str) or len(value) == 0:
                        panic(f"Type in {current_property} is required.")
                    elif not is_value_in_enum(value, PreferenceTypes):
                        panic(get_enum_error(value, PreferenceTypes))

                case PreferenceFields.OPTIONS:
                    if current_type != PreferenceTypes.DROPDOWN:
                        panic("Dropdown type is required for property options")
                    elif not isinstance(value, list) or len(value) == 0:
                        panic(f"Options in {current_property} cannot be empty")
                    else:
                        for option in value:
                            option_label = option.get("label")
                            option_value = option.get("value")

                            if is_empty_str(option_label):
                                panic(
                                    f"Label for option in {current_property} is required."
                                )

                            if not check_value_type(option_value, valid_type_list):
                                panic(
                                    f"Option {option_label} in {current_property} was expecting value of any type in {", ".join(map(lambda type: type.__name__, valid_type_list))}, but received {type(option_value).__name__}"
                                )

                case PreferenceFields.DEFAULT_VALUE:
                    if not check_value_type(value, valid_type_list):
                        panic(
                            f"Field defaultValue in {current_property} was expecting value with any type in {", ".join(map(lambda type: type.__name__, valid_type_list))} but received {value}"
                        )

                case PreferenceFields.DISABLED_ON:
                    if not isinstance(value, list):
                        panic(
                            f"Field disabledOn in {current_property} is expecting an array"
                        )
                    elif len(value) != 0:
                        for possibleOs in value:
                            if possibleOs not in VALID_OS:
                                panic(
                                    f"Field disabledOn in {current_property} is expecting one or more of {", ".join(VALID_OS)} but received {possibleOs}"
                                )

                case PreferenceFields.PLACEHOLDER:
                    if not current_type in PLACEHOLDER_TYPES:
                        panic(
                            f"Placeholder in {current_property} can only be used for types {", ".join(PLACEHOLDER_TYPES)}"
                        )

                case _:
                    panic("This should be unreachable.")

    return preferences


def convert_legacy_preferences(preferences):
    key_regex = re.compile(r"(!?)(?:(macos|windows|linux):)?([A-z0-9-_.]+)")
    new_preferences = []
    for key, label in preferences.items():
        negated, osValue, property = key_regex.search(key).groups()

        disabledOn = []

        if negated == "!" and osValue:
            disabledOn = [osValue]
        elif osValue:
            disabledOn = [i for i in VALID_OS if i != osValue]

        new_preferences.append(
            dict(
                [
                    ("property", property),
                    ("label", label),
                    ("type", "checkbox"),
                    ("disabledOn", disabledOn),
                ]
            )
        )

    return new_preferences


def get_preferences():
    with open(TEMPLATE_PREFERENCES_FILE, "r") as f:
        try:
            content = f.read()
            if content.strip() == "":
                return {}
            content = re.sub(r"```json\n*", "", content)
            content = re.sub(r"\n*```\n*", "", content)

            if content.startswith("{") and content.endswith("}"):
                print(
                    "Warning: Detected legacy preferences syntax, converting them into new syntax"
                )
                content = convert_legacy_preferences(json.loads(content))
            else:
                content = json.loads(content)

            return validate_preferences(content)
        except json.JSONDecodeError as e:
            panic("Preferences file is invalid.", e)


def validate_name(name):
    if len(name) == 0:
        panic("Name is required.")
    if len(name) > 25:
        panic("Name must be less than 25 characters.")
    for char in name:
        if not char.isalnum() and char != " ":
            panic("Name must only contain letters, numbers, and spaces.")


def validate_description(description):
    if len(description) == 0:
        panic("Description is required.")
    if len(description) > 120:
        panic("Description must be less than 100 characters.")


def download_image(image_url, image_path):
    response = requests.get(image_url, headers={"User-Agent": "Epicture"})
    if response.status_code != 200:
        panic("Image URL is invalid.")
    # Check if the image is valid and a PNG
    if response.headers["Content-Type"] != "image/png":
        panic("Image must be a PNG.")
    with open(image_path, "wb") as f:
        f.write(response.content)


def main():
    parser = argparse.ArgumentParser(description="Submit a theme to the theme repo.")
    parser.add_argument("--name", type=str, help="The theme to submit.")
    parser.add_argument("--description", type=str, help="The description of the theme.")
    parser.add_argument("--homepage", type=str, help="The homepage of the theme.")
    parser.add_argument("--author", type=str, help="The author of the theme.")
    parser.add_argument("--image", type=str, help="The image of the theme.")
    parser.add_argument(
        "--is-color-theme", type=str, help="Whether the theme is a color theme."
    )
    args = parser.parse_args()

    name = args.name
    description = args.description
    homepage = args.homepage
    author = args.author
    image = args.image
    is_color_theme = args.is_color_theme == "true"

    validate_name(name)
    validate_description(description)

    validate_url(image)
    validate_url(homepage, allow_empty=True)

    theme_id = create_theme_id()

    print(
        """
Welcome to the Zen Browser Theme Store!

Please review the information below before submitting your theme. Also... Why are you here?

This action is only for theme reviewers. If you are a theme developer, please use the theme store.
Just joking, you can do whatever you want. You're the boss.
    """
    )

    theme = {
        "id": theme_id,
        "name": name,
        "description": description,
        "homepage": homepage,
        "style": get_static_asset(theme_id, STYLES_FILE),
        "readme": get_static_asset(theme_id, README_FILE),
        "image": get_static_asset(theme_id, IMAGE_FILE),
        "author": author,
        "version": "1.0.0",
        "tags": [],
        "createdAt": time.strftime("%Y-%m-%d"),
        "updatedAt": time.strftime("%Y-%m-%d"),
    }

    os.makedirs(f"themes/{theme_id}")

    with open(f"themes/{theme_id}/{STYLES_FILE}", "w") as f:
        f.write(get_styles(is_color_theme, theme_id))

    with open(f"themes/{theme_id}/{README_FILE}", "w") as f:
        f.write(get_readme())

    if os.path.exists(TEMPLATE_PREFERENCES_FILE):
        if is_color_theme:
            panic("Color themes do not support preferences.")
        prefs_file = f"themes/{theme_id}/{PREFERENCES_FILE}"
        with open(prefs_file, "w") as f:
            prefs = get_preferences()
            if len(prefs) > 0:
                print("Detected preferences file. Please review the preferences below.")
                print(prefs)
                theme["preferences"] = get_static_asset(theme_id, PREFERENCES_FILE)
                json.dump(prefs, f, indent=4)
            else:
                print("No preferences detected.")
                os.remove(prefs_file)

    download_image(image, f"themes/{theme_id}/{IMAGE_FILE}")

    with open(f"themes/{theme_id}/theme.json", "w") as f:
        json.dump(theme, f, indent=4)

    print(f"Theme submitted with ID: {theme_id}")
    for key, value in theme.items():
        print(f"\t{key}: {value}")


if __name__ == "__main__":
    main()