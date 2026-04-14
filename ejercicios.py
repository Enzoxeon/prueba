import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

# ── EJERCICIO 1 ──────────────────────────────────────────────
print("=" * 40)
print("EJERCICIO 1")
print("=" * 40)

df1 = df[["gender", "lunch", "math score"]]

print("\n-- Primeras 12 filas --")
print(df1.head(12))

print("\n-- Últimas 8 filas --")
print(df1.tail(8))

# ── EJERCICIO 2 ──────────────────────────────────────────────
print("\n" + "=" * 40)
print("EJERCICIO 2")
print("=" * 40)

df2 = pd.read_csv("StudentsPerformance.csv")

print("\n-- Últimas 3 columnas --")
print(df2.iloc[:, -3:])

print("\n-- Espacios vacíos (NaN) --")
print(df2.isnull())

print("\n-- Cantidad de valores vacíos por columna --")
print(df2.isnull().sum())

ultima_col = df2.columns[-1]
print(f"\n-- Tipo de dato de la última columna ('{ultima_col}') --")
print(df2[ultima_col].dtype)

# ── EJERCICIO 3 ──────────────────────────────────────────────
print("\n" + "=" * 40)
print("EJERCICIO 3")
print("=" * 40)

df3 = pd.read_csv("StudentsPerformance.csv")

print("\n-- Columna reading score --")
print(df3["reading score"])

print("\n-- Cantidad de valores --")
print(df3["reading score"].count())

print("\n-- Suma total --")
print(df3["reading score"].sum())

# ── EJERCICIO 4 ──────────────────────────────────────────────
print("\n" + "=" * 40)
print("EJERCICIO 4")
print("=" * 40)

df4 = pd.read_csv("StudentsPerformance.csv")

print("\n-- Primeras 2 columnas --")
print(df4.iloc[:, :2])

print("\n-- Tipos de datos --")
print(df4.dtypes)

print("\n-- Últimas 10 filas --")
print(df4.tail(10))
