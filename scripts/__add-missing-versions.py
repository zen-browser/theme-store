import os
import json

if __name__ == "__main__":
    for themeId in os.listdir("themes"):
        themeFolder = os.path.join("themes", themeId)
        if not os.path.isdir(themeFolder):
            continue
        themeDataFile = os.path.join(themeFolder, "theme.json")
        if not os.path.exists(themeDataFile):
            continue
        with open(themeDataFile, "r") as f:
            themeData = json.load(f)
            if "version" not in themeData:
                themeData["version"] = "1.0.0"
            with open(themeDataFile, "w") as f:
                json.dump(themeData, f, indent=4)
        print(f"Added version to theme: {themeId}")
