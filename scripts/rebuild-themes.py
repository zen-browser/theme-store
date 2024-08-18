
import os
import json

THEMES_FOLDER = './themes'
THEMES_DATA_FILE = './themes.json'

def main():
    with open(THEMES_DATA_FILE, 'w') as f:
        json.dump({}, f, indent=4)
    for theme in os.listdir(THEMES_FOLDER):
        theme_folder = os.path.join(THEMES_FOLDER, theme)
        if not os.path.isdir(theme_folder):
            continue
        theme_data_file = os.path.join(theme_folder, 'theme.json')
        if not os.path.exists(theme_data_file):
            continue
        with open(theme_data_file, 'r') as f:
            theme_data = json.load(f)
            with open(THEMES_DATA_FILE, 'r') as f:
                themes_data = json.load(f)
                themes_data[theme] = theme_data
                with open(THEMES_DATA_FILE, 'w') as f:
                    json.dump(themes_data, f, indent=4)
        print(f"Rebuilt theme: {theme}")
    print("Rebuilt all themes!")
  
if __name__ == '__main__':
    main()
