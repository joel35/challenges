import string


def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """

    chars = sorted([word for word in words if word[0] not in string.digits], key=str.lower)
    nums = sorted([word for word in words if word[0] in string.digits], key=str.lower)
    return chars + nums
