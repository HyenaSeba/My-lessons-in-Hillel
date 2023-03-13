# Task 1 

my_list = ['str', 'asdas', 'write', '12asd213', 'ashda', '2131']
new_list = []

my_list_en = enumerate(my_list)

for i, k in my_list_en:
    if i % 2 != 0:                # or i % 2 == 0 -- I still don't get how we decide which numbers are even in python.
        new_list.append(k[::-1])
    else:
        new_list.append(k)

print(new_list)    

# Task 2

my_list = ['str', 'asdas', 'write', '12asd213', 'ashda', '2131']
new_list = []

my_list_en = enumerate(my_list)

for i, k in my_list_en:
    if  k.find('a') == 0:
        new_list.append(k)

print(new_list)

# Task 3 

my_list = ['str', 'asdas', 'write', '12asd213', 'ashda', '2131']
new_list = []

my_list_en = enumerate(my_list)

for i, k in my_list_en:
    if  k.find('a') != -1:
        new_list.append(k)

print(new_list)

# Task 4

list_dict = [
    {"name": "John","age": 15},
    {"name": "James", "age": 27},
    {"name": "Whitney", "age": 23},
    {"name": "Jack", "age": 45},
    {"name": "William", "age": 15},
    {"name": "Marckus", "age": 15},
    ]

youngest = []
longest = []
the_youngest = []
the_longest = []
x_sum = 0
the_average = 0

for i in list_dict:
    for key, value in i.items():
        if key == "name":
            the_longest.append(value)
        elif key == "age":
            the_youngest.append(value)
        else:
            pass

for i in the_longest:
    if len(i) == len(max(the_longest, key=len)):
        longest.append(i)
for i in the_youngest:
    if min(the_youngest) == i:
        youngest.append(i)

for i in list_dict:
    for k, j in i.items():
        if k == "age":
            x_sum += j

the_average = x_sum / len(list_dict)

print(youngest, longest, the_average)

# Task 5

my_dict1 = {"name": "John",
            "age": 13,
            "e-mail": "john@mail.com",
            }
my_dict2 = {"name": "Jessy",
            "last name": "Brown",
            "e-mail": "jessy@mail.com",
            }

keys_list = []
keys_list2 = []
new_dict = my_dict1.copy()

for key in my_dict1:
    if key in my_dict2:
        keys_list.append(key)

for key in my_dict1:
    if not key in my_dict2:
        keys_list2.append(key)
        
for key, value in my_dict2.items():
    if key in new_dict:
        _ = []
        _.append(new_dict[key])
        new_dict[key] = _
        _.append(my_dict2[key])
    else:
        new_dict[key] = my_dict2[key]

print(keys_list)
print(keys_list2)
print(new_dict)
