import sys
import collections
from os import path
sys.path.append(".")
import json
from PropertyValue import PropertyValue


x = PropertyValue("Sunroof","Yes")
x.dump_schema()
print(x.get_name())
print(x.get_value())

x.set_value("35L")
x.set_name("Nobody")

print(x.get_schema())
