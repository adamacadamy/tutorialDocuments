#!/bin/bash

name="Adam"

echo "Hello, World ${name}"

read -p "Enter your name: " user_name

echo "Hello, ${user_name}"

read -p "Enter your age: " user_age

if [ $user_age -eq 20 ]; then
    echo "You are to old" 
elif [ $user_age -eq 30 ]; then 
    echo "Option 2 selected."
else 
    echo  "Hmmm?"
fi

for i in {1..5}; do
    echo "Iteration $i"
done

count=1

while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done

count=1
until [ $count -gt 5 ]; do
    echo "Count: $count"
    ((count++))
done
 