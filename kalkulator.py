operasi = ["0.Keluar","1.Pertambahan","2.Pengurangan","3.Perkalian","4.Pembagian"]

print("----Kalkulator----")
for pilihan in operasi:
    print(pilihan)

pilihan_user = input("Pilih operasi 0/1/2/3/4: ")

if pilihan_user =="0":
    print("keluar dari program")
    exit()
if pilihan_user in ["1","2","3","4"]:
    a = int(input("Masukan Angka "))
    b = int(input("Masukan Angka "))
if pilihan_user == "1":
    tambah = a + b
    print(f"Hasil Pertambahan Dari {a} + {b} Adalah {tambah}")
elif pilihan_user == "2":
    kurang = a - b
    print(f"Hasil Pengurangan Dari {a} - {b} Adalah {kurang}")
elif pilihan_user == "3":
    kali = a * b
    print(f"Hasil Perkalian Dari {a} x {b} Adalah {kali}")
elif pilihan_user == "4":
    bagi = a / b
    print(f"Hasil Pembagian Dari {a} / {b} Adalah {bagi}")

    
else:
    print("Mohon masukan angka yang sesuai 0/1/2/3/4")
   

    

