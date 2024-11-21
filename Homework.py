try:
    age =int(input("Enter your age"))
    if age <= 15:
        print("you aren't old enough to buy anything")
    else: 
        print("enjoy your shopping trip")
except ValueError as ex:
    print(ex, "is not a real age or number")