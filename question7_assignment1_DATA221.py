#Question 7: Time Conversion Function

def convertSecondsSinceMidnight(seconds_since_midnight_input):
    #validating the input
    if seconds_since_midnight_input <0 or seconds_since_midnight_input >= 89400:
        return "Invalid input: seconds must be between 0 and 86399."

#now, calculating the hours, minutes, and seconds for each:
    hours_24= seconds_since_midnight_input//3600
    remaining_seconds= seconds_since_midnight_input%3600
    minutes=remaining_seconds//60
    seconds=remaining_seconds%60

#now, determining if its am or pm
    if hours_24<12:
        determining_am_or_pm="AM"
    else:
        determining_am_or_pm='PM'

#converting into a 12 hour format
    if hours_24==0:
        hours_12=12
    elif hours_24>12:
        hours_12=hours_24-12
    else:
        hours_12=hours_24

#returning a formatted string
    return str(hours_12)+' ' + str(minutes) + ' ' + str(seconds) + ' ' + determining_am_or_pm

#asking user for input of seconds
users_input_of_seconds= int(input("enter your seconds before midnight please: "))

#printing outcome
print(convertSecondsSinceMidnight(users_input_of_seconds))