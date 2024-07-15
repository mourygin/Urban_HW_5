import math
class Figure:
    def __init__(self, color, *sides):
        self.sides_count = len(sides)
        filled = False
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = filled
    def get_color(self):
        return self.__color
    def __is_valid_color(color):
        result = True
        if color[0] not in range(0,256):
            result = False
        if color[1] not in range(0,256):
            result = False
        if color[2] not in range(0,256):
            result = False
        return result
    def set_color(self, color):
        if Figure.__is_valid_color(color):
            self.__color = list(color)
        return
    def __is_valid_sides(self, *args):
        result = True
        for i in range(0, len(args[0])):
            if args[0][i] <= 0 or (not isinstance(args[0][i],int)):
                result = False
        if len(args[0]) != self.sides_count:
            result = False
        return result
    def get_sides(self):
        return self.__sides
    def __len__(self):
        result = 0
        for i in self.__sides:
            result += i
        return result
    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(new_sides):
            for i in range(0,self.sides_count):
                self.__sides[i] = new_sides[i]
            return
    def get_var_name(self):
        for k, v in globals().items():
            if v is self:
                return k
    def about(self):
        print('-----------------')
        print('Object name:', self.get_var_name())
        print('Object type:', type(self))
        print('Edges:', self.sides_count)
        print('Edges lenth:', self.get_sides())
        print('Edges sum lenth (perimeter):', self.__len__())
        print('Color (RGB):', self.get_color())
        print('Is filled:', self.filled == True)
        if isinstance(self,Circle):
            print('Radius:', self.get_radius())
            print('Object sum area:', self.__len__() * self.__len__() / 4 / 3.1415)
        elif isinstance(self,Triangle):
            print('Object height =', self.get_height())
            print('Object sum area:', self.get_square())
        elif isinstance(self,Cube):
            print('Object volume =', self.sides_count)
            print('Object surface area:', self.sides_count)
        else:
            pass
        print('-----------------')
class Circle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = list(sides)
        sl = []
        sl.append(self.__sides[0])#[0])
        self.__sides = sl
        self._Figure__sides = sl
        self.sides_count = 1
        self.__color = list(color)
        super().get_color()
        super().set_color(color)
        super().get_sides()
        self.__radius = self.__len__()/2/3.1415
    def get_radius(self):
        return self.__radius
    def get_square(self):
        return self.__len__() * self.__len__() / 4 / 3.1415
class Triangle(Figure):
    def get_height(self):
        max = 0
        for i in self.__sides:
            if i > max:
                max = i
        return self.get_square() * 2 / max

    def get_square(self):
        pp = 0
        for i in self.__sides:
            pp += (i / 2)
        s = math.sqrt(pp * (pp - self.__sides[0]) * (pp - self.__sides[1]) * (pp - self.__sides[2]))
        return s

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 0:
            sl = list([1, 1, 1])
        elif len(sides) == 1:
            a = sides
            sl = []
            sl.append(a[0])
            sl.append(a[0])
            sl.append(a[0])
        elif len(sides) == 2:
            a = sides[0]
            b = sides[1]
            if a > b:
                c = a
            else:
                c = b
            sl = list([a, b, c])
        elif len(sides) > 3:
            sl = sides[0:3]
        else:
            sl = sides
        max = 0
        min = sl[0]
        prm = 0
        for i in sl:
            prm += i
            if i > max:
                max = i
            if i < min:
                min = i
        if prm - max < max:
            sl = list([max, max, min])
        self.__sides = sl
        self._Figure__sides = sl
        self.sides_count = 3
        self.__height = self.get_height()
class Cube(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 0:
            sl = list([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        else:
            sl = [sides[0]] * 12
        self.__sides = sl
        self._Figure__sides = sl
        self.sides_count = 12
        super().get_color()
        super().set_color(color)
        super().get_sides()
    def get_volume(self):
        return self.__sides[0] ** 3
if __name__ == '__main__':

    # # FIGURE TEST
    # f1 = Figure((65, 11, 55), False, 11, 22, 32, 5, 5)
    # print(f1.get_color())
    # f1.set_color((65, 100, 5))
    # print(f1.get_color())
    # print(f1.get_sides())
    # print(f1.__len__())
    # print(f1.sides_count)
    # f1.set_sides(66, 67, 68, 66, 66)
    # print(f1.get_sides())
    # print(f1.__len__())
    # print(f1.about())
    #
    # # CIRCLE TEST
    # a1 = Circle((23, 86, 112), 314)
    # a1.about()
    # print(a1.get_square())
    # print(a1.sides_count)
    # print('__sides', a1._Figure__sides)
    # print(a1.get_sides())
    # print(a1.get_color())
    # a1.set_color((114, 127, 55))
    # print(a1.get_color())
    # print(a1.get_sides())
    #
    # #TRIANGLE TEST
    # t1 = Triangle((127,127,127),3,4,5)
    # t1.about()
    # # Тест "сходимости" треугольника
    # t2 = Triangle((16,44,35),15,1,1)
    # t2.about()
    #
    # # CUBE TEST
    # a1 = Cube((127,127,127),5,4)
    # a1.about()
    # a1.set_color((5,55,5))
    # a1.about()
    # a1.set_sides(66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66)
    # a1.about()
    # a1.filled = True
    # a1.about()

    # URBAN TEST
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color((55, 66, 77))  # Изменится
    print(circle1.get_color())
    cube1.set_color((300, 70, 15))  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())