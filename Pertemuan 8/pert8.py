class PerpusItem:
    def __init__(self, judul, subjek):
        self.judul = judul
        self.subjek = subjek

    def lokasi_penyimpanan(self):
        if self.subjek == "Fiksi":
            return "Rak Fiksi"
        elif self.subjek == "Non-Fiksi":
            return "Rak Non-Fiksi"
        else:
            return "Lokasi tidak diketahui"

    def info(self):
        return f"Judul: {self.judul}, Subjek: {self.subjek}"

class Katalog:
    def __init__(self):
        self.items = []
        
    def info(self):
        for item in self.items:
            print(item.info())
            print(item.lokasi_penyimpanan())
            print()

    def tambah_item(self, item):
        self.items.append(item)

    def cari(self, judul):
        for item in self.items:
            if item.judul == judul:
                print("Item ada dalam katalog")
                return item
        print("Judul tidak ditemukan.")

class Buku(PerpusItem):
    def __init__(self, judul, subjek, isbn, pengarang, jml_halaman, ukuran):
        super().__init__(judul, subjek)
        self.isbn = isbn
        self.pengarang = pengarang
        self.jml_halaman = jml_halaman
        self.ukuran = ukuran

    def info(self):
        return f"Judul: {self.judul}, Subjek: {self.subjek}, ISBN: {self.isbn}, " \
               f"Pengarang: {self.pengarang}, Jumlah Halaman: {self.jml_halaman}, Ukuran: {self.ukuran}"

class Majalah(PerpusItem):
    def __init__(self, judul, subjek, volume, issue):
        super().__init__(judul, subjek)
        self.volume = volume
        self.issue = issue

    def info(self):
        return f"Judul: {self.judul}, Subjek: {self.subjek}, Volume: {self.volume}, Issue: {self.issue}"

class DVD(PerpusItem):
    def __init__(self, judul, subjek, aktor, genre):
        super().__init__(judul, subjek)
        self.aktor = aktor
        self.genre = genre

    def info(self):
        return f"Judul: {self.judul}, Subjek: {self.subjek}, Aktor: {self.aktor}, Genre: {self.genre}"

class Pengarang:
    def __init__(self, nama):
        self.nama = nama

    def cari_buku(self, katalog):
        hasil_pencarian = []
        for item in katalog.items:
            if isinstance(item, Buku) and item.pengarang == self.nama:
                hasil_pencarian.append(item)
        return hasil_pencarian
    
buku1 = Buku("Harry Potter", "Fiksi", "1234567890", "J.K. Rowling", 300, "A5")
buku2 = Buku("Pemrograman Python", "Non-Fiksi", "0987654321", "Joe Marini", 400, "A4")
majalah1 = Majalah("National Geographic", "Non-Fiksi", "2020", "Januari")
dvd1 = DVD("Avengers", "Fiksi", "Robert Downey Jr.", "Action")

katalog = Katalog()
katalog.tambah_item(buku1)
katalog.tambah_item(buku2)
katalog.tambah_item(majalah1)
katalog.tambah_item(dvd1)

katalog.info()
print("=="*60)

katalog.cari("Harry Potter")
katalog.cari("Pemrograman Berorientasi Objek")
print("=="*60)
pengarang1 = Pengarang("J.K. Rowling")
hasil_pencarian1 = pengarang1.cari_buku(katalog)

pengarang2 = Pengarang("Joe Marini")
hasil_pencarian2 = pengarang2.cari_buku(katalog)

pengarang3 = Pengarang("Joe")
hasil_pencarian3 = pengarang3.cari_buku(katalog)

print("Hasil pencarian buku dengan pengarang J.K. Rowling:")
for buku in hasil_pencarian1:
    print(buku.info())

print("\nHasil pencarian buku dengan pengarang Joe Marini:")
for buku in hasil_pencarian2:
    print(buku.info())