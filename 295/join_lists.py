from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if not lst_of_lst:
        return None

    new_list = lst_of_lst[0]

    for i in lst_of_lst[1:]:
        new_list.append(sep)
        new_list.extend(i)

    return new_list
