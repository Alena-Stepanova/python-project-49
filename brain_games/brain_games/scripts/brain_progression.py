import random


def play_progression():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!\nWhat is the result of the expression?')
    count = 0
    while count < 3:
        lst = [i for i in range(random.randint(1, 5), random.randint(30, 40), random.randint(2, 4))]
        correct_number = random.choice(lst)
        lst = map(lambda x: str(x) if x != correct_number else "..", lst)
        answer = int(input(f'Question: {" ".join(lst)}\nYour answer: '))
        if answer == correct_number:
            count += 1
            print('Correct!')
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_number}.\nLet's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


play_progression()