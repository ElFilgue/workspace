def segundos_a_hms(segundos):
    horas = segundos // 3600
    minutos = segundos // 60
    segundos_restantes = segundos % 60
def hms_a_segundos(horas,minutos,segundos):
    return (horas*3600) + (minutos * 60) + segundos

