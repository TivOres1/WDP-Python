# Zadanie 6. Zwróc rekordy dla DE w latach >=2023 i tylko kolumny sprzedaz i marza
import pandas as pd

dane = pd.read_csv('dane.csv', sep=';')
dane['marza'] = (dane['Sprzedaz'] - dane['Koszt']) / dane['Sprzedaz']
dane_sorted = dane.sort_values(by=['Rok', 'Kraj'])

wynik = dane_sorted[(dane_sorted['Kraj'] == 'DE') & (dane_sorted['Rok'] >= 2023)][['Sprzedaz', 'marza']]
print(wynik)
