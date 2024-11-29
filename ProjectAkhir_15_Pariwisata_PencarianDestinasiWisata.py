def tampilkan_info(nama_wisata, wisata_data):
    """Menampilkan informasi tentang destinasi wisata berdasarkan nama."""
    if nama_wisata in wisata_data:
        info = wisata_data[nama_wisata]
        print(f"\nInformasi Wisata: {nama_wisata}")
        print(f"Alamat: {info['alamat']}")
        print(f"Harga Masuk: {info['harga_masuk']}")
        print(f"Penjelasan: {info['penjelasan']}")
        print(f"Kendaraan yang Cocok: {info['kendaraan_cocok']}")
        print(f"Penginapan Terdekat: {info['penginapan']}")
        print(f"Rating: {info['rating']}")
    else:
        print("Destinasi wisata tidak ditemukan.\n")


def tambah_destinasi(wisata_data):
    """Menambahkan destinasi wisata baru ke dalam data."""
    print("\nMasukkan Data Destinasi Wisata Baru: ")
    
    nama = input("Nama Wisata: ").strip()
    alamat = input("Alamat: ").strip()

    # Memastikan harga masuk hanya berupa angka
    while True:
        try:
            harga_masuk = input("Harga Masuk: ").strip()
            if harga_masuk.isdigit():
                harga_masuk = int(harga_masuk)  
                if harga_masuk >= 0:  
                    break
            else:
                print("Harga Masuk harus berupa angka. Coba lagi.")
        except ValueError:
            print("Input tidak valid, pastikan harga masuk berupa angka.")

    penjelasan = input("Penjelasan Wisata: ").strip()
    kendaraan_cocok = input("Kendaraan yang Cocok: ").strip()
    penginapan = input("Penginapan Terdekat: ").strip()

    # Memastikan input rating valid
    while True:
        try:
            rating = float(input("Rating (0 - 5): ").strip())
            if 0 <= rating <= 5:
                break
            else:
                print("Rating harus antara 0 dan 5. Coba lagi.")
        except ValueError:
            print("Input tidak valid, pastikan rating berupa angka.")

    # Menyimpan data destinasi wisata ke dalam dictionary
    wisata_data[nama] = {
        "alamat": alamat,
        "harga_masuk": harga_masuk,
        "penjelasan": penjelasan,
        "kendaraan_cocok": kendaraan_cocok,
        "penginapan": penginapan,
        "rating": rating
    }
    print(f"\nDestinasi Wisata '{nama}' berhasil ditambahkan!\n")


def edit_destinasi(wisata_data):
    """Mengedit informasi destinasi wisata yang sudah ada."""
    nama = input("\nMasukkan nama destinasi yang ingin diedit: ").strip()
    if nama in wisata_data:
        print("\nEdit Data Wisata:")
        alamat = input(f"Alamat ({wisata_data[nama]['alamat']}): ").strip() or wisata_data[nama]['alamat']
        
        # Memastikan harga masuk hanya berupa angka
        while True:
            harga_masuk = input(f"Harga Masuk ({wisata_data[nama]['harga_masuk']}): ").strip()
            if harga_masuk.isdigit():
                harga_masuk = int(harga_masuk)  
                if harga_masuk >= 0:
                    break
                else:
                    print("Harga Masuk tidak boleh negatif. Coba lagi.")
            elif not harga_masuk:
                harga_masuk = wisata_data[nama]['harga_masuk']  
                break
            else:
                print("Harga Masuk harus berupa angka. Coba lagi.")

        penjelasan = input(f"Penjelasan Wisata ({wisata_data[nama]['penjelasan']}): ").strip() or wisata_data[nama]['penjelasan']
        kendaraan_cocok = input(f"Kendaraan yang Cocok ({wisata_data[nama]['kendaraan_cocok']}): ").strip() or wisata_data[nama]['kendaraan_cocok']
        penginapan = input(f"Penginapan Terdekat ({wisata_data[nama]['penginapan']}): ").strip() or wisata_data[nama]['penginapan']
        
        while True:
            try:
                rating = input(f"Rating ({wisata_data[nama]['rating']}): ").strip()
                if rating:
                    rating = float(rating)
                if 0 <= rating <= 5:
                    break
                else:
                    print("Rating harus antara 0 dan 5. Coba lagi.")
            except ValueError:
                rating = wisata_data[nama]['rating']
                break

        # Mengupdate data destinasi wisata yang telah diupdate
        wisata_data[nama] = {
            "alamat": alamat,
            "harga_masuk": harga_masuk,
            "penjelasan": penjelasan,
            "kendaraan_cocok": kendaraan_cocok,
            "penginapan": penginapan,
            "rating": rating
        }
        print(f"\nDestinasi Wisata '{nama}' berhasil diupdate!\n")
    else:
        print("Destinasi wisata tidak ditemukan.\n")


def hapus_destinasi(wisata_data):
    """Menghapus destinasi wisata dari data."""
    nama = input("\nMasukkan nama destinasi yang ingin dihapus: ").strip()
    if nama in wisata_data:
        del wisata_data[nama]
        print(f"\nDestinasi Wisata '{nama}' berhasil dihapus!\n")
    else:
        print("Destinasi wisata tidak ditemukan.\n")


def tampilkan_semua_destinasi(wisata_data):
    """Menampilkan semua destinasi wisata yang ada dalam data."""
    if wisata_data:
        print("\nDaftar Semua Destinasi Wisata:")
        for nama, info in wisata_data.items():
            print(f"\nNama Wisata: {nama}")
            print(f"Alamat: {info['alamat']}")
            print(f"Harga Masuk: {info['harga_masuk']}")
            print(f"Penjelasan: {info['penjelasan']}")
            print(f"Kendaraan yang Cocok: {info['kendaraan_cocok']}")
            print(f"Penginapan Terdekat: {info['penginapan']}")
            print(f"Rating: {info['rating']}")
    else:
        print("\nTidak ada destinasi wisata yang tersedia.\n")


def kelola_destinasi(wisata_data):
    """Menu untuk kelola destinasi wisata: tambah, edit, hapus."""
    while True:
        print("\n=== Kelola Destinasi Wisata ===")
        print("1. Tambah Destinasi")
        print("2. Edit Destinasi")
        print("3. Hapus Destinasi")
        print("4. Kembali ke Menu Utama")
        pilihan = input("Pilih menu (1/2/3/4): ").strip()

        if pilihan == '1':
            tambah_destinasi(wisata_data)
        elif pilihan == '2':
            edit_destinasi(wisata_data)
        elif pilihan == '3':
            hapus_destinasi(wisata_data)
        elif pilihan == '4':
            break  # Kembali ke menu utama
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.\n")


def main():
    wisata_data = {}

    while True:
        print("=== Pencarian Destinasi Wisata ===")
        print("1. Lihat Destinasi")
        print("2. Kelola Destinasi")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ").strip()

        if pilihan == '1':
            tampilkan_semua_destinasi(wisata_data)
        elif pilihan == '2':
            kelola_destinasi(wisata_data)
        elif pilihan == '3':
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.\n")


if __name__ == "__main__":
    main()
