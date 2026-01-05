SELECT Nachname
FROM Kunden
WHERE EXISTS (
    SELECT 1 
    FROM Bestellungen 
    WHERE Bestellungen.KundenID = Kunden.KundenID
);
