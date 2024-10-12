import json
import time
import os
import sys


def panic(message: str):
    print(message, file=sys.stderr)
    exit(1)


def update_theme_date(theme_path):
    theme_file = os.path.join(theme_path, "theme.json")

    if not os.path.exists(theme_file):
        panic(f"{theme_file} not found.")

    # Load the theme JSON data
    with open(theme_file, "r") as f:
        try:
            theme_data = json.load(f)
        except json.JSONDecodeError as e:
            panic("Error reading theme.json: " + str(e))

    # Update the `updatedAt` field to the current date
    theme_data["updatedAt"] = time.strftime("%Y-%m-%d")

    # Write the changes back to theme.json
    with open(theme_file, "w") as f:
        json.dump(theme_data, f, indent=2)

    print(f"Updated `updatedAt` for {theme_path} to {theme_data['updatedAt']}")


if __name__ == "__main__":
    # Make sure the script is run with the theme path as an argument
    if len(sys.argv) != 2:
        panic("Usage: update_theme_date.py <path_to_theme_directory>")

    theme_path = sys.argv[1]
    update_theme_date(theme_path)