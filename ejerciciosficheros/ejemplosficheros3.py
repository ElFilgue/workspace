f= open('ficheros/aeropuertos.dat','a')
canary_iata = ('CDT', 'VLC', 'ORL')

for code in canary_iata:
    f.write(code + '\n')

f.close()