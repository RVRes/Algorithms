class Coord_value:
    # раньше нужно было задавать переменную дескриптора, сейчас появилось set_name
    # def __init__(self, name):
    #     self.__name = name

    def __set_name__(self, owner, name):
        print(name)
        self.__name = name


    def __get__(self, instance, owner):
        # return self.__value
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        # self.__value = value
        instance.__dict__[self.__name] = value

    # def __delete__(self, instance):
    #     del self.__value


class Point:
    # старый формат записи
    # coordX = Coord_value('coordX')
    coordY = Coord_value()
    coordX = Coord_value()

    def __init__(self, x, y):
        self.coordX = x
        self.coordY = y

pt = Point(4,5)
pt.coordX = 1
print(pt.coordX, pt.coordY)