class ticket:
    def __init__(self, date_time, place, dep_arr_air, page, price, sur_name):
        self.date_time = date_time
        self.place = place
        self.dep_arr_air = dep_arr_air
        self.page = page
        self.price = price
        self.sur_name = sur_name

    '''def read(self):
        lines = 0
        for line in open('input.txt', 'r'):
            lines += 1
        infile = open('input.txt', 'r')
        outfile = open('outfile.txt', 'w')
        for stroka in range(1, lines + 1):
            file_contents = infile.readline()
            date_time, place, dep_arr_air, page, price, sur_name = map(str, file_contents.split(','))
            st1 = 'date and time: ' + date_time + '  ' + 'place: ' + place
            st2 = 'departure and arrival airports: ' + dep_arr_air + '  ' + 'page: ' + page
            st3 = 'price: ' + price + '  ' + 'sur_name: ' + sur_name
            ticket = outfile.writelines(st1 + '\n')
            ticket = outfile.writelines(st2 + '\n')
            ticket = outfile.writelines(st3 + '\n')
        infile.close()
        outfile.close()'''


lines = 0
for line in open('input.txt', 'r'):
    lines += 1
infile = open('input.txt', 'r')
outfile = open('outfile.txt', 'w')
for stroka in range(1, lines + 1):
    file_contents = infile.readline()
    date_time, place, dep_arr_air, page, price, sur_name = map(str, file_contents.split(','))


# print(ticket(date_time, place, dep_arr_air, page, price, sur_name))

outfile = open('outfile.txt', 'w')
ticket = outfile.writelines(ticket(date_time, place, dep_arr_air, page, price, sur_name))
outfile.close()
