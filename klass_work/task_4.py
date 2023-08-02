from  functools import wraps


def count(c=1):
    def main_f(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal c
            print(f'запуск №-{c}')
            c += 1
            return func(*args, **kwargs)
        return wrapper
    return main_f


@count()
def fun_print_text(text):
    print(text)


if __name__ == '__main__':
    fun_print_text('привет')
    fun_print_text('человек')
    fun_print_text('ха-ха-ха')

