user_number = str(input("enter numbers: "))
def another_calc(*args):
    sum = 0
    for i in args:
        sum += i%10
    return sum

print(another_calc(int(user_number)))
