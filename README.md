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


# Longest Increasing Subsequence (LIS) dengan Tree Structure

## 1. Pendahuluan
Longest Increasing Subsequence (LIS) merupakan permasalahan klasik dalam ilmu komputer dan pemrograman dinamis, di mana dari suatu urutan bilangan harus ditemukan subsequence terpanjang yang setiap elemennya lebih besar dari elemen sebelumnya.

Program ini dibuat untuk menyelesaikan permasalahan tersebut menggunakan bahasa **Python** dengan pendekatan **Tree Structure**, dilengkapi dengan **visualisasi tree** dan **penjelasan proses pencarian pada setiap tahap**.

**Perbedaan Subsequence vs Substring:**
- **Subsequence**: Elemen tidak harus berurutan dalam urutan asli, tetapi harus mempertahankan urutan relatifnya
- **Substring**: Elemen harus berurutan dalam urutan asli

**Contoh:**
- Urutan: `[4, 1, 13, 7, 0, 2, 8, 11, 3]`
- Salah satu LIS: `[1, 2, 8, 11]` dengan panjang 4

---

## 2. Tujuan Program
Tujuan dari program ini adalah:
1. Membangun struktur tree untuk merepresentasikan semua kemungkinan increasing subsequence
2. Mencari longest increasing subsequence dari urutan bilangan yang diberikan
3. Memvisualisasikan struktur tree secara hierarkis
4. Menampilkan semua path yang mungkin dari root ke leaf
5. Menentukan path terpanjang sebagai solusi LIS

---

## 3. Cara Penggunaan Program
1. Pastikan Python telah terpasang pada komputer (Python 3.x)
2. Simpan kode program dalam sebuah file, misalnya `lis_tree.py`
3. Buka terminal atau command prompt
4. Jalankan program dengan perintah:
   ```bash
   python lis_tree.py
   ```
5. Program akan otomatis memproses urutan bilangan dan menampilkan hasil

---

## 4. Input Program

Program menerima input sebagai berikut:

### 4.1 Urutan Bilangan Default
```python
sequence = [4, 1, 13, 7, 0, 2, 8, 11, 3]
```

### 4.2 Modifikasi Input
Untuk menggunakan urutan bilangan lain, ubah baris kode pada fungsi `main()`:
```python
# Ubah ini:
sequence = [4, 1, 13, 7, 0, 2, 8, 11, 3]

# Menjadi urutan yang diinginkan:
sequence = [10, 9, 2, 5, 3, 7, 101, 18]
```

### 4.3 Format Input
- List/array bilangan integer
- Dapat berisi bilangan positif, negatif, atau nol
- Tidak ada batasan khusus pada panjang urutan (namun performa optimal untuk n < 100)

---

## 5. Proses Program

Alur kerja program adalah sebagai berikut:

1. **Inisialisasi Tree**
   - Program membuat root node tanpa nilai sebagai titik awal
   - Setiap elemen dari urutan input dijadikan children dari root

2. **Pembangunan Tree Structure**
   - Untuk setiap node, program mencari semua elemen yang lebih besar dan muncul setelahnya dalam urutan asli
   - Elemen-elemen tersebut menjadi children dari node tersebut
   - Proses dilakukan secara rekursif hingga tidak ada elemen yang lebih besar

3. **Pencarian Semua Path**
   - Program menggunakan algoritma DFS (Depth-First Search)
   - Setiap path dari root hingga leaf node dicatat
   - Semua kemungkinan increasing subsequence terekam sebagai path

4. **Penentuan LIS**
   - Program membandingkan panjang semua path yang ditemukan
   - Path dengan panjang maksimum dipilih sebagai LIS
   - Hasil diverifikasi untuk memastikan sifat increasing terpenuhi

5. **Visualisasi dan Statistik**
   - Struktur tree ditampilkan dalam format hierarkis
   - Statistik tree dihitung (jumlah node, path, kedalaman)
   - Hasil akhir LIS ditampilkan

---

## 6. Output Program

Output program ditampilkan langsung pada terminal dalam beberapa bagian.

### 6.1 Simbol yang Digunakan dalam Visualisasi Tree

`ROOT` → Node akar (tanpa nilai)

`├──` → Connector untuk child yang bukan terakhir

`└──` → Connector untuk child terakhir

`│` → Garis vertikal penghubung

Angka → Nilai node dalam tree

### 6.2 Informasi yang Ditampilkan

Pada setiap tahap pemrosesan, program menampilkan:

**A. Proses Pembangunan Tree**
- Progress pembangunan subtree untuk setiap node
- Konfirmasi jumlah node di level 1

**B. Visualisasi Struktur Tree**
```
ROOT
├── 4
│   ├── 13
│   ├── 7
│   │   ├── 8
│   │   │   └── 11
│   │   └── 11
│   ├── 8
│   │   └── 11
│   └── 11
├── 1
│   ├── 13
│   ├── 7
...
```

