import sqlite3
import csv

try:
    with sqlite3.connect("lager.db") as verbindung:
        cursor = verbindung.cursor()
        
        # Daten abfragen
        cursor.execute("SELECT ID, Name, Preis FROM Produkte ORDER BY ID")
        daten = cursor.fetchall()
        
        # Header-Informationen abrufen (Spaltennamen)
        spaltennamen = [description[0] for description in cursor.description]
        
        with open(
            'export_produkte.csv',
            'w',
            newline='',
            encoding='utf-8'
            ) as csvfile:
            csv_writer = csv.writer(csvfile)
            
            # 1. Kopfzeile schreiben
            csv_writer.writerow(spaltennamen)
            
            # 2. Datenzeilen schreiben
            csv_writer.writerows(daten)
            
            print(f"Datenbank erfolgreich in export_produkte.csv exportiert.")
            
except Exception as e:
    print(f"Fehler beim Export: {e}")
