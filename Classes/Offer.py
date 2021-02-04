"""
Class Offer : Accepts string object while instantiation.
Class Offer Methods : set_price, get_price, dump_schema, get_schema
"""
import json
class Offer:

    # Pass string price if user wants to set value while object instantiation
    def __init__(self, x: dict = {}):
        self._type = 'Offer'
        self._context = 'http://www.schema.org'
        self._price = x.get('price') 
        self._currency = x.get('currency')
        self._url = x.get('url')
        self._validity = x.get('validity')
        self._condition = x.get('itemCondition')
        self._availability = x.get('availability')

    def set_currency(self, x: str):
        self._currency = x

    def set_url(self, x: str):
        self._url = x

    def set_price_validity(self, x: str):
        self._validity = x
    
    def set_item_condition(self, x: str):
        self._condition = x

    def set_item_availability(self, x: str):
        self._availability = x
    


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
        self.d['availability'] = self._availability
        self.d['priceValidUntil'] = self._validity
        self.d['priceCurrency'] = self._currency
        self.d['url'] = self._url
        self.djson = json.dumps(self.d)
        print(self.djson)

    #Method to retrieve the JSON-LD of the object
    def get_dict(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['priceCurrency'] = self._currency
        self.d['availability'] = self._availability
        self.d['priceValidUntil'] = self._validity
        self.d['priceCurrency'] = self._currency
        self.d['url'] = self._url
        self.d['price'] = self._price
        return(self.d)
    