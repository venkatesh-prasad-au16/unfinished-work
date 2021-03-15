import psycopg2
import pandas as pd
import sys
# import os

# establishing connection
conn = psycopg2.connect(user="new_car_user", password="xdpuop5js7iirgb2",
                        host="db-automobile-do-user-7279750-0.a.db.ondigitalocean.com",
                        port=25060,
                        database="new_car_db")
print("Connection established successfully!")

# fetching from the db
dtfrm = pd.read_sql("select * from \"new_car_master_data_1\"", conn)
dtfrm.index += 1
dictionary = dtfrm.loc[2]

# mapping df to dict
df_dict = dictionary.to_dict()
print(df_dict)

