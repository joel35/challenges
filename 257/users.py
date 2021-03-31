import re


def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    lines = [line.split(':') for line in passwd.strip().splitlines()]

    return {
        user: re.sub(",+", ' ', name).strip() or 'unknown'
        for (user, name)
        in zip([line[0] for line in lines], [line[4] for line in lines])
    }
