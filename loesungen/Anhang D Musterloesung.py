import sqlite3
from sqlite3 import Connection, Cursor, Error
from datetime import date

# Name der Datenbankdatei
DB_NAME = "bibliothek_muster.db"

def create_connection(db_file: str) -> Connection:
    """
    Stellt eine Verbindung zur SQLite-Datenbank her und aktiviert Foreign Keys.

    Args:
        db_file (str): Der Pfad zur Datenbankdatei.

    Returns:
        Connection: Das Verbindungsobjekt zur Datenbank.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        # WICHTIG: Fremdschlüssel-Prüfung aktivieren!
        conn.execute("PRAGMA foreign_keys = ON;")
        print(f"Verbindung zu '{db_file}' hergestellt.")
    except Error as e:
        print(f"Fehler bei der Verbindung: {e}")
    
    return conn

# --- TEIL 1: DDL (Tabellen erstellen) ---

def setup_database(conn: Connection) -> None:
    """
    Erstellt die Tabellenstruktur (DDL).
    
    Args:
        conn (Connection): Das aktive Verbindungsobjekt.
    """
    cursor = conn.cursor()
    
    sql_create_buecher = """
    CREATE TABLE IF NOT EXISTS Buecher (
        BuchID INTEGER PRIMARY KEY,
        Titel TEXT NOT NULL,
        Autor TEXT NOT NULL,
        Erscheinungsjahr INTEGER,
        ISBN TEXT UNIQUE NOT NULL
    );
    """

    sql_create_leser = """
    CREATE TABLE IF NOT EXISTS Leser (
        LeserID INTEGER PRIMARY KEY,
        Vorname TEXT NOT NULL,
        Nachname TEXT NOT NULL,
        Geburtsdatum TEXT,
        Email TEXT UNIQUE
    );
    """

    sql_create_ausleihen = """
    CREATE TABLE IF NOT EXISTS Ausleihen (
        AusleihID INTEGER PRIMARY KEY,
        BuchID INTEGER NOT NULL,
        LeserID INTEGER NOT NULL,
        Ausleihdatum TEXT NOT NULL,
        Rueckgabedatum TEXT,
        FOREIGN KEY (BuchID) REFERENCES Buecher (BuchID),
        FOREIGN KEY (LeserID) REFERENCES Leser (LeserID)
    );
    """

    try:
        cursor.execute(sql_create_buecher)
        cursor.execute(sql_create_leser)
        cursor.execute(sql_create_ausleihen)
        conn.commit()
        print("Tabellenstruktur erfolgreich erstellt.")
    except Error as e:
        print(f"Fehler beim Erstellen der Tabellen: {e}")

# --- TEIL 2: DML (Daten einfügen & ändern) ---

def insert_initial_data(conn: Connection) -> None:
    """
    Füllt die Datenbank mit Testdaten (DML).
    """
    cursor = conn.cursor()
    
    # Bücher einfügen (Verwendung von executemany für Performance)
    buecher = [
        ("Der Herr der Ringe", "J.R.R. Tolkien", 1954, "978-3608938289"),
        ("Clean Code", "Robert C. Martin", 2008, "978-0132350884"),
        ("1984", "George Orwell", 1949, "978-0451524935"),
        ("Der Alchimist", "Paulo Coelho", 1988, "978-0062315007"),
        ("Python Crash Course", "Eric Matthes", 2019, "978-1593279288")
    ]
    
    leser = [
        ("Max", "Mustermann", "1990-05-01", "max@example.com"),
        ("Erika", "Musterfrau", "1985-11-20", "erika@example.com"),
        ("John", "Doe", "2000-02-15", "john.doe@example.com")
    ]

    try:
        cursor.executemany("INSERT OR IGNORE INTO Buecher (Titel, Autor, Erscheinungsjahr, ISBN) VALUES (?, ?, ?, ?)", buecher)
        cursor.executemany("INSERT OR IGNORE INTO Leser (Vorname, Nachname, Geburtsdatum, Email) VALUES (?, ?, ?, ?)", leser)
        
        # Ausleihen einfügen
        # Annahme: IDs sind 1, 2, 3... durch AUTOINCREMENT
        ausleihen = [
            (1, 1, "2023-10-01", None),       # Max leiht Herr der Ringe (noch nicht zurück)
            (2, 1, "2023-09-15", "2023-09-20"), # Max lieh Clean Code (zurückgegeben)
            (3, 2, "2023-10-05", None)        # Erika leiht 1984
        ]
        cursor.executemany("INSERT OR IGNORE INTO Ausleihen (BuchID, LeserID, Ausleihdatum, Rueckgabedatum) VALUES (?, ?, ?, ?)", ausleihen)
        
        conn.commit()
        print("Testdaten eingefügt.")
    except Error as e:
        print(f"Fehler beim Einfügen der Daten: {e}")

def modify_data(conn: Connection) -> None:
    """
    Führt Updates und Deletes durch (Aufgabe 5).
    """
    cursor = conn.cursor()
    try:
        # 1. Update Erscheinungsjahr
        cursor.execute("UPDATE Buecher SET Erscheinungsjahr = 2024 WHERE Titel = 'Clean Code'")
        
        # 2. Update Rückgabedatum auf heute
        cursor.execute("UPDATE Ausleihen SET Rueckgabedatum = DATE('now') WHERE AusleihID = 1")
        
        # 3. Lösche Leser ohne Ausleihen (John Doe, ID 3)
        cursor.execute("DELETE FROM Leser WHERE LeserID = 3")
        
        conn.commit()
        print("Datenaktualisierung (Update/Delete) durchgeführt.")
    except Error as e:
        print(f"Fehler bei Datenänderung: {e}")
        conn.rollback()

# --- TEIL 3: DQL (Abfragen) ---

def run_queries(conn: Connection) -> None:
    """
    Führt diverse SELECT-Abfragen aus und gibt Ergebnisse aus.
    """
    cursor = conn.cursor()
    print("\n--- ABFRAGEN ---")

    # Aufgabe 6.1: Bücher vor 2000
    print("1. Bücher vor 2000:")
    cursor.execute("SELECT Titel, Erscheinungsjahr FROM Buecher WHERE Erscheinungsjahr < 2000")
    for row in cursor.fetchall():
        print(f"   - {row[0]} ({row[1]})")

    # Aufgabe 6.3: Anzahl Bücher
    cursor.execute("SELECT COUNT(*) FROM Buecher")
    anzahl = cursor.fetchone()[0]
    print(f"2. Gesamtanzahl Bücher: {anzahl}")

    # Aufgabe 7.1: Aktive Ausleihen (INNER JOIN)
    print("3. Aktuell ausgeliehene Bücher (Titel & Leser):")
    query_join = """
    SELECT B.Titel, L.Nachname
    FROM Ausleihen AS A
    INNER JOIN Buecher AS B ON A.BuchID = B.BuchID
    INNER JOIN Leser AS L ON A.LeserID = L.LeserID
    WHERE A.Rueckgabedatum IS NULL;
    """
    cursor.execute(query_join)
    rows = cursor.fetchall()
    if not rows:
        print("   - Keine offenen Ausleihen.")
    else:
        for titel, nachname in rows:
            print(f"   - '{titel}' ausgeliehen von {nachname}")

# --- TEIL 4: Stored Procedure in Python ---

def neue_ausleihe_buchen(conn: Connection, buch_id: int, leser_id: int) -> None:
    """
    Simuliert eine Stored Procedure, um eine Ausleihe transaktionssicher zu buchen.
    
    Args:
        conn: Datenbankverbindung
        buch_id: ID des Buches
        leser_id: ID des Lesers
    """
    cursor = conn.cursor()
    print(f"\n--- Buche Ausleihe: Buch {buch_id} für Leser {leser_id} ---")
    
    try:
        # Start einer expliziten Transaktion (optional, da Python oft implizit startet, aber sauberer)
        # Überprüfen, ob das Buch überhaupt verfügbar ist (optionaler Logik-Schritt)
        cursor.execute("SELECT Rueckgabedatum FROM Ausleihen WHERE BuchID = ? AND Rueckgabedatum IS NULL", (buch_id,))
        if cursor.fetchone():
            raise ValueError("Buch ist aktuell bereits ausgeliehen!")

        # Einfügen
        sql = "INSERT INTO Ausleihen (BuchID, LeserID, Ausleihdatum) VALUES (?, ?, DATE('now'))"
        cursor.execute(sql, (buch_id, leser_id))
        
        conn.commit()
        print("✅ Ausleihe erfolgreich gebucht.")
        
    except ValueError as ve:
        print(f"❌ Abbruch der Logik: {ve}")
    except sqlite3.IntegrityError:
        print("❌ Datenbankfehler: Ungültige BuchID oder LeserID (Fremdschlüssel verletzt).")
        conn.rollback()
    except Error as e:
        print(f"❌ Allgemeiner Fehler: {e}")
        conn.rollback()

# --- Hauptprogramm ---

def main():
    # 1. Verbindung aufbauen
    conn = create_connection(DB_NAME)
    
    if conn is not None:
        # 2. Struktur und Daten
        setup_database(conn)
        insert_initial_data(conn)
        modify_data(conn)
        
        # 3. Abfragen
        run_queries(conn)
        
        # 4. Prozedur testen
        # Test 1: Gültige Buchung (Buch 5 an Leser 2)
        neue_ausleihe_buchen(conn, 5, 2)
        
        # Test 2: Fehlerhafte Buchung (Nicht existierender Leser ID 99)
        neue_ausleihe_buchen(conn, 5, 99)
        
        conn.close()
        print("\nDatenbankverbindung geschlossen.")

if __name__ == '__main__':
    main()
