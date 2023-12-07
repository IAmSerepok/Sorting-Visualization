from random import randint


class BubbleSort:
    def __init__(self, app):
        self.app = app
        self.size = app.size
        self.i, self.j = app.size, 0

    def sort_step(self):
        self.app.colors = {self.j+1: (230, 0, 0)}
        if self.i == 1:
            self.app.colors = {}
            return 0
        if self.app.arr[self.j+1] < self.app.arr[self.j]:
            buffer = self.app.arr[self.j+1]
            self.app.arr[self.j+1] = self.app.arr[self.j]
            self.app.arr[self.j] = buffer
        if self.j == self.i - 2:
            self.j = -1
            self.i -= 1
        self.j += 1
        return 1


class BubbleSortWithFlag:
    def __init__(self, app):
        self.app = app
        self.size = app.size
        self.i, self.j = app.size, 0
        self.flag = True

    def sort_step(self):
        self.app.colors = {self.j+1: (230, 0, 0)}
        if self.i == 1:
            self.app.colors = {}
            return 0
        if self.app.arr[self.j+1] < self.app.arr[self.j]:
            self.flag = False
            buffer = self.app.arr[self.j+1]
            self.app.arr[self.j+1] = self.app.arr[self.j]
            self.app.arr[self.j] = buffer
        if self.j == self.i - 2:
            self.j = -1
            self.i -= 1
            if self.flag:
                self.i = 1
            self.flag = True
        self.j += 1
        return 1


class ShakerSort:
    def __init__(self, app):
        self.app = app
        self.size = app.size
        self.i, self.k, self.j = app.size, 0, 0
        self.positive_direction = True

    def sort_step(self):
        if self.positive_direction:
            self.app.colors = {self.j + 1: (230, 0, 0)}
        else:
            self.app.colors = {self.j: (230, 0, 0)}
        # условие выхода
        if self.i == self.k:
            self.app.colors = {}
            return 0
        # работа с индексами
        if self.j > self.i - 2:
            self.app.colors = {self.j - 1: (230, 0, 0)}
            self.positive_direction = False
            self.j = self.i - 2
            self.i -= 1
        if self.j < self.k:
            self.app.colors = {self.j + 2: (230, 0, 0)}
            self.positive_direction = True
            self.j = self.k
            self.k += 1  
        # перестановка
        if self.app.arr[self.j + 1] < self.app.arr[self.j]:
            buffer = self.app.arr[self.j + 1]
            self.app.arr[self.j + 1] = self.app.arr[self.j]
            self.app.arr[self.j] = buffer

        if self.positive_direction:
            self.j += 1
        else:
            self.j -= 1

        return 1


class SelectionSort:
    def __init__(self, app):
        self.app = app
        self.size = app.size
        self.i, self.j = app.size, 0
        self.max_num, self.indx = -1, 0

    def sort_step(self):
        self.app.colors = {self.j: (230, 0, 0)}
        if self.i == 0:
            self.app.colors = {}
            return 0
        if self.app.arr[self.j] > self.max_num:
            self.max_num = self.app.arr[self.j]
            self.indx = self.j
        if self.j == self.i - 1:
            self.j = -1
            self.i -= 1
            buffer = self.app.arr[self.i]
            self.app.arr[self.i] = self.max_num
            self.app.arr[self.indx] = buffer
            self.max_num, self.indx = -1, 0
        self.app.colors[self.indx] = (0, 0, 230)
        self.j += 1
        return 1


class InsertionSort:
    def __init__(self, app):
        self.app = app
        self.size = app.size
        self.i, self.j = 0, 0

    def sort_step(self):
        self.app.colors = {self.j - 1: (0, 0, 230)}
        if self.i == self.size:
            self.app.colors = {}
            return 0
        if (self.j == 0) or (self.app.arr[self.j] > self.app.arr[self.j - 1]):
            self.i += 1
            self.j = self.i
        else:
            buffer = self.app.arr[self.j]
            self.app.arr[self.j] = self.app.arr[self.j - 1]
            self.app.arr[self.j - 1] = buffer
            self.j -= 1
        self.app.colors[self.i] = (230, 0, 0)
        return 1


class RandomPermutationSort:
    def __init__(self, app):
        self.app = app
        self.size = app.size
        self.i, self.j, self.k = randint(0, self.size - 1), randint(0, self.size - 1), 0
        while self.i == self.j:
            self.i, self.j = randint(0, self.size - 1), randint(0, self.size - 1)
        self.flag = False
        self.sorted = False
        self.count_of_permutation = 0

    def sort_step(self):
        print(self.count_of_permutation)
        self.app.colors = {self.i: (230, 0, 0), self.j: (230, 0, 0)}
        if self.sorted:
            self.app.colors = {}
            return 0
        if self.flag:
            if self.k == self.size - 2:
                self.sorted = True
            if self.app.arr[self.k] > self.app.arr[self.k + 1]:
                self.i, self.j, self.k = randint(0, self.size - 1), randint(0, self.size - 1), -1
                while self.i == self.j:
                    self.i, self.j = randint(0, self.size - 1), randint(0, self.size - 1)
                self.flag = False
                self.sorted = False
            self.k += 1
        else:
            buffer = self.app.arr[self.j]
            self.app.arr[self.j] = self.app.arr[self.i]
            self.app.arr[self.i] = buffer
            self.count_of_permutation += 1
            self.flag = True
        return 1


class DeleteSort:
    def __init__(self, app):
        self.app = app
        self.size = app.size
        self.i = 0
        self.flag = False
        self.indx = -1

    def sort_step(self):
        self.app.colors = {self.i: (230, 0, 0), self.i + 1: (230, 0, 0)}
        if self.i == self.size - 1:
            self.app.colors = {}
            return 0
        if self.flag:
            if self.app.arr[self.i + 1] < self.app.arr[self.indx]:
                self.app.arr.pop(self.i + 1)
                self.size -= 1
                self.app.width = self.app.screen_width // self.size
            else:
                self.flag = False
                self.indx = -1
        else:
            if self.app.arr[self.i] > self.app.arr[self.i + 1]:
                self.flag = True
                self.app.arr.pop(self.i + 1)
                self.size -= 1
                self.app.width = self.app.screen_width // self.size
                self.indx = self.i
            else:
                self.i += 1
        return 1
