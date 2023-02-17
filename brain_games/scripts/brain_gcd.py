import random
from brain_games import main


def play_gcd():
    name = main()
    print(f'What is the result '
          f'of the expression?')
    count = 0
    while count < 3:
        number1 = random.randint(1, 26)
        number2 = random.randint(1, 26)
        answer = int(input(f'Question: {number1} '
                           f'{number2}\nYour answer: '))
        while number1 != 0 and number2 != 0:
            if number1 > number2:
                number1 = number1 % number2
            else:
                number2 = number2 % number1
        if number1 + number2 == answer:
            count += 1
            print('Correct!')
        else:
            print(f"{answer} is wrong answer ;(. "
                  f"Correct answer was {number1 + number2}.\n"
                  f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


play_gcd()
