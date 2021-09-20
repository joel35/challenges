class Person:
    def __repr__(self):
        return 'I am a person'


class Mother(Person):
    def __repr__(self):
        return f'{super().__repr__()} and awesome mom'


class Father(Person):
    def __repr__(self):
        return f'{super().__repr__()} and cool daddy'


class Child(Father, Mother):
    def __repr__(self):
        return 'I am the coolest kid'
