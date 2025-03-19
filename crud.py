import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="telefonbuchdb"
    )
# Funktionen zum Abrufen, Hinzufügen, Aktualisieren und Löschen von Kontakten
def get_contacts():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM kontakte") 
        contacts = cursor.fetchall()
        connection.close()
        return contacts
    except mysql.connector.Error as err:
        print(f"Fehler: {err}")
        return []

def insert_contact(name, vorname, telefonnummer, handynummer):
    connection = connect_db()
    cursor = connection.cursor()
    sql = "INSERT INTO kontakte (name, vorname, telefonnummer, handynummer) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, vorname, telefonnummer, handynummer))
    connection.commit()
    connection.close()
    
def update_contact(contact_id, name, vorname, telefonnummer, handynummer):
    connection = connect_db()
    cursor = connection.cursor()
    sql = "UPDATE kontakte SET name=%s, vorname=%s, telefonnummer=%s, handynummer=%s WHERE id=%s"
    cursor.execute(sql, (name, vorname, telefonnummer, handynummer, contact_id))
    connection.commit()
    connection.close()

def delete_contact(contact_id):
    connection = connect_db()
    cursor = connection.cursor()
    sql = "DELETE FROM kontakte WHERE id=%s"
    cursor.execute(sql, (contact_id,))
    connection.commit()
    connection.close()