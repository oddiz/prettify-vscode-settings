# Prettify VSCode Settings

This script sorts and categorizes settings in a `settings.json` file, which is often used for configuration in applications like Visual Studio Code. The script uses `pyjson5` to handle JSONC (JSON with comments) and supports customization of the output file path.

## Features

- Sorts settings based on predefined default and important categories.
- Categorizes settings under uppercase category comments.
- Places extension settings at the end of the document.
- Outputs a single JSONC document enclosed in brackets, preserving comments.

## Requirements

To run this script, you'll need Python installed on your system as well as the `pyjson5` package, which can be installed using `pip`:

`pip install pyjson5`

## Usage

**Please avoid directly outputting into settings.json, instead create a new file and copy the contents over to be safe.**

Run the script with the following command-line arguments:

`python prettify_settings.py <input_path> [output_path]`

- `<input_path>`: The path to the `settings.json` file you want to prettify.
- `[output_path]`: (Optional) The path where the prettified settings file will be saved. If omitted, the script will create a file named `prettified.settings.jsonc` in the current directory.

You can customize the category order by modifying `DEFAULT_ORDER` variable in the script. The default order is opinionated and as follows:

```python
DEFAULT_ORDER = ['editor', 'workbench', 'window', 'files', 'terminal', 'github', 'git', 'security', 'python', 'typescript', 'javascript']
```

### Example

Unmodified settings.json

```jsonc
{
  "workbench.list.mouseWheelScrollSensitivity": 3,

  "css.validate": false,
  "scss.validate": false,
  "less.validate": false,

  "git.enableSmartCommit": true,
  "git.autofetch": true,
  "git.confirmSync": false,

  "editor.minimap.enabled": true,
  "editor.wordWrap": "on",
  "editor.suggestSelection": "first",
  "editor.linkedEditing": true,
  "typescript.updateImportsOnFileMove.enabled": "always",

  "javascript.updateImportsOnFileMove.enabled": "always",
  "javascript.format.insertSpaceAfterOpeningAndBeforeClosingNonemptyBrackets": true,

  "python.languageServer": "Pylance",
  "editor.stickyScroll.enabled": true,
  "editor.cursorSurroundingLines": 16,
  "terminal.integrated.smoothScrolling": true,
  "editor.stablePeek": true,
  "editor.formatOnSave": true,

  "javascript.format.insertSpaceBeforeFunctionParenthesis": true,
  "prettier.useEditorConfig": false,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "githubRepositories.autoFetch.enabled": false,
  "npm.packageManager": "yarn",
  "typescript.preferences.preferTypeOnlyAutoImports": true,
  "typescript.referencesCodeLens.enabled": true,
  "emmet.showExpandedAbbreviation": "never",
  "javascript.suggest.classMemberSnippets.enabled": false
}
```

Prettified settings.json

```jsonc
{
  //********** EDITOR SETTINGS ***********//

  "editor.cursorSurroundingLines": 16,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "editor.linkedEditing": true,
  "editor.minimap.enabled": true,
  "editor.stablePeek": true,
  "editor.stickyScroll.enabled": true,
  "editor.suggestSelection": "first",
  "editor.wordWrap": "on",

  //********** WORKBENCH SETTINGS ***********//

  "workbench.list.mouseWheelScrollSensitivity": 3,

  //********** TERMINAL SETTINGS ***********//

  "terminal.integrated.smoothScrolling": true,

  //********** GIT SETTINGS ***********//

  "git.autofetch": true,
  "git.confirmSync": false,
  "git.enableSmartCommit": true,

  //********** PYTHON SETTINGS ***********//

  "python.languageServer": "Pylance",

  //********** TYPESCRIPT SETTINGS ***********//

  "typescript.preferences.preferTypeOnlyAutoImports": true,
  "typescript.referencesCodeLens.enabled": true,
  "typescript.updateImportsOnFileMove.enabled": "always",

  //********** JAVASCRIPT SETTINGS ***********//

  "javascript.format.insertSpaceAfterOpeningAndBeforeClosingNonemptyBrackets": true,
  "javascript.format.insertSpaceBeforeFunctionParenthesis": true,
  "javascript.suggest.classMemberSnippets.enabled": false,
  "javascript.updateImportsOnFileMove.enabled": "always",

  //********** CSS SETTINGS ***********//

  "css.validate": false,

  //********** EMMET SETTINGS ***********//

  "emmet.showExpandedAbbreviation": "never",

  //********** GITHUBREPOSITORIES SETTINGS ***********//

  "githubRepositories.autoFetch.enabled": false,

  //********** LESS SETTINGS ***********//

  "less.validate": false,

  //********** NPM SETTINGS ***********//

  "npm.packageManager": "yarn",

  //********** PRETTIER SETTINGS ***********//

  "prettier.useEditorConfig": false,

  //********** SCSS SETTINGS ***********//

  "scss.validate": false
}

```

## Contributing

If you'd like to contribute to this project, please feel free to submit a pull request or open an issue to discuss potential changes or improvements.
