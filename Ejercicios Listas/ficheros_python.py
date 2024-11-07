import os
ejercicios_listas = [f for f in os.listdir('.') if f.endswith('.py') and f.startswith('l')]
print(ejercicios_listas)
