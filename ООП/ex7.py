class TrafficLight:
    '''Класс описывает работу цветофора'''
    permissible_values = ['зеленый', 'желтый', 'красный']

    def __init__(self, current_signal='зеленый', i=0):
        '''Метод инициализации'''
        self.current_signal = current_signal
        self.i = i

    def next_signal(self):
        '''Метод переключает цвета'''

        try:
            if self.current_signal == 'зеленый':
                self.i = 1
                self.current_signal = self.permissible_values[self.i]
                self.i += 1
                return self.current_signal
            elif self.current_signal == 'желтый':
                self.i = 2
                self.current_signal = self.permissible_values[self.i]
                self.i += 1
                return self.current_signal
            elif self.current_signal == 'красный':
                self.i = 3
                self.current_signal = self.permissible_values[self.i]
                self.i += 1
                return self.current_signal
        except IndexError:
            return self.permissible_values.extend(self.permissible_values)
