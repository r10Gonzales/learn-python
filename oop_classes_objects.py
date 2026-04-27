# OOP - Class dan Object
# Paradigma pemrograman berorientasi objek (OOP) didasarkan
# pada konsep "objek".

# * Object adalah instance dari class
# * Class adalah template/cetakan untuk membuat object
# * Class mendefinisikan properti dan perilaku dari object

# ==========================================
# Membuat class dasar
# ==========================================
class Animal:
    def __init__(self, name, sound):
        # __init__ adalah constructor — dijalankan saat object dibuat
        self.name = name      # Properti name
        self.sound = sound    # Properti sound

    def speak(self):
        # Method — fungsi yang dimiliki oleh class
        print(self.name + " bersuara " + self.sound)

print("-----")

# ==========================================
# Membuat object (instance) dari class
# ==========================================
cat = Animal("Kucing", "meow")
dog = Animal("Anjing", "guk")
# cat dan dog adalah dua object berbeda dari class Animal

print(cat.name)     # Mengakses properti name dari object cat
print(dog.name)     # Mengakses properti name dari object dog

print("-----")

# ==========================================
# Memanggil method dari object
# ==========================================
cat.speak()
dog.speak()

print("-----")

# ==========================================
# Mengubah properti object
# ==========================================
cat.name = "Kitty"
# Properti object bisa diubah setelah object dibuat
cat.speak()

print("-----")

# ==========================================
# Inheritance (Pewarisan)
# Class baru bisa mewarisi properti dan method dari class lain
# ==========================================
class Dog(Animal):
    def __init__(self, name):
        # Memanggil constructor dari class induk (Animal)
        super().__init__(name, "guk")

    def fetch(self):
        # Method tambahan khusus class Dog
        print(self.name + " mengambil bola!")

print("-----")

# ==========================================
# Membuat object dari class turunan
# ==========================================
my_dog = Dog("Rex")
my_dog.speak()      # Method diwarisi dari class Animal
my_dog.fetch()      # Method khusus milik class Dog
