INDENTS = 4


def print_hanging_indents(poem):
    for para in poem.strip().split("\n\n"):
        lines = para.splitlines()
        print(lines[0].strip())
        for line in lines[1:]:
            print(' ' * INDENTS + line.strip())
