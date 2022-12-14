class Usuario:
    def __init__(self,nombre,apellido,cedula,edad) :
        self.nombre=nombre
        self.apellido=apellido
        self.cedula=cedula
        self.edad=edad
        
class Cuenta(Usuario):
    def __init__(self,nombre,apellido,cedula,edad,saldo):
        Usuario.__init__(self,nombre,apellido,cedula,edad)
        self.saldo=saldo
    def setSaldo(self,saldo):
        self.saldo=saldo
    def getSaldo(self):
        return self.saldo
    
class Beneficio(Cuenta):
    def __init__(self, nombre, apellido, cedula, edad, saldo):
        super().__init__(self,nombre, apellido, cedula, edad, saldo)
    def validarEdad(self):
        return self.edad>=18 and self.edad<28
    def mostrar(self):
        interes=self.saldo*0.05
        print("El interes es :"+self.saldo+interes)