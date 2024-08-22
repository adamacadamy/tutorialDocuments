# Command Line Interface (CLI)

Visual Studio Code has a powerful command-line interface built-in that lets you control how you launch the editor. You can open files, install extensions, change the display language, and output diagnostics through command-line options (switches).

![command line example](https://code.visualstudio.com/assets/docs/editor/command-line/hero.png)

If you are looking for how to run command-line tools inside VS Code, see the [Integrated Terminal](https://code.visualstudio.com/docs/terminal/basics).

## [Command line help](https://code.visualstudio.com/docs/editor/command-line#_command-line-help)

To get an overview of the VS Code command-line interface, open a terminal or command prompt and type `code --help`. You will see the version, usage example, and list of command line options.

![command line help](https://code.visualstudio.com/assets/docs/editor/command-line/command-line-help.png)

## [Launching from command line](https://code.visualstudio.com/docs/editor/command-line#_launching-from-command-line)

You can launch VS Code from the command line to quickly open a file, folder, or project. Typically, you open VS Code within the context of a folder. To do this, from an open terminal or command prompt, navigate to your project folder and type `code .`:

![launch VS Code](https://code.visualstudio.com/assets/docs/editor/command-line/launch-vscode.png)

**Note:** Users on macOS must first run a command (**Shell Command: Install 'code' command in PATH**) to add VS Code executable to the `PATH` environment variable. Read the [macOS setup guide](https://code.visualstudio.com/docs/setup/mac) for help.

Windows and Linux installations should add the VS Code binaries location to your system path. If this isn't the case, you can manually add the location to the `Path` environment variable (`$PATH` on Linux). For example, on Windows, the default VS Code binaries location is `AppData\Local\Programs\Microsoft VS Code\bin`. To review platform-specific setup instructions, see [Setup](https://code.visualstudio.com/docs/setup/setup-overview).

> **Insiders:** If you are using the VS Code [Insiders](https://code.visualstudio.com/insiders) preview, you launch your Insiders build with `code-insiders`.

## [Core CLI options](https://code.visualstudio.com/docs/editor/command-line#_core-cli-options)

Here are optional arguments you can use when starting VS Code at the command line via `code`:

|Argument|Description|
|---|---|
|`-h` or `--help`|Print usage|
|`-v` or `--version`|Print VS Code version (for example, 1.22.2), GitHub commit ID, and architecture (for example, x64).|
|`-n` or `--new-window`|Opens a new session of VS Code instead of restoring the previous session (default).|
|`-r` or `--reuse-window`|Forces opening a file or folder in the last active window.|
|`-g` or `--goto`|When used with _file:line{:character}_, opens a file at a specific line and optional character position. This argument is provided since some operating systems permit `:` in a file name.|
|`-d` or `--diff <file1> <file2>`|Open a file difference editor. Requires two file paths as arguments.|
|`-m` or `--merge <path1> <path2> <base> <result>`|Perform a three-way merge by providing paths for two modified versions of a file, the common origin of both modified versions, and the output file to save merge results.|
|`-w` or `--wait`|Wait for the files to be closed before returning.|
|`--locale <locale>`|Set the [display language](https://code.visualstudio.com/docs/getstarted/locales) (locale) for the VS Code session. (for example, `en-US` or `zh-TW`)|

![launch with locale](https://code.visualstudio.com/assets/docs/editor/command-line/launch-locale.png)

## [Opening Files and Folders](https://code.visualstudio.com/docs/editor/command-line#_opening-files-and-folders)

Sometimes you will want to open or create a file. If the specified file does not exist, VS Code will create them for you along with any new intermediate folders:

```
code index.html style.css documentation\readme.md
```

For both files and folders, you can use absolute or relative paths. Relative paths are relative to the current directory of the command prompt where you run `code`.

If you specify more than one file at the command line, VS Code will open only a single instance.

If you specify more than one folder at the command line, VS Code will create a [Multi-root Workspace](https://code.visualstudio.com/docs/editor/multi-root-workspaces) including each folder.

|Argument|Description|
|---|---|
|`file`|Name of a file to open. If the file doesn't exist, it will be created and marked as edited. You can specify multiple files by separating each file name with a space.|
|`file:line[:character]`|Used with the `-g` argument. Name of a file to open at the specified line and optional character position.|
|`folder`|Name of a folder to open. You can specify multiple folders and a new [Multi-root Workspace](https://code.visualstudio.com/docs/editor/multi-root-workspaces) is created.|

![go to line and column](https://code.visualstudio.com/assets/docs/editor/command-line/goto-line-column.png)

## [Select a profile](https://code.visualstudio.com/docs/editor/command-line#_select-a-profile)

You can launch VS Code with a specific [profile](https://code.visualstudio.com/docs/editor/profiles) via the `--profile` command-line interface option. You pass the name of the profile after the `--profile` argument and open a folder or a workspace using that profile. The command line below opens the `web-sample` folder with the "Web Development" profile:

`code ~/projects/web-sample --profile "Web Development"`

If the profile specified does not exist, a new empty profile with the given name is created.

## [Working with extensions](https://code.visualstudio.com/docs/editor/command-line#_working-with-extensions)

You can install and manage VS Code [extensions](https://code.visualstudio.com/docs/editor/extension-marketplace) from the command line.

|Argument|Description|
|---|---|
|`--install-extension <ext>`|Install an extension. Provide the full extension name `publisher.extension` as an argument. Use `--force` argument to avoid prompts.|
|`--uninstall-extension <ext>`|Uninstall an extension. Provide the full extension name `publisher.extension` as an argument.|
|`--disable-extensions`|Disable all installed extensions. Extensions will still be visible in the **Disabled** section of the Extensions view but they will never be activated.|
|`--list-extensions`|List the installed extensions.|
|`--show-versions`|Show versions of installed extensions, when using `--list-extensions`|
|`--enable-proposed-api <ext>`|Enables proposed api features for an extension. Provide the full extension name `publisher.extension` as an argument.|

![install extension](https://code.visualstudio.com/assets/docs/editor/command-line/install-extension.png)

## [Advanced CLI options](https://code.visualstudio.com/docs/editor/command-line#_advanced-cli-options)

There are several CLI options that help with reproducing errors and advanced setup.

|Argument|Description|
|---|---|
|`--extensions-dir <dir>`|Set the root path for extensions.  <br>Overridden in [Portable Mode](https://code.visualstudio.com/docs/editor/portable) by the `data` folder.|
|`--user-data-dir <dir>`|Specifies the directory that user data is kept in, useful when running as root.  <br>Overridden in [Portable Mode](https://code.visualstudio.com/docs/editor/portable) by the `data` folder.|
|`-s, --status`|Print process usage and diagnostics information.|
|`-p, --performance`|Start with the **Developer: Startup Performance** command enabled.|
|`--disable-gpu`|Disable GPU hardware acceleration.|
|`--verbose`|Print verbose output (implies `--wait`).|
|`--prof-startup`|Run CPU profiler during startup.|
|`--upload-logs`|Uploads logs from current session to a secure endpoint.|
|**Multi-root**||
|`--add <dir>`|Add folder(s) to the last active window for a multi-root workspace.|

### [Create remote tunnel](https://code.visualstudio.com/docs/editor/command-line#_create-remote-tunnel)

VS Code integrates with other [remote environments](https://code.visualstudio.com/docs/remote/remote-overview) to become even more powerful and flexible. Our goal is to provide a cohesive experience that allows you to manage both local and remote machines from one, unified CLI.

The Visual Studio Code [Remote - Tunnels](https://marketplace.visualstudio.com/items?itemName=ms-vscode.remote-server) extension lets you connect to a remote machine, like a desktop PC or VM, via a secure tunnel. Tunneling securely transmits data from one network to another. You can then securely connect to that machine from anywhere, without the requirement of SSH.

We've built functionality into the `code` CLI that will initiate tunnels on remote machines. You can run:

```
code tunnel
```

to create a tunnel on your remote machine. You may connect to this machine through a web or desktop VS Code client.

You can review the other tunneling commands by running `code tunnel -help`:

![Output of tunnel help CLI command](https://code.visualstudio.com/assets/docs/editor/command-line/tunnel-help.png)

As you may need to run the CLI on a remote machine that can't install VS Code Desktop, the CLI is also available for standalone install on the [VS Code download page](https://code.visualstudio.com/insiders/).

For more information on Remote Tunnels, you can review the [Remote Tunnels documentation](https://code.visualstudio.com/docs/remote/tunnels).

## [Opening VS Code with URLs](https://code.visualstudio.com/docs/editor/command-line#_opening-vs-code-with-urls)

You can also open projects and files using the platform's URL handling mechanism. Use the following URL formats to:

Open a project

```
vscode://file/{full path to project}/

vscode://file/c:/myProject/
```

Open a file

```
vscode://file/{full path to file}

vscode://file/c:/myProject/package.json
```

Open a file to line and column

```
vscode://file/{full path to file}:line:column

vscode://file/c:/myProject/package.json:5:10
```

Open the Settings Editor

```
vscode://settings/setting.name

vscode://settings/editor.wordWrap
```

You can use the URL in applications such as browsers or file explorers that can parse and redirect the URL. For example, on Windows, you could pass a `vscode://` URL directly to the Windows Explorer or to the command line as `start vscode://{full path to file}`.

![vscode url in Windows Explorer](https://code.visualstudio.com/assets/docs/editor/command-line/vscode-url.png)

> **Note**: If you are using VS Code [Insiders](https://code.visualstudio.com/insiders) builds, the URL prefix is `vscode-insiders://`.