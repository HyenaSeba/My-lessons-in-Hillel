# Task 1
new_str = "myNEWstring"
print(new_str[2])
print(new_str[-2])
print(new_str[:5])
print(new_str[:(len(new_str) - 2)])
print(new_str[::2])
print(new_str[1::2])
print(new_str[::-1])
print(new_str[-1::-2])
print(len(new_str))

# Task 2
second_str = input()
number_of_words = 0
x = "  "
z = " "
while x in second_str:
    second_str = second_str.replace(x, z)
space = second_str.count(z)
if second_str[-1] == z and second_str[0] == z:
    number_of_words = space - 1
elif second_str[-1] == z or second_str[0] == z:
    number_of_words = space
else:
    number_of_words = space + 1
print(number_of_words)

# Task 3
s = input("your string: ")
ch = input("what to find: ")

number_of_ch = 0

while True:
    if s.find(ch) > -1:
        number_of_ch += 1
        s = s[(s.find(ch) + 1):]
    else:
        break

print(number_of_ch)

# Task 4

new_str = input("your string: ")

first = new_str.find('h')
last = new_str.rfind('h')

my_str = new_str[0:first+1] + new_str[first+1:last].replace('h', 'H') + new_str[last:]

print(my_str)





