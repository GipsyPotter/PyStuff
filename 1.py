class Point:
	def __init__(self, x=0, y=0):
		self.__x = x
		self.__y = y

	def get_x(self):
		...

	def get_y(self):
		...

	def set_x(self, x):
		...

	def set_y(self, y):
		...

	def distance(self, other_point) -> float:
		...

	# unit la don vi
	def go_left(self, unit):
		...

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
		# kiem tra hinh chu nhat co hop le hay chua
		# neu chua thi phai in ra canh bao cho nguoi dung
		# va yeu cau ho nhap lai
		self.__a = a
		self.__b = b
		self.__c = c

	def area(self) -> float:
		...

	def perimeter(self) -> float:
		...
	

class Rectangle(Shape):
	def __init__(self, a, b, c, d):
		self.__a = a
		self.__b = b
		self.__c = c
		self.__d = d

	# kiem tra hinh chu nhat co hop le hay chua
	# neu chua thi phai in ra canh bao cho nguoi dung
	# va yeu cau ho nhap lai

	def area(self) -> float:
		...

	def perimeter(self) -> float:
		...


if __name__ == '__main__':
	...
