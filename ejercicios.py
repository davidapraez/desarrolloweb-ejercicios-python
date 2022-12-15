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
   def __init__(self):
       self.arrayUsuarios=[]
   
   def creacionCuenta(self):
       self.nombre=input("Cual es tu nombre")
       self.apellido=input("Cual es tu apellido")
       self.cedula=input("Cual es tu cedula")
       self.edad=input("Cual es tu edad")
       self.saldo=0
       usuario=Usuario(self.nombre,self.apellido,self.cedula,self.edad)
       self.arrayUsuarios.append(Cuenta(self.nombre,self.apellido,self.cedula,self.edad,self.saldo))
   def depositoCuenta(self):
       cedula = input("Ingresa tu cédula: ")
       for cuenta in self.arrayUsuarios:
           if cuenta.usuario.cedula == cedula:
               saldo = int(input("Digite cantidad a ingresar "))
               cuenta.saldo += saldo
               break
   def mostrarSaldo(self):
       cedula = input("Ingresa tu cédula: ")
       for cuenta in self.arrayUsuarios:
           if cuenta.usuario.cedula == cedula:
               print(f"Su saldo actual es {cuenta.saldo}")
               break
   def mostrarBeneficio(self):
        cedula = input("Ingresa tu cédula: ")
        for cuenta in self.arrayUsuarios:
           if cuenta.usuario.cedula == cedula:
               interes=self.cuenta.saldo*0.05
               print("El interes es :"+self.cuenta.saldo+interes)
        
if __name__=='__main__':
    metodos=metodosOpcionales()  
    print("Administracion de cuenta de ahorros ");
    print("Digite opcion que desee ")
    print("1.Crear nueva cuenta de ahorros")
    print("2.Hacer un deposito a su cuenta de ahorros")
    print("3. Mostrar el saldo de sue cuenta de ahorro")
    print("4. Mostrar el beneficio de su cuenta de ahorros")
    opcion = 0
    while opcion != 4:
        opcion = int(input("Ingrese una opción: "))
        if opcion in [1, 2, 3, 4]:
            opciones={
                1:metodos.creacionCuenta(),
                2:metodos.depositoCuenta(),
                3:metodos.mostrarSaldo(),
                4:metodos.mostrarBeneficios()
            }
            break
        else:
            print("Opción no válida. Intente nuevamente.")
    

