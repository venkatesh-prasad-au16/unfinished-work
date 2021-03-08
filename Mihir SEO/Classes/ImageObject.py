"""
Class ImageObject : Accepts dictionary object while instantiation.
Class ImageObject Methods : set_img_url, get_img_url, set_img_repVal,
                get_img_repVal, dump_schema, get_dict
"""
import json
class ImageObject:

    # Pass dictionary with keys 'url' and 'representativeOfPage' 
    # if user wants to set values while object instantiation 
    def __init__(self, img: dict = {}):
        self._type = "ImageObject"
        self._context = "http://www.schema.org"
        self._imgURL = img.get('url')
        self._imgRepVal = img.get('representativeOfPage')

    # Method to manually set the value of img_url by passing a string
    def set_img_url(self, value: str):
        self._imgURL= value
    
    # Method to retrieve the value of img_url
    def get_img_url(self):
        return(self._imgURL)

    # Method to manually set the value of img_repVal(representativeOfPage) by passing
    # a "True" or "False" string
    def set_img_repVal(self, value: str):
        self._imgRepVal = value
    
    # Method to retrieve the value of img_repVal(representativeOfPage) 
    def get_img_repVal(self):
        return(self._imgRepVal)

    # Method to print the image object JSON-LD to console
    def dump_schema(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['url'] = self._imgURL
        self.d['representativeOfPage'] = self._imgRepVal
        print(json.dumps(self.d))

    # Method to retrieve the image object JSON-LD elsewhere   
    def get_dict(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['url'] = self._imgURL
        self.d['representativeOfPage'] = self._imgRepVal
        return(self.d)





