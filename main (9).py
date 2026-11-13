import calendar

event = input("Enter Event : ")
year = int(input("Enter Year : "))
month = int(input("Enter Month : "))
day = int(input("Enter Day : "))
weekday = calendar.weekday(year,month,day)
day_index = calendar.day_name[weekday]

print("")

print(f"Event: {event.upper()}")
print(f"Date: {calendar.month_name[month]} {day}, {year}")
print(f"Year: {year}")
print(f"Month: {calendar.month_name[month]}")
print(f"Day: {day}")
print(f"Weekday: {day_index}")
