from datetime import datetime

def getDays(old_timestamp):
    today = datetime.now()

    # Specify the target date as a string
    target_date_string = old_timestamp

    # Convert the target date string to a datetime object
    date_format = "%Y-%m-%d"
    target_date = datetime.strptime(target_date_string, date_format)

    # Calculate the difference between today's date and the target date
    time_difference =today - target_date 

    # Extract the number of days from the time difference
    days_difference = time_difference.days

    return days_difference
getDays("2023-01-01")