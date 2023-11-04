import numpy as np

# расчет условной энтропии и количества информации для двух совместных (связанных) случайных событий, которые возникают вследствие броска двух игральных костей:
#   a. событие А - значение суммы чисел на гранях игральных костей;
#   b. событие B - значение произведения чисел на гранях игральных костей

# Функция по заданию 4
def task():
    # Вычисление сумм и произведений
    s = set()
    p = set()
    for side1 in range(1, 7):
        for side2 in range(1, 7):
            s.add(side1 + side2)
            p.add(side1 * side2)
    s = sorted(s)
    p = sorted(p)

    # Создаем словари для определения индексов в таблице для суммы и для произведения
    sL = {item: s.index(item) for item in s}
    pL = {item: p.index(item) for item in p}

    # Создаем матрица с количествами комбинаций (для каждой суммы и произведения) 
    сombinations = np.zeros((len(s), len(p)))
    for side1 in range(1, 7):
        for side2 in range(1, 7):
            сombinations[sL[side1 + side2], pL[side1 * side2]] += 1

    # Вычисление матрицы с вероятностями комбинаций (для каждой суммы и произведения) 
    combinProbabilities = сombinations / 36

    cp_A = np.sum(combinProbabilities, axis=1) # матрица вероятностей для события A
    cp_B = np.sum(combinProbabilities, axis=0) # матрица вероятностей для события B

    # H(AB) - энтропия двух связанных (совместных) событий
    H_AB = -np.sum(combinProbabilities * np.log2(combinProbabilities, where=np.abs(combinProbabilities) > 1e-4))

    # H(A) - энтропия события А
    H_A = -np.sum(cp_A * np.log2(cp_A, where=np.abs(cp_A) > 1e-4))

    # H(B) - энтропия события B
    H_B = -np.sum(cp_B * np.log2(cp_B, where=np.abs(cp_B) > 1e-4))

    # Ha(B) - условная энтропия события B связанного с событием A
    Ha_B = H_AB - H_A  

    # I(A,B) - информация в событии A о событии B
    I_AB = H_B - Ha_B

    # Формирование результата
    return [round(item, 2) for item in [H_AB, H_A, H_B, Ha_B, I_AB]]


def main():
        # Вызов функции, выполняющей задание 4; печать результата работы
        print(task())

if __name__ == "__main__":
    main()
