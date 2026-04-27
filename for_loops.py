# Pengenalan For Loops
# For loop digunakan untuk menjalankan kode secara berulang.

# * For loop dibuat menggunakan sintaks for ... in
# * Bisa digunakan untuk iterasi atas list, tuple, atau urutan lainnya
# * Bisa menggunakan fungsi range() untuk menghasilkan urutan angka

# ==========================================
# Iterasi atas list dan tuple
# ==========================================
list1 = ['apples', 'bananas', 'cherries']
tup1 = (2, 6, 10)

for item in list1:
    print(item)
# Menampilkan setiap item dalam list satu per satu

for item in tup1:
    print(item)
# Menampilkan setiap item dalam tuple satu per satu

print("-----")

# ==========================================
# Menggunakan range()
# range(awal, akhir) — akhir TIDAK ikut dicetak
# ==========================================
for i in range(0, 10):
    print(i)
# Mencetak angka 0 sampai 9

print("-----")

for i in range(1, 11):
    print(i)
# Mencetak angka 1 sampai 10

print("-----")

# ==========================================
# range() dengan langkah (step)
# range(awal, akhir, langkah)
# ==========================================
for i in range(0, 11, 2):
    print(i)
# Mencetak angka genap dari 0 sampai 10

print("-----")

for i in range(5, 51, 5):
    print(i)
# Mencetak kelipatan 5 dari 5 sampai 50

print("-----")

# ==========================================
# Contoh sederhana range()
# ==========================================
for i in range(0, 5):
    print(i)
# Mencetak angka 0 sampai 4

print("-----")

# ==========================================
# Nested for loop (for loop di dalam for loop)
# ==========================================
for i in range(0, 5):
    for j in range(0, 3):
        print(i * j)
# Loop luar: i berjalan dari 0 sampai 4
# Loop dalam: j berjalan dari 0 sampai 2
# Setiap iterasi mencetak hasil perkalian i * j
