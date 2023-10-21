numbers = [5, 1, 0]
# print(min(numbers))
# print(max(numbers))

# numbers.sort()
# print(numbers[0])
# print(numbers[-1])

# find_min


# def find_min(numbers):
#     minimum = numbers[0]
#     for number in numbers:
#         if number < minimum:
#             minimum = number
#     return minimum

# TODO  با استفاده از حلقه وایل تابع بالا را بنویسید


# print(f"smallets is :{find_min(numbers)}")
# print(f"smallets is :{find_min([1,2,3,4,5])}")
# print(f"smallets is :{find_min([0,2,13,4,5])}")
# print(f"smallets is :{find_min([12,2,13,4,0])}")


# def find_max(numbers):
#     maximum = numbers[0]
#     for n in numbers:
#         if n > maximum:
#             maximum = n
#     return maximum


# print(find_max([100, 50, 70]))

# TODO  با استفاده از حلقه وایل تابع بالا را بنویسید


all_numbers = [2,4,6,8,10]
# print(sum(all_numbers))

def calc_sum(numbers):
    total = 0
    for n in numbers:
        total += n

    return total
print(calc_sum(all_numbers))

def calc_mul(numbers):
    result = 1
    for x in numbers:
        result *= x
    return result
print(calc_mul(all_numbers))