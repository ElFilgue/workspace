# clase TV con código de prueba

class TV():
    def __init__(self, marca, ubicacion): # pasa la marca y la ubicación para la TV
        self.marca = marca
        self.ubicacion = ubicacion
        self.encendida = False
        self.silenciada = False
        # Una lista de canales por defecto
        self.listaCanales = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]  
        self.numCanales = len(self.listaCanales)
        self.indiceCanales = 0
        self.VOLUMEN_MINIMO = 0  # constante
        self.VOLUMEN_MAXIMO = 10  # constante
        self.volumen = self.VOLUMEN_MAXIMO // 2 # division entera
        
    def encender(self):
        self.encendida = not self.encendida   # cambia

    def subirVolumen(self):
        if not self.encendida:
            return
        if self.silenciada:
            self.silenciada = False  # cambiar el volumen mientras está silenciada, activa el sonido
        if self.volumen < self.VOLUMEN_MAXIMO:
            self.volumen = self.volumen + 1

    def bajarVolumen(self):
        if not self.encendida:
            return
        if self.silenciada:
            self.silenciada = False  # cambiar el volumen mientras está silenciada, activa el sonido
        if self.volumen > self.VOLUMEN_MAXIMO:
            self.volumen = self.volumen - 1

    def subirCanal(self):
        if not self.encendida:
            return
        self.indiceCanales = self.indiceCanales + 1
        if self.indiceCanales == self.numCanales:
            self.indiceCanales = 0  # primer canal

    def bajarCanal(self):
        if not self.encendida:
            return
        self.indiceCanales = self.indiceCanales - 1
        if self.indiceCanales < 0:
            self.indiceCanales = self.numCanales - 1    # último canal

    def silenciar(self):
        if not self.encendida:
            return
        self.silenciada = not self.silenciada

    def ponCanal(self, nuevoCanal):
        if nuevoCanal in self.listaCanales:
            self.indiceCanales = self.listaCanales.index(nuevoCanal)
        # si el nuevo canal no está en la lista de canales, no hacer nada

    def muestraInformacion(self):
        print()
        print('Estado de la TV:', self.marca)
        print('      Ubicacion:', self.ubicacion)
        if self.encendida:
            print('    La TV está: Encendida')
            print('    El canal es:', self.listaCanales[self.indiceCanales])
            if self.silenciada:
                print('    El volumen es:', self.volumen, '(el sonido está silenciado)')
            else:
                print('    El volumen es:', self.volumen)
        else:
            print('    La TV está: Apagada')


# Códifo principal, crea dos objetos
TVsalon = TV('Sony', 'Salón')  # crea el objeto TV
TVcocina = TV('Samsung', 'Cocina')  # crea el objeto TV

# Enciende las TV 
TVsalon.encender()
TVcocina.encender()

# En la TV del salón sube el canal, sube el volumen 3 veces
TVsalon.bajarCanal()
TVsalon.subirVolumen()
TVsalon.subirVolumen()
TVsalon.subirVolumen()

# En la TV de la cocina pon el canal 44, silenciala
TVcocina.ponCanal(100)
TVcocina.encender()

# Muestra el estado de las dos TV
TVsalon.muestraInformacion()
TVcocina.muestraInformacion()
