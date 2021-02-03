"""
Class Offer : Accepts string object while instantiation.
Class Offer Methods : set_price, get_price, dump_schema, get_schema
"""
import json
class Offer:

    # Pass string price if user wants to set value while object instantiation
    def __init__(self, price: str = ""):
        self._type = 'Offer'
        self._context = 'http://www.schema.org'
        self._price = price 
        self._currency = 'INR'

    # Method to manually set the value of price
    def set_price(self, price: str):
        self._price = price
    
    # Method to retrieve the value of price
    def get_price(self):
        return(self._price)

    # Method to print JSON-LD to console
    def dump_schema(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['priceCurrency'] = self._currency
        self.d['price'] = self._price
        self.djson = json.dumps(self.d)
        print(self.djson)

    #Method to retrieve the JSON-LD of the object
    def get_dict(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['priceCurrency'] = self._currency
        self.d['price'] = self._price
        return(self.d)
    