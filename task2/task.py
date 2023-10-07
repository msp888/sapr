import csv
from typing import Callable, Optional

# Класс узла для создания дерева
class Node:
    def __init__(self, value: str, childred: dict[str, "Node"] | None = None, parent: Optional["Node"] = None) -> None:
        self.value = value                              # значение в узле
        self.parent = parent                            # предок
        if childred is None:
            childred = {}
        self.childred: dict[str, "Node"] = childred     # словарь с потомками

        # Счетчики отношений
        self.r1:int = 0     # отношение непосредственного управления
        self.r2:int = 0     # отношение непосредственного подчинения
        self.r3:int = 0     # отношение опосредованного управления
        self.r4:int = 0     # отношение опосредованного подчинения
        self.r5:int = 0     # отношение соподчинения на одном уровне

    # Выполнить действия над всеми узлами, начиная с себя
    def operate(self, func: Callable[["Node"], None]) -> None:
        func(self)  # выполняем действие для себя

        if len(self.childred) == 0:
            return None

        for child in self.childred.values():
            child.operate(func) # выплолняем действие для всех потомков

    # Добавить подчиненный узел (создать наследника)
    def append(self, value: str) -> "Node":
        node = self.__class__(value, parent=self)   # создаем новый узел
        self.childred[value] = node                 # добавляем новый узел в словарь
        return node

    # Поиск узла по значению
    def findByValue(self, value: str) -> "Node":
        # Проверяем себя
        if self.value == value:
            return self

        # Проверяем наследников
        for child in self.childred.values():
            if child.value == value:
                return child
            try:
                child_find = child.findByValue(value) # ... внуков и т.д.
            except KeyError:
                ...
            else:
                return child_find

        raise KeyError(f"Не найден узел со значением: {value}")

    # Функция обратного вызова. Определяем: отношение опосредованного управления, отношение опосредованного подчинения
    def callback_r3_r4(self, node: "Node") -> None:
        self.r3 += 1    # Если есть внук (правнук и т.д.), то текущий узел имеет с ним отношение опосредованного управления
        node.r4 += 1    # Если есть дедушка (прадедушка и т.д.), то внук (правнук и т.д.) имеет с ним отношение опосредованного подчинения

    # Определяем отношения всех узлов
    def update_relations(self) -> None:
        for child in self.childred.values():
            self.r1 += 1                                # Если у родительского узла есть подчиненные узлы, то существует отношение непосредственного управления
            child.r2 += 1                               # Если у дочернего узла усть родительский, то существует отношение непосредственного подчинения
            child.r5 = len(self.childred.values()) - 1  # Кол-во дочерних узлов минус 1, определяет отношение соподчинения на одном уровне

            # Перебираем внуков и рукурсивно определяем: отношение опосредованного управления, отношение опосредованного подчинения
            for grandchild in child.childred.values():
                grandchild.operate(self.callback_r3_r4)

            # Определяем отношения подчиненных узлов    
            child.update_relations()

# Функция по заданию 2
def task(data: str) -> str:
    # Из полученной строки создаем массив строк: каждый элемент - это пара значений
    rows = []
    for row in data.splitlines():
        rows.append(row.split(","))

    # Из массива создаем дерево
    root = Node(rows[0][0])
    for row in rows:
        root.findByValue(row[0]).append(row[1])

    # Определяем отношения всех узлов
    root.update_relations()

    # Создаем из дерева список узлов
    nodes: list[Node] = []
    root.operate(lambda node: nodes.append(node))

    # Из сортированного списка узлов длябавляем отношения каждого узла в строку
    res = ""
    for node in sorted(nodes, key=lambda node: node.value):
        res += f"{node.r1},{node.r2},{node.r3},{node.r4},{node.r5}\n"

    # Результирующая строка, содержащая отношения для всех узлов
    return res.strip()


def main():
        filename = "task2.csv" # файл, содержащий контрольные значения

        # Загружаем файл, получаем список пар из файла
        with open(filename, newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            L = list(reader)

        # Из списка создаем строку
        data = ""
        for i in L:
            data += ",".join(i)
            data += "\n" 

        # Вызов функции, выполняющей задание 2; печать результата работы
        print(task(data))


if __name__ == "__main__":
    main()
