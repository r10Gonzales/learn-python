# Try dan Except
# Blok try-except digunakan untuk menangkap error dalam kode kita.

# * Gunakan try ... except untuk menangkap exception (kesalahan)

# ==========================================
# Blok try - except dasar
# ==========================================
try:
    if name > 3:        # 'name' belum didefinisikan, akan menyebabkan error
        print("hello")
except:
    print("Terdapat error dalam kode kamu")
# Blok try  : menjalankan kode yang mungkin menyebabkan error
# Blok except: dijalankan jika ada error yang terdeteksi
