import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    from stats import count_words
    count = count_words(sys.argv[1])
    from stats import character_count
    char_count = character_count(sys.argv[1])
    from stats import dict_sort
    from stats import sort_on
    sorted = dict_sort(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {(sys.argv[1])}")
    print("---------- Word Count ----------")
    print(count)
    print("--------- Character Count -------")
    for item in sorted:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()
