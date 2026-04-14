import pandas as pd

print("\n" + "=" * 40)
print("EJERCICIO 4")
print("=" * 40)

df = pd.read_csv("StudentsPerformance.csv")

print("\n-- Primeras 2 columnas --")
print(df[["gender", "race/ethnicity"]])

print("\n-- Tipos de datos --")
print(df.dtypes)

print("\n-- Filas y columnas (shape) --")
print(df.shape)

print("\n-- Últimas 10 filas --")
print(df.tail(10))
