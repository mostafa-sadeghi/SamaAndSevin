# def my_function(name, class_name):
#     message = f"hi {name}. how are you? Welcome to {class_name} class."
#     return message


# print(my_function("sara", "java"))
# print(my_function("nikan", "python"))


# def calculate_average(score_1, score_2, score_3):
#     average = (score_1 + score_2 + score_3) / 3
#     return average


# s1 = float(input("Enter first score: "))
# s2 = float(input("Enter second score: "))
# s3 = float(input("Enter third score: "))
# result = calculate_average(s1, s2, s3)
# result = calculate_average(float(input("Enter first score: ")), float(
#     input("Enter second score: ")), float(input("Enter third score: ")))

# print(f"average is: {result:.1f}")


message = "python is the king of programming languages."

for c in message:
    print(c, end=" ")

print()

for x in range(len(message)):
    print(message[x], end=" ")


