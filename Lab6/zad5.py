# Zadanie 5. Wczytaj CSV, dodaj kolumne marza=(sprzedaz-koszt)/sprzedaz, posortuj po rok i kraj
import pandas as pd

dane = pd.read_csv('dane.csv', sep=';')
dane['marza'] = (dane['Sprzedaz'] - dane['Koszt']) / dane['Sprzedaz']
dane_sorted = dane.sort_values(by=['Rok', 'Kraj'])

print(dane_sorted.head())
