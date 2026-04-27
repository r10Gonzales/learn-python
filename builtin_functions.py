# Fungsi Bawaan Python
# Python memiliki banyak fungsi bawaan yang bisa langsung digunakan.

# ==========================================
# abs() — mengembalikan nilai absolut (mutlak)
# ==========================================
print(abs(-5))      # Output: 5
print(abs(5))       # Output: 5
print(abs(-3.14))   # Output: 3.14

print("-----")

# ==========================================
# dir() — menampilkan daftar atribut dan method dari suatu objek
# ==========================================
print(dir(str))     # Menampilkan semua method yang dimiliki string
print(dir(list))    # Menampilkan semua method yang dimiliki list

print("-----")

# ==========================================
# help() — menampilkan dokumentasi/bantuan suatu fungsi
# ==========================================
help(abs)           # Menampilkan penjelasan tentang fungsi abs()
help(len)           # Menampilkan penjelasan tentang fungsi len()

print("-----")

# ==========================================
# bool() — mengubah nilai menjadi boolean (True atau False)
# ==========================================
print(bool(1))      # Output: True
print(bool(0))      # Output: False
print(bool(""))     # Output: False  (string kosong = False)
print(bool("hi"))   # Output: True

print("-----")

# ==========================================
# int() — mengubah nilai menjadi integer (bilangan bulat)
# ==========================================
print(int(3.9))     # Output: 3     (desimal dipotong, bukan dibulatkan)
print(int("10"))    # Output: 10    (string angka diubah ke integer)
print(int(True))    # Output: 1
print(int(False))   # Output: 0

print("-----")

# ==========================================
# float() — mengubah nilai menjadi float (bilangan desimal)
# ==========================================
print(float(5))     # Output: 5.0
print(float("3.14")) # Output: 3.14  (string angka diubah ke float)
print(float(True))  # Output: 1.0

print("-----")

# ==========================================
# str() — mengubah nilai menjadi string (teks)
# ==========================================
print(str(100))     # Output: '100'
print(str(3.14))    # Output: '3.14'
print(str(True))    # Output: 'True'
