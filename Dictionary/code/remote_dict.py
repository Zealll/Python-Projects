import mysql.connector

connector = mysql.connector.connect(
    user = 'ardit700_student',
    password = 'ardit700_student',
    host = '108.167.140.122',
    database = 'ardit700_pm1database'
)

cursor = connector.cursor()

cursor.execute(f"SELECT * from Dictionary WHERE expression = 'inlay'")

results = cursor.fetchall()

print(results)