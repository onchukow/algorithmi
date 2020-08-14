# Task 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится
# букв.

x = input('1st letter: ')
y = input('2nd letter: ')
position_x = ord(x) - ord('a') + 1
position_y = ord(y) - ord('a') + 1
print(f'Positions: {position_x} and {position_y}')
print('Different letter between provided letters:', abs(position_x - position_y) - 1)

# Task 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

x = int(input('Enter a letter\'s number: '))
letter = chr(ord('a') + (x - 1))
print('Chosen letter is: ', letter)

# Task 6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он
# разносторонним, равнобедренным или равносторонним.

x = float(input('Input length of side 1: '))
y = float(input('Input length of side 2: '))
z = float(input('Input length of side 3: '))
if x < (y + z) and y < (x + z) and z < (x + y):
    print('Triangle with given side could be drawn')
    if x == y and x == z:
        print('Triangle is equilateral!')
    elif x == y or x == z or z == y:
        print('Triangle is isosceles!')
    else:
        print('Triangle is scalene!')

else:
    print('Triangle with given side impossible to draw')

# Task 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.

year = int(input('Enter a year for leap validation: '))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print('Year is a leap year')
else:
    print('Year is a common year')
