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
x.set_color("Blue")
x.set_vehicleIinteriorType("Leather")

x.set_manufacturer_name("Hyundai")
x.set_manufacturer_email("Lol@lol.com")

x.set_engine_type("Crossplane")
x.set_engine_fuel_type("Diesel")
x.set_engine_displacement("2.2L")
x.set_offer_price("22")
x.set_fuelConsumption("hi")

x.set_warranty("Hello")
x.set_logo_url("Hi")
x.set_logo_repVal("True")
x.set_image_url("www.google.com")

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
x.get_color()
x.get_vehicleInteriorType()
x.get_manufacturer_details()
x.get_offer_price()
x.get_fuelConsumption()
x.get_warranty()
x.get_logo_details()


x.dump_schema()
