'''
Создаем светофор. При запуске скрипта необходимо задать значение цвета "R, Y или G". Остановка скрипта осуществляется 
путём написания "stop"
'''



while True:
    our_status = input("Введи значение R, Y или G: ")
    if our_status == "stop":
        break
    elif our_status == "R":
        print ("Стоим, курим")
        continue
    elif our_status == "Y":
        print("Подождем мою маму?")
        continue
    elif our_status == "G":
        print("Не хлопаем ушами, едем!")
        continue
    else:
        print("Че-то ты не то вводишь")
        continue