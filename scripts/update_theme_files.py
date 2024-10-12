import os
import json

# Define the paths for the themes folder and the themes data file.
THEMES_FOLDER = "./themes"
THEMES_DATA_FILE = "./themes.json"

def main():
    # Load the themes data from the themes.json file
    with open(THEMES_DATA_FILE, "r") as f:
        themes_data = json.load(f)

    # Iterate through each theme directory in the themes folder
    for theme, theme_data in themes_data.items():
        theme_folder = os.path.join(THEMES_FOLDER, theme)
        theme_data_file = os.path.join(theme_folder, "theme.json")

        if not os.path.isdir(theme_folder):
            print(f"Skipping '{theme}': not a directory.")
            continue  # Skip if not a directory

        # Ensure the theme.json file exists
        if not os.path.exists(theme_data_file):
            print(f"Creating theme.json for '{theme}'.")
            # Create an empty theme.json if it does not exist
            with open(theme_data_file, "w") as f:
                json.dump({}, f, indent=4)

        # Open and write data to theme.json
        with open(theme_data_file, "w") as f:
            json.dump(theme_data, f, indent=4)  # Write the theme data to theme.json

        print(f"Updated theme.json for '{theme}'.")  # Log update for the theme

    print("Updated all theme.json files!")  # Final log message

if __name__ == "__main__":
    main()  # Entry point of the script