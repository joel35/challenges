class Person:
    def __str__(self):
        return 'I am a person'


class Mother(Person):
    def __str__(self):
        return f'{super().__str__()} and awesome mom'


class Father(Person):
    def __str__(self):
        return f'{super().__str__()} and cool daddy'


class Child(Father, Mother):
    def __str__(self):
        return 'I am the coolest kid'
