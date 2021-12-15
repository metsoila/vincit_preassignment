import json_read


def task(date_obj):

    prices = json_read.retrieve_list(date_obj.get_dates(), 'prices')

    return find_longest_bearish(prices)


def find_longest_bearish(prices):
    max_bearish = 0
    current_bearish = 0
    previous_price = 0

    for values in prices:

        if float(values[1]) < previous_price:
            current_bearish += 1
            
        else:
            current_bearish = 0

        if (max_bearish < current_bearish):
            max_bearish = current_bearish

        previous_price = float(values[1])

    return max_bearish



            



