import datetime


def tomorrow(date=None):
    today = datetime.date.today() if not date else date
    return today + datetime.timedelta(days=1)

