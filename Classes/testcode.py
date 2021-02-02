import sys
sys.path.append(".")
import json
from Car import Car


x = Car()


x.set_sku("www.googl.com")
x.set_model("Hello")
x.set_fuelType("Patrol")
x.set_vehicleConfiguration("LOL")
x.set_bodyType("lol")
x.set_seatingCapacity("33")
x.set_name('LOL')
x.set_driveWheelConfiguration("Fwd")
x.set_vehicleTransmission("lol")
x.set_numberOfAirbags("6")

x.get_sku()
x.get_model()
x.get_fuelType()
x.get_vehicleConfiguration()
x.get_bodyType()
x.get_seatingCapacity()
x.get_name()
x.get_driveWheelConfiguration()
x.get_vehicleTransmission()
x.get_numberOfAirbags()
# x.set_name("Nobody")

x.dump_schema()
