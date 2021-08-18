from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)


class UserDoesNotExist(Exception):
    print('User does not exist')


class UserNoPermission(Exception):
    print('No user permission')


class UserAccessExpired(Exception):
    print('Access expired')


def get_secret_token(username):
    my_user = None

    for user in USERS:
        if username == user.name:
            my_user = user

    if not my_user:
        raise UserDoesNotExist()

    if my_user.expired:
        raise UserAccessExpired()

    if my_user.role != ADMIN:
        raise UserNoPermission()

    return SECRET

