import pyjson5 as json5  
import json
from collections import defaultdict
import argparse
import pathlib
import os

# Parse arguments
parser = argparse.ArgumentParser(description='Sort and categorize VS Code settings.json file')
parser.add_argument('settings_json_path', type=str, help='Path to settings.json file')
parser.add_argument('output_json_path', nargs="?", type=str, help='Path to output file', default=None)
args = parser.parse_args()
# if no output path is specified, create a file prettified.originalfilename in current directory

# Define the order for default and important settings
DEFAULT_ORDER = ['editor', 'workbench', 'window', 'files', 'terminal', 'github', 'git', 'security', 'python', 'typescript', 'javascript']

output_path = args.output_json_path if args.output_json_path else os.path.join(os.getcwd(), "prettified." + pathlib.Path(args.settings_json_path).name +"c")


def sort_and_categorize_settings(settings_json_path, output_json_path):
    # Read the settings.json file using pyjson5
    with open(settings_json_path, 'r') as file:
        settings = json5.load(file)

    # Categorize settings by the first part of the key (before the first dot)
    categorized_settings = defaultdict(dict)
    for key, value in settings.items():
        category = key.split('.')[0]
        categorized_settings[category][key] = value



    # Sort the categories based on the predefined order and place extension settings at the end
    sorted_categorized_settings = {}
    for category in DEFAULT_ORDER:
        if category in categorized_settings:
            sorted_categorized_settings[category] = dict(sorted(categorized_settings.pop(category).items()))
    
    # Sort remaining categories alphabetically, except 'extensions' which goes last
    remaining_categories = sorted((k for k in categorized_settings.keys() if k != 'extensions'))
    for category in remaining_categories:
        sorted_categorized_settings[category] = dict(sorted(categorized_settings[category].items()))

    # Finally, add 'extensions' category if it exists
    if 'extensions' in categorized_settings:
        sorted_categorized_settings['extensions'] = dict(sorted(categorized_settings['extensions'].items()))

    # Write the categorized and sorted settings back to the file with annotations
    with open(output_json_path, 'w') as file:
        file.write('{\n')  # Start of the JSON object

        # Write settings with comments
        first = True
        for category, settings in sorted_categorized_settings.items():
            if not first:
                file.write('\n')
            first = False
            # Write the category comment in uppercase
            file.write(f"  //********** {category.upper()} SETTINGS ***********//\n")
            file.write('\n')
            for key, value in settings.items():
                json_str = json.dumps({key: value}, indent=2)[1:-1].strip()
                file.write(f"  {json_str},\n")

        file.write('}\n')  # End of the JSON object


def main():
  sort_and_categorize_settings(args.settings_json_path, output_path)
  
if __name__ == "__main__":
  main()