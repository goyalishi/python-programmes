inp=input("enter the string")
ch=input("enter the character whose occurence is to be known:")
ls=[]
count=0
for i in inp:
    count+=1
    if i==ch:
        ls.append(count-1)
for i in ls:
    print(i)
        

