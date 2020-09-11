'''
нахождение наименьшего общего кратного
выписать все кратные и перемножить, исключая присутствующие в обоих
'''
num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))

def div_num(m): #нахождение делителей числа
    r=[]
    while m != 1:
        for i in range (2, int(m)+1):
            if m%i==0:
                r.append(i)
                m = m/i
                break
    return r

div_num1 = div_num(num_1)
div_num2 = div_num(num_2)
buffer = []
min_div = []

for i in div_num1:
    if i in div_num2:
        div_num2.remove(i)
        buffer.append(i)
    else:
        min_div.append(i)
for i in div_num2:
    min_div.append(i)
for i in buffer:
    min_div.append(i)

#получаем НОК
nok=1
for i in min_div:
    nok*=i

print ("Наименьший общий делитель для чисел {} и {} - {}.".format(num_1, num_2, nok))