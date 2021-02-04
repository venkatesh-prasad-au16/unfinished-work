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
x.set_description("Car is awesome")

x.set_manufacturer_name("Hyundai")
x.set_manufacturer_email("Lol@lol.com")

x.set_engine_type("Crossplane")
x.set_engine_fuel_type("Diesel")
x.set_engine_displacement("2.2L")
x.set_offer_price("22")
x.set_offer_validity("2021-02-04")
x.set_offer_url("www.hyundai.com")
x.set_offer_availability("http://schema.org/InStock")
x.set_offer_currency("INR")
x.set_fuelConsumption("hi")
x.set_identifier("www.google.com")

x.set_warranty("Hello")
x.set_logo_url("Hi")
x.set_logo_repVal("True")
x.set_image_url("www.google.com")
x.set_brand("Hello")
x.set_car_url("www.google.com")


x.set_infotain_value("HD")
x.set_aircon_value("Climate Control")
x.set_sunroof_value("Present")
x.set_dualtone_value("Yes")
x.set_frontbrake_value("Ceramic")
x.set_rearbrake_value("Drum")
x.set_frontsuspension_value("pneumatic")
x.set_rearsuspension_value("Hydraulic")
x.set_wheelsize_value("12")
x.set_tyresize_value("22")


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
x.get_identifier()
x.get_brand()
x.get_car_url()


x.dump_schema()
