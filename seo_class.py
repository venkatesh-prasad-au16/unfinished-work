class Brand:
    def __init__(self):
            self.brand_nm = ""
            self.make = "Indian"
            self.type = "cool"
    def reveal(self):
        return(self.brand, self.make, self.type)
class Car:
    def __init__(self, nmame):
        self.sku = nmame
        self.cb = Brand()
        


    
        

x = {"sku" : "0000",
    "brand" : "Maruti"}

d = Car("c1")
d.cb.brand_nm="maruiti"

    
