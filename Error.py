try:
    num1 = int(input("Enter any number"))
    num2 = int(input("Enter any number"))
    result = num1/num2
    print("result is:", result)
    print("result is:", result1)
except ZeroDivisionError:
 print("Division with 0 is not acceptable")
except ValueError:
 print("Please enter a whole number")
except NameError as ex:
 print("The exception is", ex)


except:
  print("Some error occured")
finally:
  print("I will execute the code")