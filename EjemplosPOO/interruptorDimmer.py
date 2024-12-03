# clase interruptor dimmer

class interruptorDimmer():
    def __init__(self):
        self.interruptorEncendido = False
        self.brillo = 0
        
    def enciende(self):
        self.interruptorEncendido = True

    def apaga(self):
        self.interruptorEncendido = False

    def subirNivel(self):
        if self.brillo < 10:
            self.brillo = self.brillo + 1

    def bajarNivel(self):
        if self.brillo > 0:
            self.brillo = self.brillo - 1

    # Método extra para depuración
    def muestra(self):
        print('¿Interruptor encendido? ', self.interruptorEncendido)
        print('El brillo es: ', self.brillo)


# Código principal
objetoDimmer = interruptorDimmer() 

# Enciende el interruptor y sube el nivel 5 veces
objetoDimmer.enciende()
objetoDimmer.subirNivel()
objetoDimmer.subirNivel()
objetoDimmer.subirNivel()
objetoDimmer.subirNivel()
objetoDimmer.subirNivel()
objetoDimmer.muestra()

# Baja en nivel 2 veces y apagalo
objetoDimmer.bajarNivel()
objetoDimmer.bajarNivel()
objetoDimmer.apaga()
objetoDimmer.muestra()

# Enciende el interruptor y sube el nivel 3 veces
objetoDimmer.enciende()
objetoDimmer.subirNivel()
objetoDimmer.subirNivel()
objetoDimmer.subirNivel()
objetoDimmer.muestra()



