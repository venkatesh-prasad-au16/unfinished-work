"""
Class Organization : Accepts dictionary object while instantiation.
Class Organization Methods : set_org_name, get_org_name, set_org_email,
                get_org_email, dump_schema, get_schema
"""
import json
class Organization:
    
    # Pass dictionary with keys 'name' and 'email' 
    # if user wants to set values while object instantiation
    def __init__(self, iorg: dict = {}):
        self._type = "Organization"
        self._context = "http://www.schema.org"
        self._org_name = iorg.get('name')
        self._org_email = iorg.get('email')
    
    # Method to manually set the value of org_name by passing a string
    def set_org_name(self, value: str):
        self._org_name = value
    
    # Method to retrieve the value of org_name
    def get_org_name(self):
        return(self._org_name)

    # Method to manually set the value of org_email by passing a string
    def set_org_email(self, value: str):
        self._org_email= value
    # Method to retrieve the value of org_email
    def get_org_email(self):
        return(self._org_email)

    # Method to print the object JSON-LD to console
    def dump_schema(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['name'] = self._org_name
        self.d['email'] = self._org_email
        self.djson = json.dumps(self.d)
        print(self.djson)
    
    # Method to retrieve the object dictionary elsewhere 
    def get_dict(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['name'] = self._org_name
        self.d['email'] = self._org_email
        return(self.d)