'''Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.'''
import random
from  functools import wraps

def main_g(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
         args = list(args)
         print(args)
         if  args[0] > 100 or args[0] < 1:
             args[0] = random.randint(1, 100)
         if args[1] > 10 or args[1] < 1:
             args[1] = random.randint(1, 10)
         args = tuple(args)
         res = func(*args, **kwargs)
         return res
    return wrapper


@main_g
def magic(number_to_guess:int, number_of_attempts:int):
    count = 0
    flag = True
    v = number_of_attempts
    while flag:
        num = int(input(f'Отгадайте число от 1 до 100, за {v} раз\nВвод: '))
        if num == number_to_guess:
            print(f"Вы отгадали, это число - {number_to_guess}")
            flag = False
        elif num > number_to_guess:
            print("Загаданное число меньше")
        else:
            print('Загаданное число больше')
        count += 1
        v -= 1
        if count == number_of_attempts:
            print('Закончились попытки')
            flag = False


if __name__ == '__main__':
    magic(119, 4)