import sqlite3

datenbank_datei = "lager.db"

with sqlite3.connect(datenbank_datei) as verbindung:
    cursor = verbindung.cursor()

    # 1. Daten einfügen (Vorbereitung für die Abfrage)
    # Wichtig: Wir fügen zuerst Beispieldaten ein (DML, 
    # später vertieft)
    cursor.execute("INSERT INTO Artikel (Name, Preis, Lagerbestand) 
    VALUES ('Tastatur', 49.90, 25)")
    cursor.execute("INSERT INTO Artikel (Name, Preis, Lagerbestand) 
    VALUES ('Maus', 19.90, 5)")
    verbindung.commit() # Änderungen speichern

    # 2. SELECT-Abfrage ausführen
    sql_abfrage = "SELECT Name, Preis FROM Artikel 
    WHERE Preis < 50.00 ORDER BY Preis DESC"
    cursor.execute(sql_abfrage)

    # 3. Alle Ergebnisse abrufen
    ergebnisse = cursor.fetchall()

    print("--- Gefundene Artikel (Preis < 50.00) ---")
    for artikel in ergebnisse:
        # Die Ergebnisse kommen als Tupel zurück: ('Maus', 19.9)
        print(f"Name: {artikel[0]}, Preis: {artikel[1]} €")

    # Ergebnis:
    # Name: Tastatur, Preis: 49.9 €
    # Name: Maus, Preis: 19.9 €
