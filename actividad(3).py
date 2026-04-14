import pandas as pd
 
df = pd.read_csv("StudentsPerformance.csv")

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