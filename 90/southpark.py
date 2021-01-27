from collections import Counter, defaultdict
import csv

import requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv'  # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""

    # reader = csv.reader(content)
    # print(reader[0])
    #
    # # data = csv.reader(content)
    # data = content.splitlines()

    csv_reader = csv.reader(content, delimiter=',')

    print(type(content), type(csv_reader))

    # print(writer.writeheader())

    default_dict = defaultdict(Counter)






    # print(data[0])
    # print(data[5])

if __name__ == '__main__':
    season = 1

    content = get_season_csv_file(season)

    get_num_words_spoken_by_character_per_episode(content)
