# Pengenalan While Loops
# While loop digunakan untuk menjalankan kode secara berulang.

# * While loop dibuat menggunakan kata kunci while
# * Berjalan terus selama kondisi bernilai True

# ==========================================
# While loop dasar
# ==========================================
c = 0
while c < 5:
    c = c + 1
    print(c)
# Menambah nilai c sebesar 1 setiap iterasi
# Berhenti ketika c tidak lagi kurang dari 5

print("-----")

# ==========================================
# break — menghentikan loop sepenuhnya
# ==========================================
c = 0
while c < 5:
    c = c + 1
    if c == 3:
        break       # Keluar dari loop saat c bernilai 3
    print(c)
# Output: 1, 2 (berhenti sebelum mencetak 3)

print("-----")

# ==========================================
# continue — melewati iterasi saat ini
# ==========================================
c = 0
while c < 5:
    c = c + 1
    if c == 3:
        continue    # Lewati print saat c bernilai 3
    print(c)
# Output: 1, 2, 4, 5 (angka 3 dilewati)

print("-----")

# ==========================================
# pass — tidak melakukan apa-apa, loop tetap berjalan
# ==========================================
c = 0
while c < 5:
    c = c + 1
    if c == 3:
        pass        # Tidak ada aksi khusus saat c bernilai 3
    print(c)
# Output: 1, 2, 3, 4, 5 (pass tidak mempengaruhi apapun)
