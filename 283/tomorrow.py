import datetime


def tomorrow(date=None):
    today = date or datetime.date.today()
    return today + datetime.timedelta(days=1)

