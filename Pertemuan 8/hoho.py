class PerpusItem:
    def __init__(self, judul, subjek):
        self.judul = judul
        self.subjek = subjek

    def lokasi_penyimpanan(self):
        # Implementasi logika untuk menentukan lokasi penyimpanan
        return "Lokasi penyimpanan: Rak A1"

    def info(self):
        # Implementasi logika untuk menampilkan informasi
        return f"Judul: {self.judul}\nSubjek: {self.subjek}"


class Katalog:
    def cari(self, kata_kunci):
        # Implementasi logika untuk mencari item dalam katalog berdasarkan kata kunci
        return f"Hasil pencarian untuk: {kata_kunci}"


class Buku(PerpusItem):
    def __init__(self, judul, subjek, pengarang, penerbit):
        super().__init__(judul, subjek)
        self.pengarang = pengarang
        self.penerbit = penerbit

    def info(self):
        base_info = super().info()
        return f"{base_info}\nPengarang: {self.pengarang}\nPenerbit: {self.penerbit}"


class Majalah(PerpusItem):
    def __init__(self, judul, subjek, volume, issue):
        super().__init__(judul, subjek)
        self.volume = volume
        self.issue = issue

    def info(self):
        base_info = super().info()
        return f"{base_info}\nVolume: {self.volume}\nIssue: {self.issue}"


class DVD(PerpusItem):
    def __init__(self, judul, subjek, aktor, genre):
        super().__init__(judul, subjek)
        self.aktor = aktor
        self.genre = genre

    def info(self):
        base_info = super().info()
        return f"{base_info}\nAktor: {self.aktor}\nGenre: {self.genre}"


class Pengarang:
    def __init__(self, nama):
        self.nama = nama

    def cari_buku(self, nama_pengarang):
        # Implementasi logika untuk mencari buku berdasarkan nama pengarang
        return f"Hasil pencarian buku untuk pengarang {nama_pengarang}"

    def info_buku(self, buku):
        # Implementasi logika untuk menampilkan informasi buku
        return buku.info()


# Contoh penggunaan kelas dan metode

# Membuat objek buku
buku = Buku("Pemrograman Python", "Python", "Joe", "ABC")

# Memanggil metode lokasi_penyimpanan pada objek buku
print(buku.lokasi_penyimpanan())

# Memanggil metode info pada objek buku
# print(buku.info())

# Membuat objek pengarang
pengarang = Pengarang("Joe")

# Memanggil metode cari_buku pada objek pengarang
print(pengarang.cari_buku("Joe"))

# Memanggil metode info_buku pada objek pengarang dengan objek buku sebagai argumen
print(pengarang.info_buku(buku))