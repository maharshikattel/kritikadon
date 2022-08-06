class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def full_name(self):
        print(f"The full spec of this phone is: {self.brand} {self.model} and price is: {self.price}")


class SmartPhone(Phone):
    def __init__(self,brand,model,price,ram,memory,camera):
        super().__init__(brand,model,price)
        self.ram = ram
        self.memory = memory
        self.camera = camera

    def full_spec(self):
        print(f"The full spec of this phone is: {self.brand} {self.model} and price is: {self.price}")
        

class FlagShipPhone(SmartPhone):
    def __init__(self,brand,model,price,ram,memory,camera,security):
        super().__init__(brand,model,price,ram,memory,camera)
        self.security = security

    def full_spec(self):
        print(f"The full spec of this phone is: {self.brand} {self.model} and price is: {self.price}, moreover it has the new {self.security} for security")
        

phone1 = Phone("Maharshi","Landline",4500)
phone2 = SmartPhone("Xiaomi","Note V",45000,"3gb","64gb","20MP")
phone3 = FlagShipPhone("Samsung","Z Flip 4",450000,"8gb","512gb","78MP","Newly updated Samsung Shield")

print(phone2.full_spec())
print(FlagShipPhone.mro())
