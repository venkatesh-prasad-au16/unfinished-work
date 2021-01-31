class Brand:
    
    def __init__(self, brand: dict):
        
        self.type = "Brand"
        self.name = brand["name"]
        self.description = brand["description"]
        
    def display(self):
        self.brand_dict = {}
        self.brand_dict["@type"] = self.type
        self.brand_dict["name"] = self.name
        self.brand_dict["description"] = self.description
        return(self.brand_dict) 

class Organization:
    
    def __init__(self, org: dict):
        self.type = org["@type"]
        self.name = org["name"]
        self.email = org["email"]


    def display(self):
        self.org_dict = {}
        self.org_dict["@type"] = 
        self.org_dict["name"] = 
        self.org_dict["email"] = 
        return(self.org_dict)

class Image:
    def __init__(self, org: dict):
        self.imag_dict = {}


class Car:
    
    def __init__(self, car_dict):
        self.category = "Car"
        self.sku = car_dict["sku"]
        self.cb = Brand(brand_dict)
        


brand_dict = {"name": "Hyundai",
              "description": "Hyundai India", 
              "@type": "Brand"}
org_dict = {"name": "Hyundai", 
            "email": "hyundai@gmail.com", 
            "@type": "Organization"}
imag_dict = {"representativeOfPage": "True", 
             "url": "www.google.com", 
             "@context": "http://www.schema.org", 
             "@type": "ImageObject"}

x = {"sku" : "0000",
    "brand" : brand_dict,
    "manufacturer" : org_dict}



