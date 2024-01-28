# Acces list
# index     0(-3)      1(-2)      2(-1)
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# By leaving out the end value, the range will go on to the end of the list:
thistkist=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Panjang data
data =["apple", "banana", "cherry", "orange", "kiwi", "mango"]

panjang_data = len(data)
print(f"panjang_data = {panjang_data}")
#======================================= Add List ==============================
# menambahkan item pada list sesuai posisi
# posisi 1
data.insert (1, "watermelon")
print(f"data sesudah ditambah = \n{data}")

# menambahkan item pada list pada akhir list
data.append("cucumber")
print(f"data sesudah ditambah = \n{data}")

#menambah list dengan list baru
data_baru =("avocado", "lychee")
data.extend (data_baru)
print(f"data sesudah ditambah list = \n{data}")

# changes list
data[0] = ("strawberry")
print(f"data diubah = \n{data}")

# removing data
data.remove("banana")
print(f"data setelah diubah = \n{data}")

data_akhir = data.pop()
print(f"data diubah = \n{data}")