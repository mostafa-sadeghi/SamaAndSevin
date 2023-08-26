# 11    12      13      => th
# 1     st
# 2     nd
# 3     rd
#       th

# x = 123
# print(x % 100)
# print(x % 10)

# print("#"*10)
# x = str(x)
# print(x[-2:])
# print(x[-1])


# def my_function_one(number):
#     # if number % 100 == 11 or number % 100 == 12 or number % 100 == 13:
#     if number % 100 in (11,12,13):
#         return str(number) + "th"
#     if number % 10 == 1:
#         return str(number) + "st"
#     if number % 10 == 2:
#         return str(number) + "nd"
#     if number % 10 == 3:
#         return str(number) + "rd"
#     return str(number) + "th"

# print(my_function_one(123))
# print(my_function_one(121))
# print(my_function_one(122))
# print(my_function_one(125))
# print(my_function_one(111))
# print(my_function_one(112))
# print(my_function_one(113))
# print(my_function_one(1))
# print(my_function_one(2))
# print(my_function_one(3))


# def my_function_two(number):
#     number = str(number)
#     if number[-2:] in (11, 12, 13):
#         return number + "th"
#     if number[-1] == '1':
#         return number + 'st'
#     if number[-1] == '2':
#         return number + 'nd'
#     if number[-1] == '3':
#         return number + 'rd'
#     return number + 'th'

# print(my_function_two(123))
# print(my_function_two(121))
# print(my_function_two(122))
# print(my_function_two(125))
# print(my_function_two(111))
# print(my_function_two(112))
# print(my_function_two(113))
# print(my_function_two(1))
# print(my_function_two(2))
# print(my_function_two(3))


# print(ord('A'))
# print(ord('B'))
# print(ord('C'))

# print(chr(112))

text = input("Enter some text: ")
def convert_to_number(text):
    numbers = []
    for char in text:
        numbers.append(ord(char))
        print(ord(char))
    print(numbers)


convert_to_number(text)



def convert_to_char(numbers):
    string = ""
    for num in numbers:
        string += chr(num)
    print(string)
convert_to_char([112,113,114,117])