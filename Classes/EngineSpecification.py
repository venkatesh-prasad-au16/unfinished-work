"""
Class EngineSpecification : Accepts dictionary object while instantiation.
Class EngineSpecification Methods : set_engine_type, get_engine_type, set_engine_fuel_type,
                get_engine_fuel_type, set_engine_displacement, get_engine_displacement,
                dump_schema, get_schema
"""
import json
class EngineSpecification:

    # Pass dictionary with keys 'engineType', 'fuelType' and 'engineDisplacement' 
    # if user wants to set values while object instantiation
    def __init__(self, enginedict: dict = {}):
        self._type = 'EngineSpecification'
        self._context = 'http://www.schema.org'
        self._engineType = enginedict.get('engineType')
        self._engineFuelType = enginedict.get('fuelType')
        self._engineDisplacement = enginedict.get('engineDisplacement')

    # Method to manually set the value of engineType by passing a string object
    def set_engine_type(self, value: str):
        self._engineType = value
    
    # Method to retrieve the engineType property
    def get_engine_type(self):
        return(self._engineType)

    # Method to manually set the engineFuelType property by pasing a string object
    def set_engine_fuel_type(self, value: str):
        self._engineFuelType = value

    # Method to retrieve the engineFuelType property
    def get_engine_fuel_type(self):
        return(self._engineFuelType)

    # Method to set the engineDisplacement property by passing a string object
    def set_engine_displacement(self, value: str):
        self._engineDisplacement = value

    # Method to retrieve the engineDisplacement property
    def get_engine_displacement(self):
        return(self._engineDisplacement)

    # Method to print the EngineSpecification object JSON-LD to console
    def dump_schema(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['engineType'] = self._engineType
        self.d['fuelType'] = self._engineFuelType
        self.d['engineDisplacement'] = self._engineDisplacement
        self.djson = json.dumps(self.d)
        print(self.djson)
    
    # Method to retrieve the EngineSpecification object JSON-LD elsewhere
    def get_schema(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['engineType'] = self._engineType
        self.d['fuelType'] = self._engineFuelType
        self.d['engineDisplacement'] = self._engineDisplacement
        self.djson = json.dumps(self.d)
        return(self.djson)

    def get_dict(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['engineType'] = self._engineType
        self.d['fuelType'] = self._engineFuelType
        self.d['engineDisplacement'] = self._engineDisplacement
        return(self.d)