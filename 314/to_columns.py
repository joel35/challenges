from typing import List  # not needed when we upgrade to 3.9


def print_names_to_columns(names: List[str], cols: int = 2) -> None:
    for i, name in enumerate(names, start=1):
        print(f'| {name}\t'.expandtabs(12), end='\n' if not i % cols else '')
