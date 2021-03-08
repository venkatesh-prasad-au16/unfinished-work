import json
from Place import Place

class Event:
    def __init__(self, d: dict = {}):
        self._type = "Event"
        self._context = "https://schema.org"
        self._offer = d.get("offers")
        self._startdate = d.get("startDate")
        self._url = d.get("url")
        self._name = d.get("name")
        self._price = d.get("price")
        self._address = d.get("address")

        self._location = Place()
        self._location.set_name(d.get("LocationName"))
        self._location.set_address(d.get("LocationAddress"))

    def set_location_name(self, x: str):
        self._location.set_name(x)

    def set_location_address(self,x: str):
        self._location.set_address(x) 
    
    def set_offer(self, x: str):
        self._offer = x

    def set_start_date(self, x: str):
        self._startdate = x
    
    def set_url(self, x:str):
        self._url = x

    def set_name(self, x: str):
        self._name = x

    def set_price(self, x: str):
        self._price = x
    
    def set_address(self, x: str):
        self._address = x

    def dump_schema(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['location'] = self._location.get_dict()
        self.d['offers'] = self._offer
        self.d['name'] = self._name
        self.d['startDate'] = self._startdate
        self.d['url'] = self._url
        self.d['price'] = self._price
        self.djson = json.dumps(self.d)
        print(self.djson)