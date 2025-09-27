import datetime


def display_current_datetime():
    current_date = datetime.datetime.now()  
    formatted_dt = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_dt}")
    return current_date


def calculate_future_date(current_date):
    number_of_days = int(input("Enter the number of days to add: "))
    future_date = current_date + datetime.timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")


current_date = display_current_datetime()
calculate_future_date(current_date)
