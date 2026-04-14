import pandas as pd

print("\n" + "=" * 40)
print("EJERCICIO 2")
print("=" * 40)

df = pd.read_csv("StudentsPerformance.csv")

print("\n-- Últimas 3 columnas --")
print(df[["math score", "reading score", "writing score"]])

print("\n-- Espacios vacíos (NaN) por columna --")
print(df.isnull().sum())

print("\n-- Cantidad de valores por columna --")
print(df.count())

print("\n-- Tipo de dato de la última columna (writing score) --")
print(df[["writing score"]].dtypes)