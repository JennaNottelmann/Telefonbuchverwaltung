import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    print("Erfolgreich mit MySQL verbunden!")
    connection.close()
except mysql.connector.Error as err:
    print(f"Fehler: {err}")
