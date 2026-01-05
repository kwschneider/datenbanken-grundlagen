SELECT
    K.Vorname,
    B.BestellID
FROM
    -- Dies ist die LINKE Tabelle (alle Kunden werden gezeigt)
    Kunden AS K  
LEFT JOIN
    Bestellungen AS B
ON
    K.KundenID = B.KundenID;

