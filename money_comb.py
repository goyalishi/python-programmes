''' python program to print no of notes needed of diff combinations for the entered amount'''

a=2000
b=500
c=200
d=100
amt=int(input("Enter the amount"))
amt=amt-100
twok=amt//a
amt=amt%a
fiveh=amt//b
amt=amt%b 
twoh=amt//c 
amt=amt%c 
hun=(amt//d)+1 
print("no of Two thousand rupee notes needed=%d\n"%twok)
print("no of five hundred rupee notes needed=%d\n"%fiveh)
print("no of two hundred rupee notes needed=%d\n"%twoh)
print("no of Two thousand rupee notes needed=%d"%hun)
