
# Python Console Application: Detailed Lesson

# Creating a Python console application is a great way to build command-line tools that are both functional 
# and user-friendly. Python provides many libraries and techniques to streamline building a console application, 
# such as argparse, Click, Rich, and more. This lesson will guide you through the process of building a robust 
# console application using these tools.

# 1. What is a Console Application?

# A console application is a program designed to run in a command-line interface (CLI) where users interact with 
# the program by typing commands. Python is ideal for building these applications due to its simplicity and 
# vast ecosystem of libraries.

# 2. Basic Structure of a Python Console Application

# A simple console application involves reading user input, processing it, and outputting the result.

def main():
    print("Welcome to my console application!")
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()

# 3. Using argparse for Command-Line Arguments

# argparse is a standard Python library for handling command-line arguments. It allows users to pass arguments 
# when they run the application, making it more flexible.

import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple console app")
    parser.add_argument('name', type=str, help='Your name')
    args = parser.parse_args()

    print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()

# 4. Using Click for Command-Line Interfaces

# Click is a powerful library for creating beautiful command-line interfaces. It simplifies argument parsing 
# and provides a more user-friendly experience.

import click

@click.command()
@click.option('--name', prompt='Your name', help='The name to greet.')
def hello(name):
    click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    hello()

# 5. Adding Multiple Commands with Click

# You can define multiple commands in one application, similar to CLI tools like git or docker. Each command can 
# have its own set of arguments and options.

import click

@click.group()
def cli():
    pass

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.argument('name')
def greet(count, name):
    for _ in range(count):
        click.echo(f"Hello, {name}!")

@click.command()
@click.argument('filename')
def touch(filename):
    with open(filename, 'w') as f:
        f.write("")
    click.echo(f"File {filename} created.")

cli.add_command(greet)
cli.add_command(touch)

if __name__ == '__main__':
    cli()

# 6. Error Handling in Console Applications

# Error handling in console applications is crucial. You want your program to gracefully inform the user of issues 
# without crashing.

import click

@click.command()
@click.argument('number')
def divide_by_two(number):
    try:
        result = int(number) / 2
        click.echo(f"The result is {result}")
    except ValueError:
        click.echo("Error: Please provide a valid integer.")
    except ZeroDivisionError:
        click.echo("Error: Cannot divide by zero.")

if __name__ == '__main__':
    divide_by_two()

# 7. Using Rich for Better Output

# The Rich library provides advanced formatting options for the terminal, including colored text, tables, and even 
# progress bars.

from rich.console import Console

console = Console()

console.print("This is [bold green]green[/bold green] text!")

# 8. Logging in Console Applications

# It's essential to have a logging mechanism to track what is happening in your console application, especially for 
# debugging or error tracking.

import logging
import click

logging.basicConfig(filename='app.log', level=logging.INFO)

@click.command()
@click.argument('number')
def log_number(number):
    try:
        num = int(number)
        logging.info(f"User provided number: {num}")
        click.echo(f"Logged the number: {num}")
    except ValueError:
        logging.error("Invalid number provided")
        click.echo("Error: Please provide a valid number.")

if __name__ == '__main__':
    log_number()

# 9. Testing Console Applications

# Testing console applications is critical to ensure they behave as expected. You can use pytest along with Click's 
# testing utilities to test CLI apps.

import click
from click.testing import CliRunner
import pytest

@click.command()
@click.argument('name')
def greet(name):
    click.echo(f"Hello, {name}!")

def test_greet():
    runner = CliRunner()
    result = runner.invoke(greet, ['Alice'])
    assert result.exit_code == 0
    assert result.output == 'Hello, Alice!\n'

if __name__ == '__main__':
    pytest.main()

# 10. Deploying a Python Console Application

# Once you've built your console application, you can distribute it using setuptools and configure it to be run as 
# a command.

# setup.py example

# from setuptools import setup

# setup(
#     name='mycli',
#     version='1.0',
#     py_modules=['app'],
#     install_requires=[
#         'Click',
#     ],
#     entry_points='''
#         [console_scripts]
#         mycli=app:cli
#     ''',
# )

# 11. Advanced Topics: Subcommands and Configuration Files

# You can create more complex applications with subcommands, configuration files, and environment variables.

import click
import json

@click.group()
def cli():
    pass

@click.command()
@click.argument('key')
@click.argument('value')
def set_config(key, value):
    config = {}
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        pass

    config[key] = value
    with open('config.json', 'w') as f:
        json.dump(config, f)

    click.echo(f"Config {key} set to {value}")

@click.command()
@click.argument('key')
def get_config(key):
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        value = config.get(key, 'Not set')
        click.echo(f"{key}: {value}")
    except FileNotFoundError:
        click.echo("Config file not found.")

cli.add_command(set_config)
cli.add_command(get_config)

if __name__ == '__main__':
    cli()

# This application stores key-value pairs in a configuration file and allows you to set and retrieve configuration data.

