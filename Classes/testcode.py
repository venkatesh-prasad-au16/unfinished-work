import sys
import collections
from os import path
sys.path.append(".")
import json
from Organization import Organization


x = Organization({"name" : "www.gogle.com", "email" : "True"})
x.dump_schema()
print(x.get_org_email())
print(x.get_org_name())
x.set_org_name("www.goglee.com")
x.set_org_email("False")
print(x.get_schema())
