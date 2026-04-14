import pandas as pd
 
df = pd.read_csv("StudentsPerformance.csv")

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
