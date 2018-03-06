# -*- coding: utf-8 -*-
"""
16세에서 65세 사이의 그룹은 세금을 내야 한다.
소득이 20,000달러 미만인 사람은 20% 세금을 내야 하고, 그 외 사람은 50% 세금을 내야 한다.
만약 이 사람들 중 아이가 있으면 10% 갑세를 받을 수 있다.
"""
def Tax():
    incm = 30000
    baby = 0
    age = 26
    low_tax = incm*0.2
    high_tax = incm*0.5
    low_tax_baby = (incm*0.2)*1.1
    high_tax_baby = (incm*0.5)*1.1

    if age >= 16  and  age <= 65:
        if incm < 20000 and baby == 0:
            res = "소득의 20% {}달러를 납세하셔야 합니다.".format(low_tax)
        elif incm >= 20000 and baby == 0: 
            res = "소득의 50% {}달러를 납세하셔야 합니다.".format(high_tax)
        elif incm < 20000 and baby >= 1:
            res = "소득의 20% {}달러를 납세하셔야 하지만, 아이가 있어서 {}를 납세하시면 됩니다.".format(low_tax, low_tax_baby)
        elif incm >= 20000 and baby >= 1:
            res = "소득의 50% {}달러를 납세하셔야 하지만, 아이가 있어서 {}를 납세하시면 됩니다.".format(high_tax, high_tax_baby)
    else:
        res = "납세자가 아닙니다."
        
    return res
"""
    if incm < 20000 :
        print incm*0.2
    elif 
    else
        print incm*0.5
"""   
        
if __name__ == "__main__":
    print Tax()
