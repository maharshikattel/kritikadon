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