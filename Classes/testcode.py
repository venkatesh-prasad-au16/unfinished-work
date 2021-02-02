import sys
import collections
from os import path
sys.path.append(".")
import json
from Offer import Offer


x = Offer("22L")
x.dump_schema()
print(x.get_price())

x.set_price("35L")

print(x.get_schema())
