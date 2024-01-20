# Latihan konversi satuan termperature

# program konversi temperature sederhana

print("\nPROGRAM KONVERSI TEMPERATURE\n")

celcius = float(input("Masukan suhu dalam celcius : "))
print("suhu adalah",celcius, "C")

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah",reamur, "R")

# farenheit
Farenheit = ((9/5) * celcius + 32)
print("suhu dalam farenheit adalah",Farenheit, " F")

# Kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah ", kelvin, "K")