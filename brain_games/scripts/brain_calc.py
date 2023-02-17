import random
from brain_games.scripts import brain_games


def play_calc():
    name = brain_games.main()
    print('What is the result of the expression?')
    count = 0
    while count < 3:
        number1 = random.randint(1, 26)
        number2 = random.randint(1, 26)
        operations = ['+', '-', '*']
        operation = random.choice(operations)
        answer = int(input(f'Question: {number1} {operation} {number2}\n'
                           f'Your answer: '))
        if operation == '+':
            if number1 + number2 == answer:
                count += 1
                print('Correct!')
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was "
                      f"{number1 + number2}.\n"
                      f"Let's try again, {name}!")
                break
        elif operation == '-':
            if number1 - number2 == answer:
                count += 1
                print('Correct!')
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was "
                      f"{number1 - number2}.\n"
                      f"Let's try again, {name}!")
                break
        else:
            if number1 * number2 == answer:
                count += 1
                print('Correct!')
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was "
                      f"{number1 * number2}.\n"
                      f"Let's try again, {name}!")
                break
    else:
        print(f'Congratulations, {name}!')


play_calc()
