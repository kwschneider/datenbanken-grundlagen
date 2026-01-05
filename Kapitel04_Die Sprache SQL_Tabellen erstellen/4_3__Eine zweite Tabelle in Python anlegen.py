import sqlite3

datenbank_datei = "lager.db"

with sqlite3.connect(datenbank_datei) as verbindung:
    cursor = verbindung.cursor()

    # Tabelle 1: Artikel (aus Kapitel 3)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Artikel (
        ArtikelID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Preis REAL NOT NULL,
        Lagerbestand INTEGER
    )
    """)

    # Tabelle 2: Bestellungen (mit FOREIGN KEY)
    # Hier verwenden wir den Fremdschlüssel (FOREIGN KEY), 
    # um die Verbindung zum Kunden herzustellen!
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Bestellungen (
        BestellID INTEGER PRIMARY KEY,
        Datum TEXT NOT NULL,
        KundenID INTEGER NOT NULL,
        -- Definiert, dass dieser Wert auf eine KundenID in der 
        -- Kunden-Tabelle verweisen MUSS.
        FOREIGN KEY(KundenID) REFERENCES Kunden(KundenID)
    )
    """)

print("Die Tabellen 'Artikel' und 'Bestellungen' wurden erstellt.")
