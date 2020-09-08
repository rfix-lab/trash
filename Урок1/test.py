import math
def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

first_number = input("type a first_number: ")
if is_digit(first_number):
    print ("It`s ok")
else:
    print ("it is not a number")
second_number = input("type a second_number: ")
if is_digit(second_number):
    print ("It`s ok")
else:
    print ("it is not a number")
def summ(x,y):
    return int(x)+int(y)
print (summ(first_number, second_number))