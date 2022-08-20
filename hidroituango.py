#Entradas del problema

nivelAgua=int(input('Cual es el nivel del agua: '))

#Proceso del problema

if(nivelAgua >=0 and nivelAgua <20):
    print(f'Alerta de nivel bajo {nivelAgua} apagar motores')
elif(nivelAgua>=20 and nivelAgua<400):
    print(f'El nivel de agua  {nivelAgua} es optimo')
elif(nivelAgua>=400):
    print(f'Nivel de agua supera medida {nivelAgua} Alerta')
else:
    print('Entrada de niveles no permitidas')        
