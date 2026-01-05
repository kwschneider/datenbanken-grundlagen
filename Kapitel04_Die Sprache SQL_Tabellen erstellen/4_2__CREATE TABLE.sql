CREATE TABLE Kunden (
    KundenID INTEGER PRIMARY KEY,
    Vorname TEXT NOT NULL,
    Nachname TEXT NOT NULL,
    Email TEXT UNIQUE,
    RegistriertSeit TEXT DEFAULT CURRENT_DATE
)
