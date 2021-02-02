"""
Class Car : Accepts dictionary object while instantiation.
Class Car Methods : get for each property, set for each property, dump_schema and get_schema
"""
import json
import sys
sys.path.append(".")
from Organization import Organization
from EngineSpecification import EngineSpecification
from Offer import Offer
from QuantitativeValue import QuantitativeValue
from MerchantReturnPolicy import MerchantReturnPolicy
from ImageObject import ImageObject

class Car:

    # Pass string price if user wants to set value while object instantiation
    def __init__(self, cardict : dict = {}):
        self._type = 'Car'
        self._context = 'http://www.schema.org'
        self._sku = cardict.get('sku')
        self._mpn = cardict.get('mpn')
        self._model = cardict.get('model')
        self._name = cardict.get('name')
        self._fuelType = cardict.get('fuelType')
        self._image = cardict.get('imageURL')
        self._vehicleConfiguration = cardict.get('vehicleConfiguration')
        self._bodyType = cardict.get('bodyType')
        self._seatingCapacity = cardict.get('seatingCapacity')
        self._driveWheelConfiguration = cardict.get('driveWheelConfiguration')
        self._vehicleTransmission = cardict.get('vehicleTransmission')
        self._numberOfAirbags = cardict.get('numberOfAirbags')
        self._color = cardict.get('color')
        self._vehicleInteriorType = cardict.get('vehicleInteriorType')

        self._manufacturer = Organization()
        self._manufacturer.set_org_name(cardict.get('manufacturer'))
        self._manufacturer.set_org_email(cardict.get('email'))

        self._vehicleEngine = EngineSpecification()
        self._vehicleEngine.set_engine_type(cardict.get('engineType'))
        self._vehicleEngine.set_engine_fuel_type(cardict.get('fuelType'))
        self._vehicleEngine.set_engine_displacement(cardict.get('engineDisplacement'))
        
        self._offer = Offer()
        self._offer.set_price(cardict.get('offers'))

        self._fuelConsumption = QuantitativeValue()
        self._fuelConsumption.set_value(cardict.get('fuelConsumption'))

        self._warranty = MerchantReturnPolicy()
        self._warranty.set_description(cardict.get('warranty'))

        self._logo = ImageObject()
        self._logo.set_img_url(cardict.get("logoUrl"))
        self._logo.set_img_repVal(cardict.get("logoRepVal"))

    
    def set_image_url(self, x: str):
        self._image = x

    def get_image_url(self):
        return(self._image)

    def set_logo_url(self, x: str):
        self._logo.set_img_url(x)
    
    def set_logo_repVal(self, x: str):
        return(self._logo.set_img_repVal(x))
    
    def get_logo_details(self):
        return(self._logo.get_dict())


    def set_warranty(self, x: str):
        self._warranty.set_description(x)

    def get_warranty(self):
        return(self._warranty.get_description())

    def set_fuelConsumption(self, x: str):
        self._fuelConsumption.set_value(x)
    
    def get_fuelConsumption(self):
        return(self._fuelConsumption)

    def set_engine_type(self, x: str):
        self._vehicleEngine.set_engine_type(x)
    
    def set_engine_fuel_type(self, x:str):
        self._vehicleEngine.set_engine_fuel_type(x)
    
    def set_engine_displacement(self, x: str):
        self._vehicleEngine.set_engine_displacement(x)

    def get_engine_details(self):
        return(self._vehicleEngine.get_dict())

    # Method to manually set the string sku
    def set_sku(self, x: str):
        self._sku = x
    
    # Method to retrieve the value of sku
    def get_sku(self):
        return(self._sku)

    # Method to manually set the string sku
    def set_mpn(self, x: str):
        self._mpn = x
    
    # Method to retrieve the value of sku
    def get_mpn(self):
        return(self._mpn)

    # Method to manually set the string model
    def set_model(self, x: str):
        self._model = x 
    
    # Method to retrieve the value of model
    def get_model(self):
        return(self._model)

    # Method to manually set the string name
    def set_name(self, x: str):
        self._name = x 
    
    # Method to retrieve the value of name
    def get_name(self):
        return(self._name)
    
    # Method to manually set the string fuelType
    def set_fuelType(self, x: str):
        self._fuelType = x 
    
    # Method to retrieve the value of fuelType
    def get_fuelType(self):
        return(self._fuelType)

    def set_vehicleConfiguration(self, x: str):
        self._vehicleConfiguration = x 
    
    # Method to retrieve the value of fuelType
    def get_vehicleConfiguration(self):
        return(self._vehicleConfiguration)

    # Method to set the value of bodyType
    def set_bodyType(self, x: str):
        self._bodyType = x 
    
    # Method to retrieve the value of bodyType
    def get_bodyType(self):
        return(self._bodyType)

    # Method to set the value of seatingCapacity
    def set_seatingCapacity(self, x: str):
        self._seatingCapacity = x 
    
    # Method to retrieve the value of seatingCapacity
    def get_seatingCapacity(self):
        return(self._seatingCapacity)

    # Method to set the value of driveWheelCOnfiguration
    def set_driveWheelConfiguration(self, x: str):
        self._driveWheelConfiguration = x

    # Method to get the value of driveWheelConfiguration
    def get_driveWheelConfiguration(self):
        return(self._driveWheelConfiguration)

    # Method to set the value of vehicleTransmission
    def set_vehicleTransmission(self, x: str):
        self._vehicleTransmission = x 
    
    # Method to retrieve the value of vehicleTransmission
    def get_vehicleTransmission(self):
        return(self._vehicleTransmission)

    # Method to set the value of numberOfAirbags
    def set_numberOfAirbags(self, x: str):
        self._numberOfAirbags = x

    # Method to get the value of numberOfAirbags
    def get_numberOfAirbags(self):
        return(self._numberOfAirbags)

    # Method to set the color value
    def set_color(self, x: str):
        self._color = x

    #Method to get the color value
    def get_color(self):
        return(self._color)

    def set_manufacturer_name(self, x: str):
        self._manufacturer.set_org_name(x)
    
    def set_manufacturer_email(self, x: str):
        self._manufacturer.set_org_email(x)

    def get_manufacturer_details(self):
        self._manufacturer.get_dict()

    def set_vehicleIinteriorType(self, x: str = ""):
        self._vehicleInteriorType = x

    def get_vehicleInteriorType(self):
        return(self._vehicleInteriorType)
    
    def set_offer_price(self, x:str):
        self._offer.set_price(x)
    
    def get_offer_price(self):
        return(self._offer.get_price())


    # Method to print JSON-LD to console
    def dump_schema(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['sku'] = self._sku
        self.d['mpn'] = self._mpn
        self.d['model'] = self._model
        self.d['name'] = self._name
        self.d['color'] = self._color
        self.d['image'] = self._image
        self.d['fuelType'] = self._fuelType
        self.d['vehicleConfiguration'] = self._vehicleConfiguration
        self.d['bodyType'] = self._bodyType
        self.d['seatingCapacity'] = self._seatingCapacity
        self.d['driveWheelConfiguration'] = self._driveWheelConfiguration
        self.d['vehicleTransmission'] = self._vehicleTransmission
        self.d['numberOfAirbags'] = self._numberOfAirbags
        self.d['vehicleInteriorType'] = self._vehicleInteriorType
        self.d['manufacturer'] = self._manufacturer.get_dict()
        self.d['vehicleEngine'] = self._vehicleEngine.get_dict()
        self.d['offers'] = self._offer.get_dict()
        self.d['fuelConsumption'] = self._fuelConsumption.get_dict()
        self.d['hasMerchantReturnPolicy'] = self._warranty.get_dict()
        print(json.dumps(self.d))

    #Method to retrieve the JSON-LD of the object