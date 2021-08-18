from collections import namedtuple
from datetime import datetime
import json

blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

blog_nt = namedtuple('blog_nt', (key for key in blog.keys()))


def dict2nt(dict_):
    return blog_nt(**dict_)


def nt2json(nt):
    return json.dumps(nt._asdict(), default=str)
