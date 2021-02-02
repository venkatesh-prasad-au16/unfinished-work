import sys
import collections
from os import path
sys.path.append(".")
import json
from MerchantReturnPolicy import MerchantReturnPolicy


x = MerchantReturnPolicy("Sunroof")
x.dump_schema()
print(x.get_description())
# print(x.get_value())

x.set_description("35L")
# x.set_name("Nobody")

print(x.get_schema())
