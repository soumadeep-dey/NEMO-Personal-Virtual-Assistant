import datetime as dt
#Directive of datetime:
    #H: 24, I: 12, M: min, S: sec, p: am/pm
    #A,a: day, B,b: Month, d: date no, Y: year, w: week no.

def check_datetime(command):
    if 'time' in command:    
        current_time = dt.datetime.now().strftime('%I:%M %p')
        return f"Current time is {current_time}."

    elif 'date' in command:
        current_date = dt.date.today().strftime("%dth %B %Y")
        return f"Today is {current_date}."
    
    elif 'day' in command:
        current_day = dt.date.today().strftime("%A")
        return f"Today is {current_day}."
    
    elif 'year' in command:
        current_year = dt.date.today().strftime("%Y")
        return f"This is {current_year}."
    
    elif 'week' in command:
        current_date = dt.date.today().strftime("%w")
        return f"This is week {current_date}."
    
# print(check_datetime('year'))