import os


class Helper:

    def __init__(self, path):
        self.path = path

    def get_path(self):
        base_path = os.getcwd()
        return os.path.join(base_path, self.path)
""" 
    def get_folder(self):
        base_path = os.getcwd()
        return os.path.join(base_path, self.path)
"""


class Worker:

    def __init__(self):
        self.helper = Helper('db')

    def work(self):
        path = self.helper.get_path()
        print(f'Working on {path}')
        return path


class Pricer:

    DISCOUNT = 0.80

    def get_discounted_price(self, price):
        return price * self.DISCOUNT


if __name__ == '__main__':

    print(Worker().work())