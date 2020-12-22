import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    d_count = 0
    f_count = 0

    for _, d, f in os.walk(directory):

        d_count += len(d)
        f_count += len(f)

    return d_count, f_count
