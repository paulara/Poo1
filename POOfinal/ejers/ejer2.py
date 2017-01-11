class Persona(object):
    nombre=''
    dni=''
    direccion=''
    telefono=''
    email=''
    def mostrar(self):
        print("nombre",self.nombre,"dni",self.dni,"direccion",self.direccion,"telefono",self.telefono)
        if self.email!='':
            print("email",self.email)
            