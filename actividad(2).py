import pandas as pd
 
df = pd.read_csv("StudentsPerformance.csv")
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