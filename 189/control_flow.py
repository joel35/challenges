IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    filtered = []
    for name in names:
        if len(filtered) == MAX_NAMES:
            break
        if name[0] == QUIT_CHAR:
            break
        if name[0] == IGNORE_CHAR:
            continue
        if not name.isalpha():
            continue
        filtered.append(name)
    return filtered

