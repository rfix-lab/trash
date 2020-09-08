import math
#y = ax^2+bx+c
#D = b^2 -4ac
#D >=0
'''
проверяем строку на число
'''
def is_digit(string):
    if string.isdigit():
       return False
    else:
        try:
            float(string)
            return False
        except ValueError:
            return True

test_a=True
test_b=True
test_c=True
while test_a==True:
    a = input ("Input a: ")
    test_a=is_digit(a)
    continue
while test_b==True:
    b = input ("Input b: ")
    test_b=is_digit(b)
    continue
while test_c==True:
    c = input ("Input c: ")
    test_c=is_digit(c)
    continue
if int(a) != 0:
    D = int(b)**2 - 4*int(a)*int(c)
    if D >=0:
        x1 = (-(int(b)) + math.sqrt(D))/2*a
        x2 = (-(int(b)) - math.sqrt(D))/2*a
        print (x1,x2)
    else:
        print("there is no solutions")
else:
    if int(b)!=0:
        x=-(int(c)/int(b))
        print("x={}".format(x))
    else:
        if int(c)!=0:
            print("there is no solutions")
        else:
            print("Верно для любого х")