def get_index_different_char(chars):
    alphanumeric = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    alpha = [char for char in chars if str(char) in alphanumeric]
    not_alpha = [char for char in chars if str(char) not in alphanumeric]
    diff_item = not_alpha if len(alpha) > len(not_alpha) else alpha
    diff_index = -1

    for index, item in enumerate(chars):
        if item in diff_item:
            diff_index = index
    return diff_index

