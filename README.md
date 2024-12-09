# lab8py

RIDHO FHADLY HAMZAH

312410486

TI.24.A5

# Diagram 
![prak.pict](https://github.com/Nakii-ru/prak.pict/blob/main/diagram8.drawio.png?raw=true)

# Hasil Eksekusi Program
![prak.pict](https://github.com/Nakii-ru/prak.pict/blob/main/Screenshot%202024-12-09%20221025.png?raw=true)
![prak.pict](https://github.com/Nakii-ru/prak.pict/blob/main/Screenshot%202024-12-09%20221038.png?raw=true)
```python
class Daftar_Nilai_Mahasiswa:
    def __init__(self):
        self.daftar_mahasiswa = []
```
Program dimulai dengan menginisialisasi kelas `Daftar_Nilai_Mahasiswa`
```python
    def hitung_nilai_akhir(self, nilai_tugas, nilai_uts, nilai_uas):
        return (nilai_tugas * 0.3) + (nilai_uts * 0.35) + (nilai_uas * 0.35)
```
Fungsi ini menghitung nilai akhir mahasiswa dengan bobot:
`Nilai Tugas`: `30%`
`Nilai UTS`: `35%`
`Nilai UAS`: `35%`

lalu engembalikan hasil perhitungan dalam bentuk nilai akhir.
```python
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
```
Input: `Nama mahasiswa`, `nilai tugas`, `nilai UTS`, dan `nilai UAS`.

Menghitung nilai akhir menggunakan fungsi `hitung_nilai_akhir`.

Membuat `dictionary` mahasiswa untuk menyimpan data mahasiswa, termasuk `nilai akhir`.

Menambahkan `dictionary` tersebut ke dalam `self.daftar_mahasiswa`.

Menampilkan pesan bahwa `data telah ditambahkan`.
```python
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
```
Fungsi pada bagian ini ialah mengecek apakah daftar_mahasiswa kosong. Jika iya, menampilkan pesan "Daftar mahasiswa kosong" dan keluar dari fungsi.

jika daftar memiliki isi, maka menampilkan daftar nilai mahasiswa dengan format tabel
```python
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
```
Mencari mahasiswa berdasarkan nama di dalam daftar_mahasiswa.
Jika ditemukan:

Memperbarui `nilai tugas`, `UTS`, `UAS`, dan menghitung ulang `nilai akhir`nya.
Menampilkan pesan bahwa `data berhasil diubah`.

Jika tidak ditemukan, menampilkan pesan bahwa mahasiswa tidak ditemukan.
```python
    def hapus(self, nama):
        for mahasiswa in self.daftar_mahasiswa:
            if mahasiswa['nama'] == nama:
                self.daftar_mahasiswa.remove(mahasiswa)
                print(f"Data mahasiswa {nama} telah dihapus.")
                return
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")
```
Mencari mahasiswa berdasarkan nama di dalam daftar_mahasiswa.

Jika ditemukan, menghapus mahasiswa tersebut dari list.

Menampilkan pesan bahwa `data berhasil dihapus`.

Jika tidak ditemukan, menampilkan pesan bahwa `mahasiswa tidak ditemukan`.
```python
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
```
Membuat instance `Daftar_Nilai_Mahasiswa`.

Menyediakan menu interaktif untuk pengguna dengan opsi:

`1.Menambah Data mahasiswa.`

`2.Menampilkan daftar Data mahasiswa.`

`3.Mengubah Data mahasiswa.`

`4.Menghapus Data mahasiswa.`

`5.Keluar dari program.`

```python
if __name__ == "__main__":
    main()
```
# Flowchart
![prak.pict](https://github.com/Nakii-ru/prak.pict/blob/main/lab8.drawio.png?raw=true)
