mes=None
mes=input('Digite el mes')

if(mes=='enero' or mes=='febrero' or mes=='marzo'):
    print(f'El mes {mes} temporada de invierno')
elif(mes=='abril' or mes=='mayo' or mes=='junio'):
    print(f'El mes {mes} temporada de primavera')
elif(mes=='julio' or mes=='agosto' or mes=='septiembre'):
    print(f'El mes {mes} temporada de verano') 
elif(mes=='octubre' or mes=='noviembre' or mes=='diciembre'):
    print(f'El mes {mes} temporada de otoño')
else:
    print('mes no existe')           
