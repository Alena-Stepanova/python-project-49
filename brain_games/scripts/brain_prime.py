import random
import prompt


def play_prime():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\nAnswer "yes" '
          f'if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        number = random.randint(1, 101)
        answer = input(f'Question: {number}\n'
                       f'Your answer: ').lower()
        foo = 0
        for i in range(1, number + 1):
            if number % i == 0:
                foo += 1

        if (foo > 2 and answer == 'no') or \
                (foo == 2 and answer == 'yes'):
            count += 1
            print('Correct!')
        else:
            print(f"{'«yes»' if answer == 'yes' else '«no»'} "
                  f"is wrong answer ;(. Correct answer was "
                  f"{'«no»' if answer == 'yes' else '«yes»'}. "
                  f"Let's try again, {name}")
            break
    else:
        print(f'Congratulations, {name}!')


play_prime()
