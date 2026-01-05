SELECT *
FROM Bestellungen
-- Finde alle Bestellungen, die nach dem Datum von 'jetzt' 
-- minus 1 Monat liegen
WHERE Bestelldatum >= DATE('now', '-1 month'); 

