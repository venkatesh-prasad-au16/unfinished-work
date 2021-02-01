import json
class Organization:
    
    def __init__(self, iorg: dict = {}):
        self._type = "Organization"
        self._context = "http://www.schema.org"
        self._org_name = iorg.get('name')
        self._org_email = iorg.get('email')
    
    def set_brand_name(self, value: str):
        self._org_name = value
    def get_brand_name(self):
        return(self._org_name)

    def set_org_email(self, value: str):
        self._org_email= value
    def get_description(self):
        return(self._org_email)

    def dump_schema(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['name'] = self._org_name
        self.d['email'] = self._org_email
        self.djson = json.dumps(self.d)
        print(self.djson)
    
    def get_schema(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['name'] = self._org_name
        self.d['email'] = self._org_email
        self.djson = json.dumps(self.d)
        return(self.djson)
