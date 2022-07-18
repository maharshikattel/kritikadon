"""list1 = list(range(1,10))

def function1(num):
    square_list = []
    for i in range(1,num+1):
        square_list.append(i**2)
    return square_list




def same_square(n):
    return [i**2 for i in range(1,n+1)]

print(function1(10))
print(same_square(10))"""

list2 = ["abc","def","ghi"]
def a_list(list):
    return [(i[0]) for i in list]

print(a_list(["abc","def","ghi"]))



def filter_even(num):
    return [i for i in range(num+1) if (i%2==0)]
print(filter_even(10))



def wacky_math(num):
    return[(2*i) if (i%2==0) else (-i) for i in range(num+1)]
print(wacky_math(10))



# Nested loop
example = [[1,2,3],[1,2,3],[1,2,3]]
def nested_loop(num):
    return [[m for m in range(1,num+1)] for k in range(1,num+1)]

print(nested_loop(3))