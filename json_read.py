from urllib.request import urlopen
import datetime
import json

def retrieve_list(dates, key_word):

    from_date = str(min(dates))
    to_date = str(max(dates))

    url = ("https://api.coingecko.com/api/v3/coins/bitcoin/" +
                "market_chart/range?vs_currency=eur&from=" +
                from_date + "&to=" + to_date)

    response = urlopen(url)

    json_data = json.loads(response.read())

    list = json_data[key_word]

    return data_per_day(list)


def data_per_day(json_data):

    data_of_day = []

    for pair in json_data:
        dt = datetime.datetime.utcfromtimestamp(pair[0]/1000)

        hour = int(dt.strftime("%H"))
        min = int(dt.strftime("%M"))

        #Find the data closest to midnight
        if (hour == 0 and min < 29) or (hour == 23 and min > 31):
            data_of_day.append(pair)

    return data_of_day
