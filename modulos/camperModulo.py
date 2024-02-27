def regCampers(campus:dict):
    print('Registro de Estudiantes: ')
    id=input('Ingrese el ID: ')
    nombre=input('Ingrese el Nombre: ')
    apellidos=input('Ingrese los Apellidos: ')
    direccion=input('Ingrese la direccion:')
    telefono=input('Ingrese el numero de telefono: ')
    estado='Inscrito'
    camper={
        'id':id,
        'nombre':nombre,
        'apellidos':apellidos,
        'direccion:':direccion,
        'tele':telefono,
        'estado':estado,
        'acudientes':{

        }
    }
    campus['campers'][id]=camper
    print('Agregar acudientes: ')
    agreAcudient=bool(input('Desea agregar un acudiente? s(si) enter(No)'))
    if agreAcudient==True:
        adAcudiente=True
        while adAcudiente:
            idAcudiente=input('Ingrese el id: ')
            nombreAcu=input('Ingrese el nombre del acudiente: ')
            telAcudiente=input('Ingrese el numero de telefono del acudiente: ')
            
            acudiente={
                'id':idAcudiente,
                'nombre':nombreAcu,
                'telefono:': telAcudiente
                }
            camper['acudientes'][idAcudiente]=acudiente
            adAcudiente=bool(input('Desea agregar otro acudiente? s(Si) o enter(No)'))
    
def registrarPrueba(campus:dict):
   
    for id, camper in campus['campers'].items():
        print(f"ID: {id}:{camper['nombre']} {camper['apellidos']}, Estado: {camper['estado']}")
    camperPrueba=input('ingrese el id del estudiante que va a realizar la Prueba: ').lower()
    notaTeo=float(input(f'Ingrese la nota teorica: '))
    notaPrac=float(input('Ingrese la nota Practica: '))
    promedio= (notaTeo+notaPrac)/2
    if promedio>= 60:
        campus['campers'][camperPrueba]['estado']='Aprobado'

#notas----------------
def calcularNotaFinal(teorica, practica, quices):
    # Ponderaciones
    pesoTeorica = 0.3
    pesoPractica = 0.6
    pesoQuices = 0.1

    # Calcular notas ponderadas
    notaTeorica = sum(teorica.values()) / len(teorica) if teorica else 0
    notaPractica = sum(practica.values()) / len(practica) if practica else 0
    notaQuices = sum(quices.values()) / len(quices) if quices else 0

    # Calcular nota final
    notaFinal = (notaTeorica * pesoTeorica) + (notaPractica * pesoPractica) + (notaQuices * pesoQuices)
    return notaFinal

def agregarNotas(campus):
    for ruta in campus['rutas']:
        print(ruta)

    rutaElegida = input('Ingrese la ruta para agregar las notas a los campers correspondientes: ')
    entrenadoresRuta = campus['rutas'].get(rutaElegida, {}).get('trainerAsignado', {})

    for idEntrenador, infoEntrenador in entrenadoresRuta.items():
        print(f"\nEntrenador ID: {idEntrenador} - {infoEntrenador['nombre']}")

        estudiantes = infoEntrenador.get('estudiantes', {})
        for idEstudiante, valorEstudiante in estudiantes.items():
            print(f"  Estudiante ID: {idEstudiante} - {valorEstudiante['nombre']}")
            
            # Solicitar al usuario ingresar el ID del estudiante
            idEstudiante = input('Ingrese el ID del estudiante para agregar notas por módulo: ')
            
            # Verificar si el ID del estudiante es válido
            if idEstudiante in estudiantes:
                # Verificar si la clave 'notas' ya existe, si no, crearla
                if 'notas' not in valorEstudiante:
                    valorEstudiante['notas'] = {}
                
                notasModulos = {}
                for modulo, _ in campus['rutas'][rutaElegida]['temas'].items():
                    notaTeorica = float(input(f'Ingrese la nota Teórica para el módulo {modulo}: '))
                    notaPractica = float(input(f'Ingrese la nota Práctica para el módulo {modulo}: '))
                    notaQuices = float(input(f'Ingrese la nota de los Quices para el módulo {modulo}: '))
                    
                    # Calcular nota final para cada módulo
                    notaFinalModulo = calcularNotaFinal({'teorica': notaTeorica}, {'practica': notaPractica}, {'quices': notaQuices})
                    notasModulos[modulo] = {'teorica': notaTeorica, 'practica': notaPractica, 'quices': notaQuices, 'notaFinal': notaFinalModulo}
                
                # Agregar las notas por módulo al estudiante
                valorEstudiante['notas'][rutaElegida] = notasModulos
                
                # Actualizar estado del estudiante a 'riesgoBajo' si es necesario
                notaFinalGlobal = calcularNotaFinal(notasModulos, {}, {})
                if notaFinalGlobal < 60:
                    campus['rutas'][rutaElegida]['trainerAsignado'][idEntrenador]['estudiantes'][idEstudiante]['estado'] = 'riesgoBajo'
            else:
                print('ID de estudiante no válido. Por favor, ingrese un ID existente.')

