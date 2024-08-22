# Extension Marketplace

The features that Visual Studio Code includes out-of-the-box are just the start. VS Code extensions let you add languages, debuggers, and tools to your installation to support your development workflow. VS Code's rich extensibility model lets extension authors plug directly into the VS Code UI and contribute functionality through the same APIs used by VS Code. This article explains how to find, install, and manage VS Code extensions from the [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/VSCode).

## [Browse for extensions](https://code.visualstudio.com/docs/editor/extension-marketplace#_browse-for-extensions)

You can browse and install extensions from within VS Code. Bring up the Extensions view by clicking on the Extensions icon in the **Activity Bar** on the side of VS Code or the **View: Extensions** command (Ctrl+Shift+X).

![Extensions view icon](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/extensions-view-icon.png)

This will show you a list of the most popular VS Code extensions on the [VS Code Marketplace](https://marketplace.visualstudio.com/VSCode).

![popular extensions](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/extensions-popular.png)

Each extension in the list includes a brief description, the publisher, the download count, and a five star rating. You can select the extension item to display the extension's details page where you can learn more.

> **Note:** If your computer's Internet access goes through a proxy server, you will need to configure the proxy server. See [Proxy server support](https://code.visualstudio.com/docs/setup/network#_proxy-server-support) for details.

## [Install an extension](https://code.visualstudio.com/docs/editor/extension-marketplace#_install-an-extension)

To install an extension, select the **Install** button. Once the installation is complete, the **Install** button will change to the **Manage** gear button.

If you want to install a specific version of an extension, right-click the extension and select **Install Another Version**. You can then select a version from the available list.

When [Settings Sync](https://code.visualstudio.com/docs/editor/settings-sync) is enabled, you can share your VS Code configurations, such as extensions, across your machines. To install an extension and not sync it across your machines, right-click the extension and select **Install (Do not Sync)**.

### [Find and install an extension](https://code.visualstudio.com/docs/editor/extension-marketplace#_find-and-install-an-extension)

For example, let's install the popular [TODO Highlight](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight) extension. This extension highlights text like 'TODO:' and 'FIXME:' in your source code so you can quickly find undone sections.

![TODO Highlight extension highlighting in the editor](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/todo-highlighting.png)

In the Extensions view (Ctrl+Shift+X), type 'todo' in the search box to filter the Marketplace offerings to extensions with 'todo' in the title or metadata. You should see the **TODO Highlight** extension in the list.

![Search for todo in the Extensions view](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/search-for-todo-extension.png)

An extension is uniquely identified by its publisher and extension IDs. If you select the **TODO Highlight** extension, you will see the Extension details page, where you can find the extension ID, in this case, `wayou.vscode-todo-highlight`. Knowing the extension ID can be helpful if there are several similarly named extensions.

![TODO Highlight extension details with extension ID highlighted](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/todo-highlight-details.png)

Select the **Install** button, and VS Code will download and install the extension from the Marketplace. When the installation is complete, the **Install** button will be replaced with a **Manage** gear button.

![Manage gear button](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/manage-button.png)

To see the TODO Highlight extension in action, open any source code file and add the text 'TODO:' and you will see the text highlighted.

The TODO Highlight extension contributes the commands, **TODO-Highlight: List highlighted annotations** and **TODO-Highlight: Toggle highlight**, that you can find in the Command Palette (Ctrl+Shift+P). The **TODO-Highlight: Toggle highlight** command lets you quickly disable or enable highlighting.

![TODO Highlight commands in the Command Palette](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/todo-highlight-commands.png)

The extension also provides settings for tuning its behavior, which you can find in the Settings editor (Ctrl+,). For example, you might want the text search to be case insensitive and you can uncheck the **Todohighlight: Is Case Sensitive** setting.

![TODO Highlight settings in the Settings editor](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/todo-highlight-settings.png)

If an extension doesn't provide the functionality you want, you can always **Uninstall** the extension from the **Manage** button context menu.

![Uninstall the TODO Highlight extension](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/todo-highlight-uninstall.png)

This has been just one example of how to install and use an extension. The VS Code Marketplace has thousands of extensions supporting hundreds of programming languages and tasks. Everything from full featured language support for [Java](https://marketplace.visualstudio.com/items?itemName=redhat.java), [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python), [Go](https://marketplace.visualstudio.com/items?itemName=golang.Go), and [C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools) to simple extensions that [create GUIDs](https://marketplace.visualstudio.com/items?itemName=nwallace.createGUID), change the [color theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme), or add [virtual pets](https://marketplace.visualstudio.com/items?itemName=tonybaloney.vscode-pets) to the editor.

### [Extension details](https://code.visualstudio.com/docs/editor/extension-marketplace#_extension-details)

On the extension details page, you can read the extension's README and review the extension's:

- **Feature Contributions** - The extension's additions to VS Code such as settings, commands and keyboard shortcuts, language grammars, debugger, etc.
- **Changelog** - The extension repository CHANGELOG if available.
- **Dependencies** - Lists if the extension depends on any other extensions.

![extension contributions](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/extension-contributions.png)

If an extension is an Extension Pack, the **Extension Pack** section will display which extensions will be installed when you install the pack. [Extension Packs](https://code.visualstudio.com/api/references/extension-manifest#_extension-packs) bundle separate extensions together so they can be easily installed at one time.

![Azure Tools extension pack](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/extension-pack.png)

### [Extensions view filter and commands](https://code.visualstudio.com/docs/editor/extension-marketplace#_extensions-view-filter-and-commands)

You can filter the Extensions view with the **Filter Extensions** context menu.

![Extensions view filter context menu](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/extensions-view-filter-menu.png)

There are filters to show:

- The list of outdated extensions that can be updated
- The list of currently enabled/disabled extensions
- The list of recommended extensions based on your workspace
- The list of globally popular extensions

You can sort the extension list by **Install Count**, **Rating**, **Name**, **Published Date**, or **Updated Date** in either ascending or descending order. You can learn more about extension search filters [below](https://code.visualstudio.com/docs/editor/extension-marketplace#_extensions-view-filters).

You can run additional Extensions view commands via the `...` **View and More Actions** button.

![more button](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/more-button.png)

Through this context menu you can control extension updates, enable or disable all extensions, and use the [Extension Bisect](https://code.visualstudio.com/blogs/2021/02/16/extension-bisect) utility to isolate problematic extension behavior.

### [Search for an extension](https://code.visualstudio.com/docs/editor/extension-marketplace#_search-for-an-extension)

You can clear the Search box at the top of the Extensions view and type in the name of the extension, tool, or programming language you're looking for.

For example, typing 'python' will bring up a list of Python language extensions:

![python extensions](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/extensions-python.png)

If you know the exact identifier for an extension you're looking for, you can use the `@id:` prefix, for example `@id:vue.volar`. Additionally, to filter or sort results, you can use the [filter](https://code.visualstudio.com/docs/editor/extension-marketplace#_extensions-view-filters) and [sort](https://code.visualstudio.com/docs/editor/extension-marketplace#_sorting) commands, detailed below.

## [Manage extensions](https://code.visualstudio.com/docs/editor/extension-marketplace#_manage-extensions)

VS Code makes it easy to manage your extensions. You can install, disable, update, and uninstall extensions through the Extensions view, the **Command Palette** (commands have the **Extensions:** prefix) or command-line switches.

### [List installed extensions](https://code.visualstudio.com/docs/editor/extension-marketplace#_list-installed-extensions)

By default, the Extensions view will show the extensions you currently have installed, and all extensions that are recommended for you. You can use the **Extensions: Focus on Installed View** command, available in the **Command Palette** (Ctrl+Shift+P) or in the **More Actions** (`...`) dropdown menu > **Views** > **Installed**, to clear any text in the search box and show the list of all installed extensions, which includes those that have been disabled.

### [Uninstall an extension](https://code.visualstudio.com/docs/editor/extension-marketplace#_uninstall-an-extension)

To uninstall an extension, select the **Manage** gear button at the right of an extension entry and then choose **Uninstall** from the dropdown menu. This will uninstall the extension and prompt you to restart the extension host (**Restart Extensions**).

![uninstall an extension](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/uninstall-extension.png)

### [Disable an extension](https://code.visualstudio.com/docs/editor/extension-marketplace#_disable-an-extension)

If you don't want to permanently remove an extension, you can instead temporarily disable the extension by clicking the gear button at the right of an extension entry. You can disable an extension globally or just for your current Workspace. You will be prompted to restart the extension host (**Restart Extensions**) after you disable an extension.

If you want to quickly disable all installed extensions, there is a **Disable All Installed Extensions** command in the **Command Palette** and **More Actions** (`...`) dropdown menu.

Extensions remain disabled for all VS Code sessions until you re-enable them.

### [Enable an extension](https://code.visualstudio.com/docs/editor/extension-marketplace#_enable-an-extension)

Similarly if you have disabled an extension (it will be in the **Disabled** section of the list and marked _**Disabled**_), you can re-enable it with the **Enable** or **Enable (Workspace)** commands in the dropdown menu.

![enable extension](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/enable-extension.png)

There is also an **Enable All Extensions** command in the **More Actions** (`...`) dropdown menu.

### [Extension auto-update](https://code.visualstudio.com/docs/editor/extension-marketplace#_extension-autoupdate)

VS Code checks for extension updates and installs them automatically. After an update, you are prompted to restart the extension host (**Restart Extensions**).

If you'd rather update your extensions manually, you can disable auto-update with the **Disable Auto Update for All Extensions** command or the corresponding action in the Extensions view. You can also configure the `extensions.autoUpdate` [setting](https://code.visualstudio.com/docs/getstarted/settings). Use the **Enable Auto Update for All Extensions** command to re-enable auto update.

![Disable auto update for all extensions action](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/disable-auto-update-all-extensions.png)

You can also configure auto update for individual extensions by right-clicking on an extension and toggling the **Auto Update** item.

If you don't want VS Code to even check for updates, you can set the `extensions.autoCheckUpdates` setting to false.

### [Update an extension manually](https://code.visualstudio.com/docs/editor/extension-marketplace#_update-an-extension-manually)

If you have extensions auto-update disabled, you can quickly look for extension updates by using the **Show Outdated Extensions** command that uses the `@updates` filter. This will display any available updates for your currently installed extensions.

Select the **Update** button for the outdated extension. The update will be installed, and you'll be prompted to restart the extension host (**Restart Extensions**). You can also update all your outdated extensions at one time with the **Update All Extensions** command.

If you also have automatic checking for updates disabled, you can use the **Check for Extension Updates** command to check which of your extensions can be updated.

## [Recommended extensions](https://code.visualstudio.com/docs/editor/extension-marketplace#_recommended-extensions)

You can see a list of recommended extensions using **Show Recommended Extensions**, which sets the `@recommended` [filter](https://code.visualstudio.com/docs/editor/extension-marketplace#_extensions-view-filters). Extension recommendations can either be:

- **Workspace Recommendations** - Recommended by other users of your current workspace.
- **Other Recommendations** - Recommended based on recently opened files.

See the section below to learn how to [contribute](https://code.visualstudio.com/docs/editor/extension-marketplace#_workspace-recommended-extensions) recommendations for other users in your project.

### [Ignoring recommendations](https://code.visualstudio.com/docs/editor/extension-marketplace#_ignoring-recommendations)

To dismiss a recommendation, select on the extension item to open the Details page and then select the **Manage** gear button to display the context menu. Select the **Ignore Recommendation** menu item. Ignored recommendations will no longer be recommended to you.

![Ignore extension recommendation](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/ignore-recommendation.png)

## [Configuring extensions](https://code.visualstudio.com/docs/editor/extension-marketplace#_configuring-extensions)

VS Code extensions may have very different configurations and requirements. Some extensions contribute [settings](https://code.visualstudio.com/docs/getstarted/settings) to VS Code, which can be modified in the Settings editor. Other extensions may have their own configuration files. Extensions may also require installation and setup of additional components like compilers, debuggers, and command-line tools. Consult the extension's README (visible in the Extensions view details page) or go to the extension page on the [VS Code Marketplace](https://marketplace.visualstudio.com/VSCode) (click on the extension name in the details page). Many extensions are open source and have a link to their repository on their Marketplace page.

## [Command line extension management](https://code.visualstudio.com/docs/editor/extension-marketplace#_command-line-extension-management)

To make it easier to automate and configure VS Code, it is possible to list, install, and uninstall extensions from the [command line](https://code.visualstudio.com/docs/editor/command-line). When identifying an extension, provide the full name of the form `publisher.extension`, for example `ms-python.python`.

Example:

```
code --extensions-dir <dir>
    Set the root path for extensions.
code --list-extensions
    List the installed extensions.
code --show-versions
    Show versions of installed extensions, when using --list-extension.
code --install-extension (<extension-id> | <extension-vsix-path>)
    Installs an extension.
code --uninstall-extension (<extension-id> | <extension-vsix-path>)
    Uninstalls an extension.
code --enable-proposed-api (<extension-id>)
    Enables proposed API features for extensions. Can receive one or more extension IDs to enable individually.
```

You can see the extension ID on the extension details page under the Marketplace Info.

![extension identifier](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/extension-identifier.png)

## [Extensions view filters](https://code.visualstudio.com/docs/editor/extension-marketplace#_extensions-view-filters)

The Extensions view search box supports filters to help you find and manage extensions. You may have seen filters such as `@installed` and `@recommended` if you used the commands **Show Installed Extensions** and **Show Recommended Extensions**. Also, there are filters available to let you sort by popularity or ratings and search by category (for example 'Linters') and tags (for example 'node'). You can see a complete listing of all filters and sort commands by typing `@` in the extensions search box and navigating through the suggestions:

![intellisense on extension search filters](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/extension-search-filters.png)

Here are some of the Extensions view filters:

- `@builtin` - Show extensions that come with VS Code. Grouped by type (Programming Languages, Themes, etc.).
- `@deprecated` - Show deprecated extensions.
- `@disabled` - Show disabled installed extensions.
- `@enabled` - Show enabled installed extensions. Extensions can be individually enabled/disabled.
- `@featured` - Show featured extensions.
- `@installed` - Show installed extensions.
- `@popular` - Show popular extensions.
- `@recentlyPublished` - Show extensions that were recently published in the Marketplace.
- `@recommended` - Show recommended extensions. Grouped as Workspace specific or general use.
- `@updates` - Show outdated installed extensions. A newer version is available on the Marketplace.
- `@workspaceUnsupported` - Show extensions that are not supported for this workspace.
- `@category` - Show extensions belonging to specified category. Below are a few of supported categories. For a complete list, type `@category` and follow the options in the suggestion list:
    - `@category:themes`
    - `@category:formatters`
    - `@category:linters`
    - `@category:snippets`

These filters can be combined as well. For example: Use `@installed @category:themes` to view all installed themes.

If no filter is provided, the Extensions view displays the currently installed and recommended extensions.

### [Sorting](https://code.visualstudio.com/docs/editor/extension-marketplace#_sorting)

You can sort extensions with the `@sort` filter, which can take the following values:

- `installs` - Sort by Marketplace installation count, in descending order.
- `name` - Sort alphabetically by extension name.
- `publishedDate` - Sort by extension published date.
- `rating` - Sort by Marketplace rating (1-5 stars), in descending order.
- `updateDate` - Sort by extension last update name.

![sort by install count](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/sort-install-count.png)

### [Categories and tags](https://code.visualstudio.com/docs/editor/extension-marketplace#_categories-and-tags)

Extensions can set **Categories** and **Tags** describing their features.

![extension categories and tags](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/categories-and-tags.png)

You can filter on category and tag by using `category:` and `tag:`.

Supported categories are: `[Azure, Data Science, Debuggers, Education, Extension Packs, Formatters, Keymaps, Language Packs, Linters, Machine Learning, Notebooks, Others, Programming Languages, SCM Providers, Snippets, Testing, Themes, Visualization]`. They can be accessed through IntelliSense in the extensions search box:

![categories debuggers](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/extension-search-categories.png)

Note that you must surround the category name in quotes if it is more than one word (for example, `category:"SCM Providers"`).

Tags may contain any string and are not provided by IntelliSense, so review the Marketplace to find helpful tags.

## [Install from a VSIX](https://code.visualstudio.com/docs/editor/extension-marketplace#_install-from-a-vsix)

You can manually install a VS Code extension packaged in a `.vsix` file. Using the **Install from VSIX** command in the Extensions view command dropdown, or the **Extensions: Install from VSIX** command in the **Command Palette**, point to the `.vsix` file.

You can also install using the VS Code `--install-extension` command-line switch providing the path to the `.vsix` file.

```
code --install-extension myextension.vsix
```

You may provide the `--install-extension` multiple times on the command line to install multiple extensions at once.

> **Note**: When you install an extension via VSIX, [auto update](https://code.visualstudio.com/docs/editor/extension-marketplace#_extension-auto-update) for that extension is disabled by default.

If you'd like to learn more about packaging and publishing extensions, see our [Publishing Extensions](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) article in the Extension API.

## [Workspace recommended extensions](https://code.visualstudio.com/docs/editor/extension-marketplace#_workspace-recommended-extensions)

A good set of extensions can make working with a particular workspace or programming language more productive and you'd often like to share this list with your team or colleagues. You can create a recommended list of extensions for a workspace with the **Extensions: Configure Recommended Extensions (Workspace Folder)** command.

In a single folder workspace, the command creates an `extensions.json` file located in the workspace `.vscode` folder where you can add a list of extensions identifiers ({publisherName}.{extensionName}).

In a [multi-root workspace](https://code.visualstudio.com/docs/editor/multi-root-workspaces), the command will open your `.code-workspace` file where you can list extensions under `extensions.recommendations`. You can still add extension recommendations to individual folders in a multi-root workspace by using the **Extensions: Configure Recommended Extensions (Workspace Folder)** command.

An example `extensions.json` could be:

```
{
  "recommendations": ["dbaeumer.vscode-eslint", "esbenp.prettier-vscode"]
}
```

which recommends a linter extension and a code formatter extension.

An extension is identified using its publisher identifier and extension identifier `publisher.extension`. You can see the name on the extension's detail page. VS Code will provide you with auto-completion for installed extensions inside these files.

![Extension identifier](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/extension-identifier.png).

VS Code prompts a user to install the recommended extensions when a workspace is opened for the first time. The user can also review the list with the **Extensions: Show Recommended Extensions** command.

![Show Recommendations](https://code.visualstudio.com/assets/docs/editor/extension-marketplace/recommendations.png)
 