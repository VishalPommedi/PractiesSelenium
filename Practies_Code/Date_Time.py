from datetime import datetime

def Current_datetime():
    cuurentdatetime = datetime.now()
    Sorted_datetime = cuurentdatetime.strftime("%d-%m-%y %H-%M")

    return Sorted_datetime

