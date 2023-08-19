# name = input("enter a name: ")
# print(name.upper())


# def my_function(name):
#     res = ''
#     for c in name:
#         if c == 'm' or c == 'n' or c == 'a':  # if c in ('m', 'n' , 'a')
#             res += c.upper()
#         else:
#             res += c
#
#     return res
#
#
# print(my_function("sevin"))
# print(my_function("sama"))

"""
0               =>              0th
1               =>              1st
2               =>              2nd
3               =>              3rd


"""


def my_function(num):
    str_num = str(num)
    if num % 10 == 0:
        return str_num + "th"
    elif num % 10 == 1:
        return str_num + "st"
    elif num % 10 == 2:
        return str_num + "nd"
    elif num % 10 == 3:
        return str_num + "rd"


print(my_function(22))

"""
تمرین : تابع بالا را به این صورت تغییر دهید:
اگر دو رقم آخر 11 یا 12 یا 13 بود th را بچسباند

211      =>   211th
212      =>   212th
213      =>   213th

"""