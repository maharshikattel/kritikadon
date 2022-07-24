user_number = input("Enter numbers to sum: ")

def another_calc(num):
    sum = 0
    for i in range(3):
        i %=10
        sum += i
    return sum

for i in range(len(user_number)+1):
    num_converted_numbers = int(user_number[i])
    print(another_calc(num_converted_numbers))