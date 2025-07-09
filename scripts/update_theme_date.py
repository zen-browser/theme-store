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

    # Load the theme JSON data with single file operation
    try:
        with open(theme_file, "r") as f:
            theme_data = json.load(f)
    except json.JSONDecodeError as e:
        panic("Error reading theme.json: " + str(e))
    
    # Get the current date once and reuse
    current_date = time.strftime("%Y-%m-%d")
    
    # Combine checks and updates for efficiency
    updates_made = False
    if "createdAt" not in theme_data:
        theme_data["createdAt"] = current_date
        print(f"Set `createdAt` for {theme_path} to {theme_data['createdAt']}")
        updates_made = True

    if theme_data.get("updatedAt") != current_date:
        theme_data["updatedAt"] = current_date
        print(f"Updated `updatedAt` for {theme_path} to {theme_data['updatedAt']}")
        updates_made = True
    
    if "tags" not in theme_data:
        theme_data["tags"] = []
        print(f"Initialized `tags` for {theme_path} as an empty list")
        updates_made = True

    # Write changes only if modifications were made
    if updates_made:
        with open(theme_file, "w") as f:
            json.dump(theme_data, f, indent=4)
        print(f"Updated `updatedAt` for {theme_path} to {theme_data['updatedAt']}")

if __name__ == "__main__":
    # Make sure the script is run with the theme path as an argument
    if len(sys.argv) != 2:
        panic("Usage: update_theme_date.py <path_to_theme_directory>")

    theme_path = sys.argv[1]
    update_theme_date(theme_path)
