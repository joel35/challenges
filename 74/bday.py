from calendar import weekday, day_name


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    n = weekday(date.year, date.month, date.day)
    return day_name[n]
