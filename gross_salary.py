'''
Gross salary is the amount received by an employee without any tax deductions.
Net salary is the amount that an individual receives after all deductions have been taken out.
Gross salary = Basic salary + HRA + DA+ Other allowances.
Net salary = Gross salary - Income tax - Provident Fund - Professional tax.
'''
# HRA =House rent allowance
# DA = Dearness allowance
bs=float(input("Enter the basic salary:"))    # bs=basic salary 
if  bs<=10000:
    hra=0.2*bs
    da=0.8*bs
    
elif bs<=20000:
    hra=0.25*bs
    da=0.9*bs

else:
    hra=0.3*bs
    da=0.95*bs

gs=bs+hra+da
print("Gross Salary=%0.2f rupees"%gs)





    


