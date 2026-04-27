# Pengenalan List
# ==========================================
# Variabel individual (belum berupa list)
# ==========================================
item1 = 'apples'
item2 = 'oranges'
item3 = 'bananas'
item4 = 'cheese'
# Variabel di atas menyimpan nilai secara terpisah.
# Menggunakan list lebih praktis untuk data yang dikelompokkan.
print("-----")
# ==========================================
# Membuat list
# ==========================================
shopping_list = ['apples', 'oranges', 'bananas', 'cheese']
# Menampilkan seluruh isi list
print(shopping_list)
# Mengakses item berdasarkan index
# Index dimulai dari 0
print(shopping_list[0])   # item pertama
print(shopping_list[2])   # item ketiga
# Slicing list [awal:akhir]
# Posisi akhir TIDAK ikut diambil
print(shopping_list[0:2]) # index 0 sampai 1
print(shopping_list[0:3]) # index 0 sampai 2
print("-----")
# ==========================================
# Menambah item ke list
# ==========================================
shopping_list.append('blueberries')
# append() menambahkan item di akhir list
print(shopping_list)
print("-----")
# ==========================================
# Mengubah item dalam list
# ==========================================
shopping_list[0] = 'cherries'
# Mengganti item pertama
print(shopping_list)
print("-----")
# ==========================================
# Menghapus item dari list
# ==========================================
del shopping_list[1]
# Menghapus item pada index 1
print(shopping_list)
print("-----")
# ==========================================
# Panjang list
# ==========================================
print(len(shopping_list))
# len() mengembalikan jumlah total item
print("-----")
# ==========================================
# Menggabungkan dan mengulang list
# ==========================================
shopping_list2 = ['bread', 'jam', 'pb']
# Menggabungkan dua list
print(shopping_list + shopping_list2)
# Mengulang list sebanyak dua kali
print(shopping_list * 2)
print("-----")
# ==========================================
# max() dan min()
# ==========================================
list_num = [1, 4, 7, 23, 6]
# Angka terbesar
print(max(list_num))
# Angka terkecil
print(min(list_num))
