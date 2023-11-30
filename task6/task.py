import numpy as np
import json

def flatListSize(data) -> int:
    res = 0
    for item in data:
        if isinstance(item, list):
            for l2 in item:
                res += 1
        else:
            res += 1
    return res 

def flatList(data) -> list:
    if (type(data) != list):
        data = json.loads(data)
    res = []
    for item in data:
        if isinstance(item, list):
            item_sum = 0
            for l2 in item:
                item_sum += int(l2)
            value = item_sum/len(item)
            for l2 in item:
                res.append(value)
        else:
            res.append(int(item))
    return res 

def get_hk(data) -> list:
    res = []
    for item in data:
        if isinstance(item, list):
            res.append(len(item))
    return res 

def get_Ts(data) -> int:
    res = 0
    for item in data:
        res += item ** 3 - item
    return res 

def task(*rankings: str) -> float:

    m = len(rankings)
    if m == 0:
        print("Ошибка во входных параметрах. Количество входных строк должно быть больше 0")
        return 0

    rL = [json.loads(r) for r in rankings]
    ni = [flatListSize(r) for r in rL]
    n = ni[0]
    for item in ni:
        if item != n:
            print("Ошибка во входных параметрах. Количество количество элементов каждой строки должно быть одинаковым")
            return 0

    # матрица с учетом равных рангов
    matrix = np.array([np.array(flatList(r)) for r in rL]).T

    # суммы по строкам
    Xi = np.sum(matrix, axis=1)

    # среднее значение для сумм по строкам 
    Xavg = Xi.mean()

    # сумма квадратов разностей
    S = np.sum(np.square(Xi - Xavg))

    # дисперсия
    D = S / (n - 1)

    # количество объектов в k-ой группе с одинаковыми оценками
    hk = [get_hk(r) for r in rL]

    # Ts
    Ts = [get_Ts(h) for h in hk]

    # максимально возможная дисперсия
    Dmax = (m ** 2 * (n ** 3 - n) - m * np.sum(Ts)) / (12 * (n - 1))

    # значение коэффициента Кендалла
    W = D / Dmax

    return round(W, 2)

def main():

    str1 = '[1,[2,3],4,[5,6,7],8,9,10]'
    str2 = '[[1,2],[3,4,5],6,7,9,[8,10]]'

    '''
    str1 = '["1",["2","3"],"4",["5","6","7"],"8","9","10"]'
    str2 = '[["1","2"],["3","4","5"],"6","7","9",["8","10"]]'
    '''

    print(task(str1, str2))

    '''
    str1 = '[[1, 2],3]'
    str2 = '[1,3,2]'
    str3 = '[1,3,2]'
    str4 = '[[1,2,3]]'
    str5 = '[1,3,2]'

    print(task(str1, str2, str3, str4, str5))
    '''

if __name__ == "__main__":
    main()
