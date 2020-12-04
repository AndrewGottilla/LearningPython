### 2020-12-03
### Author: Andrew Gottilla
### Lesson 63: Handling exceptions

try:
    print(5/0)
except ZeroDivisionError:
    print('= You\'re seeing this because you can\'t divide by zero! =\n')

print('Let\'s do some math! Enter two numbers to be divided!')

while True:
    print("[Enter 'q' at any point to quit]\n")

    num1 = input('First number: ')
    if num1 == 'q':
        break

    num2 = input('Second number: ')
    if num2 == 'q':
        break

    print('-------------------------------------')
    
    try:
        ans = int(num1) / int(num2)
    except ZeroDivisionError:
        print('= You\'re seeing this AGAIN because you STILL can\'t divide by zero!')
    except:
        print('ERROR: INVALID INPUT! TRY AGAIN.')
    else:
        print(num1 + ' divided by ' + num2 + ' is ' + str(ans) + '!')
    print()

    print('\nLet\'s do it again!')