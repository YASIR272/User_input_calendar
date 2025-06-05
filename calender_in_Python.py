import calendar

# User input
year = int(input("Please enter year (e.g., 2024): "))
month = int(input("Please enter month (1-12): "))

# Monthly calendar
print("\nMonthly Calendar:")
print(calendar.month(year, month))

# Ask if user also wants the full year
show_year = input("Would you like to see the full calendar for the year? (yes/no): ").strip().lower()
if show_year == "yes":
    print("\nYearly Calendar:")
    print(calendar.calendar(year))



# Automatic month & year code

# month = datetime.datetime.now().month
# year = datetime.datetime.now().year
# result = calendar.month(year,month)
# result2 = calendar.calendar(year)
# print(result)
# print(result2)