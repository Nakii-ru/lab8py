class Daftar_Nilai_Mahasiswa:
    def __init__(self):
        self.daftar_mahasiswa = []

    def hitung_nilai_akhir(self, nilai_tugas, nilai_uts, nilai_uas):
        return (nilai_tugas * 0.3) + (nilai_uts * 0.35) + (nilai_uas * 0.35)

    def tambah(self, nama, nilai_tugas, nilai_uts, nilai_uas):
        nilai_akhir = self.hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)
        mahasiswa = {
            "nama": nama,
            "nilai_tugas": nilai_tugas,
            "nilai_uts": nilai_uts,
            "nilai_uas": nilai_uas,
            "nilai_akhir": nilai_akhir
        }
        self.daftar_mahasiswa.append(mahasiswa)
        print(f"Data mahasiswa {nama} telah ditambahkan.")

    def tampilkan(self):
        if not self.daftar_mahasiswa:
            print("Daftar mahasiswa kosong.")
            return
        print("=" * 56)
        print("   |               Daftar Nilai Mahasiswa              |")
        print("=" * 56)
        print("No | Nama       | Tugas | UTS   | UAS   | Nilai Akhir  |")
        print("=" * 56)
        for i, mahasiswa in enumerate(self.daftar_mahasiswa, start=1):
            print(f"{i:2} | {mahasiswa['nama']:<10} | {mahasiswa['nilai_tugas']:5.1f} | {mahasiswa['nilai_uts']:5.1f} | {mahasiswa['nilai_uas']:5.1f} | {mahasiswa['nilai_akhir']:5.1f}        |")
        print("=" * 56)

    def ubah(self, nama, nilai_tugas, nilai_uts, nilai_uas):
        for mahasiswa in self.daftar_mahasiswa:
            if mahasiswa['nama'] == nama:
                mahasiswa['nilai_tugas'] = nilai_tugas
                mahasiswa['nilai_uts'] = nilai_uts
                mahasiswa['nilai_uas'] = nilai_uas
                mahasiswa['nilai_akhir'] = self.hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)
                print(f"Data mahasiswa {nama} telah berhasil diubah.")
                return
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")

    def hapus(self, nama):
        for mahasiswa in self.daftar_mahasiswa:
            if mahasiswa['nama'] == nama:
                self.daftar_mahasiswa.remove(mahasiswa)
                print(f"Data mahasiswa {nama} telah dihapus.")
                return
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")

def main():
    daftar_nilai = Daftar_Nilai_Mahasiswa()
    while True:
        print("\nMenu:")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Daftar Mahasiswa")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            nama = input("Masukkan nama mahasiswa: ")
            nilai_tugas = float(input("Masukkan nilai tugas: "))
            nilai_uts = float(input("Masukkan nilai UTS: "))
            nilai_uas = float(input("Masukkan nilai UAS: "))
            daftar_nilai.tambah(nama, nilai_tugas, nilai_uts, nilai_uas)
        elif pilihan == "2":
            daftar_nilai.tampilkan()
        elif pilihan == "3":
            nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
            nilai_tugas = float(input("Masukkan nilai tugas baru: "))
            nilai_uts = float(input("Masukkan nilai UTS baru: "))
            nilai_uas = float(input("Masukkan nilai UAS baru: "))
            daftar_nilai.ubah(nama, nilai_tugas, nilai_uts, nilai_uas)
        elif pilihan == "4":
            nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
            daftar_nilai.hapus(nama)
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid")
if __name__ == "__main__":
    main()