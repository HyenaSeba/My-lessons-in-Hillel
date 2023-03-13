# Task 1 and 2
my_str = "bla BLA car"
new_char = []
result = 0

for letter in my_str:
    if letter.lower() not in new_char:
        new_char.append(letter)
        result += 1
print(result)
print(new_char)

# Task 3

my_str = "bla BLA car"
my_list = []

for i in my_str[::2]:
    my_list.append(i)
print(my_list)

# Task 4
my_str = "bla BLA car"
str_index = [0]


# Task 5

result = 0
my_int = 2134562

for i in str(my_int):
    result += 1
print(result)

# Task 6

my_number = 22882
my_list = list(str(my_number))
my_list.sort()

print(my_list[-1])

# Task 7

my_number = 123
my_list = list(str(my_number))

my_list.sort(reverse=True)
new_number = ''.join(my_list)
print(new_number)

# Task 8

my_number = 3254
my_list = list(str(my_number))

my_list.sort()
new_number1 = ''.join(my_list)
print(new_number1)

my_list.sort(reverse=True)
new_number2 = ''.join(my_list)
print(new_number2)

# Task 9

my_list_1 = [1, 2, 3]
my_list_2 = [10, 20, 30, 40, 60]

result_1 = []

my_list_1.sort(reverse=True)
my_list_2.sort(reverse=True)

if len(my_list_1) >= len(my_list_2):
    while len(my_list_1):
        num_1 = my_list_1.pop()
        num_2 = my_list_2.pop()
        result_1.append(num_1)
        result_1.append(num_2)
else:
    while len(my_list_1):
        num_1 = my_list_1.pop()
        num_2 = my_list_2.pop()
        result_1.append(num_1)
        result_1.append(num_2)
    while len(my_list_2):
        num_2 = my_list_2.pop()
        result_1.append(num_2)

print(result_1)