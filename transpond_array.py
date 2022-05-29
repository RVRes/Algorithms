import numpy as np


class Matrix:
    __array = []

    def fill_array(self, size):
        self.__array = []
        for i in range(size):
            s = [str(i) + str(j) for j in range(size)]
            for j in range(size):
                s.append(str(i) + str(j))
            self.__array.append(s)

    def fill_array2(self, size):
        self.__array = [[str(i) + str(j) for j in range(size)] for i in range(size)]

    def render_array(self):
        for s in self.__array:
            print(' '.join(s))

    def render_item(self, x, y):
        print(self.__array[x][y])

    def get_array(self):
        return self.__array

    def transpond_array(self):
        array = np.array(self.__array)
        print(array)
        array = array.T
        print(array)

    def transpond_array2(self):
        transponded = [[self.__array[j][i] for j in range(len(self.__array))] for i in range(len(self.__array[0]))]
        return transponded


if __name__ == '__main__':
    m = Matrix()

    m.fill_array2(10)
    m.render_array()
    m.render_item(5, 8)
    m.transpond_array2()
    m.render_array()
