def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    r_strip = len(text.rstrip().split(' '))
    strip = len(text.strip().split(' '))
    return r_strip - strip
