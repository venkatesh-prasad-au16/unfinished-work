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
from Brand import Brand
from URL import URL
from PropertyValue import PropertyValue

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
        self._identifier = cardict.get('identifier')
        self._description = cardict.get('description')

        self._url = URL()
        self._url.set_url(cardict.get('identifier'))

        self._manufacturer = Organization()
        self._manufacturer.set_org_name(cardict.get('manufacturer'))
        self._manufacturer.set_org_email(cardict.get('email'))

        self._brand = Brand()
        self._brand.set_brand_name(cardict.get('manufacturer'))
        self._brand.set_brand_description(cardict.get('email'))

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
        self._logo.set_img_repVal(cardict.get('logoRepVal'))

        self._infotain = PropertyValue()
        self._infotain.set_name('Infotainment System')
        self._infotain.set_value(cardict.get('infotain'))

        self._aircon = PropertyValue()
        self._aircon.set_name('Air Conditioning Type')
        self._aircon.set_value(cardict.get('aircon'))

        self._sunroof = PropertyValue()
        self._sunroof.set_name('Sun Roof Type')
        self._sunroof.set_value(cardict.get('sunroof'))

        self._dualtone = PropertyValue()
        self._dualtone.set_name('Dual Tone')
        self._dualtone.set_value(cardict.get('dualtone'))

        self._frontbrake = PropertyValue()
        self._frontbrake.set_name('Front Brake Type')
        self._frontbrake.set_value(cardict.get('frontbrake'))

        self._rearbrake = PropertyValue()
        self._rearbrake.set_name('Rear Brake Type')
        self._frontbrake.set_value(cardict.get('rearbrake'))

        self._frontsuspension = PropertyValue()
        self._frontsuspension.set_name('Front Suspension Type')
        self._frontsuspension.set_value(cardict.get('frontsuspension'))

        self._rearsuspension = PropertyValue()
        self._rearsuspension.set_name('Rear Brake Type')
        self._rearsuspension.set_value(cardict.get('rearsuspension'))

        self._wheelsize = PropertyValue()
        self._wheelsize.set_name('Wheel Size')
        self._wheelsize.set_value(cardict.get('wheelsize'))

        self._tyresize = PropertyValue()
        self._tyresize.set_name('tyre Size')
        self._tyresize.set_value(cardict.get('tyresize'))

    def set_infotain_value(self, x: str):
        self._infotain.set_value(x)

    def set_aircon_value(self, x: str):
        self._aircon.set_value(x)

    def set_sunroof_value(self, x: str):
        self._sunroof.set_value(x)
    
    def set_dualtone_value(self, x: str):
        self._dualtone.set_value(x)
    
    def set_frontbrake_value(self, x: str):
        self._frontbrake.set_value(x)

    def set_rearbrake_value(self, x: str):
        self._rearbrake.set_value(x)

    def set_frontsuspension_value(self, x: str):
        self._frontsuspension.set_value(x)

    def set_rearsuspension_value(self, x: str):
        self._rearsuspension.set_value(x)

    def set_wheelsize_value(self, x: str):
        self._wheelsize.set_value(x)
    
    def set_tyresize_value(self, x: str):
        self._tyresize.set_value(x)

    def set_car_url(self, x: str):
        self._url.set_url(x)
    
    def get_car_url(self):
        return(self._url)

    def set_brand(self, x : str):
        self._brand.set_brand_name(x)
    
    def get_brand(self):
        return(self._brand)

    def set_description(self,x: str):
        self._description = x

    def get_description(self):
        return(self._description)

    def set_identifier(self, x: str):
        self._identifier = x

    def get_identifier(self):
        return(self._identifier)

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

    def set_sku(self, x: str):
        self._sku = x
    
    def get_sku(self):
        return(self._sku)

    def set_mpn(self, x: str):
        self._mpn = x
    
    def get_mpn(self):
        return(self._mpn)

    def set_model(self, x: str):
        self._model = x 
    
    def get_model(self):
        return(self._model)

    def set_name(self, x: str):
        self._name = x 
    
    def get_name(self):
        return(self._name)
    
    def set_fuelType(self, x: str):
        self._fuelType = x 
    
    def get_fuelType(self):
        return(self._fuelType)

    def set_vehicleConfiguration(self, x: str):
        self._vehicleConfiguration = x 
    
    def get_vehicleConfiguration(self):
        return(self._vehicleConfiguration)

    def set_bodyType(self, x: str):
        self._bodyType = x 
    
    def get_bodyType(self):
        return(self._bodyType)

    def set_seatingCapacity(self, x: str):
        self._seatingCapacity = x 
    
    def get_seatingCapacity(self):
        return(self._seatingCapacity)

    def set_driveWheelConfiguration(self, x: str):
        self._driveWheelConfiguration = x

    def get_driveWheelConfiguration(self):
        return(self._driveWheelConfiguration)

    def set_vehicleTransmission(self, x: str):
        self._vehicleTransmission = x 
    
    def get_vehicleTransmission(self):
        return(self._vehicleTransmission)

    def set_numberOfAirbags(self, x: str):
        self._numberOfAirbags = x

    def get_numberOfAirbags(self):
        return(self._numberOfAirbags)

    def set_color(self, x: str):
        self._color = x

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
        self._d = {}
        self._d['@type'] = self._type
        self._d['@context'] = self._context
        self._d['sku'] = self._sku
        self._d['mpn'] = self._mpn
        self._d['model'] = self._model
        self._d['name'] = self._name
        self._d['color'] = self._color
        self._d['image'] = self._image
        self._d['fuelType'] = self._fuelType
        self._d['vehicleConfiguration'] = self._vehicleConfiguration
        self._d['bodyType'] = self._bodyType
        self._d['seatingCapacity'] = self._seatingCapacity
        self._d['driveWheelConfiguration'] = self._driveWheelConfiguration
        self._d['vehicleTransmission'] = self._vehicleTransmission
        self._d['numberOfAirbags'] = self._numberOfAirbags
        self._d['vehicleInteriorType'] = self._vehicleInteriorType
        self._d['identifier'] = self._identifier
        self._additional = [self._infotain.get_dict(),
                           self._aircon.get_dict(),
                           self._sunroof.get_dict(),
                           self._dualtone.get_dict(),
                           self._frontbrake.get_dict(),
                           self._rearbrake.get_dict(),
                           self._frontsuspension.get_dict(),
                           self._rearsuspension.get_dict(),
                           self._wheelsize.get_dict(),
                           self._tyresize.get_dict()]

        self._d['manufacturer'] = self._manufacturer.get_dict()
        self._d['vehicleEngine'] = self._vehicleEngine.get_dict()
        self._d['offers'] = self._offer.get_dict()
        self._d['fuelConsumption'] = self._fuelConsumption.get_dict()
        self._d['hasMerchantReturnPolicy'] = self._warranty.get_dict()
        self._d['brand'] = self._brand.get_dict()
        self._d['url'] = self._url.get_dict()
        self._d['additionalProperty'] = self._additional
        
        print(json.dumps(self._d))

    #Method to retrieve the dict of the object
    def dump_schema(self):
        self._d = {}
        self._d['@type'] = self._type
        self._d['@context'] = self._context
        self._d['sku'] = self._sku
        self._d['mpn'] = self._mpn
        self._d['model'] = self._model
        self._d['name'] = self._name
        self._d['color'] = self._color
        self._d['image'] = self._image
        self._d['fuelType'] = self._fuelType
        self._d['vehicleConfiguration'] = self._vehicleConfiguration
        self._d['bodyType'] = self._bodyType
        self._d['seatingCapacity'] = self._seatingCapacity
        self._d['driveWheelConfiguration'] = self._driveWheelConfiguration
        self._d['vehicleTransmission'] = self._vehicleTransmission
        self._d['numberOfAirbags'] = self._numberOfAirbags
        self._d['vehicleInteriorType'] = self._vehicleInteriorType
        self._d['identifier'] = self._identifier
        self._additional = [self._infotain.get_dict(),
                           self._aircon.get_dict(),
                           self._sunroof.get_dict(),
                           self._dualtone.get_dict(),
                           self._frontbrake.get_dict(),
                           self._rearbrake.get_dict(),
                           self._frontsuspension.get_dict(),
                           self._rearsuspension.get_dict(),
                           self._wheelsize.get_dict(),
                           self._tyresize.get_dict()]

        self._d['manufacturer'] = self._manufacturer.get_dict()
        self._d['vehicleEngine'] = self._vehicleEngine.get_dict()
        self._d['offers'] = self._offer.get_dict()
        self._d['fuelConsumption'] = self._fuelConsumption.get_dict()
        self._d['hasMerchantReturnPolicy'] = self._warranty.get_dict()
        self._d['brand'] = self._brand.get_dict()
        self._d['url'] = self._url.get_dict()
        self._d['additionalProperty'] = self._additional
        
        return(self._d)