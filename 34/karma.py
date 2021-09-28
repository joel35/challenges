from collections import namedtuple
from datetime import datetime

Transaction = namedtuple('Transaction', 'giver points date')
# https://twitter.com/raymondh/status/953173419486359552
Transaction.__new__.__defaults__ = (datetime.now(),)


class User:
    def __init__(self, name: str):
        self.name = name
        self._transactions = []

    def __add__(self, transaction: Transaction):
        self._transactions.append(transaction)

    def __str__(self):
        return f"{self.name} has a karma of {self.karma} and {self.fans} fan{'s' if self.fans > 1 else ''}"

    @property
    def karma(self):
        return sum(self.points)

    @property
    def points(self):
        return [t.points for t in self._transactions]

    @property
    def fans(self):
        return len({t.giver for t in self._transactions})
