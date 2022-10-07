import datetime
date =datetime.datetime.strptime(input('Введите дату:\n'),'%d.%m.%Y')
#метод strptime возвращает нам строку представляющую дату
print(f"{date:%m\%d\%Y}")
# f строкой изменяем под нужный нам вид)
