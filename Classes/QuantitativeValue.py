"""
Class QuantitativeValue : Accepts string object while instantiation.
Class QuantitativeValue Methods : set_value, get_value, dump_schema, get_schema
"""
import json
class QuantitativeValue:

    # Pass string price if user wants to set value while object instantiation
    def __init__(self, value: str = ""):
        self._type = 'QuantitativeValue'
        self._context = 'http://www.schema.org'
        self._value = value 

    # Method to manually set the value
    def set_value(self, value: str):
        self._price = value
    
    # Method to retrieve the value
    def get_value(self):
        return(self._value)

    # Method to print JSON-LD to console
    def dump_schema(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['value'] = self._value
        self.djson = json.dumps(self.d)
        print(self.djson)

    #Method to retrieve the JSON-LD of the object
    def get_schema(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['value'] = self._value
        self.djson = json.dumps(self.d)
        return(self.djson)
    