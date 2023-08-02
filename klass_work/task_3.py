import random
import json
import os
from  functools import wraps

def main_f(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        d = {'positional_param': list(args)}
        for k, v in kwargs.items():
            d[k] = v
        d['return_func'] = func(*args, **kwargs)
        if str(func.__name__) + '.json' in os.listdir():
            with open(str(func.__name__) + '.json', 'r', encoding='utf-8') as f_1:
                res:list = json.load(f_1)
                res.append(d)
            with open(str(func.__name__) + '.json', 'w', encoding='utf-8') as f_2:
                json.dump(res, f_2, indent=2, ensure_ascii=False)
        else:
            with open(str(func.__name__) + '.json', 'w', encoding='utf-8') as f_1:
                json.dump([d], f_1, indent=2, ensure_ascii=False)
        return d['return_func']
    return wrapper




@main_f
def jumble_of_words_in_a_sentence(a:str, b:str, /, *, c:str, d:str) -> str:
    list_f = [a, b, c, d]
    random.shuffle(list_f)
    return list_f[0] + " " + list_f[1] + ' ' + list_f[2] + " " + list_f[3]


if __name__ == '__main__':
    print(jumble_of_words_in_a_sentence('я', 'люблю', d='природу', c='зимой'))



