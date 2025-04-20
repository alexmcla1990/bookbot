from collections import Counter

def word_count(file_contents) -> int:
    book_to_list = file_contents.split()
    #print(book_to_list)
    count = len(book_to_list)
    print(f"Found {count} total words")


def char_count(file_contents) -> list:
    chars = [char for char in file_contents.lower() if "a" <= char <= 'z']
    letter_counts = Counter(chars)
    return letter_counts

def sort_data(file_contents) -> str:
    print(f"----------- Word Count ----------")
    word_count(file_contents)
    print(f"--------- Character Count -------")
    letter_dict = char_count(file_contents)
    for char, count in letter_dict.most_common():
        print(f"{char}: {count}")
    print(f"============= END ===============")