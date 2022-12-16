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
        
class metodosOpcionales():
   def creacionCuenta(self):
       nombre=input("Cual es tu nombre ")
       apellido=input("Cual es tu apellido ")
       cedula=input("Cual es tu cedula ")
       edad=input("Cual es tu edad ")
       self.usuario=Usuario(nombre,apellido,cedula,edad)
       self.cuenta=Cuenta(nombre,self.usuario.apellido,self.usuario.cedula,self.usuario.edad,0)
       return
   def depositoCuenta(self):
        saldo = int(input("Digite cantidad a ingresar "))
        self.cuenta.setSaldo(saldo)
        return
   def mostrarSaldo(self):
       print(f"Su saldo actual es {self.cuenta.getSaldo()}")
       return
   def mostrarBeneficio(self):
        interes=self.cuenta.saldo*0.05
        resultado=int(self.cuenta.saldo)+interes
        print("El interes es : {}".format(resultado))
        return
if __name__=='__main__':
    opcion = 0
    metodos=metodosOpcionales()
    while opcion != 5:
        print("Administracion de cuenta de ahorros ");
        print("Digite opcion que desee ")
        print("1.Crear nueva cuenta de ahorros")
        print("2.Hacer un deposito a su cuenta de ahorros")
        print("3. Mostrar el saldo de sue cuenta de ahorro")
        print("4. Mostrar el beneficio de su cuenta de ahorros")
        opciones = {
        1: metodos.creacionCuenta,
        2: metodos.depositoCuenta,
        3: metodos.mostrarSaldo,
        4: metodos.mostrarBeneficio
    }
        opcion = int(input("Ingrese una opción: "))
        if opcion in [1, 2, 3, 4]:
            opciones[opcion]()
        else:
            print("Opción no válida. Intente nuevamente.")
