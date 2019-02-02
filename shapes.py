# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class Shape(ABC):
	def __init__(self, sides):
		self.sides = sides
	
	def get_sides(self):
		return sides

	@abstractmethod
	def display(self):
		pass

class Circle(Shape):
	def __init__(self, radius, center):
		Shape.__init__(self, float('Inf'))
		self.radius = radius
		self.center = center
	
	def display(self):
		print("●")

class Triangle(Shape):
	def __init__(self, center):
		Shape.__init__(self, 3)
		self.center = center

	def display(self):
		print('▲')

class Square(Shape):
	def __init__(self, center):
		Shape.__init__(self, 4)
		self.center = center
	
	def display(self):
		print('◼')


database = [
	Square((9,1)),
	Triangle((9,1)),
	Circle(0.1, (1,1)),
	Square((1,1)),
	Square((1,2)),
	Circle(0.2, (2,1)),
	Circle(0.3, (1,5)),
	Circle(0.4, (1,1)),
	Square((1,3)),
	Triangle((1,3)),
	Square((9,1)),
	Square((9,1)),
	Circle(0.5, (2,1)),
	Triangle((1,1)),
	Triangle((1,2)),
	Circle(0.6, (1,20)),
	Circle(0.7, (8,1)),
	Square((1,1)),
	Square((1,2)),
	Triangle((1,1)),
	Triangle((1,2)),
	Triangle((1,3)),
	Square((1,3)),
] 

sorted_shapes = sorted(database, key=lambda x: x.sides, reverse=True)

for shape in sorted_shapes:
	shape.display()

