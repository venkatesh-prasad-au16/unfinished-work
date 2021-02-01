import json

class Brand:
    
    def __init__(self, idict: dict = {}):
        self._type = 'Brand'
        self._context = 'http://www.schema.org'
        self._brand_name = idict.get('name')
        self._description = idict.get('description')

    def set_brand_name(self, value: str):
        self._brand_name = value
    def get_brand_name(self):
        return(self._brand_name)

    def set_description(self, value: str):
        self._description = value
    def get_description(self):
        return(self._description)

    def dump_schema(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['name'] = self._brand_name
        self.d['description'] = self._description
        self.djson = json.dumps(self.d)
        print(self.djson)
