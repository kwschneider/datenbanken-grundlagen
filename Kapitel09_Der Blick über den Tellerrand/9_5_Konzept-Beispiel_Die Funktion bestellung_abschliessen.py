import sqlite3

datenbank_datei = "lager.db"

def bestellung_abschliessen(kunden_id, artikel_liste):
    """
    Führt die gesamte Geschäftslogik zum Abschluss einer Bestellung 
    aus (Python-Alternative zur Stored Procedure).
    """
    with sqlite3.connect(datenbank_datei) as verbindung:
        cursor = verbindung.cursor()
        
        try:
            # 1. Bestellung einfügen und ID holen
            cursor.execute("INSERT INTO Bestellungen 
            (KundenID, Datum) 
            VALUES (?, datetime('now'))", (kunden_id,))
            bestell_id = cursor.lastrowid 

            # 2. Artikelpositionen und Lagerbestände aktualisieren
            for artikel_id, anzahl in artikel_liste:
                # Füge in Bestellpositionen ein
                cursor.execute("INSERT INTO Bestellpositionen 
                (BestellID, ArtikelID, Anzahl) VALUES (?, ?, ?)", 
                (bestell_id, artikel_id, anzahl))
                
                # Lagerbestand reduzieren
                cursor.execute("UPDATE Artikel 
                SET Lagerbestand = Lagerbestand - ? 
                WHERE ArtikelID = ?", (anzahl, artikel_id))
            # 3. Transaktion abschließen
            verbindung.commit()
            return (f"Bestellung {bestell_id} erfolgreich" 
                    f" abgeschlossen.")
            
        except sqlite3.Error as e:
            # Bei Fehlern (z.B. Lagerbestand negativ) wird 
            # zurückgerollt (Rollback)
            verbindung.rollback()
            return f"Fehler beim Abschließen der Bestellung: {e}"

# Die gesamte "Stored Logic" ist nun in dieser einen, modularen 
# Python-Funktion gekapselt.

