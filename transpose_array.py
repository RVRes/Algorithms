import numpy as np


class Matrix:
    __array = []

    def fill(self, size):
        self.__array = [[str(i) + str(j) for j in range(size)] for i in range(size)]

    def render(self):
        for s in self.__array:
            print(' '.join(s))

    def get_item(self, x, y):
        return self.__array[x][y]

    def get(self):
        return self.__array

    def transpose(self):
        array = np.array(self.__array)
        self.__array = array.T

    def transpose_2(self):
        self.__array = [[self.__array[j][i] for j in range(len(self.__array))] for i in range(len(self.__array[0]))]

    def transpose_3(self):
        self.__array = list(map(list, zip(*self.__array)))  # zip returns Iter[Tuple[int]]. result is List[List[int]]


if __name__ == '__main__':
    m = Matrix()

    m.fill(10)
    m.render()
    print(m.get_item(5, 8))
    m.transpose_3()
    m.render()
