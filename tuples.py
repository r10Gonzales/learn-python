# Pengenalan Tuples
# Tuple mirip dengan list, tetapi bersifat immutable.
# Artinya, setelah tuple dibuat, isinya tidak bisa diubah.

# * Tuple dibuat menggunakan tanda kurung ()
# * Item dalam tuple dipisahkan oleh koma ,

# ==========================================
# Membuat tuple
# ==========================================
tup = ('oranges', 'apples', 'bananas')
print(tup)

# ==========================================
# Tuple bersifat immutable (tidak bisa diubah)
# ==========================================
# tup[0] = 'cherries'  # Hapus tanda # untuk melihat error-nya

# Slicing tuple [awal:akhir]
# Posisi akhir TIDAK ikut diambil
print(tup[0:2])  # index 0 sampai 1

print("-----")

# ==========================================
# Menggabungkan tuple
# ==========================================
tup2 = (12, 14)
tup3 = tup + tup2
# Menggabungkan dua tuple menjadi tuple baru
print(tup3)
