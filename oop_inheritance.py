# OOP - Pewarisan Class (Inheritance)
# Inheritance adalah fitur powerful dalam OOP yang memungkinkan
# kita membuat class baru berdasarkan class yang sudah ada.

# * Class baru disebut "subclass" atau "child class"
# * Class yang sudah ada disebut "superclass" atau "parent class"

# ==========================================
# Membuat parent class
# ==========================================
class Animal:
    def __init__(self, name, sound):
        # Constructor parent class
        self.name = name
        self.sound = sound

    def speak(self):
        # Method yang akan diwariskan ke child class
        print(self.name + " bersuara " + self.sound)

    def describe(self):
        print("Saya adalah hewan bernama " + self.name)

print("-----")

# ==========================================
# Membuat child class dari Animal
# ==========================================
class Dog(Animal):
    def __init__(self, name):
        # super() memanggil constructor dari parent class
        super().__init__(name, "guk")

    def fetch(self):
        # Method tambahan khusus milik Dog
        print(self.name + " sedang mengambil bola!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "meow")

    def purr(self):
        # Method tambahan khusus milik Cat
        print(self.name + " sedang mendengkur...")

print("-----")

# ==========================================
# Membuat object dari child class
# ==========================================
dog = Dog("Rex")
cat = Cat("Kitty")

# Method yang diwariskan dari parent class Animal
dog.speak()
dog.describe()

print("-----")

cat.speak()
cat.describe()

print("-----")

# ==========================================
# Method khusus masing-masing child class
# ==========================================
dog.fetch()     # Hanya dimiliki oleh Dog
cat.purr()      # Hanya dimiliki oleh Cat

print("-----")

# ==========================================
# Method Overriding
# Child class bisa menimpa method dari parent class
# ==========================================
class Bird(Animal):
    def __init__(self, name):
        super().__init__(name, "cicit")

    def speak(self):
        # Menimpa method speak() dari parent class
        print(self.name + " berkicau dengan suara " + self.sound + "!")

bird = Bird("Burung")
bird.speak()    # Menggunakan method speak() milik Bird, bukan Animal
