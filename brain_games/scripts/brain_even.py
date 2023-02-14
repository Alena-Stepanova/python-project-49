import random
from brain_games.scripts import brain_games


def play_even():
    brain_games.main()
    print(f'Answer "yes" if the number '
          f'is even, otherwise answer "no".')
    count = 0
    while count < 3:
        number = random.randint(1, 101)
        answer = input(f'Question: {number}\nYour answer: ').lower()
        if (number % 2 and answer == 'no') or \
                (number % 2 == 0 and answer == 'yes'):
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


play_even()
