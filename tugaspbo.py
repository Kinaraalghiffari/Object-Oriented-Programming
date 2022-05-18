##Kinara Al Ghiffari
##081811633049




## Merupakan kelas parent ##
class denda:
    harga = 0
    persendenda = 0
    lamadenda = 0

    ## ini adalah constructor##
    def __init__(self,harga,persendenda,lamadenda):
        self.harga = harga
        self.persendenda = persendenda
        self.lamadenda = lamadenda

    ## dibawah ini adalah abstract method ##
    def kalkulasidenda(self):
        pass

    ## dibawah ini adalah abstract method ## 
    def display(self):
        pass
     
