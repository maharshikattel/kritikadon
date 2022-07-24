import numbers


{"key":"value"} 
{"age" : 19}

# create a dictionary

days = {"day1":"Sunday","day2":"Sunday","day3":"Monday","day4":"Tuesday","day5":"Wednesday","day6":"Friday","day7":"Saturday"}
print(days)
print(type(days))

#type2
days2 = dict(day4 = "Wednesday", day5 = "Thursday", day6 = "Friday")
print(days2)
print(type(days2))

#to extract info from dictionary

print(days["day4"])


any_dict = {
        "f_name" : "Maharshi",
        "age" : 23,
        "fav_song" : ["s1","s2",11,False],
        "others":{
            "fav_game":"Football",
            "fav_programming":"Python"
        }
}
print(any_dict["fav_song"][3])
print(any_dict["others"]["fav_programming"])





k_dict = {
        "f_name" : "Aryama",
        "l_name" : "Sharma",
        "age" : 19,
        "fav_movie" : {
            "name_movie": "Thor",
            "publisher": "Marvel",
            },
        "fav_food" : {
            "food1" : "Pizza",
            "food2" : "Chowmein"
        },
        "address":"Kathmandu"
        }

print(k_dict)


#creating empty dict an adding values
empty_dict = {}
print(empty_dict)
empty_dict["name"] = "Kritika is absent.....again"
print(empty_dict)

# In keywords(conditional and looping statements)

print(any_dict)

"""if "f_name" in any_dict:
    print("present")
else:
    print("Not Present")
"""

# different methods huncha ---> keys(),values(),items(),copy(),clear(),get()

if "f_name" in any_dict.values():
    print("present")
else:
    print("Not Present")


for i in any_dict.values():
    print(i)



for i in any_dict.items():
    print(i)


for i,j in any_dict.items():
    print(f"The key is {i} and the value is {j}")


dic1 = {"day1":"Sunday","day2":"Monday"}
dic2 = {"day3":"Wednesday","day4":"Tuesday"}

dic3 = dic1.copy()

# add value to to dic3
dic3["day5"]=["Nice day","Rainy Day"]
dic3["all_day"]=["day1","day2","day3"]
print(dic3)

print(dic1)
dic1.update(dic2)

popped_item = dic1.pop("day1")
print(dic1)
print(popped_item)


#fromkeys(keys,values) method
days = dict.fromkeys(["day1","day2","day3"], "uknown")
print(days)

# print(days["day5"]) #404 error
print(days.get("day3"))
print(days.get("day5")) # --> doesnt gove error



if (any_dict.get("address")):
    print("Present")
else:
    print("Absent")


print(days.get("day5","Sorry! Your value wasnt found"))


user_info = {"fname":"Aryama","lname":"Sharma","age":30,"age":17}
print(user_info.get("age"))


number = int(input("Enter a number: "))

def cube(num):
    dic0 = {}
    for i in range(0,num+1):
        dic0[i] = i**3 
    return dic0

print(cube(number))



name_user_input = int(input("Enter a name: "))

def cube(name_in_function):
    new_dict = {}
    for char in name_in_function:
        new_dict[char] = name_in_function.lower().count(char)
    return new_dict

print(cube(name_user_input))



