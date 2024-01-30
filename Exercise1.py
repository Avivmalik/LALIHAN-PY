# Excercise
# 1. Bilangan ganjil dan genap

a = (1,2,3,4,5,6)
list_ganjil= [i for i in a if i %2 !=0]
print (f"bilangan ganjil dalam a adalah", list_ganjil)

list_genap = [i for i in a if i %2 ==0]
print (f"bilangan ganjil dalam a adalah", list_genap)