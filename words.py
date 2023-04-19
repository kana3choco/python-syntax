def print_upper_words(words):
    """"For a list of words, print out each word on a separate line, but in all uppercase"""
    for word in words:
        print(word.upper())

def print_upper_words2(words):
    """It only prints words that start with the letter e (either upper or lowercase)"""

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words3(words, must_start_with):
    """function more general than print_upper_words2: passing in a set of letters, and it only prints words that start with one of those letters"""

    for word in words:
        for char in must_start_with:
            if word.startswith(char):
                print(word.upper())
                break
