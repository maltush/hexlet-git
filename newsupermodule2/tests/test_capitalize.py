import sys
sys.path.append("./src/capitalize")

from capitalize import capitalize

if capitalize("Hello") != "Hello":
    raise Exception("Функция работает неверно!")

if capitalize("") != "":
    raise Exception("Функция работает неверно!")

print("Все тесты пройдены!")