def Leap_Year(year):
    # leap year is divisible by 4, but not by 100 (unless also amultiple of 100). 
    # '|' is used so BOTH conditions are always evaluated.
    if (year % 4 == 0) | (year % 100 != 0):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return True
        return False
    else:
        return False   # never reachable