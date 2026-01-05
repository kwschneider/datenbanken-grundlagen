-- Finde alle Artikel, deren Lagerbestand kleiner als 10 ist.
SELECT ArtikelID, Name, Lagerbestand
FROM Artikel
WHERE Lagerbestand < 10;
