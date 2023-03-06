# Task 1

my_int = 237001630
print(str(my_int).count("0"))

# Task 2

my_int = 21300321310
new_int = str(my_int).rstrip("0")
result = len(str(my_int)) - len(new_int)
print(result)

# Task 3

my_list1 = [1, 213, "sada", 3.4, "swe"]
my_list2 = [1, True, "sada", 3.4, "swe", False, None]

my_result = my_list1[::2] + my_list2[::2]  # Or did you mean my_result = my_list1[1::2] + my_list2[1::2]??
print(my_result)

# Task 4

my_list = [1, True, "sada", 3.4, "swe", False, None]
new_list = my_list[1:]
new_list.append(my_list[0])

print(new_list)

# Task 5

my_list = [1, True, "sada", 3.4, "swe", False, None]
x = my_list.pop(0)
my_list.append(x)

print(my_list)

# Task 6

my_str = "1, 2 3 asd2 asd22  44"
str_list = my_str.split()
str_new_list = []
result = 0
for string in str_list:
    digits = ''
    for i in string:
        if i.isdigit():
            digits += i
    str_new_list.append(digits)

for k in str_new_list:
    result += int(k)

print(result)

# Task 7

num_list = [1, 32, 2, 12, 0, 217, 2]
result = 0

for i in num_list[1:-1]:
    x = num_list.index(i)
    summ = num_list[x - 1] + num_list[x + 1]
    if i > summ:
        result += 1
print(result)

# Task 8

my_list = [1, 21, "23", 542, "9", 21, "25", "2"]
new_list = [i for i in my_list if type(i) == str]

print(new_list)

# Task 9

my_str = "my string is unique23"
my_list = [i for i in my_str if my_str.count(i) == 1]

print(my_list)

# Task 10

my_str = "my string is unique23"
my_str2 = "this one is not"

my_list = set(my_str)
my_list2 = set(my_str2)

result = list(my_list.intersection(my_list2))
print(result)

# Task 11

my_str = "my string is unique23"
my_str2 = "this one is not"

my_list = set(my_str)
my_list2 = set(my_str2)

first_set = my_list.intersection(my_list2)
result = list(first_set)

for i in first_set:
    if my_str.count(i) > 1 or my_str.count(i) > 1:
        result.remove(i)
print(result)
