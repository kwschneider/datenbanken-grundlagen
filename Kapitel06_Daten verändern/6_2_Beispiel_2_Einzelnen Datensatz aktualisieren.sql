UPDATE Artikel
SET Status = 'Nachbestellen'
WHERE Lagerbestand < 10;
