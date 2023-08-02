import csv
import random
import json

def name_gen(name):
    def main_a(func):
        def wrapper(*args, **kwargs):
            with open(name, 'r', newline='') as f_1:
                csv_r = list(csv.reader(f_1))
                for i in csv_r[1:]:
                    yield int(i[0]), int(i[1]), int(i[2]), func(int(i[0]), int(i[1]), int(i[2]))
        return wrapper
    return main_a



def name_json(name):
    def save_to_json(func):
        def wrapper(*args, **kwargs):
            res = []
            for i in func(args):
                if i[-1] == None:
                    res.append({'input_parameters':i[:-1], '0 корней':None})
                elif len(i[-1]) == 1:
                    res.append({'input_parameters':i[:-1], '1 корень':i[-1]})
                else:
                    res.append({'input_parameters':i[:-1], '2 корня':i[-1]})

            with open(name, 'w', encoding='utf-8') as f_1:
                json.dump(res, f_1, indent=2, ensure_ascii=False)
            return res
        return wrapper
    return save_to_json



#@name_json('new_json.json')
#@name_gen('csv_generator.csv')
def roots_of_a_quadratic_equation(a=None, b=None, c=None):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root_1 = (-b - discriminant ** 0.5) / (2 * a)
        root_2 = (-b + discriminant ** 0.5) / (2 * a)
        return root_1, root_2
    elif discriminant == 0:
        root_1 = -b / - (2 * a)
        return root_1
    else:
        return None


def csv_generator(count_string):
    with open(csv_generator.__name__ + '.csv', 'w', newline='') as f_1:
        csv_wr = csv.writer(f_1)
        csv_wr.writerow(['num_1', 'num_2', 'num_3'])
        for _  in range(count_string):
            csv_wr.writerow([random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000)])




f = name_json('new_json.json')(name_gen('csv_generator.csv')(roots_of_a_quadratic_equation))
f()
#roots_of_a_quadratic_equation()
#csv_generator(1000)
#print(roots_of_a_quadratic_equation(3, 7, -10))
