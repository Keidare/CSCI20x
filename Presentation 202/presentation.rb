def fizzbuzz(n)
  (1..n).each do |i|
    if i % 3 == 0 && i % 5 == 0
      puts "FizzBuzz"
    elsif i % 3 == 0
      puts "Fizz"
    elsif i % 5 == 0
      puts "Buzz"
    else
      puts i
    end
  end
end

puts "Enter a number:"
n = gets.chomp.to_i

# Call the fizzbuzz function with user input
fizzbuzz(n)


# Gets vs gets.chomp
# Gets returns the input with a newline character after. gets.chomp removes the newline character.
puts "Enter first text:"
text1 = gets.chomp
puts "Enter second text:"
text2 = gets.chomp
puts text1 + text2

puts "Enter first text:"
text1 = gets
puts "Enter second text:"
text2 = gets
puts text1 + text2

# Addition
sum = 5 + 3       

# Subtraction
difference = 10 - 2 

# Multiplication
product = 4 * 2     

# Division
quotient = 16 / 2   

# Exponentiation
power = 2**3        

# Modulus (remainder)
remainder = 17 % 3  

puts "#{sum}, #{difference}, #{product}, #{quotient}, #{power}, #{remainder}"

# Comparison operators
puts 5 > 3
puts 5 < 3
puts 5 >= 3
puts 5 <= 3
puts 5 == 3
puts 5 != 3

# Logical operators
puts true && true
puts true && false
puts true || false
puts !true

age = 18

if age >= 18
  puts "You are an adult."
elsif age >= 13
  puts "You are a teenager."
else
  puts "You are a child."
end

age = 18
puts age >= 18 ? "Adult" : "Minor"  # => "Adult"

grade = 'B'

case grade
when 'A'
  puts "Excellent!"
when 'B'
  puts "Good job!"
when 'C'
  puts "You passed."
else
  puts "Better luck next time."
end


def greet(name)
  "Hello, #{name}!"
end

puts greet("Alice")  # => "Hello, Alice!"

def greet(name = "Guest")
  "Hello, #{name}!"
end

puts greet          # => "Hello, Guest!"
puts greet("Bob")   # => "Hello, Bob!"

i = 1
while i <= 5
  puts i
  i += 1
end

i = 1
until i > 5
  puts i
  i += 1
end

for i in 1..5
  puts i
end

[1, 2, 3, 4, 5].each do |num|
  puts num
end

5.times do |i|
  puts i + 1
end

# Creating an array
fruits = ["apple", "banana", "cherry"]

# Accessing elements
puts "first element: #{fruits[0]}"       
puts "last: #{fruits[-1]}"      

# Adding elements
fruits << "date"

# Removing elements
fruits.delete_at(2)

puts "#{fruits}" 
# Replacing elements
fruits[0] = "apricot"

# Joining elements
puts fruits.join(", ") 

puts "fruits: #{fruits}" 

# Checking if an element exists
fruits.include?("banana") 

# Getting the size
puts fruits.length  

# Reversing the array
puts "fruits reversed: #{fruits.reverse}"  

# Sorting the array
puts "fruits sorted: #{fruits.sort}"  

# Checking if the array is empty
puts fruits.empty?  

# Iterating over an array
fruits.each do |fruit|
  puts fruit
end

# Clearing the array
fruits.clear

numbers = [1, 2, 3, 4, 5]

# Map
squares = numbers.map { |num| num ** 2 }  # => [1, 4, 9, 16, 25]
puts squares

# Select
evens = numbers.select { |num| num.even? }  # => [2, 4]
puts evens

# Reduce
sum = numbers.reduce(:+)  # => 15
puts sum

# Creating a hash
person = { name: "Alice", age: 25, city: "New York" }

# Accessing values
puts person[:name]       # => "Alice"
puts person[:age]        # => 25

# Adding or updating values
person[:job] = "Engineer"

# Iterating over a hash
person.each do |key, value|
  puts "#{key}: #{value}"
end

# Checking if a key exists
puts person.key?(:name)  # => true

# Fetching with a default value
puts person.fetch(:salary, "Not provided")  # => "Not provided"
