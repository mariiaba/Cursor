
#1. Define the id of next variables:

int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(id(int_a))
print(id(str_b))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))

#Output:

#9786624
#140362932224432
#140362932229952
#140362933127104
#140362933084672

#2. Append 4 and 5 to the lst_d and define the id one more time.

lst_d.append(4)
lst_d.append(5)
print (lst_d)
print (id(lst_d))

#Output
#[1, 2, 3, 4, 5]
#140231938635712

#3. Define the type of each object from step 1.

print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

#<class 'int'>
#<class 'str'>
#<class 'set'>
#<class 'list'>
#<class 'dict'>

#4*. Check the type of the objects by using isinstance.

print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

#Output
#True
#True
#True
#True
#True


# 5. String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."
# With .format and curly braces {}

string = "Anna has {} apples and {} peaches.".format(2, 3)
print(string)

#Anna has 2 apples and 3 peaches.

# 6. By passing index numbers into the curly braces.
print ("Anna has {0} apples and {1} peaches.".format(2,3))

# Anna has 2 apples and 3 peaches.

#7. By using keyword arguments into the curly braces.
print ("Anna has {apples} apples and {peaches} peaches.".format(apples = 2, peaches = 3))

# Anna has 2 apples and 3 peaches.

#8*. With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {0:5} apples and {1:3} peaches.".format (2,3))

# Anna has     2 apples and   3 peaches.

#9. With f-strings and variables

a=2
p=3

print(f"Anna has {a} apples and {p} peaches")

# Anna has 2 apples and 3 peaches

#10.With % operator

print("Anna has %s apples and %s peaches" %(a, p))

# Anna has 2 apples and 3 peaches

# 11*. With variable substitutions by name (hint: by using dict)

apples = 2
peaches = 3
dictionary = {"a": apples, "p": peaches}
print("Anna has %(a)s apples and %(p)s peaches" %dictionary)

#Anna has 2 apples and 3 peaches

# 12. Convert (1) to list comprehension
# (1)
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)

comprehension1 = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print (comprehension1)

# [0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]

#13 Convert (2) to regular for with if-else
# (2)
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
# print(list_comprehension)

list_comprehension = []
for num in range(10):
       if num % 2 == 0:
             list_comprehension.append (num//2)
       else:
             list_comprehension.append (num *10)
print (list_comprehension)

# [0, 10, 1, 30, 2, 50, 3, 70, 4, 90]

#14. Convert (3) to dict comprehension.
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)

comprehension3 = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(comprehension3)
# {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}


# 15*. Convert (4) to dict comprehension.
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)

comprehension4 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1,11)}
print(comprehension4)

# {1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}

# 16. Convert (5) to regular for with if.
# dict_comprehension = {x: x ** 3 for x in range(10) if x ** 3 % 4 == 0}
# print(dict_comprehension)

dict1 = {}
for x in range(10):
       if x ** 3 % 4 == 0:
              dict1[x] = x**3
print(dict1)

#{0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

# 17*. Convert (6) to regular for with if-else.
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}

dict2 = {}
for x in range(10):
       if x **3 %4 == 0:
              dict2[x] =x**3
       else:
                  dict2[x] = x
print(dict2)

#{0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}


# 18. Convert (7) to lambda function
# Lambda:
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y

foo = lambda x, y: x if x < y else y

# 19*. Convert (8) to regular function
# foo = lambda x, y, z: z if y < x and x > z else y

def foo(x,y,z):
       if y < x and x > z:
              return z
       else:
              return y


# 20. Sort lst_to_sort from min to max
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

print(sorted(lst_to_sort))

# [1, 5, 13, 15, 18, 24, 33, 55]

# 21. Sort lst_to_sort from max to min

print(sorted(lst_to_sort, reverse=True))

# [55, 33, 24, 18, 15, 13, 5, 1]

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2


list_new = (list(map(lambda x: x * 2, lst_to_sort)))
print(list_new)

#[10, 36, 2, 48, 66, 30, 26, 110]

# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]

list_new1 = list(map(lambda x,y: x+y, list_A, list_B))
print(list_new1)

# [7, 9, 11]


# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]


from functools import reduce
numbers = reduce(lambda x, y : x + y, lst_to_sort)
print(numbers)

# 164

# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.

list_new2 = list(filter(lambda x: x % 2 == 1, lst_to_sort))
print(list_new2)

# [5, 1, 33, 15, 13, 55]

# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.

b = range(-10, 10)
list_new3 = (list(filter(lambda x: x < 0, b)))
print(list_new3)

# [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

# 27*. Using the filter function, find the values that are common to the two lists:

list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]

list_new4 = list(filter(lambda x: x in list_2, list_1))
print(list_new4)

# [2, 3, 5, 7]