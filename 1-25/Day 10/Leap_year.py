

def is_leap_year(year) : 
    """Takes the year number and determine if the year is leap year or not"""
    leap_flag = False
    if year % 4 == 0 :
        leap_flag = True
        if year % 100 == 0 : 
            leap_flag = False 
            if year % 400 == 0 :
                leap_flag = True
    return leap_flag

print(is_leap_year(2000))