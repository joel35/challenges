MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.birthdays = {}

    def __setitem__(self, name, birthday):
        matching_bd = ((b.day, b.month) == (birthday.day, birthday.month)
                       for b
                       in self.birthdays.values())

        print(MSG.format(name)) if any(matching_bd) else None

        self.birthdays[name] = birthday
