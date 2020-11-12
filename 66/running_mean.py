def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""

    means = []
    list = []
    for item in sequence:
        list.append(item)
        means.append(round(sum(list) / len(list), 2))

    return means
