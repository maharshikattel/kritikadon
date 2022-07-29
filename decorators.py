# 0} Intro
def square(a):
    return a**2

s = square #not calling just assigning

print(s(7)) #but we can call and treat s as a square function
print(s.__name__)
print(s.__name__)

# 1) pass function as argument
# --> for eg: map function
any_list = [1,2,3]
print(list(map(lambda a:a**2, [1,2,3])))

any_list_2 = [4,5,6]
def my_own_map(func,list):
    new_list = []
    for item in list:
        new_list.apppend(func(item))
    return new_list

def cube(num):
    return num**3

map(cube,[1,2,3])

print(list(map(cube,[1,2,3])))

def mero_aafnai_map(fun,list):
    new_list = []
    for ele in list:
        new_list.append(fun(ele))
    return new_list

print(mero_aafnai_map(cube,[4,5,6]))

# 2) Function can return function

def out_func():
    def in_func():
        print("Hello world!")
    return in_func

any_var = out_func()
any_var() #any second function


def out_func(value1):
	def in_func(value2):
		print(f"Hello done any-->{value1} and ok --> {value2} ")
	return in_func

any_var = out_func("ok1")
any_var("any1") # calling second function

# practice 1: 
def cube_off(num):
	def calc_power(n):
		return num**n
	return calc_power

to_power = cube_off(4)
print(to_power(3))
