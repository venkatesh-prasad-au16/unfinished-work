
class ImageObject:
    
    def __init__(self, img: dict = {}):
        self._type = "ImageObject"
        self._context = "http://www.schema.org"
        self._img_url = img.get('url')
        self._img_repVal = img.get('representativeOfPage')

    def set_img_url(self, value: str):
        self._img_url= value
    def get_img_url(self):
        return(self._img_url)

    def set_img_repVal(self, value: str):
        self._img_repVal = value
    def get_img_repVal(self):
        return(self._img_repVal)

    def dump_schema(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['url'] = self._img_url
        self.d['representativeOfPage'] = self._img_repVal
        print(json.dumps(self.d))
        
    def get_schema(self):
        self.d = {}
        self.d['@type'] = self._type
        self.d['@context'] = self._context
        self.d['url'] = self._img_url
        self.d['representativeOfPage'] = self._img_repVal
        return(json.dumps(self.d))
