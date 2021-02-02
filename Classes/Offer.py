"""
Class Offer : Accepts string object while instantiation.
Class Brand Methods : set_price, get_price, dump_schema, get_schema
"""
import json
class Offer:

    # Pass string price 
    # if user wants to set values while object instantiation
    def __init__(self, price: str = ""):
        self._type = 'Offer'
        self._context = 'http://www.schema.org'
        self._price = price 

    def set_price(self, price: str):
        self._price = price
    
    def get_price(self):
        return(self._price)

    def dump_schema(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['price'] = self._price
        self.djson = json.dumps(self.d)
        print(self.djson)

    def get_schema(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['price'] = self._price
        self.djson = json.dumps(self.d)
        return(self.djson)
    