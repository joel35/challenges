import os
import urllib.request

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)


def create_chart():
    with open(SAFARI_LOGS, 'r') as f:
        data = [line.lower() for line in f.readlines()]
        date = ''

        for i, line in enumerate(data):
            if 'sending to slack channel' in line:
                line_date = line.split()[0]

                if line_date not in date:
                    print(date)
                    date = line_date + ' '

                date += PY_BOOK if 'python' in data[i - 1] else OTHER_BOOK

        print(date)
