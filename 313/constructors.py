import re


class DomainException(Exception):
    """Raised when an invalid is created."""


class Domain:

    def __init__(self, name):
        self.name = self.check_name(name)

    @staticmethod
    def check_name(name):
        if not re.match(r'.*\.[a-z]{2,3}$', name):
            raise DomainException('Invalid domain name')
        return name

    def __str__(self):
        return self.name

    @classmethod
    def parse_url(cls, url):
        return Domain(url.split('/')[2])

    @classmethod
    def parse_email(cls, email):
        return Domain(email.split('@')[1])
