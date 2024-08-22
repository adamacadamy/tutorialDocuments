# Terminal Basics

Visual Studio Code includes a full featured integrated terminal that starts at the root of your workspace. It provides integration with the editor to support features like [links](https://code.visualstudio.com/docs/terminal/basics#_links) and [error detection](https://code.visualstudio.com/docs/editor/tasks). The integrated terminal can run commands such as mkdir and git just like a standalone terminal.

You can open a terminal as follows:

- From the menu, use the **Terminal** > **New Terminal** or **View** > **Terminal** menu commands.
- From the **Command Palette** (Ctrl+Shift+P), use the **View: Toggle Terminal** command.
- In the Explorer, you can use the **Open in Integrated Terminal** context menu command to open a new terminal from a folder.
- To toggle the terminal panel, use the Ctrl+` keyboard shortcut.
- To create a new terminal, use the Ctrl+Shift+` keyboard shortcut.

VS Code's terminal has additional functionality called shell integration that tracks where commands are run with decorations on the left of a command and in the scrollbar:

![The integrated terminal can run commands such as mkdir and git just like a standalone terminal. VS Code's terminal has additional functionality called shell integration that tracks where commands are run with decorations on the left of a command and in the scrollbar.](https://code.visualstudio.com/assets/docs/terminal/basics/integrated-terminal.png)

> **Note:** If you prefer to work outside VS Code, open an external terminal with the Ctrl+Shift+C keyboard shortcut

## [Terminal shells](https://code.visualstudio.com/docs/terminal/basics#_terminal-shells)

The integrated terminal can use various shells installed on your machine, with the default being pulled from your system defaults. Shells are detected and presented in the terminal profiles dropdown.

![A detected profile can be chosen in the dropdown next to the new terminal button. Some examples on Windows include PowerShell, Command Prompt, Git Bash and WSL](https://code.visualstudio.com/assets/docs/terminal/basics/select-profile-dropdown.png)

You can learn more about configuring terminal shells in the [terminal profiles](https://code.visualstudio.com/docs/terminal/profiles) article.

## [Managing terminals](https://code.visualstudio.com/docs/terminal/basics#_managing-terminals)

The terminal tabs UI is on the right side of the terminal view. Each terminal has an entry with its name, icon, color, and group decoration (if any).

![Activating the Launch Profile button will show all detected and manually configured profiles](https://code.visualstudio.com/assets/docs/terminal/basics/tabs.png)

Add terminal instances by selecting the **+** icon on the top-right of the **TERMINAL** panel, selecting a profile from the terminal dropdown, or by triggering the Ctrl+Shift+` command. This action creates another entry in the tab list associated with that terminal.

Remove terminal instances by hovering a tab and selecting the **Trash Can** button, selecting a tab item and pressing Delete, using **Terminal: Kill the Active Terminal Instance** command, or via the right-click context menu.

Navigate between terminal groups using focus next Ctrl+PageDown and focus previous Ctrl+PageUp.

Icons may appear to the right of the terminal title on the tab label when a terminal's status changes. Some examples are a bell (macOS) and for tasks, displaying a check mark when there are no errors and an X otherwise. Hover the icon to read status information, which may contain actions.

### [Groups (split panes)](https://code.visualstudio.com/docs/terminal/basics#_groups-split-panes)

Place multiple terminals side-by-side and create a group by splitting a terminal:

- Hover over a entry in the list of terminals on the right and select the inline split button.
- Right-click the context menu and selecting the **Split** menu option.
- Alt and click on a tab, the **+** button, or the single tab on the terminal panel.
- Trigger the Ctrl+Shift+5 command.

> **Tip:** The working directory for the new terminal depends on the `terminal.integrated.splitCwd` [setting](https://code.visualstudio.com/docs/getstarted/settings).

Navigate between terminals in a group by focusing the previous pane, Alt+Left, or the next pane, Alt+Right.

Dragging and dropping tabs in the list rearranges them. Dragging a tab into the main terminal area allows moving a terminal from one group to another.

Moving a terminal into its own group can be done with the **Terminal: Unsplit Terminal** command through the Command Palette or in the right-click context menu.

## [Terminals in editor area](https://code.visualstudio.com/docs/terminal/basics#_terminals-in-editor-area)

You can open terminals in the editor area (terminal editors) with the **Terminal: Create New Terminal in Editor Area** command, the **Terminal: Create New Terminal in Editor Area to the Side** command, or by dragging a terminal from the terminal view into the editor area. Terminal editors are presented like regular editor tabs:

![Terminal editors are presented like regular text file tabs](https://code.visualstudio.com/assets/docs/terminal/basics/terminal-editor.png)

You can have terminal editors on either side or arranged in multiple dimensions using the editor group layout system, e.g. PowerShell and WSL terminals stacked to the right of file editors:

![Terminal editors are can be laid out using the editor group layout system, for example 2 terminals could sit to the right of a text editor](https://code.visualstudio.com/assets/docs/terminal/basics/terminal-editor-grid.png)

The `terminal.integrated.defaultLocation` setting can change the default `view` or `editor` area terminal location.

## [Navigating the buffer](https://code.visualstudio.com/docs/terminal/basics#_navigating-the-buffer)

The content in the terminal is called the buffer, with the section right above the bottom viewport being called "scrollback". The amount of scrollback kept is determined by the `terminal.integrated.scrollback` [setting](https://code.visualstudio.com/docs/getstarted/settings) and defaults to `1000` lines.

There are various commands available to navigate around the terminal buffer:

- Scroll up a line - Ctrl+Alt+PageUp
- Scroll down a line - Ctrl+Alt+PageDown
- Scroll up a page - Shift+PageUp
- Scroll down a page - Shift+PageDown
- Scroll to the top - Ctrl+Home
- Scroll to the bottom - Ctrl+End

**Command** navigation is also available (see [shell integration](https://code.visualstudio.com/docs/terminal/shell-integration)):

- Scroll to the previous command - Ctrl+Up
- Scroll to the next command - Ctrl+Down

Scrolling will happen instantaneously, but can be configured to animate over a short duration with the `terminal.integrated.smoothScrolling` setting.

## [Links](https://code.visualstudio.com/docs/terminal/basics#_links)

The terminal features sophisticated link detection with editor integration and even extension contributed link handlers. Hover over a link to display an underline, then hold the Ctrl/Cmd key and click.

These built-in link handlers are used in the following priority order:

- URIs/URLs: Links that look like URIs, such as `https://code.visualstudio.com`, `vscode://path/to/file` or `file://path/to/file` will open using the standard handler for the protocol. For example, `https` links will open the browser.
    
    ![Opening a URI link will open it in the system browser](https://code.visualstudio.com/assets/docs/terminal/basics/link-uri.png)
    
- File links: Links to files that have been verified to exist on the system. These will open the file in a new editor tab and support many common line/column formats such as `file:1:2`, `file:line 1, column 2`.
    
    ![Activating a file link will open it in an editor](https://code.visualstudio.com/assets/docs/terminal/basics/link-file.png)
    
- Folder links: Links to folders are similar to file links but will open a new VS Code window at the folder.
    
    ![Activating a folder link will open it in a new window](https://code.visualstudio.com/assets/docs/terminal/basics/link-folder.png)
    
- Word links: Fallback link type that uses the `terminal.integrated.wordSeparators` setting. The setting defines word boundaries and make nearly all text into words. Activating a word link searches the workspace for the word. If there is a single result it will open, otherwise it will present the search results. Word links are considered "low confidence" and will not show an underline or tooltip unless you hold the Ctrl/Cmd key. They also have limited support for line and column suffixes.
    
    ![Activating a word link 'terminal:15' will open a Quick Pick searching the workspace for all files containing 'terminal', choosing an option will open the file at line 15](https://code.visualstudio.com/assets/docs/terminal/basics/link-word.png)
    

The **Open Detected Link** command (Ctrl+Shift+G) can be used to access links via the keyboard:

![Open Detected Link opens a quick pick with all links in the viewport, split into categories](https://code.visualstudio.com/assets/docs/terminal/basics/link-open-detected.png)

> **Tip:** If link verification causes performance issues, like in high latency remote environments, disable it via the `terminal.integrated.enableFileLinks` [setting](https://code.visualstudio.com/docs/getstarted/settings).

### [Extensions handling links](https://code.visualstudio.com/docs/terminal/basics#_extensions-handling-links)

Extensions can contribute **link providers** which allow the extension to define what happens when clicked. An example of this is the [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) extension detecting Git branch links.

![When GitLens is installed, hovering a branch name will provide custom behavior to open the branch in the UI](https://code.visualstudio.com/assets/docs/terminal/basics/link-extension.png)

### [Keyboard accessibility](https://code.visualstudio.com/docs/terminal/basics#_keyboard-accessibility)

Links are keyboard accessible through several commands that open links based on the type of link.

- **Terminal: Open Last Local File Link** - Opens the most recent local file link. No default keybinding.
- **Terminal: Open Last URL link** - Opens the most recent URI/URL link. No default keybinding.
- **Terminal: Open Detected Link...** - Opens a searchable Quick Pick with all detected links, including word links. The default keybinding is Ctrl/Cmd+Shift+O, which is the same as the **Go to Symbol in Editor** keyboard shortcut.

## [Copy & paste](https://code.visualstudio.com/docs/terminal/basics#_copy-paste)

The keybindings for copy and paste follow platform standards:

- Linux: Ctrl+Shift+C and Ctrl+Shift+V; selection paste is available with Shift+Insert
- macOS: Cmd+C and Cmd+V
- Windows: Ctrl+C and Ctrl+V

Copying is done automatically on selection when `terminal.integrated.copyOnSelection` is enabled.

By default, there is a warning when pasting multiple lines, which can be disabled with the `terminal.integrated.enableMultiLinePasteWarning` setting. This is only done when the shell does not support "bracketed paste mode". When that mode is enabled, the shell is indicating that it can handle multiple line pasting.

## [Using the mouse](https://code.visualstudio.com/docs/terminal/basics#_using-the-mouse)

### [Right-click behavior](https://code.visualstudio.com/docs/terminal/basics#_rightclick-behavior)

The right-click behavior differs based on the platform:

- Linux: Show the context menu.
- macOS: Select the word under the cursor and show the context menu.
- Windows: Copy and drop selection if there is a selection, otherwise paste.

This can be configured using the `terminal.integrated.rightClickBehavior` setting. The options are:

- `default` - Show the context menu.
- `copyPaste` - Copy when there is a selection, otherwise paste.
- `paste` - Paste on right-click.
- `selectWord` - Select the word under the cursor and show the context menu.
- `nothing` - Do nothing and pass event to terminal.

### [Reposition the cursor with Alt](https://code.visualstudio.com/docs/terminal/basics#_reposition-the-cursor-with-alt)

Alt and left-click will reposition the cursor to underneath the mouse. This works by simulating arrow keystrokes, which may not work reliably for some shells or programs. This feature can be disabled with the `terminal.integrated.altClickMovesCursor` setting.

### [Mouse events mode](https://code.visualstudio.com/docs/terminal/basics#_mouse-events-mode)

When applications running in the terminal turn on mouse events mode, such as Vim mouse mode, mouse interaction is sent to the application instead of the terminal. This means that clicking and dragging will no longer create a selection. Terminal selection can be forced by holding the Alt key on Windows and Linux, this can also be done with the Option key on macOS but requires enabling the `terminal.integrated.macOptionClickForcesSelection` setting first.

## [Find](https://code.visualstudio.com/docs/terminal/basics#_find)

The integrated terminal has find functionality that can be triggered with Ctrl+F.

![Find in the terminal will highlight all text matching the query](https://code.visualstudio.com/assets/docs/terminal/basics/terminal-find.png)

> **Tip:** Ctrl+F can be sent to the shell by removing the `workbench.action.terminal.focusFind` command from [commands to skip shell](https://code.visualstudio.com/docs/terminal/advanced#_keybinding-and-the-shell).

## [Run selected text](https://code.visualstudio.com/docs/terminal/basics#_run-selected-text)

To use the `runSelectedText` command, select text in an editor and run the command **Terminal: Run Selected Text in Active Terminal** via the **Command Palette** (Ctrl+Shift+P), the terminal will attempt to run the selected text. If no text is selected in the active editor, the entire line that the cursor is on will run in the terminal.

> **Tip:** Also run the active file using the command `workbench.action.terminal.runActiveFile`.

## [Maximizing the terminal](https://code.visualstudio.com/docs/terminal/basics#_maximizing-the-terminal)

The terminal view can be maximized by clicking the maximize panel size button with the upwards chevron icon. This will temporarily hide the editors and maximize the panel. This is useful to temporarily focus on a large amount of output. Some developers use VS Code as a standalone terminal by opening a new window, maximizing the panel, and hiding the side bar.

Note that the panel can only be maximized if its [alignment](https://code.visualstudio.com/docs/editor/custom-layout#_panel-alignment) option is set to **Center**.

## [Select all](https://code.visualstudio.com/docs/terminal/basics#_select-all)

There is a **Terminal: Select All** command, which is bound to Cmd+A on macOS, but does not have a default keybinding on Windows and Linux as it may conflict with shell hotkeys. To use Ctrl+A to select all, add this custom keybinding:

```
{
  "key": "ctrl+a",
  "command": "workbench.action.terminal.selectAll",
  "when": "terminalFocus && !isMac"
},
```

## [Drag and drop file paths](https://code.visualstudio.com/docs/terminal/basics#_drag-and-drop-file-paths)

Dragging a file into the terminal will input the path into the terminal, with escaping to match the active shell.

## [Automating terminals with tasks](https://code.visualstudio.com/docs/terminal/basics#_automating-terminals-with-tasks)

The [Tasks](https://code.visualstudio.com/docs/editor/tasks) feature can be used to automate the launching of terminals, for example, the following `.vscode/tasks.json` file will launch a Command Prompt and PowerShell terminal in a single terminal group when the window starts:

```
{
  "version": "2.0.0",
  "presentation": {
    "echo": false,
    "reveal": "always",
    "focus": false,
    "panel": "dedicated",
    "showReuseMessage": true
  },
  "tasks": [
    {
      "label": "Create terminals",
      "dependsOn": [
        "First",
        "Second"
      ],
      // Mark as the default build task so cmd/ctrl+shift+b will create them
      "group": {
        "kind": "build",
        "isDefault": true
      },
      // Try start the task on folder open
      "runOptions": {
        "runOn": "folderOpen"
      }
    },
    {
      // The name that shows up in terminal tab
      "label": "First",
      // The task will launch a shell
      "type": "shell",
      "command": "",
      // Set the shell type
      "options": {
        "shell": {
          "executable": "cmd.exe",
          "args": []
        }
      },
      // Mark as a background task to avoid the spinner animation on the terminal tab
      "isBackground": true,
      "problemMatcher": [],
      // Create the tasks in a terminal group
      "presentation": {
        "group": "my-group"
      }
    },
    {
      "label": "Second",
      "type": "shell",
      "command": "",
      "options": {
        "shell": {
          "executable": "pwsh.exe",
          "args": []
        }
      },
      "isBackground": true,
      "problemMatcher": [],
      "presentation": {
        "group": "my-group"
      }
    }
  ]
}
```

This file could be committed to the repository to share with other developers or created as a user task via the `workbench.action.tasks.openUserTasks` command.

## [Working directory](https://code.visualstudio.com/docs/terminal/basics#_working-directory)

By default, the terminal will open at the folder that is opened in the Explorer. The `terminal.integrated.cwd` setting allows specifying a custom path to open instead:

```
{
  "terminal.integrated.cwd": "/home/user"
}
```

Split terminals on Windows will start in the directory that the parent terminal started with. On macOS and Linux, split terminals will inherit the current working directory of the parent terminal. This behavior can be changed using the `terminal.integrated.splitCwd` setting:

```
{
  "terminal.integrated.splitCwd": "workspaceRoot"
}
```

There are also extensions available that give more options such as [Terminal Here](https://marketplace.visualstudio.com/items?itemName=Tyriar.vscode-terminal-here).

## [Fixed dimension terminals](https://code.visualstudio.com/docs/terminal/basics#_fixed-dimension-terminals)

The **Terminal: Set Fixed Dimensions** command allows changing the number of columns and rows that the terminal and it's backing pseudoterminal uses. This will add scroll bars when necessary, which may lead to an unpleasant UX and is generally not recommended, but it is a common ask on Windows in particular for reading logs or long lines when paging tools aren't available.

You can also right-click on a terminal tab and select **Toggle Size to Content Width** (Alt+Z) to resize the number of terminal columns to the largest wrapped line in the terminal.

## [Next steps](https://code.visualstudio.com/docs/terminal/basics#_next-steps)