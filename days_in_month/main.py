def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year: int, month: int):
    if month < 1 or month > 12:
        return "Invalid month"
    month_days = [31, 29 if is_leap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return month_days[month - 1]

selected_year = int(input("Select a year: "))
selected_month = int(input("Select a month in numbers: "))

print(days_in_month(year=selected_year, month=selected_month))
