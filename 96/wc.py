def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""

    with open(file_) as file:
        data = file.read()
        lines = len(data.splitlines())
        words = len(data.split())
        chars = len(list(data))

    return f'{lines}\t{words}\t{chars}\t{file.name}'


if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))