**C. Contoh Path yang Ditemukan**
```
1. [4, 13] (panjang: 2)
2. [4, 7, 8, 11] (panjang: 4)
3. [4, 7, 11] (panjang: 3)
4. [4, 8, 11] (panjang: 3)
...
```

**D. Statistik Tree**
- Total nodes dalam tree
- Total paths dari root ke leaf
- Kedalaman maksimum tree
- Jumlah elemen input

---

## 7. Hasil Akhir Program

Setelah seluruh proses selesai, program menampilkan:

### 7.1 Hasil LIS
```
Urutan input           : [4, 1, 13, 7, 0, 2, 8, 11, 3]
Longest Increasing     : [1, 2, 8, 11]
Subsequence (LIS)        
Panjang LIS            : 4
```

### 7.2 Verifikasi
Program memverifikasi bahwa hasil adalah increasing subsequence yang valid:
```
Verifikasi increasing  : ✓ VALID
```

Verifikasi dilakukan dengan memeriksa:
- Setiap elemen i < elemen i+1 untuk semua i dalam LIS
- Jika semua pasangan memenuhi syarat, status **✓ VALID**
- Jika ada pasangan yang tidak memenuhi, status **✗ TIDAK VALID**

### 7.3 Contoh Output untuk Input Lain

**Input:** `[10, 9, 2, 5, 3, 7, 101, 18]`
```
Urutan input           : [10, 9, 2, 5, 3, 7, 101, 18]
Longest Increasing     : [2, 3, 7, 101]
Subsequence (LIS)        
Panjang LIS            : 4
Verifikasi increasing  : ✓ VALID
```

**Input:** `[0, 1, 0, 3, 2, 3]`
```
Urutan input           : [0, 1, 0, 3, 2, 3]
Longest Increasing     : [0, 1, 2, 3]
Subsequence (LIS)        
Panjang LIS            : 4
Verifikasi increasing  : ✓ VALID
```

---

## 8. Algoritma yang Digunakan

Program ini menggunakan kombinasi:

### 8.1 Dynamic Programming dengan Tree Structure
- Membangun tree untuk menyimpan semua kemungkinan subsequence
- Setiap node merepresentasikan elemen dalam subsequence
- Children dari node adalah elemen yang lebih besar dan muncul setelahnya

### 8.2 Depth-First Search (DFS)
- Menelusuri semua path dari root ke leaf
- Mencatat setiap subsequence yang mungkin
- Efisien dalam eksplorasi struktur tree

### 8.3 Greedy Selection
- Memilih path dengan panjang maksimum sebagai LIS
- Menggunakan fungsi `max()` dengan key=len untuk efisiensi

**Kompleksitas:**
- **Waktu**: O(n²) untuk pembangunan tree, O(n × 2^n) worst case untuk pencarian path
- **Ruang**: O(n²) untuk struktur tree

Pendekatan ini memberikan visualisasi yang jelas tentang bagaimana subsequence terbentuk, menjadikannya sangat edukatif untuk memahami konsep LIS.

---

## 9. Perbandingan dengan Algoritma Lain

| Algoritma | Kompleksitas Waktu | Kompleksitas Ruang | Kelebihan | Kekurangan |
|-----------|-------------------|-------------------|-----------|------------|
| Brute Force | O(2^n) | O(n) | Sederhana | Sangat lambat |
| DP Array | O(n²) | O(n) | Efisien | Kurang visual |
| **Tree (program ini)** | **O(n²)** | **O(n²)** | **Visual & edukatif** | **Memori lebih besar** |
| Binary Search + DP | O(n log n) | O(n) | Paling cepat | Kompleks |

---

## 10. Troubleshooting

### Program tidak berjalan
- Pastikan Python 3.x terinstall
- Periksa syntax error: `python -m py_compile lis_tree.py`

### Output tidak sesuai ekspektasi
- Verifikasi format input (harus list of integers)
- Periksa apakah urutan input sudah benar

### Memory error untuk input besar (n > 1000)
- Tree structure menggunakan banyak memori
- Untuk input besar, pertimbangkan algoritma DP array atau Binary Search + DP

### Program berjalan lambat
- Waktu eksekusi bergantung pada jumlah kemungkinan subsequence
- Untuk n > 50, waktu proses bisa signifikan meningkat

---

## 11. Lisensi dan Penggunaan

Program ini dibuat untuk tujuan edukatif dan dapat digunakan secara bebas untuk:
- Pembelajaran algoritma dan struktur data
- Tugas akademik
- Penelitian dan pengembangan

Diperbolehkan untuk dimodifikasi dan didistribusikan dengan tetap mencantumkan sumber asli.
