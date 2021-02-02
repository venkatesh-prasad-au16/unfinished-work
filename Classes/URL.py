"""
Class URL : Accepts string object while instantiation.
Class URL Methods : set_url, get_url, dump_schema, get_schema
"""
import json
class URL:

    # Pass string price if user wants to set value while object instantiation
    def __init__(self, url: str = ""):
        self._type = 'URL'
        self._context = 'http://www.schema.org'
        self._url = url 

    # Method to manually set the string url
    def set_url(self, url: str):
        self._url = url
    
    # Method to retrieve the value of url
    def get_url(self):
        return(self._url)

    # Method to print JSON-LD to console
    def dump_schema(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['value'] = self._url
        self.djson = json.dumps(self.d)
        print(self.djson)

    #Method to retrieve the JSON-LD of the object
    def get_schema(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['url'] = self._url
        self.djson = json.dumps(self.d)
        return(self.djson)
    