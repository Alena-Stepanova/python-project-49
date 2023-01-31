import random


def play_even():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!\nAnswer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        number = random.randint(1, 101)
        answer = input(f'Question: {number}\nYour answer: ').lower()
        if (number % 2 and answer == 'no') or (number % 2 == 0 and answer == 'yes'):
            count += 1
            print('Correct!')
        else:
            print(f"{'«yes»' if answer == 'yes' else '«no»'} is wrong answer ;(. Correct answer was "
                  f"{'«no»' if answer == 'yes' else '«yes»'}. Let's try again, {name}")
            break
    else:
        print(f'Congratulations, {name}!')


play_even()
