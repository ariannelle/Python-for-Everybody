def computepay(hrs, rat):
    if float(hrs) <= 40:
        paycalc = float(hrs) * float(rat)
        return paycalc
    else:
        float(hrs) > 40
        paycalc = ((float(hrs) - 40) * (float(rat) * 1.5)) + (float(rat) * 40)
        return paycalc

hrs = input('Enter hours worked: ')
try: # if hrs worked is non integer
    numhrs = float(hrs)
except:
    print('Error, please enter numeric input')
    quit()

rat = input('Enter rate: ')
try: #if pay is non integer
    numrat = float(rat)
except:
    print('Error, please enter numeric input')
    quit()

pay = computepay(hrs, rat)
print(pay)
