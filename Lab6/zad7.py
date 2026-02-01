# Zadanie 7. Generuj losowe dane, dodaj kolumne marza, rok i filtruj po kraju oraz sumuj sprzedaz
import pandas as pd
import numpy as np

rng = np.random.default_rng(42)
daty = pd.date_range("2024-01-01", periods=120, freq="D")
kraje = rng.choice(["PL", "DE", "US"], size=len(daty))
spr = rng.integers(50, 250, size=len(daty))
kos = spr * rng.uniform(0.4, 0.8, size=len(daty))
prod = rng.choice(["A", "B", "C"], size=len(daty))

df = pd.DataFrame({
    "Data": daty,
    "Kraj": kraje,
    "Produkt": prod,
    "Sprzedaz": spr,
    "Koszt": np.round(kos, 2),
    "Waluta": "PLN"
})

df['marza'] = np.where(df['Sprzedaz']==0, 0, (df['Sprzedaz']-df['Koszt'])/df['Sprzedaz'])
df['Rok'] = df['Data'].dt.year

print(df[(df['Kraj']=='PL') & (df['Produkt']=='A')])
print('\n', '='*10, '\n')
print(df.groupby('Kraj')['Sprzedaz'].sum().sort_values(ascending=False))
print('\n', '='*10, '\n')
print(df.groupby('Kraj', group_keys=False).apply(lambda g: g.nlargest(20, 'marza')))
