import pandas as pd

# ── EJERCICIO 1 ──────────────────────────────────────────────
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

# ── EJERCICIO 2 ──────────────────────────────────────────────
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

# ── EJERCICIO 3 ──────────────────────────────────────────────
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

# ── EJERCICIO 4 ──────────────────────────────────────────────
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
