# def get_cost_coffee(number_of_coffees, price_per_coffee):
#     # تعداد قهوه های رایگان
#     number_of_free_coffees = number_of_coffees // 9
#     number_of_paid_coffees = number_of_coffees - number_of_free_coffees
#     return number_of_paid_coffees * price_per_coffee

# print(get_cost_coffee(7,2.5))
# print(get_cost_coffee(8,2.5))
# print(get_cost_coffee(9,2.5))
# print(get_cost_coffee(10,2.5))

# get_cost_coffee(7,2.5) -> 17.5
# get_cost_coffee(8,2.5) -> 20
# get_cost_coffee(9,2.5) -> 20
# get_cost_coffee(10,2.5) -> 22.5

import string
import random
LOWER_LETTERS = string.ascii_lowercase
UPPER_LETTERS = string.ascii_uppercase
NUMBERS = string.digits
SPECIAL = '~!@#$%^&*()_+'

ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL


def create_password(length):
    if length < 12:
        length = 12

    password = []

    password.append(LOWER_LETTERS[random.randint(0, 25)])
    password.append(UPPER_LETTERS[random.randint(0, 25)])
    password.append(NUMBERS[random.randint(0, 9)])
    password.append(SPECIAL[random.randint(0, 12)])

    while len(password) < length:
        password.append(ALL_CHARS[random.randint(0, 74)])

    random.shuffle(password)

    return ''.join(password)


print(create_password(13))
print(create_password(5))


# yeapyear

def is_leap_year(year):
    pass


# 2016 -> leapyear
"""
بر چهار بخش پذیر است؟
سالی که بر صد بخش پذیر باشد کبیسه نیست
اما سالی که بر چهار بخش پذیر باشد کبیسه است


"""
