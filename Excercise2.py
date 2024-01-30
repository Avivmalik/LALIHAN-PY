# 2. Program zodiak
print ("========= PROGRAM ZODIAK===========\n")
print ("masukan bulan dan tanggal lahir untuk mengetahui zodiakmu")

bulan = int(input("bulan (dalam angka)\t:"))
tanggal = int(input ("tanggal lahir\t\t:"))

if (bulan == 12 and 31 >= tanggal >= 22) or (bulan == 1 and 31 >= tanggal <= 19):
        zodiak = "Capricorn"
elif (bulan == 1 and 31 >= tanggal >= 20) or (bulan == 2 and 29 >= tanggal <= 18):
        zodiak = "Aquarius"
elif (bulan == 2 and 29 >= tanggal >= 19) or (bulan == 3 and 31 >= tanggal <= 20):
        zodiak = "Pisces"
elif (bulan == 3 and 31 >= tanggal >= 21) or (bulan == 4 and 30 >= tanggal <= 19):
        zodiak = "Aries"
elif (bulan == 4 and 30 >= tanggal >= 20) or (bulan == 5 and 31 >= tanggal <= 20):
        zodiak = "Taurus"
elif (bulan == 5 and 31 >= tanggal >= 21) or (bulan == 6 and 30 >= tanggal <= 20):
        zodiak = "Gemini"
elif (bulan == 6 and 30 >= tanggal >= 21) or (bulan == 7 and 31 >= tanggal <= 22):
        zodiak = "Cancer"
elif (bulan == 7 and 31 >= tanggal >= 23) or (bulan == 8 and 31 >= tanggal <= 22):
        zodiak = "Leo"
elif (bulan == 8 and 31 >= tanggal >= 23) or (bulan == 9 and 30 >= tanggal <= 22):
        zodiak = "Virgo"
elif (bulan == 9 and 30 >= tanggal >= 23 ) or (bulan == 10 and 31 >= tanggal <= 22):
        zodiak = "Libra"
elif (bulan == 10 and 31 >= tanggal >= 23) or (bulan == 11 and 30 >= tanggal <= 21):
        zodiak = "Scorpio"
elif (bulan == 11 and 30 >= tanggal >= 22) or (bulan == 12 and 31 >= tanggal <= 21):
        zodiak = "Sagittarius"
else : 
        print("masukan data dengan benar")

print(f"zodiak kamu adalah:", zodiak)

print ("Program Selesai")
