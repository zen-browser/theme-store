
import os
import argparse
import json
import uuid
import sys
import requests
import imghdr

STYLES_FILE = "chrome.css"
README_FILE = "readme.md"
IMAGE_FILE = "image.png"
PREFERENCES_FILE = "preferences.json"

TEMPLATE_STYLES_FILE = "./theme-styles.css"
TEMPLATE_README_FILE = "./theme-readme.md"
TEMPLATE_PREFERENCES_FILE = "./theme-preferences.json"

def create_theme_id():
    return str(uuid.uuid4())

def get_static_asset(theme_id, asset):
    return f"https://raw.githubusercontent.com/zen-browser/theme-store/main/themes/{theme_id}/{asset}"

def get_styles():
    with open(TEMPLATE_STYLES_FILE, 'r') as f:
        content = f.read()
        content = content[len("```css"):]
        content = content[:-len("```")]
        return content
    
def get_readme():
    with open(TEMPLATE_README_FILE, 'r') as f:
        content = f.read()
        content = content[len("```markdown"):]
        content = content[:-len("```")]
        return content
    
def validate_preferences(preferences):
    for key, value in preferences.items():
        if not isinstance(key, str):
            print("Preference key must be a string.", file=sys.stderr)
            exit(1)
        if not isinstance(value, str):
            print("Preference description must be a string.", file=sys.stderr)
            exit(1)
        if len(key) == 0:
            print("Preference key is required.", file=sys.stderr)
            exit(1)
        for char in key:
            if not char.isalnum() and char != '.' and char != '-' and char != '_':
                print("Preference key must only contain letters, numbers, periods, dashes, and underscores.", file=sys.stderr)
                exit(1)
        if len(value) == 0:
            print("Preference description is required.", file=sys.stderr)
            exit(1)
    return preferences

def get_preferences():
    with open(TEMPLATE_PREFERENCES_FILE, 'r') as f:
        try:
            content = f.read()
            if content.strip() == "":
                return {}
            content = content[len("```json"):]
            content = content[:-len("```")]
            return validate_preferences(json.loads(content))
        except json.JSONDecodeError as e:
            print("Preferences file is invalid.", file=sys.stderr)
            print(e, file=sys.stderr)
            exit(1)

def validate_name(name):
    if len(name) == 0:
        print("Name is required.", file=sys.stderr)
        exit(1)
    if len(name) > 20:
        print("Name must be less than 50 characters.", file=sys.stderr)
        exit(1)
    for char in name:
        if not char.isalnum() and char != ' ':
            print("Name must only contain letters, numbers, and spaces.", file=sys.stderr)
            exit(1)
  
def validate_description(description):
    if len(description) == 0:
        print("Description is required.", file=sys.stderr)
        exit(1)
    if len(description) > 120:
        print("Description must be less than 100 characters.", file=sys.stderr)
        exit(1)

def download_image(image_url, image_path):
    response = requests.get(image_url)
    if response.status_code != 200:
        print("Image URL is invalid.", file=sys.stderr)
        exit(1)
    with open(image_path, 'wb') as f:
        f.write(response.content)
    # Check if the image is valid and a PNG
    if imghdr.what(image_path) != 'png':
        print("Image must be a PNG.", file=sys.stderr)
        exit(1)

def main():
    parser = argparse.ArgumentParser(description='Submit a theme to the theme repo.')
    parser.add_argument('--name', type=str, help='The theme to submit.')
    parser.add_argument('--description', type=str, help='The description of the theme.')
    parser.add_argument('--homepage', type=str, help='The homepage of the theme.')
    parser.add_argument('--author', type=str, help='The author of the theme.')
    parser.add_argument('--image', type=str, help='The image of the theme.')
    args = parser.parse_args()

    name = args.name
    description = args.description
    homepage = args.homepage
    author = args.author
    image = args.image

    validate_name(name)
    validate_description(description)

    theme_id = create_theme_id()

    print("""
Welcome to the Zen Browser Theme Store!

Please review the information below before submitting your theme. Also... Why are you here?
          
This action is only for theme reviewers. If you are a theme developer, please use the theme store.
Just joking, you can do whatever you want. You're the boss.  
    """)

    theme = {
        'id': theme_id,
        'name': name,
        'description': description,
        'homepage': homepage,
        'style': get_static_asset(theme_id, STYLES_FILE),
        'readme': get_static_asset(theme_id, README_FILE),
        'image': get_static_asset(theme_id, IMAGE_FILE),
        'author': author
    }

    os.makedirs(f"themes/{theme_id}")

    with open(f"themes/{theme_id}/{STYLES_FILE}", 'w') as f:
        f.write(get_styles())

    with open(f"themes/{theme_id}/{README_FILE}", 'w') as f:
        f.write(get_readme())

    with open(f"themes/{theme_id}/{PREFERENCES_FILE}", 'w') as f:
        prefs = get_preferences()
        if len(prefs) > 0:
            print("Detected preferences file. Please review the preferences below.")
            print(prefs)
            theme['preferences'] = get_static_asset(theme_id, PREFERENCES_FILE)
            json.dump(prefs, f)

    download_image(image, f"themes/{theme_id}/{IMAGE_FILE}")

    with open(f"themes/{theme_id}/theme.json", 'w') as f:
        json.dump(theme, f)

    print(f"Theme submitted with ID: {theme_id}")
    for key, value in theme.items():
        print(f"\t{key}: {value}")

if __name__ == '__main__':
    main()
