import random


class SignUpData:
    email = 'evgenyerjomin19001@ya.ru'
    password = '776655'
    name = 'Евгений'
    incorrect_password = '123'


class RandomEmail:
    email = 'evgenyerjomin19' + str(random.randint(1, 999)) + '@ya.ru'
