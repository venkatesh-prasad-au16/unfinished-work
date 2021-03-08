"""
Class PropertyValue : Accepts two string objects while instantiation.
Class PropertyValue Methods : set_name, get_name, set_value, get_value, dump_schema, get_schema
"""
import json
class PropertyValue:

    # Pass string price if user wants to set value while object instantiation
    def __init__(self, name: str = "", value: str = ""):
        self._type = 'PropertyValue'
        self._context = 'http://www.schema.org'
        self._name = name
        self._value = value 

    # Method to manually set the name
    def set_name(self, name: str):
        self._name = name
    
    # Method to retrieve the name
    def get_name(self):
        return(self._name)

    # Method to manually set the value
    def set_value(self, value: str):
        self._value = value
    
    # Method to retrieve the value
    def get_value(self):
        return(self._value)

    # Method to print JSON-LD to console
    def dump_schema(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['name'] = self._name
        self.d['value'] = self._value
        self.djson = json.dumps(self.d)
        print(self.djson)

    #Method to retrieve the JSON-LD of the object
    def get_dict(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['name'] = self._name
        self.d['value'] = self._value
        return(self.d)
    