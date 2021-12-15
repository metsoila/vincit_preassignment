import a_task
import b_task
import c_task
import dates


def check_input(input):
    return ()


def main():

    print('\n'+10*'*'+'Scrooge program'+10*'*'+'\n')

    while True:
        user_input = input('Choose assignment (A, B or C) or G for guit: ')

        if (user_input.upper() not in ['A', 'B', 'C', 'G']):
            print('Try again')
            continue

        if user_input in ['G', 'g']:
            print('Bye!\n')
            break

        dates_obj = dates.task_dates()
        input1, input2 = dates_obj.ask_dates()


        if user_input in ['A', 'a']:
            result = a_task.task(dates_obj)

            print("\nIn bitcoin’s historical data from CoinGecko, the price " +
                    f"decreased {result} day(s) in a row at most for the " +
                    f"inputs from between {input1} and {input2}\n")

        #result is a list containing date and the volume
        elif user_input in ['B', 'b']:
            result = b_task.task(dates_obj)
            date = dates.unix_to_date(result[0])

            print(f"\n{date} had the highest trading volume of " +
                    f"{result[1]:.2f} € for the inputs from between " +
                    f"{input1} and {input2}\n")

        #result is a list containing the trading days as first and second
        #and third is the percentage
        elif user_input in ['C', 'c']:
            result = c_task.task(dates_obj)
            print(result)
            date1 = dates.unix_to_date(result[0])
            date2 = dates.unix_to_date(result[1])

            if result[2] == 0:
                print(f'\nValue increases not even once between the given days of '+
                      f"{input1} and {input2}, so any trades should not be done.\n")
            else:
                print(f"\nScrooge should travel to {date1} to buy bitcoin" +
                        f" and sell them on {date2} to have the best profit" +
                        f"-percentage of {result[2]:.2f} %.\n")

        else :
            print("Try again\n")

        



if __name__ == "__main__":
    main()