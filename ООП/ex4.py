class User:
    '''Класс пользователи'''
    def __init__(self, id, nick_name, first_name, last_name=None, middle_name=None, gender=None):
        '''Метод инициализации'''
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def update(self, new_id, new_nick_name, new_first_name, new_last_name=None, new_middle_name=None, new_gender=None):
        '''Метод обновления данных пользователя'''
        if new_id != 0:
            self.id = new_id
        if new_nick_name == '':
            self.nick_name = self.nick_name
        else:
            self.nick_name = new_nick_name

        if new_first_name == '':
            self.first_name = self.first_name
        else:
            self.first_name = new_first_name

        if new_last_name == None or new_last_name == '':
           self.last_name = self.last_name
        else:
            self.last_name = new_last_name

        if new_middle_name != None:
            self.middle_name = new_middle_name
        if new_gender == None or new_gender == '':
            self.gender = self.gender
        else:
            self.gender = new_gender

    def __repr__(self):
        '''Метод предствления ввиде машинного кода'''
        return self.nick_name
    def __str__(self):
        '''Метод предствления ввиде понятном человеку'''
        if self.last_name != None and self.middle_name != None and self.gender != None:
            return format('ID: ' + str(self.id)+' '+'LOGIN: '+self.nick_name+' '+'NAME: '+self.last_name+' '+self.first_name+' '+self.middle_name+' '+'GENDER: '+self.gender)
        elif self.last_name == None and self.middle_name == None and self.gender == None:
            return format('ID: '+str(self.id)+' '+'LOGIN: '+self.nick_name+' '+'NAME: '+self.first_name)
        elif self.last_name == None and self.middle_name == None and self.gender != None:
            return format('ID: '+str(self.id)+' '+'LOGIN: '+self.nick_name+' '+'NAME: '+self.first_name+' '+'GENDER: '+self.gender)
        elif self.last_name == None and self.middle_name != None and self.gender != None:
            return format('ID: '+str(self.id)+' '+'LOGIN: '+self.nick_name+' '+'NAME: '+self.first_name+' '+self.middle_name+' '+'GENDER: '+self.gender)
        elif self.last_name == None and self.middle_name != None and self.gender == None:
            return format('ID: '+str(self.id)+' '+'LOGIN: '+self.nick_name+' '+'NAME: '+self.first_name+' '+self.middle_name)
        elif self.last_name != None and self.middle_name == None and self.gender == None:
            return format('ID: '+str(self.id)+' '+'LOGIN: '+self.nick_name+' '+'NAME: '+' '+self.last_name+' '+self.first_name)
        elif self.last_name != None and self.middle_name != None and self.gender == None:
            return format('ID: '+str(self.id)+' '+'LOGIN: '+self.nick_name+' '+'NAME: '+self.last_name+' '+self.first_name+' '+self.middle_name)
        elif self.last_name != None and self.middle_name == None and self.gender != None:
            return format('ID: '+str(self.id)+' '+'LOGIN: '+self.nick_name+' '+'NAME: '+self.last_name+' '+self.first_name+' '+'GENDER: '+self.gender)
