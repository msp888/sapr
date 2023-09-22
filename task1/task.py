import csv
import sys
import os.path

def main():
    if len(sys.argv) >= 4:
        filename = sys.argv[1]
        if not os.path.exists(filename):
            print('Указанный путь не существует:', filename)
            return

        if not os.path.isfile(filename):
            print('Указанный путь не определяет файл:', filename)
            return

        try:
            row = int(sys.argv[2])
            col = int(sys.argv[3])
        except Exception as e:
            print('Ошибка во входных параметрах:', e)
            print('В качестве номера столбца или строки нужно указать целое число')
            return

        if (row < 0) or (col < 0):
            print('В качестве номера столбца или строки нужно указать положительное целое число')
            return

        with open(filename, newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            L = list(reader)
            if row >= len(L):
                print("Строки с номером", row, "нет в файле, максимальное допустимое значение", len(L)-1)
            else:
                if col >= len(L[row]):
                    print("Колонки с номером", col, "нет в указанной строке в файле, максимальное допустимое значение", len(L[row])-1)
                else:
                    print(L[row][col])
    else:
        print("Необходимо указать 3 параметра командной строки:")
        print("\t 1) путь к файлу *.csv")
        print("\t 2) номер строки")
        print("\t 3) номер колонки")
        print("например> task.py example.csv 3 4")
        
    return


if __name__ == "__main__":
    main()
