"""
Class Product : Accepts dictionary object while instantiation.
Class Product Methods : set method for all class properties and dump schema method
"""
import sys
sys.path.append(".")
import json
from Brand import Brand
from Offer import Offer
from AggregateRating import AggregateRating

class Product:
    def __init__(self, product: dict = {}):
        self._type = "Product"
        self._context = "http://schema.org/"
        self._sku = product.get('sku')
        self._gtin = product.get('gtin')
        self._image = product.get('image')
        self._name = product.get('name')
        self._description = product.get('description')

        self._brand = Brand()
        self._offer = Offer()
        self._rating = AggregateRating()

    def set_sku(self, x: str):
        self._sku = x
    
    def set_gtin(self, x: str):
        self._gtin = x
    
    def set_image(self, x: list):
        self._image = x

    def set_name(self, x : str):
        self._name = x

    def set_description(self, x: str):
        self._description = x

    def set_brand_name(self, x : str):
        self._brand.set_brand_name(x)
    
    def set_offer_price(self, x: str):
        self._offer.set_price(x)
    
    def set_offer_url(self, x: str):
        self._offer.set_url(x)
    
    def set_offer_availability(self, x: str):
        self._offer.set_item_availability(x)
    
    def set_offer_currency(self, x: str):
        self._offer.set_currency(x)
    
    def set_offer_validity(self, x: str):
        self._offer.set_price_validity(x)

    def set_rating(self, x: str):
        self._rating.set_rating(x)
    
    def set_rating_count(self, x: str):
        self._rating.set_rating_count(x)

    def dump_schema(self):
        self._d = {}
        self._d["@type"] = self._type
        self._d["@context"] = self._context
        self._d["name"] = self._name
        self._d["sku"] = self._sku
        self._d["gtin14"] = self._gtin
        self._d["brand"] = self._brand.get_dict()
        self._d['description'] = self._description
        self._d['image'] = self._image
        self._d['offers'] = self._offer.get_dict()
        self._d['aggregateRating'] = self._rating.get_dict()
        print(json.dumps(self._d))
