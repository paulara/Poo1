class Cuenta(object):
    saldo= 0.0
    def ingresar (self,cantidad):
        self.saldo=self.saldo+cantidad
    def retirar (self,cantidad):
        if cantidad<self.saldo:
            self.saldo-=cantidad
        else:
            print("Su saldo no es suficiente")