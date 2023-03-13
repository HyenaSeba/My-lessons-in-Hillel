# Task 1
def updated_list(input_list):
    my_list_en = enumerate(input_list)
    new_list = []
    for i, k in my_list_en:
        if i % 2 != 0:                # or i % 2 == 0 -- I still don't get how we decide which numbers are even in python.
            new_list.append(k[::-1])
        else:
            new_list.append(k)
    return new_list

my_list = ['str', 'asdas', 'write', '12asd213', 'ashda', '2131']

print(updated_list(my_list))

# Task 2

def updated_list(input_list):
    new_list = []
    my_list_en = enumerate(input_list)
    for i, k in my_list_en:
        if k.startswith("a"):
            new_list.append(k)
    return new_list

my_list = ['str', 'asdas', 'write', '12asd213', 'ashda', '2131']

print(updated_list(my_list))

# Task 3

def updated_list(input_list):
    new_list = []
    my_list_en = enumerate(input_list)
    for i, k in my_list_en:
        if k.find('a') != -1:
            new_list.append(k)
    return new_list

my_list = ['str', 'asdas', 'write', '12asd213', 'ashda', '2131']

print(updated_list(my_list))

# Task 4

def updated_list(input_list):
    new_list = [i for i in input_list if type(i) == str]
    return new_list

my_list = [1, 'asdas', 'write', '12asd213', 123, '2131']

print(updated_list(my_list))

# Task 5

def updated_str(input_str):
    my_list = [i for i in input_str if input_str.count(i) == 1]
    return my_list

my_str = "my string is unique23"

print(updated_str(my_str))

# Task 6

def updated_str(input_str1, input_str2):
    my_list = set(input_str1)
    my_list2 = set(input_str2)

    result = list(my_list.intersection(my_list2))
    return result
    
my_str = "my string is unique23"
my_str2 = "this one is not"

print(updated_str(my_str, my_str2))

# Task 7

def updated_str(input_str1, input_str2):
    my_list = set(input_str1)
    my_list2 = set(input_str2)

    first_set = my_list.intersection(my_list2)
    result = list(first_set)

    for i in first_set:
        if input_str1.count(i) > 1 or input_str2.count(i) > 1:
            result.remove(i)
    return result
    
my_str = "my string is unique23"
my_str2 = "this one is not"

print(updated_str(my_str, my_str2))

# Task 8
import random
from string import ascii_lowercase # because only lowercase is used in e-mail formating

def mail(input_list1, input_list2):
    random_int = random.randint(100, 999)
    s = ascii_lowercase
    n = random.randint(5, 7)
    random_str = ''.join(random.choice(s) for i in range(n))
    random_email = (f"{random.choice(input_list1)}.{random_int}@{random_str}.{random.choice(input_list2)}")
    return random_email

names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]

print(mail(names, domains))
