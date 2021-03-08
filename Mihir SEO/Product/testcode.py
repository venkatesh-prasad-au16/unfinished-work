import sys
sys.path.append(".")
import json
from Product import Product

p = Product()

p.set_name("Magnifique")
p.set_brand_name("Magnifique")
p.set_description("Its great")
p.set_gtin("1234")
p.set_sku("1234")
p.set_image(["http://www.google.com"])
p.set_offer_price("30")
p.set_offer_currency("SGD")
p.set_offer_availability("http://schema.org/InStock")
p.set_offer_validity("2020-11-30")
p.set_offer_url("www.google.com")
p.set_rating("5")
p.set_rating_count("5")
p.dump_schema()