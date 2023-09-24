import random
import os

def make_num():
    return [random.randrange(5, 20) for _ in range(5)]


def use_fun():
    x = make_num()
    avg = sum(x) / len(x)
    if avg > 10:
        return 'Super'
    else:
        return 'Duper'


print(use_fun())


def work_on():
    path = os.getcwd()
    print(f'Working path is {path}')
    return path


def work_on_env():
    path = os.path.join(os.getcwd(), os.environ['my_var'])
    print(f'Working on {path}')
    return path