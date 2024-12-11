from functools import reduce
import os
from pathlib import Path
import re

commands_file_path = Path(os.path.dirname(os.path.realpath(__file__))) / "commands.txt"

def execute_multiply_commands():
    """
    Executes all multiply commands in the commands file.
    mul() takes two integers and multiplies them together.
    This function prints the sum of all mul commands
    """
    with open(commands_file_path, "r") as commands_file:
        commands = commands_file.read().replace("\n", "")

        command_string = get_startup_commands(commands)
        command_string += "".join(get_enabled_commands(commands))

        # Pattern for detecting the mul() commands
        command_pattern = re.compile(r"(mul\(\d+,\d+\))")

        # Pattern for detecting the parameters inside a mul command
        parameters_pattern = re.compile(r"\d+,\d+")

        total_sum = 0
        for command in command_pattern.findall(command_string):
            digits = parameters_pattern.search(command).group().split(",")
            total_sum += reduce(lambda x,y: int(x) * int(y), digits)
    
    print(f"Total command sum is {total_sum}")

def get_startup_commands(data: str) -> str:
    """
    Gets all commands before the first don't()
    Commands are enabled until don't() disables them
    """
    startup_pattern = re.compile(r".*?(?=don't\(\))")
    return startup_pattern.search(data).group()

def get_enabled_commands(data: str) -> str:
    """
    Gets all commands between do's and don'ts.
    These count as enabled commands
    """
    enable_pattern = re.compile(r"(?<=do\(\))(.*?)(?=don't\(\))")
    return enable_pattern.findall(data)


execute_multiply_commands()