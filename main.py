from crud import insert_contact, get_contacts, update_contact, delete_contact

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
        elif choice == "2":
            get_contacts()
        elif choice == "3":
            contact_id = int(input("Kontakt-ID: "))
            name = input("Neuer Name: ")
            vorname = input("Neuer Vorname: ")
            telefonnummer = input("Neue Telefonnummer: ")
            handynummer = input("Neue Handynummer: ")
            update_contact(contact_id, name, vorname, telefonnummer, handynummer)
        elif choice == "4":
            contact_id = int(input("Kontakt-ID: "))
            delete_contact(contact_id)
        elif choice == "5":
            break
        else:
            print("Ungültige Eingabe!")

if __name__ == "__main__":
    menu()