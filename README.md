# Knight’s Tour

## 1. Pendahuluan
Knight’s Tour merupakan permasalahan klasik dalam ilmu komputer dan matematika diskrit, di mana sebuah bidak kuda pada papan catur harus mengunjungi setiap kotak tepat satu kali dengan mengikuti aturan pergerakan kuda.  
Program ini dibuat untuk menyelesaikan permasalahan tersebut menggunakan bahasa **Python**, dilengkapi dengan **visualisasi papan catur** dan **penjelasan perpindahan kuda pada setiap iterasi**.

Program mendukung dua jenis perjalanan:
- **Open Tour**: perjalanan berakhir di sembarang kotak
- **Closed Tour**: perjalanan berakhir di *attacking square*, yaitu kotak terakhir dapat menyerang kotak awal

---

## 2. Tujuan Program
Tujuan dari program ini adalah:
1. Menentukan rute Knight’s Tour pada papan catur 8×8.
2. Memvisualisasikan setiap langkah bidak kuda secara bertahap.
3. Menunjukkan semua kemungkinan arah perpindahan kuda pada setiap iterasi.
4. Membandingkan solusi **Open Tour** dan **Closed Tour**.

---

## 3. Cara Penggunaan Program
1. Pastikan Python telah terpasang pada komputer.
2. Simpan kode program dalam sebuah file, misalnya `knights_tour_visual.py`.
3. Buka terminal atau command prompt.
4. Jalankan program dengan perintah:
   ```bash
   python knights_tour_visual.py
   ```
5. Program akan menampilkan menu pemilihan mode dan meminta input dari pengguna.

---

## 4. Input Program

Program menerima input sebagai berikut:
### 4.1 Pemilihan Mode
Pengguna diminta memilih jenis Knight’s Tour:
```bash
1 → Open Tour (berhenti di sembarang kotak)

2 → Closed Tour (berhenti di attacking square)
```

### 4.2 Posisi Awal Kuda
Pengguna memasukkan koordinat awal bidak kuda:
```bash
Baris awal (0 – 7)
Kolom awal (0 – 7)
```
Koordinat menggunakan indeks berbasis nol, di mana (0, 0) merepresentasikan sudut kiri atas papan catur.

--- 

## 5. Proses Program

Alur kerja program adalah sebagai berikut:
1. Program menginisialisasi papan catur 8×8 dengan status belum dikunjungi.
2. Bidak kuda ditempatkan pada posisi awal sesuai input pengguna.
3. Pada setiap iterasi:
   - Program menghitung seluruh langkah kuda yang valid.
   - Semua langkah yang memungkinkan ditampilkan pada papan.
   - Langkah terbaik dipilih menggunakan heuristik Warnsdorff, yaitu memilih langkah dengan jumlah kemungkinan lanjutan paling sedikit.
4. Langkah yang dipilih ditandai sebagai langkah selanjutnya, dan papan diperbarui.
5. Proses diulang hingga seluruh kotak papan telah dikunjungi.
6. Jika mode Closed Tour dipilih, program memeriksa apakah posisi akhir dapat menyerang posisi awal.

--- 

## 6. Output Program
Output program ditampilkan langsung pada terminal dalam bentuk papan catur visual (ASCII).

### 6.1 Simbol yang Digunakan

`K` → Posisi bidak kuda saat ini

`*` → Kemungkinan langkah yang dapat diambil pada iterasi tersebut

`.` → Kotak yang belum dikunjungi

`XX` → Kotak yang sudah dikunjungi

### 6.2 Informasi yang Ditampilkan
Pada setiap iterasi, program menampilkan:
- Nomor langkah (iterasi)
- Posisi kuda saat ini
- Daftar koordinat semua kemungkinan langkah
- Arah perpindahan kuda yang dipilih
- Visualisasi papan catur setelah langkah dilakukan

## 7. Hasil Akhir Program
Setelah seluruh kotak papan dikunjungi:

Jika mode **Open Tour** dipilih dan berhasil, program menampilkan pesan:
``` python
OPEN TOUR BERHASIL
```

Jika mode **Closed Tour** dipilih dan posisi akhir dapat menyerang posisi awal, program menampilkan pesan:
``` python
CLOSED TOUR BERHASIL (attacking square)
```
Jika syarat perjalanan tidak terpenuhi, program menampilkan pesan kegagalan.

## 8. Algoritma yang Digunakan
Program ini menggunakan kombinasi:

- **Backtracking** untuk menelusuri kemungkinan langkah kuda

- **Heuristik Warnsdorff** untuk mengurangi kompleksitas pencarian solusi

Pendekatan ini membuat program lebih efisien dibandingkan pencarian brute-force murni.