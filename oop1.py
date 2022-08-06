"""
1) Create your first cloass
class, inti method/costructor, attributes, instance variable and create object"""


class Person:
    # init method/constructir
    def __init__(self,name,age,sex): # name, age, sex ---> attribute
        print("My beautiful init method called")
        # instance variable
        self.f_name = name
        self.age = age
        self.sex = sex
        self.address = "Thapathali"
    
p1 = Person("Samay", 21, "Male")
p2 = Person("Rushav", 19, "M")
print(p1.f_name)


class Laptop:
    dell_dicount= 0.1
    def __init__(laptop,name,price,colour,model,count):
        laptop.l_name = name
        laptop.price = price
        laptop.colour = colour
        laptop.model = model
        laptop.full = name + model
        Laptop.count  = count + 1
        return Laptop.count
    def discount(laptop):
        laptop.percent = laptop.price - (0.1*laptop.price)
        return laptop.percent
    #class method creation
    @classmethod
    def countt_all_laptop(own_class):
        return f"You have total {own_class.count} in your {own_class.__name__} store"






l1 = Laptop("Dell",50000,"black","Inspiron 15")
l2 = Laptop("Lenovo",60000,"silver","Thinkpad 2")

print(l2.full)
print(l2.discount())
print(Laptop.count)



