import requests

STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off, multiply by 1,000 and return
         value as float"""

    if cap != 'n/a':
        return float(cap.strip('$MB')) if 'M' in cap else float(cap.strip('$MB')) * 1000
    return 0


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""

    cap_sum = 0

    for i in data:
        if i['industry'] == industry:
            cap_sum += _cap_str_to_mln_float(i['cap'])

    return round(cap_sum, 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""

    highest_cap = 0
    highest_cap_symbol = ''

    for i in data:
        cap = _cap_str_to_mln_float(i['cap'])
        if cap > highest_cap:
            highest_cap, highest_cap_symbol = (cap, i['symbol'])

    return highest_cap_symbol


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""

    



if __name__ == '__main__':
    print(get_industry_cap("Business Services"))
