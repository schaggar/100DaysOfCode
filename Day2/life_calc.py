year = 365
months = 12
weeks = 52
max_days = 90*year
max_months = 90*months
max_weeks = 90*weeks
age = float(input("Enter your age:"))

yourdays = int(age*year)
yourmonth = int(age*months)
yourweeks = int(age*weeks)

days_left = int(max_days-yourdays)
months_left = int(max_months-yourmonth)
weeks_left = int(max_weeks-yourweeks)

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left")
