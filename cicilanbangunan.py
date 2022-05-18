##Merupakan kelas anak##
from tugaspbo import denda
class cicilanbangunan(denda) :
    biayapotongdenda = 0
    biayaakhir = 0
    bunga = 0.15

    ## dibawah ini adalah sebuah constructor##
    def __init__(self,harga,persendenda,lamadenda):
        self.harga = harga
        self.persendenda = persendenda
        self.lamadenda = lamadenda

    ## Dibawah ini adalah method overrriding kalkulasidenda yang di override dari parent##
    ## Merupakan Bagian dari polimorfisme ##
    def kalkulasidenda(self):
        self.biayapotongdenda = ((self.harga*self.persendenda)+self.harga)

        
    def kalkulasirumah(self):
        self.biayaakhir = ((self.biayapotongdenda*self.bunga)+ self.biayapotongdenda)
        
    ## Dibawah ini adalah method overrriding display yang di override dari parent##
    ## Merupakan Bagian dari polimorfisme ##
    def display(self):
        print("cicilan akhir setelah ditambah denda dan bunga")
        print(self.biayaakhir)




