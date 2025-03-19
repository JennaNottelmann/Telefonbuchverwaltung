import tkinter as tk
from tkinter import messagebox
from crud import insert_contact, get_contacts, update_contact, delete_contact

# Funktion zum Hinzufügen eines neuen Kontakts
def add_contact():
    name = name_entry.get()
    vorname = vorname_entry.get()
    telefonnummer = telefon_entry.get()
    handynummer = handy_entry.get()
    
    # Mindestens ein Name (Vorname oder Nachname) und eine Telefonnummer müssen angegeben sein
    if (name or vorname) and (telefonnummer or handynummer):
        insert_contact(name, vorname, telefonnummer, handynummer)
        messagebox.showinfo("Erfolg", "Kontakt erfolgreich hinzugefügt")
        refresh_contacts()
    else:
        messagebox.showerror("Fehler", "Mindestens ein Name und eine Telefonnummer oder Handynummer müssen angegeben sein")

# Funktion zum Vorladen der Kontaktdaten in die Eingabefelder
def load_selected_contact():
    if (selected := contact_listbox.curselection()):
        contact_text = contact_listbox.get(selected)
        contact_data = contact_text.split(': ')[1].split(' - ')
        
        name_vorname = contact_data[0].split()
        telefonnummer, handynummer = contact_data[1].split(' / ')
        
        name_entry.delete(0, tk.END)
        vorname_entry.delete(0, tk.END)
        telefon_entry.delete(0, tk.END)
        handy_entry.delete(0, tk.END)
        
        if len(name_vorname) > 1:
            name_entry.insert(0, name_vorname[0])
            vorname_entry.insert(0, " ".join(name_vorname[1:]))
        else:
            name_entry.insert(0, name_vorname[0])
        
        telefon_entry.insert(0, telefonnummer if telefonnummer != '-' else '')
        handy_entry.insert(0, handynummer if handynummer != '-' else '')
    else:
        messagebox.showerror("Fehler", "Kein Kontakt ausgewählt")

# Funktion zum Bearbeiten eines Kontakts
def edit_selected_contact():
    if (selected := contact_listbox.curselection()):
        contact_text = contact_listbox.get(selected)
        contact_id = contact_text.split(':')[0].strip()  # ID korrekt extrahieren

        if contact_id.isdigit():  # Prüfen, ob die ID eine Zahl ist
            _extracted_from_edit_selected_contact_7(contact_id)
        else:
            messagebox.showerror("Fehler", "Fehler beim Extrahieren der Kontakt-ID")
    else:
        messagebox.showerror("Fehler", "Kein Kontakt ausgewählt")


# TODO Rename this here and in `edit_selected_contact`
def _extracted_from_edit_selected_contact_7(contact_id):
    name = name_entry.get()
    vorname = vorname_entry.get()
    telefonnummer = telefon_entry.get()
    handynummer = handy_entry.get()

    update_contact(int(contact_id), name, vorname, telefonnummer, handynummer)
    messagebox.showinfo("Erfolg", "Kontakt erfolgreich aktualisiert")
    refresh_contacts()

# Funktion zum Löschen eines ausgewählten Kontakts
def delete_selected_contact():
    if (selected := contact_listbox.curselection()):
        contact_text = contact_listbox.get(selected)
        contact_id = contact_text.split(':')[0].strip()  # ID korrekt extrahieren
        
        if contact_id.isdigit():  # Prüfen, ob die ID eine Zahl ist
            delete_contact(int(contact_id))
            messagebox.showinfo("Erfolg", "Kontakt erfolgreich gelöscht")
            refresh_contacts()
        else:
            messagebox.showerror("Fehler", "Fehler beim Extrahieren der Kontakt-ID")
    else:
        messagebox.showerror("Fehler", "Kein Kontakt ausgewählt")

# Funktion zum Aktualisieren und Anzeigen aller gespeicherten Kontakte
def refresh_contacts():
    contact_listbox.delete(0, tk.END)  # Liste leeren
    contacts = get_contacts()
    
    if contacts is None:
        messagebox.showerror("Fehler", "Fehler beim Abrufen der Kontakte. Überprüfe die Datenbankverbindung.")
        return
    
    if not contacts:
        contact_listbox.insert(tk.END, "Keine Kontakte gefunden")
    else:
        for contact in contacts:
            if len(contact) >= 5:
                contact_id, name, vorname, telefonnummer, handynummer = contact[:5]
                contact_display = f"{contact_id}: {name} {vorname} - {telefonnummer if telefonnummer else '-'} / {handynummer if handynummer else '-'}"
                contact_listbox.insert(tk.END, contact_display)

# Hauptfenster der GUI erstellen
root = tk.Tk()
root.title("Telefonbuch Verwaltung")  # Titel des Fensters setzen
root.geometry("500x450")  # Fenstergröße festlegen

# Eingabefelder für die Kontaktinformationen
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Vorname").pack()
vorname_entry = tk.Entry(root)
vorname_entry.pack()

tk.Label(root, text="Telefonnummer").pack()
telefon_entry = tk.Entry(root)
telefon_entry.pack()

tk.Label(root, text="Handynummer").pack()
handy_entry = tk.Entry(root)
handy_entry.pack()

# Button zum Hinzufügen eines Kontakts
tk.Button(root, text="Kontakt hinzufügen", command=add_contact).pack()

# Label und Listbox zur Anzeige der gespeicherten Kontakte
tk.Label(root, text="Gespeicherte Kontakte").pack()
contact_listbox = tk.Listbox(root, width=50, height=10)
contact_listbox.pack()

# Buttons für Bearbeiten, Löschen, Vorladen und Aktualisieren
tk.Button(root, text="Kontakt laden", command=load_selected_contact).pack()
tk.Button(root, text="Kontakt bearbeiten", command=edit_selected_contact).pack()
tk.Button(root, text="Kontakt löschen", command=delete_selected_contact).pack()
tk.Button(root, text="Aktualisieren", command=refresh_contacts).pack()

# Kontakte initial abrufen
refresh_contacts()

# Hauptloop der GUI starten
root.mainloop()