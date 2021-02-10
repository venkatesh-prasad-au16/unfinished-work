import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="venky",
    password="1234")

cur = conn.cursor()
cur.execute("SELECT * FROM new_car_master_data_1")
x = cur.fetchall()
print(x)