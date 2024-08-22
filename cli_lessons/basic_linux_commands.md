# Basic Linux Commands:

## 1. `pwd` (Print Working Directory)

The `pwd` command displays the current directory you're in. This is incredibly useful for confirming your location within the file system, especially when navigating through directories.

pwd

## 2. `ls` (List)

To see the files and directories in your current directory, use the `ls` command. It can be expanded with options to show detailed information:

- `-l`: Lists files and directories with detailed information like permissions, number of links, owner, group, size and the time of last modification.
- `-a`: Shows all files, including hidden files (those beginning with a dot).

ls -l  
ls -a

# 3. `cd` (Change Directory)

The `cd` command is used to move between directories. By default, `cd` takes you to the home directory, but you can specify paths to navigate elsewhere:

- `cd /path/to/directory`: Changes to the specified directory.
- `cd ..`: Moves up one directory level.

cd /var/www  
cd ..

# 4. `mkdir` (Make Directory)

If you need to create a new directory, `mkdir` is the command you'll use. It allows you to set up a new folder anywhere where you have permission.

mkdir new_folder

## 5. `rmdir` (Remove Directory)

To delete an empty directory, use `rmdir`. This command will only work if the directory is empty, ensuring that you don't accidentally delete files.

rmdir old_folder

## 6. `rm` (Remove)

For removing files or directories containing files, `rm` is the command you need. Use caution with this command, as deleting files or directories is irreversible:

- `-r`: Recursive delete to remove directories and their contents.
- `-f`: Force delete to remove files without prompting for confirmation.

rm filename.txt  
rm -rf directory_name

## 7. `touch` (Create File or Update Timestamp)

The `touch` command is used to create new, empty files or to update the timestamps on existing files.

touch newfile.txt

 
 
## 8. `cat` (Concatenate)

`cat` is often used to display the contents of a file on the standard output (screen). It can also concatenate multiple files.

cat filename.txt

## 9. `cp` (Copy)

To copy files from one place to another, `cp` is the utility you'll use. It can also be used to copy entire directories with the `-r` option:

cp source.txt destination.txt  
cp -r source_directory new_directory

## 10. `mv` (Move)

The `mv` command is used to move or rename files and directories. It's a powerful tool for organizing files or changing their names:

mv oldname.txt newname.txt  
mv file.txt /path/to/directory/

## 11. `**chmod**` **(Change Mode)**

`chmod` changes the file mode bits of each given file according to mode, which can be either a symbolic representation of changes to make, or an octal number representing the bit pattern for the new mode bits.

chmod 755 script.sh

## 12. `**man**` **(Manual)**

Whenever you need more information about any command, `man` brings up a detailed manual page. It’s a great resource for learning command syntax, options and other details:

man ls

## **13. ln (Link)**

The `ln` command is used to create hard and symbolic links. A hard link is another name for an existing file, while a symbolic link (or symlink) is a reference to another file or directory.

- `ln source_file link_name`: Creates a hard link.
- `ln -s source_file symlink_name`: Creates a symbolic link.

ln file.txt hardlink.txt  
ln -s /path/to/file symlink

## **14. clear (Clear Screen)**

The `clear` command clears the terminal screen, providing a clean slate for your next set of commands. This is useful for improving readability and reducing clutter in the terminal.

clear

## **15. echo (Echo)**

The `echo` command displays a line of text or a variable value. It is often used in scripts to output status messages or variable values.

echo "Hello, World!"

 