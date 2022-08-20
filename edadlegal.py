edad=int(input('Digite su es edad '))

if(edad >=0 and edad <=14):
    print(f'La persona con la edad de {edad} es niño')
elif(edad >=15 and edad <28):
    print(f'La persona con la edad de {edad} es joven') 
elif(edad >=28 and edad <60):
    print(f'La persona con la edad de {edad} es adulto')
elif(edad >=60 or edad<150):
    print(f'La persona con la edad de {edad} es Adulto mayor')  
elif(edad<150):
    print(f'La persona con la edad de {edad} esta  Extinto')

else:
    print('edad no admitida')               