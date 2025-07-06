

def store(price):
    tax = 0.08
    taxSum = (price * tax)
    
    if price < 100 and price > 0:
        discount = price * 0

    elif price >= 100 and price < 200:
        discount = price * 0.10

    elif price > 200:
        discount = price * 0.20

    sum = price  - discount + taxSum    

    return sum   


money= store(int(input("Enter amount: ")))

print(money)