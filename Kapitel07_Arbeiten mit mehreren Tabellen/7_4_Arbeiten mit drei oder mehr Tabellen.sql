SELECT
    B.BestellID,
    A.Name AS Artikelname,
    A.Preis
FROM
    Bestellungen AS B
INNER JOIN
    Bestellpositionen AS BP -- 1. Join
ON
    B.BestellID = BP.BestellID
INNER JOIN
    Artikel AS A            -- 2. Join
ON
    BP.ArtikelID = A.ArtikelID
WHERE
    B.BestellID = 101;

