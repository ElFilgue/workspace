# Interruptor Orientado a Objetos

class interruptor():
    def __init__(self):
        self.interruptorEncendido = False

    def enciende(self):
        # enciende la luz 
         self.interruptorEncendido = True

    def apaga(self):
        # apaga la luz
         self.interruptorEncendido = False

    def muestra(self):  # añadido para pruebas
        print(self.interruptorEncendido)
    
# Código principal
objetoInterruptor = interruptor()  # crea el objeto interruptor

#  Calls to methods
objetoInterruptor.muestra() # call the muestra method of objetoInterruptor
objetoInterruptor.enciende() # call the enciende method of objetoInterruptor
objetoInterruptor.muestra()
objetoInterruptor.apaga() # call the apaga method of objetoInterruptor
objetoInterruptor.muestra()
objetoInterruptor.enciende() # call the enciende method of objetoInterruptor
objetoInterruptor.muestra()
