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
def insert_user_data():
    for i in range(1, 101):
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(6, 12)))
        password = ''.join(
            random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase + "!@#$%^&*()",
                           k=random.randint(8, 16)))
        tel = "1" + ''.join(random.choices(string.digits, k=10))  # 生成以1开头的11位电话号码

        query = (
            "INSERT INTO users (UserID, Username, Password, Tel) "
            "VALUES (%s, %s, %s, %s)"
        )
        values = (i, username, password, tel)
        cursor.execute(query, values)

    conn.commit()


# 执行插入数据
insert_user_data()

# 关闭数据库连接
cursor.close()
conn.close()

print("100条数据已成功插入到users表中。")