# Selamat Datang di Dictionaries!
# Dictionary di Python adalah kumpulan pasangan key-value.
# Bersifat tidak berurutan, bisa diubah, dan terindeks.

# * Dictionary ditulis dengan kurung kurawal {}
# * Memiliki key dan value yang dipisahkan oleh titik dua :
# * Setiap pasangan key-value dipisahkan oleh koma ,

# ==========================================
# Menyimpan data tanpa dictionary (kurang praktis)
# ==========================================
students = ['bob', 12, 'rachel', 13, 'emily', 15]
print(students)

print("-----")

# ==========================================
# Membuat dictionary
# ==========================================
students = {'bob': 12, 'rachel': 13, 'emily': 15}
print(students)

# Mengakses value berdasarkan key
print(students['rachel'])
print(students['bob'])

print("-----")

# ==========================================
# Mengubah value dalam dictionary
# ==========================================
students['rachel'] = 14
# Mengganti value dari key 'rachel'
print(students)

print("-----")

# ==========================================
# Menghapus item dari dictionary
# ==========================================
del students['emily']
# Menghapus pasangan key-value 'emily'
print(students)

print("-----")

# ==========================================
# Panjang dictionary
# ==========================================
print(len(students))
# len() mengembalikan jumlah pasangan key-value

print("-----")

# ==========================================
# Key duplikat dalam dictionary
# ==========================================
students = {'bob': 12, 'bob': 13, 'bob': 15}
# Key yang sama hanya disimpan sekali
# Value terakhir yang akan digunakan
print(students)
