def main_g(number_to_guess:int, number_of_attempts:int):
    def magic():
        count = 0
        flag = True
        v = number_of_attempts
        while flag:
            num = int(input(f'Отгадайте число от 1 до 100, за {v} раз\nВвод:'))
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
    return magic

go = main_g(44, 10)

go()
