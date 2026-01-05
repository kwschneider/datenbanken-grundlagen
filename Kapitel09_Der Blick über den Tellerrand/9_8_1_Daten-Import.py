import sqlite3
import csv

# Annahme: 'daten.csv' enthält Zeilen wie: ID, Name, Preis
try:
    with sqlite3.connect("lager.db") as verbindung:
        cursor = verbindung.cursor()
        
        with open('produkte.csv', 'r', encoding='utf-8') as csvfile:
            # Annahme: Der CSV-Header ist in der ersten Zeile
            csv_reader = csv.reader(csvfile)
            next(csv_reader) # Überspringt die Kopfzeile
            
            # Alle Zeilen als Tupel abrufen und in die DB einfügen
            daten_zum_einfuegen = [tuple(row) for row in csv_reader]
            
            # Die Liste in einem Rutsch einfügen (optimiert)
            cursor.executemany(
                "INSERT INTO Produkte (ID, Name, Preis) 
                VALUES (?, ?, ?)", daten_zum_einfuegen)
            verbindung.commit()
            print(
                  f"{len(daten_zum_einfuegen)} "
                  f"Produkte erfolgreich importiert."
            )
            
except Exception as e:
    print(f"Fehler beim Import: {e}")
