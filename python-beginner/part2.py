# Exercise: Typecasting
#
number = float(input('Please provide a float: '))

print(f'Integer part: {int(number)}')
print(f'Decimal part: {number - int(number)}')

# Exercise: Age of maturity
#
age = int(input('Please state your age: '))

if age >= 18:
    print('You are of age!')
else:
    print('You are not of age!')

# Exercise: Leap year 
#
year = int(input('Please provide a year: '))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print('That year is not a leap year.')
    else:
        print('That year is a leap year.')
else:
    print('That year is not a leap year.')

# Exercise: Shall we continue
#
answer = ''
while answer != 'no':
    print('hi')
    answer = input('Shall we continue?')


