import pandas as pd

print("\n" + "=" * 40)
print("EJERCICIO 3")
print("=" * 40)

df = pd.read_csv("StudentsPerformance.csv")

print("\n-- Columna reading score --")
print(df[["reading score"]])

print("\n-- Cantidad de valores --")
print(df[["reading score"]].count())

print("\n-- Suma total --")
print(df["reading score"].sum())