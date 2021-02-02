import sys
import collections
from os import path
sys.path.append(".")
import json
from EngineSpecification import EngineSpecification


x = EngineSpecification({"engineType" : "crossplane", "fuelType" : "True", "engineDisplacement" : "22L"})
x.dump_schema()
print(x.get_engine_type())
print(x.get_engine_fuel_type())
print(x.get_engine_displacement())
x.set_engine_type("Hello")
x.set_engine_fuel_type("Diesel")
x.set_engine_displacement("22L")
print(x.get_schema())
