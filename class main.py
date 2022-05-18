## Merupakan kelas Main ##
from tugaspbo import denda
from cicilankendaraan import cicilanmotor
from cicilanbangunan import cicilanbangunan
class main :
    print (" Nama : Kinara Al Ghiffari ")
    print (" NIM : 081811633049 ")
    print ("tanggal pembuatan : 19 Desember 2019 ")
    print ("judul proyek : perhitungan akhir cicilan setelah denda dan bunga")
    
    print ("=== Perhitungan cicilan akhir kendaraan bermotor===")
    harga = float(input("biayacicilan : "))
    persendenda = float(input("persendenda(dalam koma) : "))
    lamadenda = int(input("lama denda(dalam hari) : "))
    
    ##dibawahini merupakan tahapan untuk menginisiasi objek###
    A = cicilanmotor(harga,persendenda,lamadenda)
    
    ##dibawahini adalah merupakan tahapan pemanggilan method###
    A.kalkulasidenda()
    A.kalkulasimotor()
    A.display()
    
    print ("=== Perhitungan cicilan akhir bangunan ===")
    harga = float(input("biaya cicilan : "))
    persendenda = float(input("persentase denda(dalam koma) : "))
    lamadenda = int(input("lama denda(dalam hari) : "))
    
    ##dibawahini merupakan tahapan untuk menginisiasi objek###
    B = cicilanbangunan(harga,persendenda,lamadenda)
    
    ##dibawahini adalah merupakan tahapan pemanggilan method###
    B.kalkulasidenda()
    B.kalkulasirumah()
    B.display()


