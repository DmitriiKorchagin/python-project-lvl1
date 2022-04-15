#!/usr/bin/env python3
import prompt
from random import randint


def main():
    print()


print("Welcome to the Brain Games!")
user_count_answers = 0
user_name = prompt.string('May I have your name? ')
print(f'Hello, {user_name}!')


def is_even_number(num):
    if num % 2 == 0:
        return True
    else:
        return False


print('Answer "yes" if the number is even, otherwise answer "no".')

while user_count_answers < 3:
    random_number = randint(1, 100)
    print('Question: ' + str(random_number))
    user_answer = input(str('Your answer: '))
    if is_even_number(random_number) is True and user_answer == 'yes':
        user_count_answers += 1
        print('Correct!')
    elif is_even_number(random_number) is False and user_answer == 'no':
        user_count_answers += 1
        print('Correct!')
    elif is_even_number(random_number) is True and user_answer == 'no':
        print("'no' is wrong answer ;(. Correct answer was 'yes'.")
        print(f"Let's try again, {user_name}!!")
        break
    elif is_even_number(random_number) is False and user_answer == 'yes':
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        print(f"Let's try again, {user_name}!!")
        break
    else:
        print(f"Let's try again, {user_name}!!")
        break

if user_count_answers == 3:
    print(f"Congratulations, {user_name}!!")

if __name__ == '__main__':
    main()
