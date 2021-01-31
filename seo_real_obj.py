from schemaorg.main import Schema

def add_prop(obj, key, val):
    obj.add_property(key,val)
    return obj

img = Schema('ImageObject')
img = add_prop(img,"representativeOfPage","True")
img = add_prop(img,"url","www.google.com")


morg = Schema('Organization')
morg = add_prop(morg,"name","Hyundai")
morg = add_prop(morg,"email","hyundai@gmail.com")

mbrand = Schema('Brand')
mbrand = add_prop(mbrand,"name","Hyundai")
mbrand = add_prop(mbrand,"description","Hyundai India")

mengine = Schema('EngineSpecification')
mengine = add_prop(mengine, "value", "1.2L")
mengine = add_prop(mengine, "description", "1200 cc")

maggregaterating = Schema('AggregateRating')
maggregaterating = add_prop(maggregaterating,"ratingValue","4.0")
maggregaterating = add_prop(maggregaterating,"reviewCount","89")

mQuantVal = Schema('QuantitativeValue')
mQuantVal = add_prop(mQuantVal, "value", "5")

mInfotain = Schema('PropertyValue')
mInfotain = add_prop(mInfotain, "name", "Infotainment")
mInfotain = add_prop(mInfotain, "value", "HD")

mAC = Schema('PropertyValue')
mAC = add_prop(mAC, "name", "AC Type")
mAC = add_prop(mAC, "value", "Climate Control")

mSunRoof = Schema('PropertyValue')
mSunRoof = add_prop(mSunRoof, "name", "Sunroof")
mSunRoof = add_prop(mSunRoof, "value", "Present")

mDualTone = Schema('PropertyValue')
mDualTone = add_prop(mDualTone, "name", "Dual Tone")
mDualTone = add_prop(mDualTone, "value", "Present")

mFrontBrake = Schema('PropertyValue')
mFrontBrake = add_prop(mFrontBrake, "name", "Front Brake")
mFrontBrake = add_prop(mFrontBrake, "value", "Disc")

mRearBrake = Schema('PropertyValue')
mRearBrake = add_prop(mRearBrake, "name", "Rear Brake")
mRearBrake = add_prop(mRearBrake, "value", "Drum")

mFrontSus = Schema('PropertyValue')
mFrontSus = add_prop(mFrontSus, "name", "Front Suspension") 
mFrontSus = add_prop(mFrontSus, "value", "Hydraulic")

mRearSus = Schema('PropertyValue')
mRearSus = add_prop(mRearSus, "name", "Rear Suspension")
mRearSus = add_prop(mRearSus, "value", "Pneumatic")

mWheelSize = Schema('PropertyValue')
mWheelSize = add_prop(mWheelSize, "name", "Wheel Size")
mWheelSize = add_prop(mWheelSize, "value", "20")

mTyreSize = Schema('PropertyValue')
mTyreSize = add_prop(mTyreSize, "name", "Tyre Size")
mTyreSize  = add_prop(mTyreSize, "value", "20")

mWarranty = Schema('Organization')
mWarranty = add_prop(mWarranty, "inStoreReturnsOffered", "true")

mOffer = Schema('Offer')
mOffer = add_prop(mOffer, "seller", "Hyundai")
mOffer = add_prop(mOffer, "price", "9-15 L")


imag_dict = {"representativeOfPage": "True", "url": "www.google.com", "@context": "http://www.schema.org", "@type": "ImageObject"}

org_dict = {"name": "Hyundai", "email": "hyundai@gmail.com", "@type": "Organization"}

brand_dict = {"name": "Hyundai",
              "description": "Hyundai India", 
              "@type": "Brand"}

rating_dict = {"ratingValue": "4.0", "reviewCount": "89", "@type": "AggregateRating"}

engine_dict = {"description": "1200 cc", "@context": "http://www.schema.org", "@type": "EngineSpecification"}

fuelType_dict = {"value": "5", "@context": "http://www.schema.org", "@type": "QuantitativeValue"}



