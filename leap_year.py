def Leap_Year(year):

#every decision has exactly one True and one False branch, so 100% statement coverage is achieved.

    if year % 4 == 0:
        if year % 100 != 0:
            return True
        if year % 400 == 0:
            return True
        return False
    return False