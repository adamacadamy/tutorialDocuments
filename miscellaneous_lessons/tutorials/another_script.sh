#!/bin/bash
 
function greet(){
    echo  "Hello, $1 $2"
}

greet "adam" "fuzum"
 
function add(){
    echo $((${1} + ${2}))
}

add 5 5

result=$(add 5 5)

echo $result

if [ -f file.txt ]; then 
    echo "file.txt  exists."
else  
    echo "file.txt does not exist."
fi

while IFS= read -r this_line; do
    echo "${this_line}"
done <  file.txt


echo "ዓወት፥ ካሕሰ እወ ኣይትበል" > output.txt