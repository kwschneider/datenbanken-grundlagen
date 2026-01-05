SELECT KundenID, COUNT(BestellID) AS Anzahl_Bestellungen
FROM Bestellungen
GROUP BY KundenID;
