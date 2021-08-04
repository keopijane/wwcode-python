#https://wwcodemanila.github.io/WWCodeManila-Python/#/basic_concepts/lists?id=challenge
# Write a program that accepts 3 integers and separate these into odd and even numbers.
# Duplicates are permited in the input but not in the output.

# Example

# >>> Enter first number: 3567
# >>> Enter second number: 789
# >>> Enter third number: 1234
# odd: {789, 3567}
# even: {1234}

odd = []
even = []
first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
third_number = int(input('Enter third number: '))
numbers=sorted([first_number,second_number,third_number])

for x in numbers:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

odd_numbers = set(odd)
even_numbers = set(even)
print('odd: {}'.format(odd_numbers))
print('even: {}'.format(even_numbers))