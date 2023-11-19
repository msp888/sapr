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

def createRow(visited: set, cur: int, n:int) -> np.array:
    row = []
    for i in range(n):
        row.append(1 if i+1 in visited else 0)
    return np.array(row)

def createMatrix(data: list) -> np.array:
    visited = set()
    matrix = list()

    n = flatListSize(data)

    for elem in data:
        if (type(elem) != list):
            visited.add(int(elem))
            row = createRow(visited=visited, cur=int(elem), n=n)
            matrix.append({'num': int(elem), 'row': row})
        else:
            for subelem in elem:
                visited.add(int(subelem))
            for subelem in elem:
                row = createRow(visited=visited, cur=int(subelem), n=n)
                matrix.append({'num': int(subelem), 'row': row})

    matrix.sort(key=(lambda x: x['num']))
    raw = [elem['row'] for elem in matrix]

    return np.array(raw)

def isStrResultType(str1, str2) -> bool:
    str1 = json.loads(str1)
    str2 = json.loads(str2)
    res = True
    for elem in str1:
        if (type(elem) != list):
            res = res and (type(elem) == str)
        else:
            for subelem in elem:
                res = res and (type(subelem) == str)
    for elem in str2:
        if (type(elem) != list):
            res = res and (type(elem) == str)
        else:
            for subelem in elem:
                res = res and (type(subelem) == str)
    return res

def S(str1, str2, isStr) -> list:
    str1 = eval(str1)
    str2 = eval(str2)    
    
    matrix1 = createMatrix(str1)
    matrix2 = createMatrix(str2)

    matrix12 = matrix1 * matrix2
    matrix12T = matrix1.T * matrix2.T

    criterion = matrix12 | matrix12T 

    answer = []
    for i in range(criterion.shape[0]):
        for j in range(i):
            if criterion[i][j] == 0:
                if isStr:
                    answer.append([str(j+1), str(i+1)])
                else:
                    answer.append([j+1, i+1])

    return answer

def S3(str1, str2, str3, isStr) -> list:
    str1 = eval(str1)
    str2 = eval(str2)    
    str3 = eval(str3)    
    
    matrix1 = createMatrix(str1)
    matrix2 = createMatrix(str2)
    matrix3 = createMatrix(str3)

    matrix12 = matrix1 * matrix2 * matrix3
    matrix12T = matrix1.T * matrix2.T * matrix3.T

    criterion = matrix12 | matrix12T 

    answer = []
    for i in range(criterion.shape[0]):
        for j in range(i):
            if criterion[i][j] == 0:
                if isStr:
                    answer.append([str(j+1), str(i+1)])
                else:
                    answer.append([j+1, i+1])

    return answer

def flatList(data) -> list:
    if (type(data) != list):
        data = json.loads(data)
    res = []
    i = 1
    for item in data:
        if isinstance(item, list):
            for l2 in item:
                res.append((l2, i, 1, item))
                i += 1
        else:
            res.append((item, i, 0, []))
            i += 1
    return res 

def flatList2(data) -> list:
    if (type(data) != list):
        data = json.loads(data)
    res = []
    for item in data:
        if isinstance(item, list):
            for l2 in item:
                res.append(l2)
        else:
            res.append(item)
    return res 

def getSforItem(value, Sab) -> list:
    for item in Sab:
        if value in item:
            return item
    return []

def isUsed(S_item, used) -> bool:
    for item in S_item:
        if item in used:
            return True
    return False

def f2(str1, str2, isStr) -> list:
    Sab = S(str1, str2, isStr)
    AL = flatList(str1)
    BL = flatList(str2)
    SL2 = flatList2(Sab)

    used = []
    n = len(AL)
    x = []
    for i in range(n):
        if (not (AL[i][0] in SL2)) and (not (AL[i][0] in x)) and (AL[i][2] == 0):
            x.append(AL[i][0])
        if (not (BL[i][0] in SL2)) and (not (BL[i][0] in x)) and (BL[i][2] == 0):
            x.append(BL[i][0])

    resL = []
    for i in range(n):
        if not isUsed([AL[i][0]], used):
            S_item = getSforItem(AL[i][0], Sab)
            if (len(S_item) > 0):
                    for item in S_item:
                        used.append(item)
                    resL.append(S_item)

        if not isUsed([BL[i][0]], used):
            S_item = getSforItem(BL[i][0], Sab)
            if (len(S_item) > 0):
                    for item in S_item:
                        used.append(item)
                    resL.append(S_item)

        isAddA = False
        if (AL[i][0] in x) and (not isUsed([AL[i][0]], used)):
            resL.append(AL[i][0])
            used.append(AL[i][0])
            isAddA = True

        isAddB = False
        if (BL[i][0] in x) and (not isUsed([BL[i][0]], used)):
            resL.append(BL[i][0])
            used.append(BL[i][0])
            isAddB = True

        if (not isAddA) and (not isAddB):
            L = list(set(AL[i][3]) & set(BL[i][3]))
            L2 = []
            for item in L:
                if not (item in x) and (not isUsed([item], used)):
                    L2.append(item)
            if len(L2) == 1:
                if not isUsed([L2[0]], used):
                    resL.append(L2[0])
                    used.append(L2[0])
            elif len(L2) > 1:
                resL.append(L2)
                for item in L2:
                    used.append(item)
        elif (not isAddA):
            L = AL[i][3]
            L2 = []
            for item in L:
                if not (item in x) and (not isUsed([item], used)):
                    L2.append(item)
            if len(L2) == 1:
                if not isUsed([L2[0]], used):
                    resL.append(L2[0])
                    used.append(L2[0])
            elif len(L2) > 1:
                resL.append(L2)
                for item in L2:
                    used.append(item)
        elif (not isAddB):
            L = BL[i][3]
            L2 = []
            for item in L:
                if not (item in x) and (not isUsed([item], used)):
                    L2.append(item)
            if len(L2) == 1:
                if not isUsed([L2[0]], used):
                    resL.append(L2[0])
                    used.append(L2[0])
            elif len(L2) > 1:
                resL.append(L2)
                for item in L2:
                    used.append(item)
        
    return resL

