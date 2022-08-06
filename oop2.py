"""class Laptop:
    dell_dicount= 0.1
    def __init__(self,name,model_name,price):
        self.name = name
        self.modle_name = model_name
        self.__price = price #private (for naming convention)
        

new_laptop = Laptop("Lenovo","i7",70000)
new_laptop._Laptop__price = 60000
print(new_laptop._Laptop__price)"""





# Getter and setter 
class Laptop:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self._price = price
        self.model_name = model_name
        # self.full_specs = f"The brand is {brand} andd price is {price}"
        self._price = max(price,0) # problem 1 and 2 solved
    
    @property #getter
    def price(self):
        return self._price
    
    @price.setter #setter
    def price(self,new_price):
        self._price = max(new_price,0)

    @property
    def full_spec(self):
        return  f"The brand is {self.brand} andd price is {self._price}"

new_laptop = Laptop("Lenovo","i7",-70000)
new_laptop.price = -50000
# print(new_laptop._price)
print(new_laptop.full_spec)
print(new_laptop.price)

# inheritance

class Phone: #base class / #parent class
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self._price=price
    
    def full_spec(self):
        return f"brand name: {self.brand} and model name: {self.model_name} "
    
    def dial(self,number):
        return f"dialing... {number}"

p1= Phone("Apple","XS",10000)
p2= Phone("MI","Note 10",90000)
print(p1.dial(9841509543))
print(p2.full_spec())



class SmartPhone(Phone): #derived class / #child class
    def __init__(self,brand,model_name,price,ram,memory,camera):
        # two way
        super().__init__(brand,model_name,price)
        self.ram=ram
        self.memory=memory
        self.camera=camera
      
    def open_browser(self,browser_name):
        return f"Opening {browser_name} browser"

iphone = SmartPhone("Apple","XS",100000,"2GB","64GB","2MP")
redmi = SmartPhone("Redmi","Note 4",80000,"3GB","128GB","20MP")
print(redmi.full_spec())


'''
class SmartPhone(Phone): #base class / #parent class
    def __init__(self,brand,model_name,price,ram,memory,camera):
        #two ways
        Phone.__init__(self,brand,model_name,price) # un-common way
        super().__init__(brand,model_name,price) # common way
        self.ram=ram
        self.memory=memory
        self.camera=camera
        
    def open_browser(self,browser_name):
        return f"Opening {browser_name} browser"
'''
# 3 --> Multiple inheritance

class A:
    def class_a_method():
        print("Hello im class A method")

    def my_method():
        print("This is my method")
        
        


class B:
    def class_b_method():
        print("Hello im class B method")

    def my_method():
        print("This is my method")

class C(A,B):
    pass





