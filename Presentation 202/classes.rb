
def make_it_quack(duck_like)
  if duck_like.respond_to?(:quack)
    duck_like.quack
  else
    puts "This doesn't quack!"
  end
end


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


class Cat
  def meow
    puts "Meow! I'm a Cat."
  end
end


duck = Duck.new
person = Person.new
cat = Cat.new

make_it_quack(duck)    
make_it_quack(person)  
make_it_quack(cat)    
