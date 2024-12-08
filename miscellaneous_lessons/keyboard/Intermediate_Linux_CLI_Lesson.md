
# Intermediate Linux Terminal CLI Lesson

---

## **1. Advanced File Manipulation**
- **Find files and directories:**
  ```bash
  find <directory> -name <file_name>
  find <directory> -type d -name <dir_name>  # Find directories
  ```

- **Search within files:**
  ```bash
  grep -i "search_term" <file_name>       # Case-insensitive search
  grep -r "search_term" <directory_name> # Recursive search in a directory
  ```

- **Concatenate and view files (cat):**
  ```bash
  cat <file_name>           # View file contents
  cat <file1> <file2>       # Concatenate files
  cat > <file_name>         # Write to a file (Ctrl+D to save)
  ```

- **Display file contents with line numbers:**
  ```bash
  cat -n <file_name>
  ```

---

## **2. Output and Text Creation**
- **echo** (Print text or variables to the terminal):
  ```bash
  echo "Hello, World!"                # Print text
  echo $HOME                          # Print environment variable
  echo "This is a test" > file.txt    # Write text to a file
  echo "Append this" >> file.txt      # Append text to a file
  ```

- **Use echo with colors (example):**
  ```bash
  echo -e "\033[1;32mThis is green text\033[0m"
  ```

---

## **3. Bash Scripting with Variables**
- **Declare and use variables:**
  ```bash
  # Define a variable
  NAME="John"
  
  # Use the variable
  echo "Hello, $NAME"
  ```

- **Positional parameters (script arguments):**
  ```bash
  # Access script arguments
  echo "First argument: $1"
  echo "Second argument: $2"
  ```

- **Special variables:**
  ```bash
  echo "Script name: $0"     # Script name
  echo "Number of args: $#"  # Number of arguments
  echo "All arguments: $@"   # All arguments
  ```

---

## **4. Bash Scripting with Functions**
- **Define and call functions:**
  ```bash
  # Define a function
  greet() {
      echo "Hello, $1!"
  }
  
  # Call the function
  greet "Alice"
  ```

- **Return values from functions:**
  ```bash
  add() {
      local sum=$(( $1 + $2 ))
      echo $sum
  }

  result=$(add 5 10)
  echo "Sum: $result"
  ```

---

## **5. Bash Scripting with Arrays**
- **Define and access arrays:**
  ```bash
  # Define an array
  NUMBERS=(1 2 3 4 5)
  
  # Access elements
  echo "First element: ${NUMBERS[0]}"
  
  # Access all elements
  echo "All elements: ${NUMBERS[@]}"
  ```

- **Loop through arrays:**
  ```bash
  for num in "${NUMBERS[@]}"; do
      echo "Number: $num"
  done
  ```

---

## **6. Control Structures in Bash**
- **Conditional statements:**
  ```bash
  if [ $1 -gt 10 ]; then
      echo "Number is greater than 10"
  else
      echo "Number is 10 or less"
  fi
  ```

- **Case statements:**
  ```bash
  case $1 in
      start)
          echo "Starting the service..."
          ;;
      stop)
          echo "Stopping the service..."
          ;;
      *)
          echo "Unknown command"
          ;;
  esac
  ```

- **Loops:**
  ```bash
  # While loop
  count=1
  while [ $count -le 5 ]; do
      echo "Count: $count"
      ((count++))
  done
  
  # For loop
  for i in {1..5}; do
      echo "Number: $i"
  done
  ```

---

## **7. Debugging Bash Scripts**
- **Run a script in debug mode:**
  ```bash
  bash -x script.sh
  ```

- **Add debug output in scripts:**
  ```bash
  set -x  # Enable debugging
  set +x  # Disable debugging
  ```

---

## **8. Useful Tools**
- **curl** (Make HTTP requests):
  ```bash
  curl -I <url>          # Fetch headers
  curl -O <url>          # Download a file
  ```

- **wget** (Download files):
  ```bash
  wget <url>
  ```

- **awk** (Pattern scanning and processing):
  ```bash
  awk '{print $1}' <file_name>    # Print the first column
  ```

- **sed** (Stream editor for text manipulation):
  ```bash
  sed 's/old/new/g' <file_name>   # Replace 'old' with 'new'
  ```

---

