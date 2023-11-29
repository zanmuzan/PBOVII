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
        print("Volume: ", self.volume)
        print("Issue: ", self.issue)
        
class DVD(PerpusItem):
    def __init__(self, aktor, genre):
        self.aktor = aktor
        self.genre = genre
    
    def info(self):
        print("Aktor: ", self.aktor)
        print("Genre: ", self.genre)

class pengarang():
        def __init__(self, nama):
            self.nama = nama
            
        # cari buku berdasarkan nama pengarang
        
        
            
perpus_item = PerpusItem("Pemrograman Python", "Python")
# perpus_item.info()

buku = Buku("Pemrograman Python", "Python", "Joe", "ABC")
# buku.info()

majalah = Majalah("Vol 1", "Issue 1")
# majalah.info()

dvd = DVD("Aktor 1", "Komedi")
# dvd.info()

# cari pengarang dari buku Pemrograman Python
pengarang = pengarang("Pemrograman Python")
pengarang.info()


# buat program dengan class perpusitem berisi judul, subjek dengan method lokasi penyimpanan dan info. class katalog dengan method cari. class anak dari perpusitem yaitu buku, majalah, dvd. buku berisi pengarang dan penerbit, majalah berisi volume dan issue, dvd berisi aktor dan genre. dan class pengarang dengan atribut nama, dan method cari buku berdasarkan nama pengarang beserta info buku tersebut.