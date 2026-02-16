# Exercise: Print Numbers
#
num = 0
while num != 30:
    num += 2
    print(num)

# Exercise: Countdown
#
print("Are you ready?")
number = int(input("Please type in a number: "))
while number != 0:
    print(number)
    number -= 1
print("Now!")

# Exercise: Numbers
#
num = int(input('Upper limit: '))

i = 1
while i < num:
    print(i)
    i += 1

# Exercise: Powers of two 
#
limit = int(input('Upper limit: '))

num = 1
while num <= limit:
    print(num)
    num *= 2

# Exercise: String multiplied
#
word = input('Please type a string: ')
amount = int(input('Please type in an amount: '))
print(word * amount)

# Exercise: The longer string 
#
in1 = input('Please type in a string 1: ')
in2 = input('Please type in a string 2: ')
if len(in1) > len(in2):
    print(in1 + ' is longer')
elif len(in1) < len(in2):
    print(in2 + ' is longer')
else:
    print('The strings are equally long')

# Exercise: End to beginning
#
inp = input('Please type in a string: ')
i = len(inp) - 1
while i != -1:
    print(inp[i])
    i -= 1

# Exercise: Second and second to last characters
#
inp = input('Please type in a string: ')
if inp[1] == inp[-2]:
    print('The second and the second to last characters are ' + inp[1])
else:
    print('The second and the second to last characters are different')

# Exercise: Substrings, part 1 
#
inp = input('Please type in a string: ')

i = 0
while i != len(inp) + 1:
    print(inp[:i])
    i+=1

# Exercise: Substrings, part 2 
#
inp = input('Please type in a string: ')

i = len(inp)
while i >= 0:
    print(inp[i:])
    i -= 1

# Exercise: Does it contain vowels
#
inp = input('Please type in a string: ')

if 'a' in inp:
    print('a found')
else:
    print('a not found')

if 'e' in inp:
    print('e found')
else:
    print('e not found')

if 'o' in inp:
    print('o found')
else:
    print('o not found')

# Exercise: Multiplication
#
num = int(input('Please type in a number: '))

i = 1
while i <= num:
    j = 1
    while j <= num:
        print(f'{i} x {j} = {i*j}')
        j += 1
    i += 1

# Exercise: Seven brothers 
#
def seven_brothers():
    print('Aapo\nEero\nJuhani\nLauri\nSimeoni\nTimo\nTuomas\n')

# Exercise: The first character 
#
def first_character(text):
    print(text[0])
# write your code here
#
# testing the function:
if __name__ == "__main__":
    first_character('python')
    first_character('yellow')
    first_character('tomorrow')
    first_character('heliotrope')
    first_character('open')
    first_character('night')

# Exercise: Mean 
#
def mean(num1, num2, num3):
    avg = (num1 + num2 + num3) / 3
    print(avg)
# Testing the function
if __name__ == "__main__":
    mean(1, 2, 3)


