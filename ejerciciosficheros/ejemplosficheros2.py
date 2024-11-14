f= open('ficheros/aeropuertos.dat','w')
canary_iata = ('TFN', 'TFS', 'LPA', 'GMZ', 'VDE', 'SPC', 'ACE', 'FUE')

for code in canary_iata:
    f.write(code + '\n')

f.close()