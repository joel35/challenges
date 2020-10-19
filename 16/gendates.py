from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    date = PYBITES_BORN
    count = 1
    count2 = 1
    while True:
        birthday = date.replace(year=date.year + count)
        hundred_days = datetime(date.year, date.month, date.day) + timedelta(days=count2 * 100)

        if birthday <= hundred_days:
            count += 1
            yield birthday
        else:
            count2 += 1
            yield hundred_days


