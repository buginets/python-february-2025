# years=int(input("Enter number of years: "))

# units=input("""
# Choose unit: 
# 1 - days
# 2 - weeks
# 3 - hours 
#  """)


# if units == "1":
#     print(f"In {years} years there are {365*years} days")
# elif units == "2":
#     print(f"In {years} years there are {52*years} weeks")
# elif units == "3":  
#     print(f"In {years} years there are {365*years*24} hours")
# else:
#     print("Incorect input! Please chhose between 1 , 2 and 3")   

        # TASK !
age = int(input("Please enter your age: "))  

if age < 13:
    print(f"You are {age} years old and you are child")
elif age >= 13 and age < 18:
     print(f"You are {age} years old and you are teenager") 
elif age >= 18 and age < 65:
     print(f"You are {age} years old and you are adult")  
elif age >= 65 :
     print(f"You are {age} years old and you are elder") 
else:
    print("Please enter coorrcet number")   

    # TASK 2

tip = int(input("""
Please select your tip amount: 
1 - 15%
2 - 18%
3 - 20%
4 - Enter a different amount
"""))


if tip == 1:
  print("standart")
elif tip == 2:
  print("good")
elif tip == 3:
  print("great")
elif tip >=20:
  print("my hero")         