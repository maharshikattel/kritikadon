def decorator_function(any_function):
    def wrapper_function(*args,**kwargs):
        """THIS IS A WRAPPER FUNCTION"""
        print("This is extra function")
        return any_function(*args,**kwargs)
    return wrapper_function


def decorator_function2(any_function):
    def wrapper_function(*args,**kwargs):
        print("This is extra function")
        return any_function(*args,**kwargs)
    return wrapper_function

# Extra line = "This is extra function"
def fun1():
    print("function --> 1")

# Extra line = "This is extra function"
@decorator_function
def fun2(any_value):
    print(f"function --> 2 with {any_value}")

@decorator_function
def add_two_num(num1,num2):
    """THIS FUNCTION TAKES TWO NUMBERS AND RETURNS THE SUM"""
    return num1 + num2

# fun2(5)
print(add_two_num(3,5))
# print(decorator_function(5))


# importing function
from functools import wraps
from re import T
def decorator_function3(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        """THIS IS WRAPPER FUNCTION"""
        print("This is extra function")
        return any_function(*args,**kwargs)
    return wrapper_function

@decorator_function3
def add(a,b): #return
    """THIS IS ADD FUNCTION"""
    return a+b

add(2,3)
print(add(2,4))
print(add.__name__)
print(add.__doc__) # print the doc string of wrapper function (problem)



def show_function4(func):
    @wraps(func)
    def wrapper_function(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper_function

@show_function4
def adding(a,b):
    """This is adding function"""
    return a+b

adding(3,2)
print(adding.__doc__)
print(adding(3,2))



import time as t
t1 = t.time()
print(t1)
for i in range(1,100,1):
    print(i)
t2 = t.time()
total_required_time = t2 - t1
print(f"total_required_time is {total_required_time}")


def show_time(any_function):
	def wrapper_function(*args,**kwargs):
		''' this is wrapper function '''
		print(f"Executing func {any_function.__name__}")
		t1= t.time()
		returned_value=any_function(*args,**kwargs)
		t2= t.time()
		total_time = t2-t1
		print(f"This func took {total_time} time")
		return returned_value
	return wrapper_function

@show_time
def sq_finder(n):
	return [i**2 for i in range(1,n+1)]

sq_finder(500)


# Decorator practice 3
def only_int_allowed(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        if all([type(arg)==int for arg in args]):
            return any_function(*args,**kwargs)
        else:
            print("Only int is allowed")
    return wrapper_function

@only_int_allowed
def add_func2(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add_func2(1,2,3,4))



# Decorator practice 4

## Decorators with argument


def which_data_allow(data_type):
    def decorator_function(any_function):
        @wraps(any_function)
        def wrapper_function(*args,**kwargs):
            if all([type(arg)==data_type for arg in args]):
                return any_function(*args,**kwargs)
            else:
                print("Only string is allowed")
        return wrapper_function
    return decorator_function

@which_data_allow(int)
def string_join(*args):
	joined_string = ""
	for i in args:
		joined_string += i
	return joined_string

print(string_join("Kritika"," Deo")) 