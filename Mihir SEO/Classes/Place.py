import json

class Place:
    def __init__(self, d: dict = {}):
        self._type = "Place"
        self._context = "https://schema.org"
        self._name = d.get("name")
        self._address = d.get("address")
    
    def set_name(self, x: str):
        self._name = x

    def set_address(self, x: str):
        self._address = x

    def get_dict(self):
        self.d = {}
        self.d['type'] = self._type
        self.d['name'] = self._name
        self.d['address'] = self._address
        return (self.d)

