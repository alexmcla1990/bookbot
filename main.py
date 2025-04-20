
from stats import *
import sys


def get_book_txt(filepath) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    script_name = sys.argv[0]
    num_args = len(sys.argv) - 1

    if num_args < 1:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path_arg = sys.argv[1]
    print(f"Analyzing book found at {file_path_arg}...")
    contents = get_book_txt(file_path_arg)
    sort_data(contents)





if __name__ == "__main__":
    #"books/frankenstein.txt"
    main()