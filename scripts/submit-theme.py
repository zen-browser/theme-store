
import os
import argparse
import json
import uuid

STYLES_FILE = "chrome.css"
README_FILE = "readme.md"

def create_theme_id():
    return str(uuid.uuid4())

def get_static_asset(theme_id, asset):
    return f"https://raw.githubusercontent.com/zen-browser/theme-store/main/themes/{theme_id}/{asset}"

def main():
    parser = argparse.ArgumentParser(description='Submit a theme to the theme repo.')
    parser.add_argument('name', type=str, help='The theme to submit.')
    parser.add_argument('description', type=str, help='The description of the theme.')
    parser.add_argument('homepage', type=str, help='The homepage of the theme.')
    parser.add_argument('style', type=str, help='The style of the theme.')
    parser.add_argument('readme', type=str, help='The README of the theme.')
    parser.add_argument('author', type=str, help='The author of the theme.')
    args = parser.parse_args()

    name = args.name
    description = args.description
    homepage = args.homepage
    style = args.style
    readme = args.readme
    author = args.author

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
        'author': author
    }

    os.makedirs(f"themes/{theme_id}")
    with open(f"themes/{theme_id}/theme.json", 'w') as f:
        json.dump(theme, f)

    with open(f"themes/{theme_id}/{STYLES_FILE}", 'w') as f:
        f.write(style)

    with open(f"themes/{theme_id}/{README_FILE}", 'w') as f:
        f.write(readme)

    print(f"Theme submitted with ID: {theme_id}")
    for key, value in theme.items():
        print(f"\t{key}: {value}")

if __name__ == '__main__':
    main()
