# 0) Track the position without enumerate function

list_names = ["subbu","rishu","talu","syau","maharshi"]
"""
position=0
for i in list_names:
    print(f"The name is {i} is in {position} position")
    position+=1"""


"""for location,name in enumerate(list_names):
    print(f"The name {name} is in {location} position")"""


"""def find(name_list,target_name):
    for position,name in enumerate(name_list):
        if name.title() == target_name.title():
            print(position+1)

print(find(list_names,"talu"))"""



def square(*args):
    square_1 = []
    for i in args:
        square_1.append(i**2)
    return square_1
list1 = [1,2,3,4] #iterables
print(square(*list1))

def squares(a):
    return a**2

k_ho = list(map(squares,list1)) #iterators
print(k_ho)

for i in k_ho:
    print(f"k_ho: {i}")

k_ho = list(map(lambda a:a**2,list1))

num_list = [1,2,3,4,5,6,7,8] # iterables

# iter() ---> iterator ma convert garne

"""iterator_converted = iter(num_list)
print(next(iterator_converted))
print(next(iterator_converted))
print(next(iterator_converted))
print(next(iterator_converted))

for i in num_list:
    print(i)"""

def filter_even(nums):
    return[i for i in nums if i%2==0]

print(filter_even(num_list))



def even_func(i):
    return i%2==0

print(filter(even_func,num_list))
even_list = tuple(filter(even_func,num_list))
even_list2 = list(filter(lambda a: a%2==0,num_list))
print(even_list)
print(even_list2)

# print(filter_even(num_list))
# print(filter_even2(num_list))


small_char_list = ["a","b","c"]
num_list = [1,2,3,4,5,6,7,8]
big_char_list = ["A","B","C","D"]

print(tuple(zip(small_char_list,num_list,big_char_list)))

l = (list(zip(small_char_list,num_list)))

#  for un-zip
l1,l2 = zip(*l)
print(l1)
print(l2)



# To find highest number among two lists which is separated in order of their evenness or oddness

user_input_number = int(input("Enter a number: "))

def input_func(input_number):
    input_list = []
    for i in range(0, input_number+1):
        input_list.append(i)
    return input_list

def odd_even(function_ko_list):
    function_odd = []
    function_even =[]
    for i in function_ko_list:
        if i%2==0:
            function_even.append(i)
        else:
            function_odd.append(i)
    return(list(zip(function_even,function_odd)))

def greater(function_ko_zipped):
    unzip_1, unzip_2 = zip(*function_ko_zipped)
    if unzip_1[0] > unzip_2[0]:
        return unzip_1
    else:
        return unzip_2

user_made_list = input_func(user_input_number)
print(user_made_list)
zipped_list = odd_even(user_made_list)
print(zipped_list)
greater_numbers_outside_loop = greater(zipped_list)
print(greater_numbers_outside_loop)



"""to define a function which takes lists and adds the elements of list to bring a average of three"""

average_calculator = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
print(average_calculator([1,2,3],[4,5,6],[7,8,9]))



# any/all functions any->or operator, all->and operator
even_list = [True,True,True]

print(all(even_list))

even_list = [False,True,True]
print(any(even_list))

def check_even(list):
    even_list=[]
    for i in list:
        even_list.append(i%2==0)
    return even_list

print(check_even(num_list))
# allternate
print(all([num%2==0 for num in num_list]))



# practice for all and any

def sum(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        total = 0
        for num in args:
            total += num
        return total
    else:
        return "Int or Float are allowed only"

print(sum(1,3.9))