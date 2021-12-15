import json_read

def task(date_obj):

    prices = json_read.retrieve_list(date_obj.get_dates(), 'prices')

    return find_maximum_profit(prices)

def find_maximum_profit(prices):
    index = 0
    highest_percentage = 0
    dates_and_percentage = []

    for daily in prices:
        for i in range(index, len(prices)):
            current_percentage = prices[i][1]/daily[1]*100

            if (current_percentage > highest_percentage):

                highest_percentage = current_percentage
                dates_and_percentage = [float(daily[0]), #date
                                        float(prices[i][0]), #date
                                        float(highest_percentage)-100]

    return dates_and_percentage