import json
import re


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""

    movies = []

    for file in files:
        with open(file) as json_file:
            data = json.load(json_file)
            movies.append(data)
    return movies


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        if 'Comedy' in movie.get('Genre'):
            return movie.get('Title')


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""

    nominations = [
        (movie.get('Title'), int(re.split(r'(\d+).nominations', movie.get('Awards'))[1]))
        for movie in movies
    ]
    return sorted(nominations, key=lambda movie: movie[1])[-1][0]


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    runtimes = [
        (movie.get('Title'), int(movie.get('Runtime').split()[0]))
        for movie in movies
    ]
    return sorted(runtimes, key=lambda movie: movie[1])[-1][0]
