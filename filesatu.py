# BELAJAR GIT LAGI KARENA UDAH AGAK BERKARAT

# ini adalah file ke satu
# saya mau bikin perhitungan simpel disini

def diskon(nilai,persen):
    diskon = nilai * persen / 100
    hasil = nilai - diskon
    return round(hasil)

nilai = 100000
persen = 20 # dalam persen

print("Mendapat diskon!")
print("Harga awal \t:",nilai)
print("Harga akhir \t:",diskon(nilai, persen))


    