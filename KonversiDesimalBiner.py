desimal = int(input("masukan bilangan desimal"))

#validasi input
if desimal < 0:
    print("masukan bilangan desimal yang valid(>= 0).")

#jika angka 0
elif desimal == 0:
    print("0 dalam biner adalah 0")

else:
    angka = desimal
    biner = ""
    proses = ""
# perulangan pembagian dengan 2
    while angka > 0:
        hasilBagi = angka // 2
        sisa = angka % 2
        # menyimpan proses 
        proses += (
            str(angka) +
            " ÷ 2 = " +
            str(hasilBagi) +
            " sisa " +
            str(sisa) +
            "\n"
        )
        # Sisa dimasukan ke depan
        biner = str(sisa) + biner
        # angka berikutnya
        angka = hasilBagi

    # menampilkan hasil
    print()
    print("Bilangan Desimal:", desimal)
    print()
    print("Tahapan Perhitungan:")
    print(proses)
    print("Baca sisa dari bawah ke atas:")
    print(biner)
    print()
    print(
        "Jadi,",
        desimal,
        "desimal =",
        biner,
        "biner"
    )


