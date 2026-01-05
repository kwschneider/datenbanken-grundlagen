import sqlite3

try:
    with sqlite3.connect("lager.db") as verbindung:
        cursor = verbindung.cursor()
        
        # 1. Versuch: SQL-Befehl ausführen
        # Hier könnte ein IntegrityError wegen eines doppelten 
        # Primary Keys auftreten
        cursor.execute("INSERT INTO Produkte (Name, Preis) 
        VALUES ('Tastatur', 49.99)")
        verbindung.commit()
        print("Produkt erfolgreich hinzugefügt.")
        
except sqlite3.IntegrityError as e:
    # 2. Fehler abfangen (z.B. Fremdschlüssel- oder Unique-
    # Constraint-Verletzung)
    print(    
          f"FEHLER: Datenintegrität verletzt. Die Daten wurden"    
          f" nicht gespeichert. Details: {e}"
    )    
    # Der with-Block ruft hier automatisch rollback() auf, 
    # aber es ist gut, den Fehler zu melden.
    
except sqlite3.Error as e:
    # 3. Alle anderen SQLite-spezifischen Fehler abfangen 
    # (z.B. Syntaxfehler)
    print(
          f"FEHLER: Ein allgemeiner Datenbankfehler ist"
          f" aufgetreten: {e}"
    )
    
except Exception as e:
    # 4. Alle anderen allgemeinen Python-Fehler abfangen
    print(f"FEHLER: Ein unerwarteter Fehler ist aufgetreten: {e}")
