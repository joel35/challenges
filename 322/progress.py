from datetime import datetime


def ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:

    if not day_of_year:
        today = datetime.today()
        start_of_year = datetime(year=today.year, month=1, day=1)
        day_of_year = (today - start_of_year).days

    read_progress = books_read / books_goal
    year_progress = day_of_year / 365

    return read_progress >= year_progress

