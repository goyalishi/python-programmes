inp=input()
emp=[]
freq=[]
for i in inp:
    if i not in emp:
        emp.append(i)
        c=inp.count(i)
        freq.append(c)
l=len(emp)
for i in range(l):
    print(emp[i],":",freq[i])


