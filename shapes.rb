class Shape
  attr_reader :sides, :center

  def initialize(sides, center)
    @sides = sides
    @center = center
  end

  def display
    raise "should be implemented in subclass"
  end
end

class Circle < Shape
  attr_reader :radius
  def initialize(radius, center)
    super(Float::INFINITY, center)
    @radius = radius
  end

  def display
    puts "●"
  end
end

class Triangle < Shape
  def initialize(center)
    super(3, center)
  end

  def display
    puts "▲"
  end
end

class Square < Shape
  def initialize(center)
    super(4, center)
  end
  
  def display
    puts "◼"
  end
end

database = [
  Square.new([9,1]),
	Triangle.new([9,1]),
	Circle.new(0.1, [1,1]),
	Square.new([1,1]),
	Square.new([1,2]),
	Circle.new(0.2, [2,1]),
	Circle.new(0.3, [1,5]),
	Circle.new(0.4, [1,1]),
	Square.new([1,3]),
	Triangle.new([1,3]),
	Square.new([9,1]),
	Square.new([9,1]),
	Circle.new(0.5, [2,1]),
	Triangle.new([1,1]),
	Triangle.new([1,2]),
	Circle.new(0.6, [0,20]),
	Circle.new(0.7, [8,1]),
	Square.new([1,1]),
	Square.new([1,2]),
	Triangle.new([1,1]),
	Triangle.new([1,2]),
	Triangle.new([1,3]),
	Square.new([1,3]),
]


sorted = database.sort_by {|obj| obj.sides}

for s in sorted do
  s.display
end
