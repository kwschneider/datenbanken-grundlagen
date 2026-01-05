# Beispiel für einen manuellen Rollback (ohne 'with')
verbindung = sqlite3.connect("lager.db")
cursor = verbindung.cursor()

try:
    cursor.execute("UPDATE Konten SET Kontostand = Kontostand - 100 
    WHERE KontoID = 1")
    # Hier könnte ein Fehler auftreten, der den zweiten Schritt 
    # verhindert!
    cursor.execute("UPDATE Konten SET Kontostand = Kontostand + 100 
    WHERE KontoID = 2")
    
    verbindung.commit() # Nur, wenn beide Schritte klappten
    
except sqlite3.Error as e:
    print(f"Fehler: {e}. Transaktion wird zurückgenommen.")
    verbindung.rollback() # Alles zurücksetzen

finally:
    verbindung.close()
