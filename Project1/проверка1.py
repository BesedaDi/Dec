import datetime

# Значение: datetime.datetime(2017, 4, 5, 0, 18, 51, 980187)
now = datetime.datetime.today()
a = int(input())  # Год
b = int(input())  # Месяц
c = int(input())  # День
then = datetime.datetime(a, b, c)

# Кол-во времени между датами.
delta = then - now

print(delta.days)
