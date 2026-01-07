#percabangan if else
nama = str (input("Masukan Nama: "))
umur = int (input("Masukan Umur: "))
tinggi = float (input("Masukan Tinggi Badan: "))
status = input("Kamu Masih Sekolah? Y/N ")

print(f"Nama Kamu {nama}!")
print(f"Umur Kamu {umur} Tahun")
print(f"Tinggi Badan Kamu {tinggi} Cm")
print(f"Status Kamu{status}")
if umur < 18:
    print("Kamu Masih Di Bawah Umur")
else:
    print("Kamu Sudah Dewasa")

if  150 >= tinggi <= 159:
    print("Kamu Pendek Botol Yakult")
elif 160 <= tinggi <= 200 :
    print("Kamu Masuk Rata Rata Orang Tinggi")
else:
    print("Gila Ga Normal Bagi Tingginya Dong")

if status in ["Y","N","y","n"]:
    status == "Y" or status == "y"
    print("Kamu Masih Sekolah ")
elif status == "N" or status == "n":
    print("Kamu sudah tidak bersekolah ")
else:
    print("Mohon Masukan Input Yang Benar Y/N")