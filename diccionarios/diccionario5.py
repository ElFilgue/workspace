diccionario = {
 'Matemáticas': 7,
 'Física': 8,
 'Historia': 9
}
minimo=10
for asignatura,nota in diccionario.items():
    if nota>minimo:
        asignatura_min= asignatura
print(f"la clave con valor mas bajo es:{asignatura_min}")
