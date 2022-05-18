## Merupakan kelas anak ##
from tugaspbo import denda
class cicilanmotor(denda):
    biayapotongdenda = 0
    biayaakhir = 0
    bunga = 0

    
    ## dibawah ini adalah constructor##
    def __init__(self,harga,persendenda,lamadenda):
        self.harga = harga
        self.persendenda= persendenda
        self.lamadenda = lamadenda

    ##dibawah ini adalah method overriding kalkulasidenda yang dioverride dari parent##
    ## Merupakan Bagian dari polimorfisme ##
    def kalkulasidenda(self):
        if (self.lamadenda > 30 or self.lamadenda == 0 ):
            print ("karena anda melakukan pelanggaran yaitu menunggak cicilan lebih dari 30 hari maka pengali denda anda adalah lama denda dikurang 30")
            print ("apabila anda tidak menunggak cicilan maka kalkulasi denda adalah nol")
            self.lamadenda = (self.lamadenda - 30)
            for i in range (1,self.lamadenda):
                self.biayapotongdenda = (self.harga*self.persendenda*self.lamadenda)+self.harga
        else : 
            self.biayapotongdenda = ((self.harga*self.persendenda)+self.harga)
        

    def kalkulasimotor(self):
        if (self.harga > 2000000):
            self.bunga = 0.7
            self.biayaakhir = ((self.biayapotongdenda*self.bunga)+ self.biayapotongdenda)
            print("karena harga cicilan lebih dari 2000000 maka mendapat tambahan bunganya adalah 0.7")
        else :
            self.bunga = 0.3
            self.biayaakhir = ((self.biayapotongdenda*self.bunga)+ self.biayapotongdenda)
            print("karen harga kurang dari 2000000 maka mendapat tambahan bunga adalaj 0.3")      

    ##dibawah ini adalah method overriding display yang dioverride dari parent##        
    ## Merupakan Bagian dari polimorfisme ##
    def display(self):
        print ("cicilan akhir setelah cicilan dikalkulasi dengan denda dan bunga")
        print(self.biayaakhir)


            
                
            
    
