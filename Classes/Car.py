"""
Class Car : Accepts dictionary object while instantiation.
Class Car Methods : get for each property, set for each property, dump_schema and get_schema
"""
import json
import sys
sys.path.append(".")
from Organization import Organization

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
        self._manufacturer.get_schema()

    def set_interiorType(self, x: )

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
        self.d['fuelType'] = self._fuelType
        self.d['vehicleConfiguration'] = self._vehicleConfiguration
        self.d['bodyType'] = self._bodyType
        self.d['seatingCapacity'] = self._seatingCapacity
        self.d['driveWheelConfiguration'] = self._driveWheelConfiguration
        self.d['vehicleTransmission'] = self._vehicleTransmission
        self.d['numberOfAirbags'] = self._numberOfAirbags
        self.d['manufacturer'] = self._manufacturer.get_dict()
        self.djson = json.dumps(self.d)
        print(self.djson)

    #Method to retrieve the JSON-LD of the object
