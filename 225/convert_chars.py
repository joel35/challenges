PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    new_text = ''
    for i in text:
        if i.lower() in PYBITES:
            if i.isupper():
                new_text += i.lower()
            elif i.islower():
                new_text += i.upper()
        else:
            new_text += i
    return new_text
