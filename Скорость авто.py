
speedCar = int(input("Введите скорость автомобиля..."))
freeSpeed = 90
delta = speedCar - freeSpeed

if delta >= 20 and delta <= 40:
    print("Штраф составляет 500 рублей.")
elif delta >= 40 and delta <= 60:
    print("Штраф составляет 1500 рублей.")
elif delta >= 60 and delta <= 80:
    print("Штраф составляет 2500 рублей или лишение прав на 4 месяца.")
elif delta >= 80:
    print("Штраф сотавляет 5000 рублей или лишение прав на пол года.")

else:
    print()
#str
close = int(input("Нажмите ""Enter" " чтобы закрыть программу."))