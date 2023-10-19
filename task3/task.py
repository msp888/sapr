import csv
import math

# Функция по заданию 3
def task(data: str) -> float:
    # Из полученной строки создаем массив строк: каждый элемент - это пара значений
    rows = []
    for row in data.splitlines():
        rows.append(row.split(","))

    n = len(rows)

    res = 0.0
    for row in rows:
       for item in row:
           l = int(item)
           if int(l) > 0:
               res += (l/(n - 1)) * math.log(l/(n - 1), 2)

    #Энтропия, с округлением до одного знака после запятой
    return -round(res, 1)


def main():
        filename = "task3.csv" # файл, содержащий контрольные значения

        # Загружаем файл, получаем список пар из файла
        with open(filename, newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            L = list(reader)

        # Из списка создаем строку
        data = ""
        for i in L:
            data += ",".join(i)
            data += "\n" 

        # Вызов функции, выполняющей задание 3; печать результата работы
        print(task(data))


if __name__ == "__main__":
    main()
