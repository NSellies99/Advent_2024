import os
from pathlib import Path
import re

WORD = ["X", "M", "A", "S"]

CROSS_KERNEL = [(-1,-1), (-1,1), (1,-1), (1,1)]

CROSSWORD_KERNEL = [(-1,-1,), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def search_xmas():
    """Searches for all instances of the word XMAS in the crossword"""
    crossword = load_crossword()
    
    width, height = crossword.index("\n"), crossword.count("\n") + 1
    
    # Construct a squashed version for getting letter positions and a list for searching
    squashed_data = crossword.replace("\n", "")
    crossword_list = list(crossword.split("\n"))
    
    words_found = 0
    # Starts looking at X, as other parts would not be important
    for match in re.compile("X").finditer(squashed_data):
        position = match.start() % width
        line = int(match.start() / width)
        
        # Uses the modifiers in the kernel to check 
        # neighbouring lines and positions for parts of the word
        for line_mod, position_mod in CROSSWORD_KERNEL:
            for word_idx in range(len(WORD)):
                check_line = line + line_mod * word_idx
                check_position = position + position_mod * word_idx
                if (not 0 <= check_line < height or not 0 <= check_position < width
                    or crossword_list[check_line][check_position] != WORD[word_idx]):
                    break
            else:
                words_found += 1
        
    print(f"Found XMAS {words_found} times.")

def search_x_mas():
    """Searches for all instances of a cross shaped MAS in the crossword"""
    crossword = load_crossword()
    
    width, height = crossword.index("\n"), crossword.count("\n") + 1

    # Construct a squashed version for getting letter positions and a list for searching
    squashed_data = crossword.replace("\n", "")
    crossword_list = list(crossword.split("\n"))

    x_mas_found = 0

    # Use A as a hub to look around
    for match in re.compile("A").finditer(squashed_data):
        position = match.start() % width
        line = int(match.start() / width)

        found_s: list[tuple[int, int]] = []
        found_m: list[tuple[int, int]] = []

        # Uses the kernel to look for S and M around the A
        for line_mod, position_mod in CROSS_KERNEL:
            check_line = line + line_mod
            check_position = position + position_mod
            if (0 <= check_line < height and 0 <= check_position < width):
                # Save the position to compare to the other instance of the character
                if crossword_list[check_line][check_position] == "S":
                    found_s.append((line_mod, position_mod))
                elif crossword_list[check_line][check_position] == "M":
                    found_m.append((line_mod, position_mod))
        
        if check_chars(found_s) and check_chars(found_m):
            x_mas_found += 1

    print(f"Found x shaped mas {x_mas_found} times.")

def check_chars(chars: list[tuple[int, int]]) -> bool:
    """Checks if both characters in the cross mas are on the same line or side"""
    return (
        len(chars) == 2 and (chars[0][0] == chars[1][0] or chars[0][1] == chars[1][1])
    )
                    
def load_crossword() -> str:
    """Loads crossword from file"""
    crossword_path = Path(os.path.dirname(os.path.realpath(__file__))) / "crossword.txt"
    with open(crossword_path, "r") as crossword:
        return crossword.read()

search_xmas()
search_x_mas()
