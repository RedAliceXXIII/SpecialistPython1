# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43
def my_time(sec):
    hours = sec // 3600
    minutes = (sec - hours * 3600) // 60
    sec = sec - hours * 3600 - minutes * 60
    return f'{hours:>2}:{minutes:>2}:{sec:>2}'


print(my_time(10000))
