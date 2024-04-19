# 在上面的代码中，我们已经将CSV文件中的数据导入到了MySQL数据库。下面的代码将从数据库中检索数据并打印出来。

import mysql.connector

# MySQL数据库连接信息

host = 'localhost'
user = 'root'
password = '123456'
database = 'novel_info'

# 连接到MySQL数据库

try:
    conn = mysql.connector.connect(host=host,user=user,password=password,database=database)
    cursor = conn.cursor()

    # 查询author_info表中的所有记录
    cursor.execute("SELECT * FROM author_info")

    # 获取所有行数据
    rows = cursor.fetchall()

    # 打印所有行数据
    for row in rows:
        print(row)

except mysql.connector.Error as e:
    print('MySQL连接错误:', e)

finally:
    # 关闭数据库连接
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()