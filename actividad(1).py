import pandas as pd

print("=" * 40)
print("EJERCICIO 1")
print("=" * 40)

df = pd.read_csv("StudentsPerformance.csv")

print("\n-- Columnas gender y math score --")
print(df[["gender", "math score"]])

print("\n-- Primeras 12 filas --")
print(df.head(12))

print("\n-- Últimas 8 filas --")
print(df.tail(8))
