# clase TV con código de prueba

class TV():
    def __init__(self):
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
        print('Estado de la TV:')
        if self.encendida:
            print('    La TV está: Encendida')
            print('    El canal es:', self.listaCanales[self.indiceCanales])
            if self.silenciada:
                print('    El volumen es:', self.volumen, '(el sonido está silenciado)')
            else:
                print('    El volumen es:', self.volumen)
        else:
            print('    La TV está: Apagada')


# Códifo principal
objetoTV = TV()  # crea el objeto TV

# Enciende la TV y muestra el estado
objetoTV.encender()
objetoTV.muestraInformacion()

# Sube el canal 2 veces, sube el volumen 2 veces, muestra el estado
objetoTV.subirCanal()
objetoTV.subirCanal()
objetoTV.subirVolumen()
objetoTV.subirVolumen()
objetoTV.muestraInformacion()

# Apaga la TV, muestra el estado, enciende la TV, muestra el estado
objetoTV.encender()
objetoTV.muestraInformacion()
objetoTV.encender()
objetoTV.muestraInformacion()

# Baja el volumen, silencia el sonido, muestra el estado
objetoTV.bajarVolumen()
objetoTV.silenciar()
objetoTV.muestraInformacion()

# cambia al canal 11, activa el sonido, muestra el estado
objetoTV.ponCanal(11)
objetoTV.silenciar()
objetoTV.muestraInformacion()
