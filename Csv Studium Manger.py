import pandas as pd

#Datei Pfad
FILE_Studium = r'C:/Users/MDarweesh/OneDrive - apsolut GmbH/Documents/Studium/.vscode/studium.csv'

#Datei einlesen
studium = pd.read_csv(FILE_Studium, sep=';', encoding='utf-8')

#Nur relevante Spalten
result = studium[['Vorname', 'Nachname', 'Studiengang']]

print(result)