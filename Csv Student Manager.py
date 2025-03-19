import pandas as pd

# Datei-Pfade (falls benötigt, hier anpassen)
studierende_file = "Studierende.csv"
studiengaenge_file = "studiengaenge.csv"
zugeordnete_file = "zugeordnete_studiengaenge.csv"

# CSV-Dateien einlesen (mit korrektem Trennzeichen ";")
studierende = pd.read_csv(studierende_file, sep=';', encoding='utf-8')
studiengaenge = pd.read_csv(studiengaenge_file, sep=';', encoding='utf-8')
zugeordnete = pd.read_csv(zugeordnete_file, sep=';', encoding='utf-8')

# Spalten umbenennen, um einheitliche Namen zu haben
studierende.rename(columns={'Martikelnummer': 'studierende_id', 'Vorname': 'vorname', 'Nachname': 'name'}, inplace=True)
zugeordnete.rename(columns={'Studierende_Matrikelnummer': 'studierende_id', 'Studiengang_Nr': 'studiengang_id'}, inplace=True)
studiengaenge.rename(columns={'Nr': 'studiengang_id', 'Name': 'studiengang'}, inplace=True)

# Daten kombinieren
merged_df = zugeordnete.merge(studierende, on='studierende_id')
merged_df = merged_df.merge(studiengaenge, on='studiengang_id')

# Relevante Spalten auswählen
result = merged_df[['vorname', 'name', 'studiengang']]

# Ergebnis ausgeben
print(result)
