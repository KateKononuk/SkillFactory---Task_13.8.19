quantity_of_tickets = int(input("Сколько билетов вы хотите приобрести?\n"))
sum = 0
for i in range(quantity_of_tickets):
    age = int(input(f"Укажите ваш возраст для билета № {i+1}  "))
    if 0 < age < 18:
        print("Вход на конфиренцию бесплатный")
    elif 18 <= age <= 25:
        sum += 990
        print("Стоимость билета составляет: 990 руб.")
    elif 25 < age < 100:
        sum += 1390
        print("Стоимость билета составляет: 1390 руб.")
    else:
        print("Ошибка")
if quantity_of_tickets >= 3:
    sum = sum - (sum * 0.1)
    print("Итоговая сумма со скидкой 10% составляет: ", sum)
else:
    print("Итоговая сумма: ", sum) 
