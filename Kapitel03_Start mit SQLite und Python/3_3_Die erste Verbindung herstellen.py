## Schritt 1: Die Verbindung herstellen
import sqlite3

# Stellt die Verbindung zur Datenbankdatei her.
# Wenn die Datei "lager.db" nicht existiert, wird sie erstellt.
datenbank_datei = "lager.db"
verbindung = sqlite3.connect(datenbank_datei)

print(f"Erfolgreich mit der Datenbank {datenbank_datei} \
verbunden.")

## Schritt 2: Den Cursor erstellen
# Der Cursor wird erstellt, um SQL-Befehle auszuführen
cursor = verbindung.cursor()

## Schritt 3: Eine Tabelle anlegen (DDL-Befehl)
# Hier wird der SQL-Befehl in Python als String gespeichert
sql_befehl = """
CREATE TABLE Artikel (
    ArtikelID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Preis REAL NOT NULL,
    Lagerbestand INTEGER
)
"""

# Der Cursor führt den Befehl aus
cursor.execute(sql_befehl)

## Schritt 4: Änderungen speichern und Verbindung schließen
# Die Änderungen in der Datenbank dauerhaft speichern
verbindung.commit()

# Die Datenbankverbindung sauber schließen
verbindung.close()

print("Tabelle 'Artikel' erstellt und Verbindung geschlossen.")

