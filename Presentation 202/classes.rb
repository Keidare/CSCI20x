# Define a method that accepts any object that responds to `quack`
def make_it_quack(duck_like)
  if duck_like.respond_to?(:quack)
    duck_like.quack
  else
    puts "This doesn't quack!"
  end
end

# Define two classes with a `quack` method
class Duck
  def quack
    puts "Quack! I'm a Duck."
  end
end

class Person
  def quack
    puts "Quack! I'm a person pretending to be a duck."
  end
end

# Another class without a `quack` method
class Cat
  def meow
    puts "Meow! I'm a Cat."
  end
end

# Create instances
duck = Duck.new
person = Person.new
cat = Cat.new

# Call the method
make_it_quack(duck)    # Output: Quack! I'm a Duck.
make_it_quack(person)  # Output: Quack! I'm a person pretending to be a duck.
make_it_quack(cat)     # Output: This doesn't quack!
