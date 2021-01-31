class Brand:
    
    def __init__(self, brand: dict):
        self.type = "Brand"
        self.context = "http://www.schema.org"
        self.name = brand["name"]
        self.description = brand["description"]
        
    def retrieve(self):
        self.brand_dict = {}
        self.brand_dict["@type"] = self.type
        self.brand_dict["@context"] = self.context
        self.brand_dict["name"] = self.name
        self.brand_dict["description"] = self.description
        return(self.brand_dict)

    def print(self):
        self.brand_dict = {}
        self.brand_dict["@type"] = self.type
        self.brand_dict["@context"] = self.context
        self.brand_dict["name"] = self.name
        self.brand_dict["description"] = self.description
        print(self.brand_dict) 

class Organization:
    
    def __init__(self, org: dict):
        self.type = "Organization"
        self.context = "http://www.schema.org"
        self.name = org["name"]
        self.email = org["email"]
    
    def retrieve(self):
        self.org_dict = {}
        self.org_dict["@type"] = self.type
        self.org_dict["@context"] = self.context
        self.org_dict["name"] = self.name
        self.org_dict["email"] = self.email
        return(self.org_dict)
    
    def print(self):
        self.org_dict = {}
        self.org_dict["@type"] = self.type
        self.org_dict["@context"] = self.context
        self.org_dict["name"] = self.name
        self.org_dict["email"] = self.email
        return(self.org_dict)

class ImageObject:
    
    def __init__(self, img: str):
        self.type = "ImageObject"
        self.context = "http://www.schema.org"
        self.url = img["url"]

    def retrieve(self):
        self.image_dict = {}
        self.image_dict["@type"] = self.type
        self.image_dict["@context"] = self.context
        self.image_dict["url"] = self.url
        return(self.image_dict)

    def print(self):
        self.image_dict = {}
        self.image_dict["@type"] = self.type
        self.image_dict["@context"] = self.context
        self.image_dict["url"] = self.url
        print(self.image_dict)

class EngineSpecificaton:
        
    def __init__(self, engine: dict):
        self.type = "EngineSpecificaton"
        self.context = "http://www.schema.org"
        self.engineType = engine["engineType"]
        self.fuelType = engine["fuelType"]
        self.engineDisplacement = engine["engineDisplacement"]
        
    def retrieve(self):
        self.engine_dict = {}
        self.engine_dict["@type"] = self.type
        self.engineType["@context"] = self.context
        self.engine_dict["engineType"] = self.engineType
        self.engine_dict["fuelType"] = self.fuelType
        self.engine_dict["engineDisplacement"] = self.engineDisplacement
        return(self.engine_dict)

    def print(self):
        self.engine_dict = {}
        self.engine_dict["@type"] = self.type
        self.engineType["@context"] = self.context
        self.engine_dict["engineType"] = self.engineType
        self.engine_dict["fuelType"] = self.fuelType
        self.engine_dict["engineDisplacement"] = self.engineDisplacement
        print(self.engine_dict)

class Offer:
    
    def __init__(self, price):
        self.type = "Offer"
        self.context = "http://www.schema.org"
        self.price = price
    
    def retrieve(self):
        self.offer_dict = {}
        self.offer_dict["@type"]= self.type
        self.offer_dict["@context"] = self.context
        self.offer_dict["price"] = self.price
        return(self.offer_dict)

    def print(self):
        self.offer_dict = {}
        self.offer_dict["@type"]=self.type
        self.offer_dict["@context"] = self.context
        self.offer_dict["price"] = self.price
        print(self.offer_dict)

class QuantitativeValue:
    
    def __init__(self, value):
        self.type = "QuantitativeValue"
        self.context = "http://www.schema.org"
        self.value = value

    def retrieve(self):
        self.d = {}
        self.d["@type"] = self.type
        self.d["@context"] = self.context
        self.d["value"] = self.value
        return (self.d)

    def print(self):
        self.d = {}
        self.d["@type"] = self.type
        self.d["@context"] = self.context
        self.d["value"] = self.value
        print(self.d)

class PropertyValue:

    def __init__(self, x: str, y:str):
        self.type = "PropertyValue"
        self.context = "http://www.schema.org"
        self.name = x
        self.value = y
    
    def retrieve(self):
        self.d = {}
        self.d["@type"] = self.type
        self.d["@context"] = self.context
        self.d["name"] = self.name
        self.d["value"] = self.value
        return(self.d)

    def print(self):
        self.d = {}
        self.d["@type"] = self.type
        self.d["@context"] = self.context
        self.d["name"] = self.name
        self.d["value"] = self.value
        print(self.d)

