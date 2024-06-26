def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 'True'
            else:
                return 'False'
        else:
            return 'True'
    else:
        return 'False'


def days_in_month(year, month):
  is_leap(year)
  if is_leap and month == 2:
      return 29
  else:
      month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
      return month_days[month - 1]
