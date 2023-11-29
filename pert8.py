class PerpusItem:
    def __init__(self,judul, subjek ):
        self.judul = judul
        self.subjek = subjek

    def lokasiPenyimpanan(self):
        return "Rak Buku"
    
    def info(self):
        print("Judul: ", self.judul)
        print("Subjek: ", self.subjek)
        print("Lokasi Penyimpanan: ", self.lokasiPenyimpanan())

class katalog:
    def cari(self):
        print("Caricari")
    
        
class Buku(PerpusItem):
    def __init__(self, judul, subjek, pengarang, penerbit):
        super().__init__(judul, subjek)
        self.pengarang = pengarang
        self.penerbit = penerbit

    def info(self):
        super().info()
        print("Pengarang: ", self.pengarang)
        print("Penerbit: ", self.penerbit)
        
class Majalah(PerpusItem):
    def __init__(self, volume, issue):
        self.volume = volume
        self.issue = issue
    
    def info(self):
        super().info()
        print("Volume: ", self.volume)
        print("Issue: ", self.issue)
        
class DVD(PerpusItem):
    def __init__(self, aktor, genre):
        self.aktor = aktor
        self.genre = genre
    
    def info(self):
        return super().info()

class pengarang():
        def __init__(self, nama):
            self.nama = nama
        
        def info(self):
            print("Nama: ", self.nama)