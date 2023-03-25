# additional 20% surcharge is added to the bill
unit=int(input("enter the electricity units formed"))
if unit<=50:
    bill=unit*0.50
    
elif unit>50 and unit<=150:
    bill=(50*0.50)+((unit-50)*0.75)    

elif unit>150 and unit<=250:
    bill=(50*0.50)+(100*0.75)+(unit-150)*1.20

else:
    bill=(50*0.50)+(100*0.75)+(100*1.20)+(unit-250)*1.50

tot_bill=0.2*bill+bill 
print("Total Electricity Bill=Rs.%0.2f"%tot_bill)
