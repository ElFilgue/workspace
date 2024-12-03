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
interruptor1 = interruptor()  # crea el objeto interruptor1
interruptor2 = interruptor()  # crea el objeto interruptor2

# Llamadas a métodos
interruptor1.muestra() # llamada al método muestra de interruptor1
interruptor1.enciende() # llamada al método enciende de interruptor1
interruptor1.muestra()
interruptor1.apaga() # llamada al método apaga de interruptor1

interruptor2.muestra() # llamada al método muestra de interruptor2
interruptor2.enciende() # llamada al método enciende de interruptor2
interruptor2.muestra()
interruptor2.apaga() # llamada al método apaga de interruptor2
