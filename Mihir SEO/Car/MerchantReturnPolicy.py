"""
Class MerchantReturnPolicy : Accepts string object while instantiation.
Class MerchantReturnPolicy Methods : set_description, get_description, dump_schema, get_dict
"""
import json
class MerchantReturnPolicy:

    # Pass string price if user wants to set value while object instantiation
    def __init__(self, description: str = ""):
        self._type = 'MerchantReturnPolicy'
        self._context = 'http://www.schema.org'
        self._description = description 

    # Method to manually set the value of description
    def set_description(self, description: str):
        self._description = description
    
    # Method to retrieve the value of description
    def get_description(self):
        return(self._description)

    # Method to print JSON-LD to console
    def dump_schema(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['description'] = self._description
        self.djson = json.dumps(self.d)
        print(self.djson)

    #Method to retrieve the dictionary of Object
    def get_dict(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['description'] = self._description
        return(self.d)
    