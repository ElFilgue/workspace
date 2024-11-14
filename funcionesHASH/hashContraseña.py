import hashlib

# Contraseña original
contraseña_original = "Adivinanza"

# Crea un objeto hash utilizando SHA256
objeto_hash = hashlib.sha256()

# Agrega la contraseña al objeto hash
objeto_hash.update(contraseña_original.encode('utf-8'))

# Obtiene la versión encriptada (hasheada) de la contraseña
contraseña_hasheada = objeto_hash.hexdigest()

print (f"Contrasña original: {contraseña_original}")
print (f"Contrasña hasheada: {contraseña_hasheada}")

# Pêdimos al usuario que introduzca una contraseña
contraseña_usuario = input("Introduce la contraseña: ")

# crea un nuevo objeto hash
objeto2_hash = hashlib.sha256()

# Agrega la contraseña del usuario al objeto2_hash
objeto2_hash.update(contraseña_usuario.encode('utf-8'))

# Compara ambas contraseñas:
if objeto2_hash.hexdigest() == contraseña_hasheada:
    print("Las contraseñas coinciden")
else:
    print("Las contraseñas NO coinciden")

