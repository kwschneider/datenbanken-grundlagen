# Finde den teuersten Artikel
cursor.execute("SELECT MAX(Preis) FROM Artikel")

# Index [0] greift auf das erste Element des Tupels zu
hoechster_preis = cursor.fetchone()[0] 
print(f“Der höchste Preis beträgt: {hoechster_preis} €“)
