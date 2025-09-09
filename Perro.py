#Autor: Miguel Silva
#Crear una clase llamada Perro y crear distintos metodos

class Perro:
    def __init__(self, color, raza, peso, edad, nombre):
        self.color=color
        self.raza=raza
        self.peso=int(peso)
        self.edad=int(edad)
        self.nombre=nombre
    
    def __str__(self):
        str_color=f"-------------\nColor: {self.color}\n"
        str_raza=f"Raza: {self.raza}\n"
        str_peso=f"Peso: {self.peso}kg\n"
        str_edad=f"Edad: {self.edad} años\n"
        str_nombre=f"Nombre: {self.nombre}\n-------------"
        return str_color + str_raza + str_peso + str_edad + str_nombre

    def ladrar(self):
        print("\nGuau!\n")
    
    def dar_comida(self, cantidad_comida):
        self.cantidad_comida=int(cantidad_comida)
        if self.cantidad_comida<=3 and self.cantidad_comida>0:
            print(f"Le has dado al perro {self.cantidad_comida} cucharadas de comida, {self.nombre} sigue triste.")
        elif self.cantidad_comida>3:
            print(f"Le has dado al perro {self.cantidad_comida} cucharadas de comida, {self.nombre} esta feliz.")
        elif self.cantidad_comida<0:
            raise ValueError("No puedes dar cantidades negativas.")
    
    def acariciar_perro(self):
        print("El perro esta feliz, porque lo estas acariciando\n")

    def pasear_perro(self, tiempo_paseo):
        self.tiempo_paseo=tiempo_paseo
        while self.tiempo_paseo>0:
            print(f"Quedan {self.tiempo_paseo} minutos de paseo.")
            self.tiempo_paseo-=1

        
def perro():
    #Mi perro
    color_perro=input("Ingrese el color de su perro: ")
    raza_perro=input("Ingrese la raza de su perro: ")
    peso_perro=int(input("Ingrese el peso de su perro en kg: "))
    edad_perro=int(input("Ingrese la edad de su perro: "))
    nombre_perro=input("Ingrese el nombre de su perro: ")
    mi_perro= Perro(color_perro,raza_perro,peso_perro,edad_perro,nombre_perro)
    print(mi_perro)
    
    #Pasear perro
    tiempo_paseo_perro=int(input(f"\nCuantos minutos quieres pasear a {nombre_perro}: "))
    mi_perro.pasear_perro(tiempo_paseo_perro)

    #Dar de comer al perro
    cantidad_comida_perro=int(input(f"\nCuantas cucharadas de comida le quieres dar a {nombre_perro}: "))
    mi_perro.dar_comida(cantidad_comida_perro)

    #Ladrar
    mi_perro.ladrar()

def main():
    perro()

if __name__=="__main__":
    main()