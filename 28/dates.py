import collections
from datetime import datetime
import os
import re
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
RSS_FEED = 'pybites_feed.rss.xml'
PUB_DATE = re.compile(r'<pubDate>(.*?)</pubDate>')
TMP = os.getenv("TMP", "/tmp")


def _get_dates():
    """Downloads PyBites feed and parses out all pub dates returning
       a list of date strings, e.g.: ['Sun, 07 Jan 2018 12:00:00 +0100',
       'Sun, 07 Jan 2018 11:00:00 +0100', ... ]"""
    remote = os.path.join(BASE_URL, RSS_FEED)
    local = os.path.join(TMP, RSS_FEED)
    urlretrieve(remote, local)

    with open(local) as f:
        return PUB_DATE.findall(f.read())


def _remove_timezone(date_str):
    return re.split(r'\s\+|\s-', date_str)[0]


def convert_to_datetime(date_str):
    """Receives a date str and convert it into a datetime object"""
    date_string = _remove_timezone(date_str)
    dt_format = '%a, %d %b %Y %H:%M:%S'
    return datetime.strptime(date_string, dt_format)


def get_month_most_posts(dates):
    """Receives a list of datetimes and returns the month (format YYYY-MM)
       that occurs most"""
    months = [datetime(year=date.year, month=date.month, day=1) for date in dates]
    most_common_month = collections.Counter(months).most_common(1)[0][0]
    return most_common_month.strftime('%Y-%m')
