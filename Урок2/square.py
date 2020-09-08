import math

#проверяем строку на число

def is_digit(string):
    if string.isdigit():
       return False
    else:
        try:
            float(string)
            return False
        except ValueError:
            return True
#убеждаемся, что ввели число
test_a=True
test_b=True
test_c=True
while test_a==True:
    a = float(input ("Input a: "))
    test_a=is_digit(str(a))
    continue
while test_b==True:
    b = float(input ("Input b: "))
    test_b=is_digit(str(b))
    continue
while test_c==True:
    c = float(input ("Input c: "))
    test_c=is_digit(str(c))
    continue
if a != 0: #проверяем, чтобы в знаменателях не было нулей
    D = b**2 - 4*a*c
    if D >=0:
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
        print ("x1={:.2f}, x2={:.2f}".format(x1,x2))
    else:
        print("there is no solutions!")
else:
    if b!=0:
        x=-c/b
        print("x={:.2f}".format(x))
    else:
        if c!=0:
            print("there is no solutions")
        else:
            print("Верно для любого х")
