import string
import random
from math import pi
from datetime import datetime

def generate_password(length: int) -> str:
    """
    generate password with given length

    Homework
    функция должна возвращать строку из случайных символов заданной длины.
    """
    password = ''
    for _ in range(length):
        password += random.choice(string.ascii_lowercase)
    return password




def encrypt_message(message: str) -> str:
    """
    encrypt message
    зашифровать сообщение по алгоритму.
    Сместить каждый символ по ASCII таблице на заданное рассояние.
    """
    key = 2
    return ''.join(
        chr(num + key)
        for num in map(ord, message)
    )



def lucky_number(ticket: str) -> bool:
    """
    lucky number (tram ticket)
    667766 - is lucky (6 + 6 + 7 == 7 + 6 + 6)
    сумма первых трех числе должна равняться сумме последних трех чисел
    """
    first_part = [int(sym) for sym in ticket[:3]]
    second_part = [int(sym) for sym in ticket[3:]]
    return sum(first_part) == sum(second_part)



def fizz_buzz(num: int) -> str:
    """
    fizz buzz
    усли число, кратно трем, программа должна выводить слово «Fizz»,
    а вместо чисел, кратных пяти — слово «Buzz».
    Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz»
    в остальных случаях число как строку
    """
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)


def password_is_strong(password: str) -> bool:
    """
    is password is strong
    (has number, char, lowercase, uppercase, at least length is 10)
    вернуть True если пароль надежный
    Праметры:
        1. Пароль должен содержать как минимум одну цифру
        2. Пароль должен содержать как минимум один сивол в нижнем регистре
        3. Пароль должен содержать как минимум один сивол в верхнем регистре
        4. Пароль должен быть как минимум 10 символов
    """
    isDigit = False
    isChar = False
    isLower = False
    isUpper = False
    if len(password) >= 10:
        for sym in password:
            if sym.isdigit():
                isDigit = True
            if sym.isalpha():
                isChar = True
            if sym.islower():
                isLower = True
            if sym.isupper():
                isUpper = True
    else:
        return False

    return isDigit and isChar and isLower and isUpper


def number_is_prime(num: int) -> bool:
    """
    number is prime
    на вход принимаем число
    вернуть True если число является простым
    https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%B5_%D1%87%D0%B8%D1%81%D0%BB%D0%BE#:~:text=2%2C%203%2C%205%2C%207,%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%B1%D1%8B%D1%82%D1%8C%20%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%8B%D0%BC%20%D0%BD%D0%B0%D0%B7%D1%8B%D0%B2%D0%B0%D0%B5%D1%82%D1%81%D1%8F%20%D0%BF%D1%80%D0%BE%D1%81%D1%82%D0%BE%D1%82%D0%BE%D0%B9.
    """
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            return True



def decrypt_message(message: str) -> str:
    """
    decrypt message
    функция обратная encrypt_message
    Расшифровать сообщение по заданному ключу
    """
    key = 2
    return ''.join(
        chr(num - key)
        for num in map(ord, message)
    )



def volume_of_sphere(radius: float) -> float:
    """
    Volume of a Sphere
    на вход принимаем радиус сферы.
    Необходимо рассчитать объем сферы и округлить результат до двух знаков после точки
    round to 2 places
    """
    volume = round((4/3)*pi*pow(radius, 3), 2)
    return volume




def days_diff(start_date: ..., end_date: ...) -> int:
    """
    calculate number of days between two dates.
    найти разницу между двумя датами
    """
    date_1 = datetime.strptime(start_date, '%d.%m.%Y')
    date_2 = datetime.strptime(end_date, '%d.%m.%Y')
    diff = abs(date_2 - date_1).days
    return diff



def prs(client_choice: str) -> str:
    """
    paper rock scissors
    принимаем значение от клиента из списка значений (например ['p', 'r', 's'])
    сгенерировать случайный выбор на сервере
    реализовать игру в камень-ножницы-бумага между клиент-сервер
    """
    server_choice = random.choice(['p', 'r', 's'])
    if client_choice == 'p' and server_choice == 'p':
        return 'Draw'
    elif client_choice == 'p' and server_choice == 'r':
        return 'You won'
    elif client_choice == 'p' and server_choice == 's':
        return 'You lost'
    elif client_choice == 'r' and server_choice == 'p':
        return 'You lost'
    elif client_choice == 'r' and server_choice == 'r':
        return 'Draw'
    elif client_choice == 'r' and server_choice == 's':
        return 'You won'
    elif client_choice == 's' and server_choice == 'p':
        return 'You won'
    elif client_choice == 's' and server_choice == 'r':
        return 'You lost'
    elif client_choice == 's' and server_choice == 's':
        return 'Draw'
    else:
        return 'Incorrect item'



