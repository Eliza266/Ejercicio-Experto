import os

def matriculas(campus: dict):
    for key, valor in campus['campers'].items():
        if valor['estado'] == 'Aprobado':
            print(f"ID: {key} - {valor['nombre']} {valor['apellidos']} - Estado: {valor['estado']}")

    idcamper = input('Ingrese el Id del estudiante que desea matricular: ')
    os.system('cls')  # o 'clear' en sistemas UNIX
    camper = campus['campers'].get(idcamper)

    if camper is not None and camper['estado'] == 'Aprobado':
        print(f"Matriculando a {camper['nombre']} {camper['apellidos']} en una ruta.")

        for ruta in campus['rutas']:
            print(f'--{ruta}')

        rutaElegida = input(f'Ingrese la Ruta que desea asignarle a {camper["nombre"]}: ')
        os.system('cls')

        print('TRAINERS DISPONIBLES PARA LA RUTA ASIGNADA')
        trainers_disponibles = campus['rutas'].get(rutaElegida, {}).get('trainerAsignado', {})

        if trainers_disponibles:
            for id_trainer, info_trainer in trainers_disponibles.items():
                print(f"ID: {id_trainer} - {info_trainer['nombre']}")

            id_trainer_asignado = input('Ingrese el id del Trainer a asignar: ')
            fecha_inicio = input('Ingrese la fecha de inicio: ')
            fecha_finalizacion = input('Ingrese la fecha de finalización de la ruta: ')

            nuevaMatricula = {
                'id': idcamper,
                'nombre': camper['nombre'],
                'ruta': rutaElegida,
                'trainer': id_trainer_asignado,
                'ingreso': fecha_inicio,
                'finalizacion': fecha_finalizacion,
                'notas': {},
                'estado': ''
            }

            campus['rutas'][rutaElegida]['trainerAsignado'][id_trainer_asignado]['estudiantes'][idcamper] = nuevaMatricula
            campus['rutas'][rutaElegida]['trainerAsignado'][id_trainer_asignado]['nEstudiantes'] += 1

            print(f"Matrícula exitosa para {camper['nombre']} en la ruta {rutaElegida}.")
        else:
            print(f"No hay trainers disponibles para la ruta {rutaElegida}.")
    else:
        print(f"El estudiante con ID {idcamper} no está aprobado o no existe.")

