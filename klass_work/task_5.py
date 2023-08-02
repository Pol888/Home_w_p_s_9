'''Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов'''
import task_2, task_3, task_4


@task_3.main_f
@task_4.count(1)
@task_2.main_g
def magic(number_to_guess:int, number_of_attempts:int):
    count = 0
    v = number_of_attempts
    while True:
        num = int(input(f'Отгадайте число от 1 до 100, за {v} раз\nВвод: '))
        if num == number_to_guess:
            print(f"Вы отгадали, это число - {number_to_guess}")
            return True
        elif num > number_to_guess:
            print("Загаданное число меньше")
        else:
            print('Загаданное число больше')
        count += 1
        v -= 1
        if count == number_of_attempts:
            print('Закончились попытки')
            return False


if __name__ == '__main__':
    #magic(55, 4)
    #magic(33, 5)
    #magic(10, 10)
    #magic(111, 9)
    print(magic.__name__)