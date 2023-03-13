# Task 6

my_str = "1, 2 3 asd2 asd22  44"
for i in my_str:
    if not i.isdigit():
        my_str.replace(i, ' ').split(' ')

print(my_str)