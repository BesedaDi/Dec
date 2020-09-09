# задание 1
def half_digit(k):
    summ_1 = 0
    summ_2 = 0
    string = str(k)
    print(int(string[:len(string) // 2]))
    if len(string) % 2 != 0:
        for i in range(len(string[:len(string) // 2])):
            summ_1 += int(string[i])
        print(summ_1)
        for i in range(len((string[:len(string) // 2])), len(string)-1):
            summ_2 += int(string[i])
        print(summ_2)
        if summ_1 < summ_2:
            return int(string[(len(string) // 2) + 1:] + string[(len(string) // 2)] + string[:len(string) // 2])
        else:
            return k

    else:
        for i in range(len(string[:len(string) // 2])):
            summ_1 += int(string[i])
        for i in range(len(string[:len(string) // 2]), len(string)):
            summ_2 += int(string[i])
        if summ_1 < summ_2:
            return (string[(len(string) // 2) :] + string[:len(string) // 2])
        else:
            return k

k = int(input())
print(half_digit(k))
# 2
def count_variant(x):
    k = 0
    for i in range(1, x+1):
        for j in range(1, x+1):
            if i**2 + j**2 == x:
                k += 1
    return k//2


x = int(input())
print(count_variant(x))
# 4
def alphabet(s):
    lst = []
    lst_new = []
    lst_pr = []
    alp = 'a. b. c. d. e. f. g. h. i. j. k. ' \
          'l. m. n. o. p. q. r. s. t. u. v. w. x. y. z.'
    for i in s:
        d = alp.find(i)
        if d != -1:
            lst.append(i)
    k = 0
    stroka = ''
    for i in lst:
        for j in lst:
            if i == j:
                k += 1
        stroka += i + str(k)
        if stroka not in lst_new:
            lst_new.append(stroka)
        k = 0
        stroka = ''
    l = len(lst_new)
    for i in range(l):
        lst_pr.append(min(lst_new))
        lst_new.remove(min(lst_new))
    return lst_pr


s = input().lower()
print(alphabet(s))
# 3
def count_expr(n):
    action = '+-*/'
    for i in action:
        for j in action:
            for k in action:
                for h in action:
                    if ((((1i2)j3)k4))
# 5
def longest_dna(s):
    string = ''
    n = 0
    max_len = 0
    max_string = ''
    for i in range(len(s)):
        if s[i] in ['а', 'А', 'г', 'Г', 'т', 'Т', 'Ц', 'ц']:
            string = string + s[i]
            n += 1
        if n > max_len:
            max_len = n
            max_string = string
        if s[i] not in ['а', 'А', 'г', 'Г', 'т', 'Т', 'Ц', 'ц']:
            string = ''
            n = 0
    return max_string


s = input()
print(longest_dna(s))
# 6
def storage(file_in, file_out):
    infile = open(file_in, 'r')
    for i in infile:
        file_contents = infile.readline()
        print(file_contents)

storage('file_in.txt', 'file_out.txt')

# 3
def count_expr(n):
    counter = 0
    action = '+-*/'
    for act_1 in action:
        for act_2 in action:
            for act_3 in action:
                for act_4 in action:
                    for act_5 in action:
                        s = act_1 + act_2 + act_3 + act_4 + act_5
                        value = 1
                        a = 2
                        for i in s:
                            if i == '+':
                                value += a
                            elif i == '-':
                                value -= a
                            elif i == '*':
                                value = value * a
                            elif i == '/':
                                value = value / a
                            a += 1
                        if value == n:
                            counter += 1
    return counter


res = count_expr(35)
print(res)
#


