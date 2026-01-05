SELECT
    B.BestellID,
    K.Vorname,
    K.Nachname,
    B.Datum
FROM
    Bestellungen AS B  -- Tabelle umbenennen (Alias)
INNER JOIN
    Kunden AS K        -- Tabelle umbenennen (Alias)
ON
    B.KundenID = K.KundenID;
