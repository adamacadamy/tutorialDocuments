  
### Windows File System, CMD and VSCode
## 1. File System Structure

- **Drive Letters:** Represent storage volumes (e.g., `C:`, `D:`).

- **Directories (Folders):** Organize files hierarchically.

- **Files:** Basic units of data storage, have names and extensions (e.g., `.txt`, `.exe`).

  

## 2. File Permissions

- **Permissions:** Control access to files/folders (e.g., Read, Write, Execute).

- **Ownership:** Typically, the creator is the owner and can set permissions.

  

## 3. Basic Operations

- **File Creation:** Done by users or applications.

- **File Deletion:** Moves files to the Recycle Bin; can be permanently deleted.

- **File Copying/Moving:** Copy duplicates the file; Move transfers it.

  

## 4. Advanced Features

- **File Compression:** Reduces file size to save space.

- **Encryption:** Secures files with encryption.

- **Symbolic Links:** Shortcuts pointing to files/folders.

- **Volume Shadow Copy:** Creates snapshots for file recovery.

- **Disk Quotas:** Limits disk space usage per user.

  

## 5. CMD Commands for Windows

  

### Basic File and Directory Operations

- **`dir`:** Lists files and directories in the current directory.

  ```bash

  dir

  ```

- **`cd`:** Changes the current directory.

  ```bash

  cd path o\directory

  ```

- **`md` or `mkdir`:** Creates a new directory.

  ```bash

  md new_directory

  ```

- **`del`:** Deletes one or more files.

  ```bash

  del filename.ext

  ```

- **`rmdir` or `rd`:** Removes a directory (must be empty).

  ```bash

  rmdir directory_name

  ```

- **`copy`:** Copies files from one location to another.

  ```bash

  copy source_file destination_folder

  ```

- **`move`:** Moves files from one location to another.

  ```bash

  move source_file destination_folder

  ```

  

## 6. Basic VSCode Commands in CMD

  

### Opening Files and Folders

- **`code .`:** Opens the current directory in Visual Studio Code.

  ```bash

  code .

  ```

- **`code filename.ext`:** Opens a specific file in Visual Studio Code.

  ```bash

  code filename.ext

  ```

- **`code path  o\directory`:** Opens a specific directory in Visual Studio Code.

  ```bash

  code path o\directory

  ```

  

### Working with Extensions

- **`code --install-extension <extension-id>`:** Installs an extension in Visual Studio Code.

  ```bash

  code --install-extension ms-python.python

  ```

- **`code --list-extensions`:** Lists all installed extensions.

  ```bash

  code --list-extensions

  ```

- **`code --uninstall-extension <extension-id>`:** Uninstalls an extension from Visual Studio Code.

  ```bash

  code --uninstall-extension ms-python.python

  ```

  

### Other Useful Commands

- **`code --version`:** Displays the current version of Visual Studio Code.

  ```bash

  code --version

  ```

- **`code --help`:** Displays help information about the `code` command.

  ```bash

  code --help

  ```

  

## 7. Installing Basic VSCode Markdown Extensions

  

Markdown is a popular markup language that is widely used for documentation, README files, and more. Visual Studio Code supports Markdown editing natively, but several extensions can enhance your Markdown editing experience.

  

### Recommended Markdown Extensions

  

1. **Markdown All in One**

   - A comprehensive extension that provides features like keyboard shortcuts, table of contents generation, auto-preview, and more.

   - **Install Command:**

     ```bash

     code --install-extension yzhang.markdown-all-in-one

     ```

  

2. **MarkdownLint**

   - A linter for Markdown files that helps ensure your Markdown is consistent and follows best practices.

   - **Install Command:**

     ```bash

     code --install-extension DavidAnson.vscode-markdownlint

     ```

  

3. **Markdown Preview Enhanced**

   - An extension that enhances Markdown preview capabilities with additional features like rendering diagrams, charts, and LaTeX.

   - **Install Command:**

     ```bash

     code --install-extension shd101wyy.markdown-preview-enhanced

     ```

  

4. **Markdown Table Formatter**

   - Automatically formats tables in Markdown, making it easier to edit and maintain them.

   - **Install Command:**

     ```bash

     code --install-extension takanabe.markdown-table-formatter

     ```

  

5. **vscode-pandoc**

   - Allows you to convert Markdown to different formats like PDF, HTML, or DOCX using Pandoc.

   - **Install Command:**

     ```bash

     code --install-extension DougFinke.vscode-pandoc

     ```

  

### How to Install Extensions

  

To install any of these extensions, open a terminal or command prompt and use the `code --install-extension` command followed by the extension ID. For example:

  

```bash

code --install-extension yzhang.markdown-all-in-one

```

  

You can also install extensions directly from the Visual Studio Code Marketplace by searching for the extension name.

  

## 8. Conclusion

Understanding the Windows file system, basic command-line operations, and how to use Visual Studio Code from the Command Prompt is essential for efficient file management, system maintenance, and development workflows. Installing useful Markdown extensions in Visual Studio Code can greatly enhance your documentation and note-taking process. Mastery of these concepts and commands will significantly enhance your ability to interact with and manage Windows systems effectively.