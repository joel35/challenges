def get_profile(arg=None, name='julian', profession='programmer'):
    if arg is None:
        return f'{name} is a {profession}'
    else:
        raise TypeError
