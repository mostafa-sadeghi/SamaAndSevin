x = [1,2,3,4,5,9]

new_number = int(input("Enter a number: "))
x.append(new_number)
print("my list is:", x)

my_number = int(input("enter a number: "))
for n in x:
    if n == my_number:
        x.remove(my_number)
print("my list is:", x)

if my_number in x:
    x.remove(my_number)
print("my list is:", x)
    