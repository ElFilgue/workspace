# Interruptor Procedimental

def enciende():
    global interruptorPulsado
    # enciende la luz 
    interruptorPulsado = True

def apaga():
    global interruptorPulsado
    # apaga la luz
    interruptorPulsado = False
    
# Código Principal
interruptorPulsado = False     # una variable booleana global

# Código de prueba
print(interruptorPulsado)
enciende()
print(interruptorPulsado)
apaga()
print(interruptorPulsado)
enciende()
print(interruptorPulsado)

