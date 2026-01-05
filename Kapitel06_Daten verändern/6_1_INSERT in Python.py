import sqlite3

datenbank_datei = "lager.db"

def neuen_artikel_einfuegen(name, preis, bestand):
    with sqlite3.connect(datenbank_datei) as verbindung:
        cursor = verbindung.cursor()
        
        # 1. SQL-Befehl mit Platzhaltern (?)
        sql_befehl = "INSERT INTO Artikel (Name, Preis, 
        Lagerbestand) 
        VALUES (?, ?, ?)"
        
        # 2. Werte als Tupel übergeben (Vermeidung von 
        # SQL-Injections)
        artikel_daten = (name, preis, bestand)
        
        cursor.execute(sql_befehl, artikel_daten)
        
        # 3. Änderungen speichern
        # verbindung.commit() ist hier durch das 'with' 
        # Statement abgedeckt, aber zur Verdeutlichung:
        verbindung.commit()

# Beispiel: Zwei neue Artikel hinzufügen
neuen_artikel_einfuegen("USB-C Kabel", 12.50, 40)
neuen_artikel_einfuegen("Mauspad XL", 8.99, 15)

print("Zwei neue Artikel eingefügt.")
