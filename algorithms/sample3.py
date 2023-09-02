# def write_to_file(filename, text):
#     with open(filename, 'w') as file:
#         file.write(text)


# write_to_file("sevin_and_sama.txt",
#               "welcome to pyhton class.")

# ########################################################

# def read_from_file(filename):
#     with open(filename, "r") as file:
#         return file.read()

# print(read_from_file("sevin_and_sama.txt"))

# ########################################################


# def append_to_file(filename, text):
#     with open(filename, "a") as file:
#         file.write(text)


# append_to_file("sevin_and_sama.txt", "hello sama.\nHello Sevin")


# def get_chess_square_color(row, column):
#     if row % 2 == column % 2:
#         return "White"
#     else:
#         return "Black"


# print(get_chess_square_color(2, 2))
# print(get_chess_square_color(2, 3))
# print(get_chess_square_color(2, 4))
# print(get_chess_square_color(4, 6))


text = "The fox"

# x = text.find("fox")
# print(text[x:x+len("fox")])

# print(text.index("fox"))

print(text.replace("fox", "dog"))