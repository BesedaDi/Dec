class NotSleeping:
    '''класс "засыпающего" человека'''

    def __init__(self, name, count_sheeps=0):
        '''метод иницыализации'''
        self.name = name
        self.count_sheeps = count_sheeps

    def add_sheep(self):
        '''метод подсчета овец'''
        self.count_sheeps += 1

    def __str__(self):
        '''Метод строкового представления объектов'''
        return self.count_sheeps
