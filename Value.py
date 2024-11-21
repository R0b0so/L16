try:
  X = int(input("Enter any number"))
  print("The number entered is", X)
except ValueError as ex:
  print("Exception:", ex)