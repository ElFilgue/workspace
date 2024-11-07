#programa de ejemplo de doble bucle for

saludos = ['hola', 'saludos', 'hi']
nombres = ['j2logo', 'antonio', 'vega']
frases = ['{} {}'.format(saludo.title(), nombre.title()) for saludo in saludos for nombre in nombres]
print(frases)