def f3(str1, str2, str3, isStr) -> list:
    Sabc = S3(str1, str2, str3, isStr)
    #print('Sabc:', Sabc)

    fl = []
    fl.append(flatList(str1))
    fl.append(flatList(str2))
    fl.append(flatList(str3))
    SL2 = flatList2(Sabc)
    #print('SL2:', SL2)

    used = []
    n = len(fl[0])
    x = []
    for j in range(len(fl)):
        for i in range(n):
            if (not (fl[j][i][0] in SL2)) and (not (fl[j][i][0] in x)) and (fl[j][i][2] == 0):
                x.append(fl[j][i][0])
    #print('x:', x)

    resL = []
    for i in range(n):
        for j in range(len(fl)):
            if not isUsed([fl[j][i][0]], used):
                S_item = getSforItem(fl[j][i][0], Sabc)
                if (len(S_item) > 0):
                        for item in S_item:
                            used.append(item)
                        resL.append(S_item)

        isAdd = np.zeros((len(fl)), bool)
        for j in range(len(fl)):
            isAdd[j] = False
            if (fl[j][i][0] in x) and (not isUsed([fl[j][i][0]], used)):
                resL.append(fl[j][i][0])
                used.append(fl[j][i][0])
                isAdd[j] = True

        if (not isAdd[0]) and (not isAdd[1]) and (not isAdd[2]):
            L = list(set(fl[0][i][3]) & set(fl[1][i][3]) & set(fl[2][i][3]))
            L2 = []
            for item in L:
                if not (item in x) and (not isUsed([item], used)):
                    L2.append(item)
            if len(L2) == 1:
                if not isUsed([L2[0]], used):
                    resL.append(L2[0])
                    used.append(L2[0])
            elif len(L2) > 1:
                resL.append(L2)
                for item in L2:
                    used.append(item)
        elif (not isAdd[0]):
            L = fl[0][i][3]
            L2 = []
            for item in L:
                if not (item in x) and (not isUsed([item], used)):
                    L2.append(item)
            if len(L2) == 1:
                if not isUsed([L2[0]], used):
                    resL.append(L2[0])
                    used.append(L2[0])
            elif len(L2) > 1:
                resL.append(L2)
                for item in L2:
                    used.append(item)
        elif (not isAdd[1]):
            L = fl[1][i][3]
            L2 = []
            for item in L:
                if not (item in x) and (not isUsed([item], used)):
                    L2.append(item)
            if len(L2) == 1:
                if not isUsed([L2[0]], used):
                    resL.append(L2[0])
                    used.append(L2[0])
            elif len(L2) > 1:
                resL.append(L2)
                for item in L2:
                    used.append(item)
        elif (not isAdd[2]):
            L = fl[2][i][3]
            L2 = []
            for item in L:
                if not (item in x) and (not isUsed([item], used)):
                    L2.append(item)
            if len(L2) == 1:
                if not isUsed([L2[0]], used):
                    resL.append(L2[0])
                    used.append(L2[0])
            elif len(L2) > 1:
                resL.append(L2)
                for item in L2:
                    used.append(item)
        #print(resL)

    return resL

def task(str1, str2, str3) -> list:
    return f3(str1, str2, str3, isStrResultType(str1, str2))

def main():
    #str1 = '["1", ["2","3"],"4", ["5", "6", "7"], "8", "9", "10"]'
    #str2 = '[["1","2"], ["3","4","5"], "6", "7", "9", ["8","10"]]'

    #str1 = '[1,[2,3],4,[5,6,7],8,9,10]'
    #str2 = '[3,[1,4],2,6,[5,7,8],[9,10]]'

    #str1 = '["1",["2","3"],"4",["5","6","7"],"8","9","10"]'
    #str2 = '["3",["1","4"],"2","6",["5","7","8"],["9","10"]]'

    #str1 = '[1,[2,3],4,[5,6,7],8,9,10]'
    #str2 = '[[1,2],[3,4,5],6,7,9,[8,10]]'



    str1 = '[1,[2,3],4,[5,6,7],8,9,10]'
    str2 = '[[1,2],[3,4,5],6,7,9,[8,10]]'
    str3 = '[3,[1,4],2,6,[5,7,8],[9,10]]'

    '''
    str1 = '["1",["2","3"],"4",["5","6","7"],"8","9","10"]'
    str2 = '[["1","2"],["3","4","5"],"6","7","9",["8","10"]]'
    str3 = '["3",["1","4"],"2","6",["5","7","8"],["9","10"]]'
    '''

    print(task(str1, str2, str3))

if __name__ == "__main__":
    main()
