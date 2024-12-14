# Bash Scripting Tutorial

This lesson provides a comprehensive guide to understanding and creating Bash scripts, focusing on practical examples and common use cases.

---

## **1. What is a Bash Script?**

A Bash script is a text file containing a series of commands that the Bash shell can execute. Bash scripts automate repetitive tasks, configure systems, and simplify workflows.

### **Basic Script Structure**
A Bash script typically starts with a shebang (`#!/bin/bash`), which specifies the script interpreter.

Example:
```bash
#!/bin/bash
# This is a comment

echo "Hello, World!"
```

---

## **2. Creating and Running a Bash Script**

### **a. Create a Script File**
1. Use a text editor to create a file (e.g., `script.sh`):
   ```bash
   nano script.sh
   ```
2. Add your commands to the file.

### **b. Make the Script Executable**
Set execute permissions on the script:
```bash
chmod +x script.sh
```

### **c. Run the Script**
Execute the script using:
```bash
./script.sh
```
Alternatively, run it with the Bash interpreter:
```bash
bash script.sh
```

---

## **3. Variables in Bash**

### **a. Defining Variables**
```bash
name="Alice"
echo "Hello, $name!"
```

### **b. Reading User Input**
```bash
read -p "Enter your name: " user_name
echo "Hello, $user_name!"
```

### **c. Command Substitution**
```bash
current_date=$(date)
echo "Today is $current_date"
```

---

## **4. Conditional Statements**

### **a. if-else Statement**
```bash
if [ condition ]; then
    # Commands if true
else
    # Commands if false
fi
```
Example:
```bash
if [ -f file.txt ]; then
    echo "file.txt exists."
else
    echo "file.txt does not exist."
fi
```

### **b. elif Statement**
```bash
if [ $1 -eq 1 ]; then
    echo "Option 1 selected."
elif [ $1 -eq 2 ]; then
    echo "Option 2 selected."
else
    echo "Invalid option."
fi
```

---

## **5. Loops**

### **a. for Loop**
```bash
for i in {1..5}; do
    echo "Iteration $i"
done
```

### **b. while Loop**
```bash
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done
```

### **c. until Loop**
```bash
count=1
until [ $count -gt 5 ]; do
    echo "Count: $count"
    ((count++))
done
```

---

## **6. Functions**

### **a. Defining a Function**
```bash
function greet() {
    echo "Hello, $1!"
}

# Call the function
greet "Alice"
```

### **b. Return Values**
```bash
function add() {
    echo $(($1 + $2))
}

result=$(add 5 3)
echo "Result: $result"
```

---

## **7. File Operations**

### **a. Check if a File Exists**
```bash
if [ -f file.txt ]; then
    echo "file.txt exists."
else
    echo "file.txt does not exist."
fi
```

### **b. Read a File Line by Line**
```bash
while IFS= read -r line; do
    echo "$line"
done < file.txt
```

### **c. Write to a File**
```bash
echo "This is a line of text." > output.txt
```

---

## **8. Script Arguments**

### **a. Accessing Arguments**
- `$0`: Script name.
- `$1`, `$2`, ...: Positional arguments.
- `$@`: All arguments.
- `$#`: Number of arguments.

Example:
```bash
#!/bin/bash
echo "Script name: $0"
echo "First argument: $1"
echo "All arguments: $@"
echo "Number of arguments: $#"
```

### **b. Handling Missing Arguments**
```bash
if [ $# -lt 1 ]; then
    echo "Usage: $0 <arg1> [arg2]"
    exit 1
fi
```

---

## **9. Debugging Scripts**

### **a. Enable Debug Mode**
Run the script with `-x` to see command execution:
```bash
bash -x script.sh
```

### **b. Add Debugging Statements**
```bash
echo "Debug: Current value of count is $count"
```

---

## **10. Practice Exercises**

1. Write a script to print "Hello, World!".
2. Create a script to check if a file exists and display its size.
3. Write a script that accepts a number as input and prints its factorial.
4. Create a script that counts the number of lines in a file.
5. Write a script to back up a directory to a `.tar.gz` file.

 