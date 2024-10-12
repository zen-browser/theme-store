import os
import json
from submit_theme import convert_legacy_preferences

THEMES_FOLDER = "./themes"
THEMES_DATA_FILE = "./themes.json"


def get_color_css_variable(color):
    if color == "primaryColor":
        return "--zen-colors-primary"
    if color == "secondaryColor":
        return "--zen-colors-secondary"
    if color == "tertiaryColor":
        return "--zen-colors-tertiary"
    if color == "colorsBorder":
        return "--zen-colors-border"
    if color == "dialogBg":
        return "--zen-dialog-background"
    if color == "accentColor":
        return "--zen-primary-color"
    print(f"Unknown color: {color}")
    exit(1)


def write_colors(colors_file, output_file):
    with open(colors_file, "r") as f:
        colors = json.load(f)

        with open(output_file, "w") as f:
            f.write("/* This is an auto generated color theme. */\n")
            f.write(":root {\n")

            for color in colors:
                if color == "isDarkMode":
                    continue
                f.write(
                    f"    {get_color_css_variable(color)}: {colors[color]} !important;\n"
                )

            f.write("}\n")
        return colors


def main():
    with open(THEMES_DATA_FILE, "w") as f:
        json.dump({}, f, indent=4)
    for theme in os.listdir(THEMES_FOLDER):
        theme_folder = os.path.join(THEMES_FOLDER, theme)

        if not os.path.isdir(theme_folder):
            continue

        theme_data_file = os.path.join(theme_folder, "theme.json")

        if not os.path.exists(theme_data_file):
            continue

        with open(theme_data_file, "r") as f:
            theme_data = json.load(f)

            with open(theme_data_file, "w") as f:
                json.dump(theme_data, f, indent=4)  # format the json file

            with open(THEMES_DATA_FILE, "r") as f:
                themes_data = json.load(f)
                theme_colors_file = os.path.join(theme_folder, "colors.json")

                if os.path.exists(theme_colors_file):
                    print(f"  Found colors.json in theme: {theme}")

                    theme_colors_output = os.path.join(theme_folder, "chrome.css")
                    colors = write_colors(theme_colors_file, theme_colors_output)

                    if "tags" not in theme_data:
                        theme_data["tags"] = []

                    # Add 'color theme' tag if colors.json is present
                    theme_data["tags"].append("color theme")

                    # Add 'dark' tag if colors.json specifies dark mode
                    if "isDarkMode" in colors and colors["isDarkMode"]:
                        theme_data["tags"].append("dark")
                        
                themes_data[theme] = theme_data

                with open(THEMES_DATA_FILE, "w") as f:
                    json.dump(themes_data, f)
                    del themes_data

            preferences_data_file = os.path.join(theme_folder, "preferences.json")

            if os.path.exists(preferences_data_file):
                print(f"Found preferences.json in theme: {theme}")

                with open(preferences_data_file, "r") as f:
                    preferences_data = json.load(f)

                    if isinstance(preferences_data, dict):
                        print(
                            "Legacy preferences found, performing transformation into new structure."
                        )
                        preferences_data = convert_legacy_preferences(preferences_data)

                    with open(preferences_data_file, "w") as f:
                        json.dump(preferences_data, f, indent=4)
                        del preferences_data

        print(f"Rebuilt theme: {theme}")
    print("Rebuilt all themes!")


if __name__ == "__main__":
    main()