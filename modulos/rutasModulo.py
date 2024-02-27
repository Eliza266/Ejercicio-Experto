def addRutas(campus: dict):
    print('*******RUTAS*******\n')
    for ruta in campus['rutas']:
        print(f'--{ruta}')
    rutaE = input('Ingrese el nombre de la ruta: \n--').lower()

    for ruta, subclaves in campus['rutas'][rutaE]['temas'].items():
        print(ruta)
    selec = input('Ingrese el nombre del Modulo al que desea agregarle el stack : \n--').lower()
    stack = input('Ingrese el Stack: ')
    myStack = {
        
        'id': str(len(campus['rutas'][rutaE]['temas'][selec]) + 1).zfill(2),
        'nombre': stack
    }

    campus['rutas'][rutaE]['temas'][selec][myStack['id']] = myStack
    print(f"Diccionario actualizado para {rutaE}/{selec}:\n{campus['rutas'][rutaE][selec]}")


        