class Warranty:

    def __init__(self, x: str):
        self.type = "MerchantReturnPolicy"
        self.context = "http://www.schema.org"
        self.description = x

    def retrieve(self):
        self.warranty = {}
        self.warranty["@type"] = self.type
        self.warranty["@context"] = self.context
        self.warranty["description"] = self.description
        return(self.warranty)

    def print(self):
        self.warranty = {}
        self.warranty["@type"] = self.type
        self.warranty["@context"] = self.context
        self.warranty["description"] = self.description
        print(self.warranty)

class URL:
    def __init__(self, x: str):
        self.type = "URL"
        self.context = "http://www.schema.org"
        self.url = x

    def retrieve(self):
        self.d = {}
        self.d["@type"] = self.type
        self.d["@context"] = self.context
        self.d["url"] = self.url
        return(self.d)
    
    def print(self):
        self.d = {}
        self.d["@type"] = self.type
        self.d["@context"] = self.context
        self.d["url"] = self.url
        print(self.d)

class Car:
    
    def __init__(self, car_dict: dict):
        self.type = "Car"
        self.context = "http://www.schema.org"
        self.sku = car_dict["sku"]
        self.model = car_dict["model"]
        self.fuelType = car_dict["fuelType"]
        self.vehicleConfiguration = car_dict["vehicleConfiguration"]
        self.bodyType = car_dict["bodyType"]
        self.seatingCapacity = car_dict["seatingCapacity"]
        self.driveWheelCOnfiguration = car_dict["driveWheelCOnfiguration"]
        self.bodyType = car_dict["bodyType"]
        self.seatingCapacity = car_dict["seatingCapacity"]
        self.vehicleTransmission = car_dict["vehicleTransmission"]
        self.numberOfAirbags = car_dict["numberOfAirbags"]
        self.vehicleInteriorType = car_dict["vehicleInteriorType"]
        self.color = car_dict["color"]

        self.manufacturer = Organization(car_dict["manufacturer"]).retrieve()
        self.vehicleEngine = EngineSpecificaton(car_dict["vehicleEngine"]).retrieve()
        self.offers = Offer(car_dict["offer"]).retrieve()
        self.fuelConsumption = QuantitativeValue(car_dict["fuelConsumption"]).retrieve()
        self.additionalProperty0 = PropertyValue("Infotainment System",car_dict["infotain"]).retrieve()
        self.additionalProperty1 = PropertyValue("Air Conditioner type",car_dict["airCon"]).retrieve()
        self.additionalProperty2 = PropertyValue("Sunroof",car_dict["sunRoof"]).retrieve()
        self.additionalProperty3 = PropertyValue("Dual Tone Color",car_dict["dualtone"]).retrieve()
        self.additionalProperty4 = PropertyValue("Front Brake Type",car_dict["frontBrake"]).retrieve()
        self.additionalProperty5 = PropertyValue("Rear Brake Type",car_dict["rearBrake"]).retrieve()
        self.additionalProperty6 = PropertyValue("Front Suspension",car_dict["frontSus"]).retrieve()
        self.additionalProperty7 = PropertyValue("Rear Suspension",car_dict["rearSus"]).retrieve()
        self.additionalProperty8 = PropertyValue("Wheel Size",car_dict["wheelSize"]).retrieve()
        self.additionalProperty8 = PropertyValue("Tyre Size",car_dict["tyreSize"]).retrieve()
        self.warranty = Warranty(car_dict["warranty"]).retrieve()
        self.logo = ImageObject(car_dict["logo"]).retrieve()
        self.image = ImageObject(car_dict["image"]).retrieve()
        self.identifier = URL(car_dict["url"]).retrieve()
        self.url = URL(car_dict["url"]).retrieve()

    def retrieve(self):
        self.final = {}
        self.final["@type"] = self.type
        self.final["@context"] = self.context
        self.final["sku"] = self.sku
        self.final["model"] = self.model
        self.final["fuelType"] = self.fuelType
        self.final["vehicleConfiguration"] = self.vehicleConfiguration
        self.final["bodyType"] = self.bodyType
        self.final["seatingCapacity"] = self.seatingCapacity
        self.final["driveWheelCOnfiguration"] = self.driveWheelCOnfiguration
        self.final["bodyType"] = self.bodyType
        self.final["seatingCapacity"] = self.seatingCapacity
        self.final["vehicleTransmission"] = self.vehicleConfiguration
        self.final["numberOfAirbags"] = self.numberOfAirbags
        self.final["vehicleInteriorType"] = self.vehicleInteriorType
        self.final["color"] = self.color
