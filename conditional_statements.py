# Pernyataan Kondisional
# Pernyataan kondisional digunakan untuk menjalankan kode
# berdasarkan kondisi tertentu. Di Python, terdapat:

# * Pernyataan if
# * Pernyataan elif
# * Pernyataan else

# ==========================================
# Pernyataan if dasar
# ==========================================
if 5 > 3:
    print("hello")
# Kondisi bernilai True, maka kode di dalam if dijalankan

print("-----")

# ==========================================
# Pernyataan if - else
# ==========================================
if 3 < 2:
    print("hello")
else:
    print("kondisi tidak terpenuhi")
# Kondisi bernilai False, maka blok else yang dijalankan

# Operator relasi (perbandingan):
# >  (lebih dari)
# <  (kurang dari)
# >= (lebih dari atau sama dengan)
# <= (kurang dari atau sama dengan)
# == (sama dengan)
# != (tidak sama dengan)

# Hapus tanda # di bawah untuk melihat error-nya
# if 5 = 3:       # SALAH: = adalah assignment, bukan perbandingan
#   print('hello')

print("-----")

# ==========================================
# Menggunakan operator == (sama dengan)
# ==========================================
if 5 == 3:
    print('hello')
# Kondisi bernilai False, tidak ada output

print("-----")

# ==========================================
# Pernyataan if - elif - else
# ==========================================
age = 16
if age <= 15:
    print("Kamu lebih muda dari 16")
elif age == 16:
    print("Kamu berusia 16 tahun")
elif age == 17:
    print("Kamu berusia 17 tahun")
else:
    print("Kamu lebih tua dari 16")

print("-----")

# ==========================================
# Menggunakan operator AND
# ==========================================
age = 16
if age < 13:
    print("Kamu masih anak-anak")
elif age >= 13 and age < 18:
    print("Kamu seorang remaja")
    # and: kedua kondisi harus True
else:
    print("Kamu sudah dewasa")

print("-----")

# ==========================================
# Menggunakan operator OR
# ==========================================
if 5 > 3 or 2 < 1:
    print("hi")
# or: cukup salah satu kondisi yang True
