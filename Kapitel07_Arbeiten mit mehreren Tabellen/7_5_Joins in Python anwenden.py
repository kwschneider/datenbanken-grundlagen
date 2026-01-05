import sqlite3

datenbank_datei = "lager.db"

def bestell_details_abrufen(bestell_id):
    with sqlite3.connect(datenbank_datei) as verbindung:
        cursor = verbindung.cursor()

        # SQL-Abfrage aus 7.4. mit Platzhalter
        sql_abfrage = """
        SELECT
            A.Name,
            A.Preis,
            BP.Anzahl
        FROM
            Bestellungen AS B
        INNER JOIN Bestellpositionen AS BP 
        ON B.BestellID = BP.BestellID
        INNER JOIN Artikel AS A 
        ON BP.ArtikelID = A.ArtikelID
        WHERE
            B.BestellID = ?;
        """

        cursor.execute(sql_abfrage, (bestell_id,))
        ergebnisse = cursor.fetchall()

        if ergebnisse:
            print(f"--- Details zur Bestellung {bestell_id} ---")
            for name, preis, anzahl in ergebnisse:
                print(f"  {anzahl}x {name} (Einzelpreis:"
                      f" {preis} €)")
        else:
            print(f"Bestellung {bestell_id} nicht gefunden"
                  f" oder leer.")

# Wir müssten die Tabellen 'Kunden', 'Artikel', 'Bestellungen' und 
# 'Bestellpositionen' zuerst erstellen und mit Beispieldaten 
# füllen, um diesen Code auszuführen.
bestell_details_abrufen(101)