def integer_as_roman(integer: int) -> str:
    """
    ***
    integer to Roman Number
    вывести значение в виде римского числа
    """
    data = {
        '1': 'I',
        '2': 'II',
        '3': 'III',
        '4': 'IV',
        '5': 'V',
        '6': 'VI',
        '7': 'VII',
        '8': 'VIII',
        '9': 'IX',
        '10': 'X',
        '20': 'XX',
        '30': 'XXX',
        '40': 'XL',
        '50': 'L',
        '60': 'LX',
        '70': 'LXX',
        '80': 'LXXX',
        '90': 'XC',
        '100': 'C',
        '200': 'CC',
        '300': 'CCC',
        '400': 'CD',
        '500': 'D',
        '600': 'DC',
        '700': 'DCC',
        '800': 'DCCC',
        '900': 'CM',
        '1000': 'M',
        '2000': 'MM',
        '3000': 'MMM'
    }
    integer_list = list(str(integer))
    add_list = []
    roman = ''
    for sym in integer_list:
        for i in range(len(integer_list) - integer_list.index(sym) - 1):
            sym += '0'
        add_list.append(sym)
    for num in add_list:
        roman += data[num]
    return roman




if __name__ == '__main__':
    assert encrypt_message('Dima') == 'Fkoc'
    assert encrypt_message('Vova') == 'Xqxc'
    assert encrypt_message('Andrew') == 'Cpftgy'
    assert encrypt_message('John') == 'Lqjp'
    assert encrypt_message('Vasya') == 'Xcu{c'

    assert lucky_number('667766') == True
    assert lucky_number('519780') == True
    assert lucky_number('756111') == False
    assert lucky_number('665197') == True
    assert lucky_number('870994') == False

    assert fizz_buzz(9) == 'Fizz'
    assert fizz_buzz(15) == 'FizzBuzz'
    assert fizz_buzz(20) == 'Buzz'
    assert fizz_buzz(1000) == 'Buzz'
    assert fizz_buzz(45) == 'FizzBuzz'

    assert password_is_strong('gnom454') == False
    assert password_is_strong('vasyaPupkin1884') == True
    assert password_is_strong('enstain34yohho') == False
    assert password_is_strong('posterPechkin76') == True
    assert password_is_strong('MYPASSWORD654') == False

    assert number_is_prime(2) == True
    assert number_is_prime(4) == False
    assert number_is_prime(37) == True
    assert number_is_prime(88) == False
    assert number_is_prime(97) == True

    assert decrypt_message('Fkoc') == 'Dima'
    assert decrypt_message('Xqxc') == 'Vova'
    assert decrypt_message('Cpftgy') == 'Andrew'
    assert decrypt_message('Lqjp') == 'John'
    assert decrypt_message('Xcu{c') == 'Vasya'

    assert volume_of_sphere(10) == 4188.79
    assert volume_of_sphere(2) == 33.51
    assert volume_of_sphere(5) == 523.6
    assert volume_of_sphere(0.5) == 0.52
    assert volume_of_sphere(1.1) == 5.58

    assert days_diff('12.01.2020', '14.01.2020') == 2
    assert days_diff('28.07.1994', '26.12.2020') == 9648
    assert days_diff('05.03.1884', '14.01.2020') == 49622
    assert days_diff('12.11.2018', '09.10.2043') == 9097
    assert days_diff('25.05.2002', '22.02.2019') == 6117

    assert integer_as_roman(1234) == 'MCCXXXIV'
    assert integer_as_roman(13) == 'XIII'
    assert integer_as_roman(354) == 'CCCLIV'
    assert integer_as_roman(637) == 'DCXXXVII'
    assert integer_as_roman(5) == 'V'

