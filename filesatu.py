# BELAJAR GIT LAGI KARENA UDAH AGAK BERKARAT

# ini adalah file ke satu
# saya mau bikin perhitungan simpel disini

def diskon(nilai,persen):
    diskon = nilai * persen / 100
    hasil = nilai - diskon
    return round(hasil)


print("Mendapat diskon!")
print("Masukkan harga awal \t:")
nilai = input()
print("Masukkan besar diskon \t:")
persen = input()
print("Harga setelah diskon \t:",diskon(int(nilai), int(persen)))


    