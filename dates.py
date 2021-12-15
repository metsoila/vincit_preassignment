import datetime
import time

class task_dates():

    def __init__(self):
        self.__dates = []


    def get_dates(self):
        return self.__dates


    def add_date(self, date):
        self.__dates.append(date)


    def ask_dates(self):
        first_input = input("Give first date in form of 'dd.MM.yyyy': ")
        second_input = input("Give second date in form of 'dd.MM.yyyy': ")

        if (not self.check_dates(first_input, second_input)):
            first_input, second_input = self.ask_dates()
            return first_input, second_input
        
        return first_input, second_input


    def check_dates(self, date1, date2):

        for date in [date1, date2]:
            parts = date.split('.')

            if (len(parts) != 3):
                print("\nGive date in form of 'dd.MM.yyyy'\n")
                return False

            try:
                date_time = datetime.date(
                    int(parts[2]),
                    int(parts[1]),
                    int(parts[0]))
                unix_date = int(time.mktime(date_time.timetuple()))

                if unix_date > time.time():
                    print("There's no data from future.. yet.\n")
                    return False

            except ValueError as e:
                print(e)
                return False

            except OverflowError as e:
                print('\nYear out of range.\n')
                return False

            self.__dates.append(unix_date)

        #Adding hours to 'to date', to make sure we get it 
        self.__dates[1] += 10800
        return True

def unix_to_date(unix):
    
    return time.strftime("%d.%m.%Y", time.localtime(int(unix)/1000))
