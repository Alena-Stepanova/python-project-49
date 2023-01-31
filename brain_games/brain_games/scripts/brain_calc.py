import random


def play_calc():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!\nWhat is the result of the expression?')
    count = 0
    while count < 3:
        number1 = random.randint(1, 26)
        number2 = random.randint(1, 26)
        operations = ['+', '-', '*']
        operation = random.choice(operations)
        answer = int(input(f'Question: {number1} {operation} {number2}\nYour answer: '))

        if operation == '+':
            if number1 + number2 == answer:
                count += 1
                print('Correct!')
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was {number1 + number2}.\nLet's try again, {name}!")
                break
        elif operation == '-':
            if number1 - number2 == answer:
                count += 1
                print('Correct!')
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was {number1 - number2}.\nLet's try again, {name}!")
                break
        else:
            if number1 * number2 == answer:
                count += 1
                print('Correct!')
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was {number1 * number2}.\nLet's try again, {name}!")
                break
    else:
        print(f'Congratulations, {name}!')


play_calc()
