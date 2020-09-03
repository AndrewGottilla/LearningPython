number1 = 6
number2 = 2
number3 = 6 + 2

# WILL NOT WORK: print(number1 + " + " + number2 + " = " + number3)
# Tell Python to handle integer values as strings using str() method
print(str(number1) + " + " + str(number2) + " = " + str(number3))

# 6 / 2
print(str(number1) + " / " + str(number2) + " = " + str(number1/number2))

# 6 * 2
print(str(number1) + " * " + str(number2) + " = " + str(number1*number2))

# Exponentials
print(str(number1) + "^" + str(number2) + " = " + str(number1**number2))
print(str(number1) + "^" + str(number3) + " = " + str(number1**number3))

# Order of Operations
print("6 + 2 * 8 = " + str(6 + 2 * 8))
print("(6 + 2) * 8 = " + str((6 + 2) * 8))