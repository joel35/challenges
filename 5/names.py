NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    deduped = []

    [deduped.append(str.title(name)) for name in names if str.title(name) not in deduped]
    return deduped

def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names_sorted = sorted(names, key=lambda x: x.split()[1], reverse=True)
    return names_sorted


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    shortest = names[0].split()[0]
    for name in names:
        if len(name.split()[0]) < len(shortest):
            shortest = name.split()[0]
    return shortest

# print(dedup_and_title_case_names(NAMES))

# print(sort_by_surname_desc(NAMES))
# print(shortest_first_name(NAMES))
