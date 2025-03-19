import mysql.connector

# Funktion zum Erstellen der Datenbank und Verbindung zur Datenbank
def create_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS telefonbuchdb")
    connection.close()

# Funktion zum Erstellen der Tabelle für Kontakte
def create_table():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="telefonbuchdb"
    )
    # Cursor erstellen (Vermittler für Datenbankoperationen)
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