# Game Tebak Angka

Program game tebak angka sederhana berbasis terminal yang ditulis dalam Python. Pemain harus menebak angka rahasia yang dipilih secara acak oleh komputer dalam jumlah kesempatan terbatas.

## Deskripsi Game

Game ini adalah permainan tebak angka klasik dimana:
- Komputer akan memilih angka rahasia secara acak antara 1 hingga 67
- Pemain memiliki 3 kali kesempatan untuk menebak
- Setiap tebakan akan diberi petunjuk "kekecilan" atau "kebesaran"
- Game berakhir ketika pemain berhasil menebak atau kehabisan kesempatan

## Cara Bermain

1. Jalankan program:
```bash
python tebak_angka.py
```

2. Program akan menampilkan pesan: `gas tebak angka 1-67`
3. Masukkan tebakan angka Anda
4. Ikuti petunjuk yang diberikan:
   - Jika tebakan terlalu kecil: muncul pesan "kekecilan"
   - Jika tebakan terlalu besar: muncul pesan "kebesaran"
   - Jika tebakan benar: muncul pesan "hoki [angka] adalah angka yang benar"
5. Anda memiliki 3 kali kesempatan untuk menebak
6. Jika kehabisan kesempatan, program akan menampilkan angka rahasia

## Contoh Gameplay

```
gas tebak angka 1-67
masukan angka: 34
kekecilan
masukan angka: 50
kebesaran
masukan angka: 42
hoki 42 adalah angka yang benar
```

Contoh jika kehabisan kesempatan:
```
gas tebak angka 1-67
masukan angka: 20
kekecilan
masukan angka: 60
kebesaran
masukan angka: 40
kekecilan
maaf kesempatan habis, angka yang benar adalah 42
```

## Fitur

- **Angka Acak**: Setiap game memiliki angka rahasia yang berbeda (1-67)
- **Batasan Kesempatan**: Pemain hanya diberi 3 kali kesempatan menebak
- **Petunjuk Interaktif**: Petunjuk "kekecilan" atau "kebesaran" untuk membantu pemain
- **Validasi Input**: Program akan menangani input yang tidak valid (bukan angka)
- **Informasi Hasil**: Menampilkan angka rahasia jika pemain kehabisan kesempatan

## Logika Program

```python
# Angka rahasia acak antara 1-67
secret_number = random.randint(1, 67)

# Loop selama tebakan belum benar dan kesempatan masih ada
while tebakan != secret_number and nyoba > 0:
    # Kurangi kesempatan setiap kali menebak
    nyoba -= 1
    
    # Beri petunjuk berdasarkan perbandingan
    if tebakan < secret_number:
        print("kekecilan")
    elif tebakan > secret_number:
        print("kebesaran")
```

## Requirements

- Python 3.x
- Module random (built-in)

## Struktur Kode

Program terdiri dari:
- Fungsi `tebak_angka()` yang berisi seluruh logika game
- Import module `random` untuk generate angka acak
- Validasi input menggunakan try-except
- Loop utama dengan kondisi berhenti yang jelas
- Penghitung kesempatan (3 kali percobaan)

## Kustomisasi

Anda dapat memodifikasi game dengan mengubah beberapa parameter:
- **Batas angka**: Ubah parameter `random.randint(1, 67)` untuk mengubah range angka
- **Jumlah kesempatan**: Ubah nilai variabel `nyoba = 3` untuk menambah/mengurangi percobaan
- **Pesan**: Ubah teks dalam fungsi `print()` sesuai keinginan

## Contoh Modifikasi

Untuk membuat game dengan angka 1-100 dan 5 kali kesempatan:
```python
secret_number = random.randint(1, 100)
nyoba = 5
```

## Tujuan Pembelajaran

Game ini cocok untuk pembelajaran dasar Python:
- Penggunaan module random
- Loop while dengan kondisi
- Percabangan if-elif-else
- Try-except untuk validasi input
- Variabel counter
- Fungsi dan pemanggilan fungsi

## Lisensi

Program ini dapat digunakan dan dimodifikasi secara bebas untuk keperluan pembelajaran dan pengembangan skill programming.

---
**Selamat bermain dan semoga berhasil menebak!** 🎮
