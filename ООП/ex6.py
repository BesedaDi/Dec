import math

class Point:
    '''Класс описывает точку'''
    def __init__(self, koord=(0, 0)):
        self.x = koord[0]
        self.y = koord[1]

    def get_x(self):
        '''метод определяет значение х'''
        return self.x

    def get_y(self):
        '''метод определяет значение у'''
        return self.y

    def distance(self, other):
        '''метод определяет ратсояние между точками'''
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    def sum(self, other):
        '''метод определяет сумму координат'''
        x = self.x + other.x
        y = self.y + other.y
        return Point((x, y))

    def __repr__(self):
        '''метод предстваления в машинном коде'''
        return format('('+str(self.x) + '; ' + str(self.y)+')')

    def __str__(self):
        '''метод строкового представления'''
        return format('('+str(self.x) + '; ' + str(self.y)+')')

# 15, 18, 22