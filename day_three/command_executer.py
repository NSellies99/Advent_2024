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

        # Pattern for detecting the mul() commands
        command_pattern = re.compile(r"(don't\(\))|(do\(\))|(mul\(\d+,\d+\))")

        # Pattern for detecting the parameters inside a mul command
        parameters_pattern = re.compile(r"\d+")

        total_sum = 0
        execute_commands = True
        for command_match in command_pattern.finditer(commands):
            command = command_match.group()
            match(command):
                case "don't()":
                    execute_commands = False
                case "do()":
                    execute_commands = True
                case _:
                    if execute_commands:
                        digits = parameters_pattern.findall(command)
                        total_sum += reduce(lambda x,y: int(x) * int(y), digits)
    
    print(f"Total command sum is {total_sum}")

execute_multiply_commands()