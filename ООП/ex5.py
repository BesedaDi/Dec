class Game:
    '''Класс описывает процесс игры'''
    def __init__(self,  dict, summ1=0, summ2=0):
        '''Метод инициализации'''
        self.command1 = dict.get('command1')
        self.command2 = dict.get('command2')
        self.summ1 = summ1
        self.summ2 = summ2

    def ball_thrown(self, command, points):
        '''Метод подсчитывает количество очков'''
        if command == 1:
            self.summ1 = self.summ1 + points
        if command == 2:
            self.summ2 = self.summ2 + points

    def get_score(self):
        '''Метод выводит счет игры'''
        a = []
        a.append(self.summ1)
        a.append(self.summ2)
        return tuple(a)

    def get_winner(self):
        '''Метод определяет победителя'''
        if self.summ1 < self.summ2:
            return self.command2
        elif self.summ1 > self.summ2:
            return self.command1
        else:
            return 'Ничья'








