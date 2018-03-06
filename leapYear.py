#-*- coding: utf-8 -*-
def LEAP_YEAR(n):
    if (n % 4 == 0) & (n % 100 == 0) & (n % 400 == 0):
        a="윤년"    
    elif (n % 4 == 0) & (n % 100 == 0):
        a="평년"
    elif (n % 4 == 0):
        a="윤년"
    else:
        a="평범한년"
    return a

if __name__ == "__main__":
    print LEAP_YEAR(1988)
    print LEAP_YEAR(1900)
    print LEAP_YEAR(1600)
    print LEAP_YEAR(1994)
