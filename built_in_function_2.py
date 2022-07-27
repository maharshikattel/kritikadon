def any_fun(string):
    return len(string)

names = ["Apple","Joy","Om","Ram Kumar"]

print(max(names,key=any_fun))

print(max(names,key = lambda name: len(name)))

#1 find the name of highest marks:
student1 = [
    {"name":"Ram","score":60,"age":19},
    {"name":"kiran","score":70,"age":20},
    {"name":"om","score":80,"age":21}
    ]

student2 = {
    "Ram":{"score":60,"age":19},
    "kiran":{"score":70,"age":20},
    "om":{"score":80,"age":21}
    }

print(max(student1, key = lambda dict_item: dict_item.get("score"))["name"])

# in a tuple sort doesnt work as tuple isnt immutable but sorted works as it returs the sorted tuple as a list





