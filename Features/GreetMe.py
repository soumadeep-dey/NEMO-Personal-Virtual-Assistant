import datetime

def greet():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        return f"Good Morning,"
    
    elif hour > 12 and hour < 17:
        return f"Good Afternoon,"

    else:
        return f"Good Evening,"
