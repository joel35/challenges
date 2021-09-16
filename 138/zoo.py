import itertools


class Animal:
    sequence = itertools.count(start=10001, step=1)
    animals = []

    def __init__(self, name: str):
        self.animal = f'{next(self.sequence)}. {name.capitalize()}'
        self.animals.append(self.animal)

    def __str__(self):
        return self.animal

    @classmethod
    def zoo(cls):
        return '\n'.join(cls.animals)
