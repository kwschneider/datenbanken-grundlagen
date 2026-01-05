import sqlite3

# Kurzversion mit with-Statement:
datenbank_datei = "lager.db"

with sqlite3.connect(datenbank_datei) as verbindung:
    cursor = verbindung.cursor()

    sql_befehl = """
    CREATE TABLE IF NOT EXISTS Lagerort (
        OrtID INTEGER PRIMARY KEY,
        Bezeichnung TEXT NOT NULL
    )
    """
    # Hier muss kein verbindung.commit() aufgerufen werden, 
    # da das with-Statement dies automatisch macht,
    # wenn der Block erfolgreich durchlaufen wurde.
    cursor.execute(sql_befehl)

print("Tabelle 'Lagerort' erstellt und Verbindung automatisch \
geschlossen.")
