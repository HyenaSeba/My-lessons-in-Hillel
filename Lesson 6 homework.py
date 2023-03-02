# Task 1

my_list = [1, 10, 213, -100, 2311, -293, 12, 934]
for i in my_list:
    if i > 100:
        print(i)

# Task 2

my_list = [1, 20, 213, -102, 2312, -21312, 22, 1241]
my_results = []
for i in my_list:
    if i > 100:
        my_results.append(i)
print(my_results)

# Task 3

last_sum = my_list[-1] + my_list[-2]
my_list = [1, 20, 213, -102, 2312, -21312, 22, 1241]

if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(last_sum)
print(my_list)
