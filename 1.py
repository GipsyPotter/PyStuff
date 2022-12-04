import math


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def distance(self, other) -> float:
        dis = math.sqrt((self.__x - other.__x) ** 2 + (self.__y - other.__y) ** 2)
        return dis

    # unit la don vi
    def go_left(self, unit):
        self.__x -= unit

    def go_right(self, unit):
        self.__x += unit

    def go_up(self, unit):
        self.__y += unit

    def go_down(self, unit):
        self.__y -= unit


# lam tuong tu voi right up down


class Shape:
    def __init__(self):
        pass

    def area(self) -> float:
        ...

    def perimeter(self) -> float:
        ...

    def export_point(self):
        ...


# nhớ tìm hiểu thêm các phép biến hình như tịnh tiến, xoay, ...
# sau đó tự define hàm nhé!


class Triangle(Shape):
    def __init__(self, a: Point, b: Point, c: Point):
        if a.distance(b) + a.distance(c) <= b.distance(c) or a.distance(b) + b.distance(c) <= a.distance(c) or a.distance(c) + b.distance(c) <= a.distance(b):
            raise ValueError("Khong phai tam giac")
        self.__a = a
        self.__b = b
        self.__c = c

    def area(self) -> float:
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.__a.distance(self.__b)) * (p - self.__a.distance(self.__c)) * (p - self.__b.distance(self.__c)))

    def perimeter(self) -> float:
        return self.__a.distance(self.__b) + self.__a.distance(self.__c) + self.__b.distance(self.__c)


class Rectangle(Shape):
    def __init__(self, a, b, c, d):
        if a.distance(b) != c.distance(d) or a.distance(d) != b.distance(c):
            raise ValueError("Khong phai hinh chu nhat")
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d

    def area(self) -> float:
        return self.__a.distance(self.__b) * self.__a.distance(self.__d)

    def perimeter(self) -> float:
        return 2 * (self.__a.distance(self.__b) + self.__a.distance(self.__d))


if __name__ == '__main__':
    ...