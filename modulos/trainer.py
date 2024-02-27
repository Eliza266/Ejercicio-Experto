import os
def regtrainers(campus:dict):
    print('*****Registro de Trainers*****')
    id=input('Ingrese el ID: ')
    nombre=input('Ingrese el Nombre completo: ')
    os.system('cls')
    
    rutaElegida=[]
    rut=True
    while rut:
        print('*****ASIGNACION DE RUTAS*****')
        for ruta in campus['rutas']:
            print(f'--{ruta}')
        rutaE = input(f'Ingrese el nombre de la ruta que desea asignarle a {nombre}: \n--').lower()
        os.system('cls')

        for areas in campus['areas']:
            print(f'--{areas}')
        area=input('Ingrese el area de Trabajo: \n--').lower()
        os.system('cls')

        
        horabool=True
        while horabool:
            for horario in campus['areas'][area]['horarios']:
                print(f'--{horario}')
            hora=input('Ingrese el horario: \n--')
        
            if campus['areas'][area]['horarios'][hora]=='libre':
                campus['areas'][area]['horarios'][hora]='ocupado'
                trainer={
                    'id':id,
                    'nombre':nombre,
                    'area':area,
                    'horario':hora,
                    'rutas':rutaElegida,
                    'nEstudiantes':0,
                    'estudiantes':{}
                }
                campus['rutas'][rutaE]['trainerAsignado'][id]=trainer
                horabool=False
            else:
                print('Area ocupada en ese horario')

        rut=bool(input('Desea asignarle otra ruta? s(Si) o enter(No)'))
    

    