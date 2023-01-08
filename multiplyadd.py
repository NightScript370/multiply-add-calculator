import math

multiplysum = int(input("What is the multiplication sum?"))
additionsum = int(input("What is the addition sum?"))

number1 = -2 * multiplysum / (-1 * additionsum + math.sqrt(additionsum * additionsum - 4 * multiplysum))
number2 = -2 * multiplysum / (-1 * additionsum - math.sqrt(additionsum * additionsum - 4 * multiplysum))

print(number1, number2)