vehicleDict = {}
vehicleDict["image"] = imag_dict
vehicleDict["identifier"] = "www.google.com"
vehicleDict["url"] = "www.google.com"
vehicleDict["logo"] = imag_dict
vehicleDict["sku"] = "0000"
vehicleDict["category"] = "Car"
vehicleDict["manufacturer"] = org_dict
vehicleDict["brand"] = brand_dict
vehicleDict["model"] = "Verna"
vehicleDict["name"] = "Verna"
vehicleDict["color"] = "Red"
vehicleDict["aggregateRating"] = rating_dict
vehicleDict["fuelType"] = "Petrol"
vehicleDict["vehicleConfiguration"] = "Variant"
vehicleDict["offers"] = "Ex-Showroom price : 9L - 15 L"
vehicleDict["bodyType"] = "Sedan"
vehicleDict["seatingCapacity"] = "5"
vehicleDict["driveWheelCOnfiguration"] = "FWD"
vehicleDict["vehicleEngine"] = engine_dict
# vehicleDict["fuelConsumption"] = fuel_dict
vehicleDict["vehicleTransmission"] = "Manual"
vehicleDict["numberOfAirbags"] = "4"
vehicleDict["vehicleInteriorType"] = "Leather"
vehicleDict["hasMerchantReturnPolicy"] = mWarranty.dump_json()
vehicleDict["additionalProperty1"] = mInfotain.dump_json()
vehicleDict["additionalProperty2"] = mAC.dump_json()
vehicleDict["additionalProperty3"] = mSunRoof.dump_json()
vehicleDict["additionalProperty4"] = mDualTone.dump_json()
vehicleDict["additionalProperty5"] = mFrontBrake.dump_json()
vehicleDict["additionalProperty6"] = mRearBrake.dump_json()
vehicleDict["additionalProperty7"] = mFrontSus.dump_json()
vehicleDict["additionalProperty8"] = mRearSus.dump_json()
vehicleDict["additionalProperty9"] = mWheelSize.dump_json()
vehicleDict["additionalProperty10"] = mTyreSize.dump_json()

# Create Car Schema Object
mcar = Schema('Car')

# Assign Car image 
mcar = add_prop(mcar, "image", vehicleDict["image"])

# Assign unique identifier
mcar = add_prop(mcar, "identifier", vehicleDict["identifier"])


# Assign url for product
mcar = add_prop(mcar, "url", "www.google.com")

# Assign logo for product
mcar = add_prop(mcar, "logo", img)

# Assign stock keeping unit
mcar = add_prop(mcar, "sku", "0000")

# Assign category 
mcar = add_prop(mcar, "category", "Car")

# Assign manufacturer
mcar = add_prop(mcar, "manufacturer", morg)

# Assign brand
mcar = add_prop(mcar, "brand", mbrand)

# Assign model
mcar = add_prop(mcar, "model","Verna")

# Assign name
mcar = add_prop(mcar, "name","Verna")

# Assign Color
mcar = add_prop(mcar, "color", "Red")

# Assign Rating
mcar = add_prop(mcar, "aggregateRating", maggregaterating)

# Assign Fuel Type
mcar = add_prop(mcar, "fuelType","Petrol")

# Assign Variant
mcar = add_prop(mcar, "vehicleConfiguration","Variant")

# Assign Price
mcar = add_prop(mcar, "vehicleTransmission", "Manual")

# Assign Fuel Efficiency
mcar = add_prop(mcar, "fuelConsumption", mQuantVal)


# Assign Number of Airbags
mcar = add_prop(mcar, "numberOfAirbaga", "4")

# Assign Vehicle Interior Type
mcar = add_prop(mcar, "vehicleInteriorType", "Leather")

# Assign Warranty Offer
mcar = add_prop(mcar, "hasMerchantReturnPolicy", mWarranty)

# Writing json of Additional Properties to String
l = [mInfotain, mAC, mSunRoof, mDualTone, mFrontBrake, mRearBrake, mFrontSus, mRearSus, mWheelSize,mTyreSize]
s = ""
for each in l:
    s += each.dump_json()+","

# Assign all Additional Properties together to Car Schema Object    
mcar = add_prop(mcar, "additionalProperty", s)


#mcar = add_prop(mcar, "additionalProperty", mInfotain)
# mcar = add_prop(mcar, "additionalProperty", mAC)
# mcar = add_prop(mcar, "additionalProperty", mSunRoof)
# mcar = add_prop(mcar, "additionalProperty", mDualTone)
# mcar = add_prop(mcar, "additionalProperty", mFrontBrake)
# mcar = add_prop(mcar, "additionalProperty", mRearBrake)
# mcar = add_prop(mcar, "additionalProperty", mFrontSus)
# mcar = add_prop(mcar, "additionalProperty", mRearSus)
# mcar = add_prop(mcar, "additionalProperty", mWheelSize)
# mcar = add_prop(mcar, "additionalProperty", mTyreSize)

print(vehicleDict)

print("======")

print(mcar.dump_json())
