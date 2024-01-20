# Input user

# data yang masuk pasti string

data = input("masukan data: ")
print("data = ",data,",type=",type(data))

# # jika ingin mengambil int, maka
angka = int(input("masukan angka: "))
angka = float(input("masukan angka: "))
print("data= ",data_int,", type=",type(angka))

# untuk bolean perlu di casting ke integer
biner = bool(int(input("masukan nilai bololean: ")))
print("data = ",biner,"<type +",type(biner))
