import mysql.connector

def create_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS telefonbuch_db")
    connection.close()

def create_table():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="DAA123",
        database="telefonbuch_db"
    )
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS kontakte (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            vorname VARCHAR(100),
            telefonnummer VARCHAR(50),
            handynummer VARCHAR(50)
        )
    ''')
    connection.close()

if __name__ == "__main__":
    create_database()
    create_table()