# def get_color(row, col):
#     if row % 2 == col % 2:
#         return "white"

#     else:
#         return "black"


# print(get_color(1,1))
# print(get_color(2,1))
# print(get_color(1,2))
# print(get_color(8,8))
# print(get_color(0,8))

# 'The fox', 'fox', 'dog'   => The dog

# print('The fox'.replace('fox', 'dog'))
# print('The fox'.find('fox'))
# print('The fox'.index('fox'))

def find_and_replace(text, old_text, new_text):
    result = ''
    i = 0
    while i < len(text):
        if text[i:i+len(old_text)] == old_text:
            result += new_text
            i += len(old_text)

        else:
            result += text[i]
            i += 1

    return result


print(find_and_replace('The fox', 'fox', 'dog'))
print(find_and_replace('The fox is going to find another fox', 'fox', 'dog'))


# TODO

"""
تابعی بنویسید که یک عدد بگیرد و عدد را تبدیل به زمان کند
یعنی به ساعت ، دقیقه و ثانیه تبدیل کند
90       =>      1m 30s
30       =>      30s
60       =>      1m

3600     =>      1h
3601     =>      1h 1s

def get_hour_minutes_seconds(time):
    

"""
