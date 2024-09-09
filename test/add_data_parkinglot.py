import mysql.connector
import random
import string

# 数据库连接配置
config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123456',
    'database': 'chao_db'
}

# 连接到数据库
conn = mysql.connector.connect(**config)
cursor = conn.cursor()


# 插入数据的函数
def insert_data():
    for i in range(1, 501):
        parking_name = ''.join(random.choices(string.ascii_uppercase, k=5)) + 'Lot'
        longitude = random.uniform(-180, 180)
        latitude = random.uniform(-90, 90)
        capacity = random.randint(50, 500)
        rates = round(random.uniform(1.0, 10.0), 2)

        query = (
            "INSERT INTO parkinglot (ParkingLotID, ParkingName, Longitude, Latitude, Capacity, Rates) "
            "VALUES (%s, %s, %s, %s, %s, %s)"
        )
        values = (i, parking_name, longitude, latitude, capacity, rates)
        cursor.execute(query, values)

    conn.commit()


# 执行插入数据
insert_data()

# 关闭数据库连接
cursor.close()
conn.close()

print("500条数据已成功插入到parkinglot表中。")