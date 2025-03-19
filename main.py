from crud import insert_contact, get_contacts, update_contact, delete_contact

# Funktion zum Anzeigen des Menüs und Verwalten der Kontakte
def menu():
    while True:
        print("\nTelefonbuch Verwaltung")
        print("1. Neuen Kontakt hinzufügen")
        print("2. Alle Kontakte anzeigen")
        print("3. Kontakt bearbeiten")
        print("4. Kontakt löschen")
        print("5. Beenden")
        
        choice = input("Option wählen: ")
        
        if choice == "1":
            name = input("Name: ")
            vorname = input("Vorname: ")
            telefonnummer = input("Telefonnummer: ")
            handynummer = input("Handynummer: ")
            insert_contact(name, vorname, telefonnummer, handynummer)
            print("Kontakt erfolgreich hinzugefügt!")
        elif choice == "2":
            if contacts := get_contacts():
                print("\nGespeicherte Kontakte:")
                for contact in contacts:
                    print(f"ID: {contact[0]}, Name: {contact[1]}, Vorname: {contact[2]}, Telefonnummer: {contact[3]}, Handynummer: {contact[4]}")
            else:
                print("Keine Kontakte gefunden.")
            input("Drücke Enter, um zum Menü zurückzukehren...")
        elif choice == "3":
            contact_id = int(input("Kontakt-ID: "))
            name = input("Neuer Name: ")
            vorname = input("Neuer Vorname: ")
            telefonnummer = input("Neue Telefonnummer: ")
            handynummer = input("Neue Handynummer: ")
            update_contact(contact_id, name, vorname, telefonnummer, handynummer)
            print("Kontakt erfolgreich aktualisiert!")
        elif choice == "4":
            contact_id = int(input("Kontakt-ID: "))
            delete_contact(contact_id)
            print("Kontakt erfolgreich gelöscht!")
        elif choice == "5":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Eingabe! Bitte erneut versuchen.")

if __name__ == "__main__":
    menu()
