"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import urllib.request

DICTIONARY = os.path.join('/tmp', 'dictionary_m_words.txt')
urllib.request.urlretrieve('http://bit.ly/2Cbj6zn', DICTIONARY)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    word = ''.join(letter.lower() for letter in word if letter.isalpha())
    word_reversed = word[::-1]
    return word == word_reversed


def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    all_words = load_dictionary() if not words else words
    palindromes = [word for word in all_words if is_palindrome(word)]
    return max(palindromes, key=len)
