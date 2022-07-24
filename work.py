


"""
def even_odd_spearator(input_number):
    the_dict = {}
    for i in range (0,input_number + 1):
        if i%2 == 0:
            the_dict[i] = "Even"   
        else:
            the_dict[i] = "Odd"
    return the_dict

print(even_odd_spearator(user_input_number))
"""
"""def even_odd_separator(input_number):
    return{i :"even" if i%2==0 else "odd" for i in range (input_number+1)}
print(even_odd_separator(user_input_number))"""

"""name_user_input = input("Enter name: ")

def counter(word_input):
    return{char: word_input.lower().count(char.lower()) for char in word_input.lower()}
print(counter(name_user_input))"""

"""user_input_number = int(input("Enter a number: "))

def set1(input_num):
    return{(i**2) for i in range (input_num+1)}
print(set1(user_input_number))"""


"""def set1(input_num):
    return{(i,i**2) for i in range (input_num+1)}
print(set1(user_input_number))"""


list_of_names = []
for i in range (0,5):
    list_of_names.append(input("Enter names: "))

def initials(names):
    return{i[0] for i in names}

print(initials(list_of_names))


