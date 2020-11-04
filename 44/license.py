import secrets
import string


def gen_key(*, parts=4, chars_per_part=8):
    chars = string.ascii_uppercase + string.digits
    return '-'.join(''.join(secrets.choice(chars) for char in range(chars_per_part)) for part in range(parts))
