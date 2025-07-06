

def store(price):

    taxSum = (price * tax)
    
    if price < 100 and price > 0:
        discount = price * 0
        sum = price  - discount + taxSum
        print(f"Your tax amount is {taxSum}")
        print(f"Your total amount was {price + taxSum}")
        print(f"Your saving is ${discount}")
    elif price >= 100 and price < 200:
        discount = price * 0.10
        
        sum = price  - discount + taxSum
        print(f"Your tax amount is {taxSum}")
        print(f"Your total amount was {price + taxSum}")
        print(f"Your saving is ${discount}")  
    elif price > 200:
        discount = price * 0.20
        
        sum = price  - discount + taxSum
        print(f"Your tax amount is {taxSum}")
        print(f"Your total amount was {price + taxSum}")
        print(f"Your saving is ${discount}")
    return sum    



tax = 0.08
discount = 0

money= store(int(input("Enter amount: ")))

print(money)
