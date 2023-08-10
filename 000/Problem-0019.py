"""
You are given the following information,
but you may prefer to do some research
for yourself.

1. January 1, 1900, was a Monday.
2. 30 days has September, April, June, and November.
3. All the rest have 31,
4. Saving February alone, which has 28, rain or shine.
5. And on leap years, 29.

A leap year occurs on any year evenly divisible by 4,
but not on a century unless it is divisible by 400.

Problem: How many Sundays fell on the first of
the month during the twentieth century
(from January 1, 1901, to December 31, 2000)?
"""


def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def count_first_sundays():
    day_of_week = 2

    count = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if year == 1901 and month == 1:
                day_of_week = (day_of_week + 31) % 7
            elif month in [4, 6, 9, 11]:
                day_of_week = (day_of_week + 30) % 7
            elif month == 2:
                if is_leap_year(year):
                    day_of_week = (day_of_week + 29) % 7
                else:
                    day_of_week = (day_of_week + 28) % 7
            else:
                day_of_week = (day_of_week + 31) % 7

            if day_of_week == 0:
                count += 1

    return count


print(count_first_sundays())
