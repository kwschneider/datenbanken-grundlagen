import sqlite3

datenbank_datei = "lager.db"

with sqlite3.connect(datenbank_datei) as verbindung:
    cursor = verbindung.cursor()
    # Achtung: Aktiviert die Fremdschlüsselprüfung!
    # Dieser Befehl muss in JEDER neuen Verbindung 
    # ausgeführt werden.
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    # Jetzt kannst du DDL (CREATE TABLE) oder DML (INSERT) 
    # sicher ausführen
    # Füge eine Bestellung mit einer KundenID ein, die in 
    # der Kunden-Tabelle existiert.
    
    try:
        # Versucht eine Bestellung für KundenID 999 einzufügen, 
        # der nicht existiert
        cursor.execute("INSERT INTO Bestellungen (Datum, KundenID) 
        VALUES ('2025-01-01', 999)")
        verbindung.commit()
    except sqlite3.IntegrityError as e:
        # Wenn PRAGMA ON ist, fängt Python hier den Fehler ab!
        print(f"Fehler: {e}. Der Fremdschlüssel ist ungültig!") 
        verbindung.rollback()
