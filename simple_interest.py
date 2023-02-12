p=float(input("enter the principal amount"))
rate=float(input("enter the rate of interest"))
time=float(input("enter the time period"))
si=(p*rate*time)/100
tot_amt=p+si
print('Simple Interest=%f'%si)
print('total amount=%f'%tot_amt)