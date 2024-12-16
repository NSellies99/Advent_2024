import os
from pathlib import Path
import re

WORD = ["X", "M", "A", "S"]


def search_word():
    crossword = load_crossword()
    
    kernel = [(-1,-1,), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

    width, height = crossword.index("\n"), crossword.count("\n") + 1
    squashed_data = crossword.replace("\n", "")
    crossword_list = list(crossword.split("\n"))
    
    words_found = 0
    for match in re.compile("X").finditer(squashed_data):
        position = match.start() % width
        line = int(match.start() / width)

        for line_mod, position_mod in kernel:
            for word_idx in range(len(WORD)):
                check_line = line + line_mod * word_idx
                check_position = position + position_mod * word_idx
                if (not 0 <= check_line < height or not 0 <= check_position < width
                    or crossword_list[check_line][check_position] != WORD[word_idx]):
                    break
            else:
                words_found += 1
        
    print(f"Found {"".join(WORD)} {words_found} times.")

def load_crossword() -> str:
    crossword_path = Path(os.path.dirname(os.path.realpath(__file__))) / "crossword.txt"
    with open(crossword_path, "r") as crossword:
        return crossword.read()

search_word()