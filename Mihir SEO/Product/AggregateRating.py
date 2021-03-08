import json
 
class AggregateRating:

    def __init__(self, x: dict = {}):
        self._type = "AggregateRating"
        self._context = "http://www.schema.org"
        self._rating = x.get('ratingValue')
        self._ratingCount = x.get('ratingCount')

    def set_rating(self, x:str):
        self._rating = x

    def set_rating_count(self, x:str):
        self._ratingCount = x

    def get_dict(self):
        self._d = {}
        self._d['@type'] = self._type
        self._d['@context'] = self._context
        self._d['ratingValue'] = self._rating
        self._d['ratingCount'] = self._ratingCount
        return(self._d)
    