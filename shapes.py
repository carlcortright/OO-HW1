from abc import ABC


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
		super.__init__(int('Inf'))
		self.radius = radius
		self.center = center
	
	def display(self):
		print("○")

class Triangle(Shape):
	def __init__(self, center):
		super.__init__(3)
		self.center = center

	def display(self):
		print('▲')

class Square(Shape):
	def __init__(self, center):
		super.__init__(4)
		self.center = center
	
	def display(self):
		print('◼')


c = Circle(10000000)

print(c.sides)
