# Buat class diagram dengan tema Teknologi.
# Class diagram memiliki induk class dan anak sejumlah 2 class. Salah satu anak class memiliki 1 class anak.
# Class induk memiliki atribut dan method yang dapat diturunkan kepada anak classnya.
# Anak class memiliki atribut dan method yang bukan hasil turunan dari induknya.
# Berikan perbedaan akses modifier pada atribut dan method yang digunakan.
# Buat kode programnya yang sesuai dengan class diagram yang anda bangun.
# Terapkan konsep inheritance, enkapsulasi, dan polimorfisme baik overloading maupun overriding.
# Gunakan operator aritmatika dan logika.
# Gunakan perulangan dan percabangan

# Hasilnya dituliskan pada file Word (TAVII_NPM_Nama):
# Class Diagram
# Kode program >> font courier new ukuran 12 (bukan screenshot)
# Screenshot hasil running program
# Kode program up di Github yang sudah diinfokan sebelumnya


# Kode Program
class Komunikasi:
    def __init__(self, nama, jenis, harga):
        self._nama = nama
        self._jenis = jenis
        self._harga = harga

    def get_nama(self):
        return self._nama

    def get_jenis(self):
        return self._jenis

    def get_harga(self):
        return self._harga

class Smartphone(Komunikasi):
    def __init__(self, nama, jenis, harga, merk):
        super().__init__(nama, jenis, harga)
        self._merk = merk

    def get_merk(self):
        return self._merk

    def display_info(self): 
        print("Nama: ", self.get_nama())
        print("Jenis: ", self.get_jenis())
        print("Harga: ", self.get_harga())
        print("Merk: ", self.get_merk())

class TV(Komunikasi):
    def __init__(self, nama, jenis, harga, ukuran):
        super().__init__(nama, jenis, harga)
        self._ukuran = ukuran

    def get_ukuran(self):
        return self._ukuran

    def display_info(self): 
        print("Nama: ", self.get_nama())
        print("Jenis: ", self.get_jenis())
        print("Harga: ", self.get_harga())
        print("Ukuran: ", self.get_ukuran())

class Digital(TV):
    def __init__(self, nama, jenis, harga, ukuran, resolusi):
        super().__init__(nama, jenis, harga, ukuran)
        self._resolusi = resolusi

    def get_resolusi(self):
        return self._resolusi

    def display_info(self): # Overriding
        super().display_info()
        print("Resolusi: ", self.get_resolusi())

class Analog(TV):
    def __init__(self, nama, jenis, harga, ukuran, warna):
        super().__init__(nama, jenis, harga, ukuran)
        self._warna = warna

    def get_warna(self):
        return self._warna

    def display_info(self): # Overriding
        super().display_info()
        print("Warna: ", self.get_warna())


print(20*"=")
smartphone1 = Smartphone("iPhone 12", "Smartphone", 15000000, "Apple")
smartphone1.display_info()
print(20*"=")
digital_tv1 = Digital("Samsung OLED", "TV", 20000000, 55, "4K")
digital_tv2 = Digital("LG OLED", "TV", 25000000, 65, "4K")
analog_tv1 = Analog("Sony CRT", "TV", 5000000, 32, "Hitam")

daftar_tv_digital = [digital_tv1, digital_tv2]
print("Daftar TV Digital: ")
print(20*"=")

# Perulangan
for tv in daftar_tv_digital:
    tv.display_info()
    print(20*"=")
    
print("TV Analog: ")
print(20*"=")
analog_tv1.display_info()
print(20*"=")

# Operator aritmatika
harga_digitaltv1 = digital_tv1.get_harga()
harga_digitaltv2 = digital_tv2.get_harga()
median_harga_digitaltv = (harga_digitaltv1 + harga_digitaltv2) / 2
# Percabangan
if harga_digitaltv1 > median_harga_digitaltv:
    print("Harga TV Digital 1 lebih mahal dari median harga TV Digital")
else:
    print("Harga TV Digital 1 lebih murah dari median harga TV Digital")
if harga_digitaltv2 > median_harga_digitaltv:
    print("Harga TV Digital 2 lebih mahal dari median harga TV Digital")
else:
    print("Harga TV Digital 2 lebih murah dari median harga TV Digital")