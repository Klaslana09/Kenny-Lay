Menu = ['1. Report Penjualan Barang Toko',
        '2. Menambahkan Barang Toko',
        '3. Menghapus Barang Toko',
        '4. Mengubah Barang Toko',
        '5. Keluar']

Barang = [{'Id': 100, 'Nama': 'Pensil', 'Harga': 2000, 'Stok': 100},
            {'Id': 101, 'Nama': 'Pulpen', 'Harga': 15000, 'Stok': 50},
            {'Id': 102, 'Nama': 'Penghapus', 'Harga': 5000, 'Stok': 75},
            {'Id': 200, 'Nama': 'Novel', 'Harga': 30000, 'Stok': 30},
            {'Id': 201, 'Nama': 'Komik', 'Harga': 25000, 'Stok': 20},
            {'Id': 202, 'Nama': 'Majalah', 'Harga': 10000, 'Stok': 40},
            {'Id': 300, 'Nama': 'Keripik', 'Harga': 5000, 'Stok': 200},
            {'Id': 301, 'Nama': 'Oreo', 'Harga': 3000, 'Stok': 150},
            {'Id': 302, 'Nama': 'Permen', 'Harga': 1000, 'Stok': 180},
            {'Id': 400, 'Nama': 'Air Mineral', 'Harga': 3000, 'Stok': 500},
            {'Id': 401, 'Nama': 'Teh Botol', 'Harga': 6000, 'Stok': 400},
            {'Id': 402, 'Nama': 'Kopi Instan', 'Harga': 12000, 'Stok': 250},
            {'Id': 500, 'Nama': 'Keyboard', 'Harga': 125000, 'Stok': 10},
            {'Id': 501, 'Nama': 'Mouse', 'Harga': 100000, 'Stok': 15},
            {'Id': 502, 'Nama': 'Headset', 'Harga': 150000, 'Stok': 25}]


def Report_barang():
    while True:
        print("\n+++++++ Report Penjualan Barang Toko +++++++")
        print("1. Report Seluruh Barang Toko")
        print("2. Report Barang Toko Berdasarkan Kategori")
        print("3. Kembali ke Menu Utama")
        read = input("Masukkan pilihan Anda (1-3): ")
        if read == '1':
            if Barang:
                print("Daftar barang:")
                for j, i in enumerate(Barang):
                    print(f"{j+1}. Id: {i['Id']}, Nama: {i['Nama']}, Harga: {i['Harga']}, Stok: {i['Stok']}")
            else:
                print("+++++++ Tidak ada Barang Tersedia +++++++")
        elif read == '2':
            print("Kategori:\n1) Alat Tulis\n2) Buku\n3) Makanan\n4) Minuman\n5) Elektronik")
            kategori = input("Masukkan kategori (1-5): ")
            kategori_range = {
                '1': (100, 199),
                '2': (200, 299),
                '3': (300, 399),
                '4': (400, 499),
                '5': (500, 599)
            }
            if kategori not in kategori_range:
                print("Kategori tidak valid.")
                continue
            id_min, id_max = kategori_range[kategori]
            filtered = [i for i in Barang if id_min <= i['Id'] <= id_max]
            if filtered:
                for j, i in enumerate(filtered):
                    print(f"{j+1}. Id: {i['Id']}, Nama: {i['Nama']}, Harga: {i['Harga']}, Stok: {i['Stok']}")
            else:
                print("Tidak ada barang dalam kategori ini.")
        elif read == '3':
            break
        else:
            print("Pilihan tidak valid.")


def tambahkan_barang():
    if password := input("Masukkan password untuk menambahkan barang: ") != "123":
        print("Password salah. Penambahan barang dibatalkan.")
        return
    print("\n+++++++ Tambahkan Barang Toko +++++++")
    print("Jenis-Jenis Barang dan ID:\n1) Alat Tulis\n2) Buku\n3) Makanan\n4) Minuman\n5) Elektronik")
    kategori = input("Pilih jenis barang (1-5): ")
    kategori_range = {
        '1': (100, 199),
        '2': (200, 299),
        '3': (300, 399),
        '4': (400, 499),
        '5': (500, 599)
    }
    if kategori not in kategori_range:
        print("Kategori tidak valid.")
        return
    id_min, id_max = kategori_range[kategori]
    id_terakhir = id_min - 1
    for barang in Barang:
        if id_min <= barang['Id'] <= id_max and barang['Id'] > id_terakhir:
            id_terakhir = barang['Id']
    id_baru = id_terakhir + 1
    if id_baru > id_max:
        print("Tidak bisa menambahkan barang, ID dalam kategori ini sudah penuh.")
        return
    nama = input("Masukkan nama barang: ")
    harga = input("Masukkan harga barang: ")
    stok = input("Masukkan jumlah stok: ")
    if not (harga.isdigit() and stok.isdigit()):
        print("Harga dan stok harus berupa angka.")
        return
    Barang.append({'Id': id_baru, 'Nama': nama, 'Harga': int(harga), 'Stok': int(stok)})
    print(f"Barang berhasil ditambahkan dengan ID: {id_baru}")


def hapus_barang():
    if not Barang:
        print("Belum ada data barang.")
        return
    if password := input("Masukkan password untuk menghapus barang: ") != "123":
        print("Password salah. Hapus barang dibatalkan.")
        return
    for b in Barang:
        print(f"- {b['Id']} ({b['Nama']})")
    id_input = input("Masukkan ID barang yang ingin dihapus: ")
    if id_input.isdigit():
        id_barang = int(id_input)
        for i in Barang:
            if i['Id'] == id_barang:
                Barang.remove(i)
                print(f"Barang dengan ID {id_barang} berhasil dihapus.")
                return
        print(f"Barang dengan ID {id_barang} tidak ditemukan.")
    else:
        print("Input ID harus berupa angka.")


def ubah_barang():
    if not Barang:
        print("Belum ada data barang.")
        return
    if password := input("Masukkan password untuk mengubah barang: ") != "123":
        print("Password salah. Ubah barang dibatalkan.")
        return
    for b in Barang:
        print(f"- {b['Id']} ({b['Nama']})")
    id_input = input("Masukkan ID barang yang ingin diubah: ")
    if id_input.isdigit():
        id_barang = int(id_input)
        for i in Barang:
            if i['Id'] == id_barang:
                print(f"Barang ditemukan: Id: {i['Id']}, Nama: {i['Nama']}, Harga: {i['Harga']}, Stok: {i['Stok']}")
                nama = input("Masukkan nama baru barang: ")
                harga = input("Masukkan harga baru barang: ")
                stok = input("Masukkan stok baru barang: ")
                if harga.isdigit() and stok.isdigit():
                    i['Nama'] = nama
                    i['Harga'] = int(harga)
                    i['Stok'] = int(stok)
                    print(f"Barang dengan ID {id_barang} berhasil diubah.")
                else:
                    print("Harga dan stok harus berupa angka.")
                return
        print(f"Barang dengan ID {id_barang} tidak ditemukan.")
    else:
        print("Input ID harus berupa angka.")


def main():
    while True:
        print("\n+++++++ Menu Utama +++++++")
        for item in Menu:
            print(item)
        pilihan = input("Masukkan pilihan Anda (1-5): ")
        if pilihan == '1':
            Report_barang()
        elif pilihan == '2':
            tambahkan_barang()
        elif pilihan == '3':
            hapus_barang()
        elif pilihan == '4':
            ubah_barang()
        elif pilihan == '5':
            print("Terima Kasih.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
