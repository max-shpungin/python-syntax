def print_upper_words(words, must_start_with):
    """Accepts a list filled with strings "words" and an object filled with
    characters. Does the following:
    - Determines if word start's with any of the characters provided
    - If so
        - Makes the entire word to uppercase
        - Only prints words that start with "e"
    - Otherwise does nothing
    """
    for word in words:
        if word[0] in must_start_with:
            upper_case_word = word.upper()
            print(upper_case_word)

print_upper_words(
    ["hello", "hey", "goodbye", "yo", "yes"],
    must_start_with={"h", "y"})