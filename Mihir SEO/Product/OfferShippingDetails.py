class OfferShippingDetails:
    def __init__(self, shipping: dict = {}):
        self._type = "OfferShippingDetails"
        self._value = shipping.get('value')
        self._currency = shipping.get('currency')

    