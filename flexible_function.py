"""def sum(a,b):
    return a+b

print(sum(3,4,5))

def another_sum(*args):
    print(args)
    print(type(args))

print(another_sum(2,3,4))

def another_calc(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(another_calc(3,4,5,6))


#  Make a sum function but user gives the sum

def another_calc(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(another_calc(3,4,5,6))"""

# if we use * over lists, it unpacks into a tuple

"""given_list = [2,3,4]
given_power = int(input("Enter the power: "))"""

"""def power_generator(power,*list):
    answer = []
    for i in list:
        answer.append(i**power)
    return answer
print(power_generator(given_power,*given_list))"""

"""def power_generator(power,*list):
    return[i**power for i in list]
print(power_generator(given_power,*given_list))
"""

# **KWARGS
# It makes a dictionaru

"""def sum_of_all_num(**kwargs):
    for key,value in kwargs.items():
        print(f"Your first name is {value}")

print(sum_of_all_num(first_name="Arayama",last_name="Sharma"))"""



"""dict = {"a":1,"b":2,"c":3}
 
def sum(**kwargs):
    sum1 = 0
    for value in kwargs.values():
        sum1 += value
    return sum1

print(sum(**dict))
"""


# FUNCTIONS WITH ALL TYPES OF PARAMETER  PADK (parameter,argument,default,kwargs)



list_names = ["subbu","rishu","talu","syau","maharshi"]
def  capital(name_list,**kwargs):
    ''' To reverse you must give {is_reverse=True} either True or False''' # doc string
    if kwargs["is_reverse"]:
        return[name[-1::-1].title() for name in name_list]
    else:
        return[name.title() for name in name_list]
print(capital(list_names,is_reverse=True))
print(capital.__doc__)





