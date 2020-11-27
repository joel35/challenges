from pytz import timezone, utc
from datetime import datetime

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""

    print(naive_utc_dt)
    print(utc.zone)

    AUSTRALIA.zone

    return AUSTRALIA.zone, SPAIN.zone


naive_utc_dt = datetime(2018, 4, 27, 22, 55, 0)

if __name__ == '__main__':
    aus_dt, es_dt = what_time_lives_pybites(naive_utc_dt)
    print(aus_dt, es_dt)
