
def ensure_packages_have_version(theme_data):
    if theme_data.get('version', None) is None:
        print("  Version is required in theme.json. Adding default value of 1.0.0.")
        theme_data['version'] = '1.0.0'
    return theme_data
