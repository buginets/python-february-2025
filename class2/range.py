# Print numbers until 100

n = [0]


for i in n:
    i += 1
    n.append(i)
    if i == 100:
        break
print(*n) 

# or print(i) inside loop block
    

# easier way:

for i in range(100):  #this will print from 0 to 99 (100 numbers total)
    print(i)

for i in range(1,101):  #this will print from 1 to 100
    print(i)

for i in range(1,101,2):  #this will print from 1 to 100 but like this: 1 3 5 7 9 11 ...etc
    print(i)

for i in range(10):
    if i % 2 == 0:      # % is reminder operator, this will print all even numbers like: 0,2,4,6,8
        print(i) 
        
           
