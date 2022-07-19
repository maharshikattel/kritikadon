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