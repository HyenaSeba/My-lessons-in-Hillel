# Task 1

def new_list(my_list):
    n_list = []
    my_list_en = enumerate(my_list)
    for i, k in my_list_en:
        if i % 2 != 0:  # or i % 2 == 0 -- I still don't get how we decide which numbers are even in python.
            n_list.append(k[::-1])
        else:
            n_list.append(k)
    return n_list


m_list = ['str', 'asdas', 'write', '12asd213', 'ashda', '2131']

print(new_list(m_list))

# Task 2


def new_list(my_list):
    n_list = []
    my_list_en = enumerate(my_list)
    for i, k in my_list_en:
        if k.startswith('a'):
            n_list.append(k)
    return n_list


m_list = ['str', 'asdas', 'write', '12asd213', 'ashda', '2131']

print(new_list(m_list))

# Task 3


def new_list(my_list):
    n_list = []
    my_list_en = enumerate(my_list)
    for i, k in my_list_en:
        if k.find('a') != -1:
            n_list.append(k)
    return n_list


m_list = ['str', 'asdas', 'write', '12asd213', 'ashda', '2131']

print(new_list(m_list))

# Task 4


def new_list(my_list):
    n_list = [i for i in my_list if type(i) == str]
    return n_list


m_list = [1, 21, "23", 542, "9", 21, "25", "2"]

print(new_list(m_list))

# Task 5


def new_list(my_str):
    n_list = [i for i in my_str if my_str.count(i) == 1]
    return n_list


m_str = "my string is unique23"

print(new_list(m_str))

# Task 6


def new_list(my_str1, my_str2):
    my_list = set(my_str1)
    my_list2 = set(my_str2)
    result = list(my_list.intersection(my_list2))

    return result


my_str1 = "my string is unique23"
my_str2 = "this one is not"

print(new_list(my_str1, my_str2))

# Task 7


def new_list(my_str1, my_str2):
    my_list = set(my_str1)
    my_list2 = set(my_str2)
    first_set = my_list.intersection(my_list2)
    result = list(first_set)

    for i in first_set:
        if my_str1.count(i) > 1 or my_str2.count(i) > 1:
            result.remove(i)
    return result


my_str1 = "my string is unique23"
my_str2 = "this one is not"

print(new_list(my_str1, my_str2))

# Task 8
import random
from string import ascii_lowercase # because only lowercase is used in e-mail formating


def email(my_list1, my_list2):
    num = random.randint(100, 999)
    s = random.randint(5, 7)
    ss = ''.join(random.choice(ascii_lowercase) for i in range(s))
    result = f"{random.choice(names)}.{num}@{ss}.{random.choice(domains)}"
    return result


names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]

print(email(names, domains))
