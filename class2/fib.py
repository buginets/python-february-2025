

limit=int(input("Enter number: "))
n = [0,1]
while n[-1]+ n[-2] < limit:
    s = n[-1] + n[-2]
    n.append(s)
print(*n)    

