def get_index_different_char(chars):
    alphanumeric = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    alpha = [char for char in chars if str(char) in alphanumeric and char != '']
    not_alpha = [char for char in chars if str(char) not in alphanumeric or char == '']
    diff_item = not_alpha if len(alpha) > len(not_alpha) else alpha

    for index, item in enumerate(chars):
        if item in diff_item:
            return index

