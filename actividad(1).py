import pandas as pd
 
df = pd.read_csv("StudentsPerformance.csv")

print("=" * 40)
print("EJERCICIO 1")
print("=" * 40)
 
df1 = df[["gender", "lunch", "math score"]]
 
print("\n-- Primeras 12 filas --")
print(df1.head(12))
 
print("\n-- Últimas 8 filas --")
print(df1.tail(8))