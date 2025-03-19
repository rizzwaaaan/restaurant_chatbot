import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='yourdatabase'
    )
    print("Connected successfully!")
except pymysql.MySQLError as e:
    print(f"Error: {e}")
finally:
    if 'connection' in locals():
        connection.close()
