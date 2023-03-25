l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
add=[]
for i in l1:
    for j in l2:
        if l1.index(i)==l2.index(j):
            add.append(i+j)
    
print("sum of lists=\n",add)