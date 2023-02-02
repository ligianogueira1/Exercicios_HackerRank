#Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
#Input Format
#Read year, the year to test.

#Constraints
#1900 <= year <= 10**5

def is_leap(year):
    leap = False
    if (year % 4 == 0) and (year % 100 != 0):
        leap = True
    elif (year % 400 == 0) and (year % 100 == 0):
        leap = True
    else:
        pass
    return leap


print(is_leap(2020))
print(is_leap(2022))
