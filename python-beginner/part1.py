# Exercise: Emoticon

print(':-)')

#Exercise: Seven Brothers

print("Aapo")
print("Eero")
print("Juhani")
print("Lauri")
print("Simeoni")
print("Timo")
print("Tuomas")

# Exercise: Row, Row, Row your Boat

print('Row, row, row your boat,')
print('Gently down the stream.')
print('Merrily, merrily, merrily, merrily,')
print('Life is but a dream.')

# Exercise: Minutes in a year

print(365 * 24 * 60)

# Exercise: Print some code

print('print("Hello there!")')

# Exercise: Name twice
#
name = input('What is your name?')
print(name)
print(name)

# Exercise: Name and exclamation marks 
#
name = input('What is your name?')
print('!' + name + '!' + name + '!')

# Exercise: Story
#
name = input('What is your name?')
year = input('State a year')

print(name + " is a valiant knight, born in the year " + year + 
    ". One morning Mary woke up to an awful racket: a dragon was approaching the village. Only Mary could save the village's residents.")

# Exercise: Extra space
#
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old \n")
print("my skills are")
print(f" - {skill1} ({level1})")
print(f" - {skill2} ({level2})")
print(f" - {skill3} ({level3})\n")
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")

# Exercise: Print a single line 
#
print(5, end='')
print(" + ", end='')
print(8, end='')
print(" - ", end='')
print(4, end='')
print(" = ", end='')
print(5 + 8 - 4, end='')

# Exercise: Times five 
#
number = int(input("Please provide a number: "))
print(f'{number} times 5 is {number * 5}')

# Exercise: Product
#
# number = int(input("Please type in the first number: "))
number *= int(input("Please type in the second number: "))
number *= int(input("Please type in the third number: "))

print("The product is", number)

# Exercise: Orwell
#
num = int(input('Please provide an integer number: '))

if num == 1984:
    print('Orwell')

# Exercise: Solving quadratics
#
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

a = int(input('Please provide a first integer: '))
b = int(input('Please provide a second integer: '))
c = int(input('Please provide a third integer: '))

x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)

print(f'The roots are {x1} and {x2}')

