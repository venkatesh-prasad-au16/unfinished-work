import psycopg2
import pandas as pd
import sys

# establishing connection
conn = psycopg2.connect(user='new_car_user',
                        host='db-automobile-do-user-7279750-0.a.db.ondigitalocean.com',
                        password='xdpuop5js7iirgb2',
                        port=25060,
                        database='new_car_db')
print('Connection established successfully!')

# fetching from the db
df1 = pd.read_sql('select * from \"new_car_master_data_1\"', conn)
df1.index += 1
d1 = df1.loc[2]

# mapping df to dict
d2 = d1.to_dict()
# print(d2)

d3 = {}
for i in d2.keys():
    if i == 'primary_key':
        d3['sku'] = d2['primary_key']
    elif i == 'model_name':
        d3['model'] = d2['model_name']
    elif i == 'fuel_type':
        d3['fuelType'] = d2['fuel_type']
    elif i == 'body':
        d3['bodyType'] = d2['body']
    elif i == 'variant_name':
        d3['name'] = d2['variant_name']
    elif i == 'transmission_type':
        d3['vehicleTransmission'] = d2['transmission_type']
    elif i == 'manufacturer':
        d3['manufacturer_name'] = d2['manufacturer']
    elif i == 'engine_cc':
        d3['engine_displacement'] = d2['engine_cc']
    elif i == 'model_name':
        d3['model'] = d2['model_name']
    elif i == 'model_name':
        d3['model'] = d2['model_name']
    elif i == 'model_name':
        d3['model'] = d2['model_name']
    elif i == 'model_name':
        d3['model'] = d2['model_name']
    elif i == 'model_name':
        d3['model'] = d2['model_name']

print(d3)