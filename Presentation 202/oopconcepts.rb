class Animal
  def speak
    "Animal sound"
  end
end

class Dog < Animal
  def speak
    "Woof!"
  end
end

dog = Dog.new
puts dog.speak  # Outputs: Woof!

class Cat < Animal
  def speak
    "Meow!"
  end
end

animals = [Dog.new, Cat.new]
animals.each { |animal| puts animal.speak }

