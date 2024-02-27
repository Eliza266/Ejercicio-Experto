import os
from tabulate import tabulate
def CampersInscritos(campus):
    for key, valor in campus['campers'].items():
        if valor['estado'] == 'Inscrito':
            print(f"ID: {key} - {valor['nombre']} {valor['apellidos']} - Estado: {valor['estado']}")
    os.system('pause')
    os.system('clr')

def CampersAprobados(campus):
    for key, valor in campus['campers'].items():
        if valor['estado'] == 'Aprobado':
            print(f"ID: {key} - {valor['nombre']} {valor['apellidos']} - Estado: {valor['estado']}")
    os.system('pause')
    os.system('clr')
def MostrarTrainers(campus):
    print("Entrenadores en el campus:")
    for ruta, infoRuta in campus['rutas'].items():
        trainerAsignado = infoRuta.get('trainerAsignado', {})
        for idEntrenador, infoEntrenador in trainerAsignado.items():
            print(f"ID: {idEntrenador}, Nombre: {infoEntrenador['nombre']}, Área: {infoEntrenador['area']}, Horario: {infoEntrenador['horario']}, Ruta: {infoEntrenador['rutas']}, Número de Estudiantes: {infoEntrenador['nEstudiantes']}")
            # Puedes agregar más información según sea necesario


def lista(campus):
    listaEe = []
    
    for ruta, infoRuta in campus['rutas'].items():
        trainerAsignado = infoRuta.get('trainerAsignado', {})
        
        for idEntrenador, infoEntrenador in trainerAsignado.items():
            entrenadorInfo = {
                'ruta': ruta,
                'idTrainer': idEntrenador,
                'nombreTrainer': infoEntrenador['nombre'],
                'estudiantes': []
            }
            
            estudiantes = infoEntrenador.get('estudiantes', {})
            
            for idEstudiante, infoEstudiante in estudiantes.items():
                estudianteInfo = {
                    'idEstudiante': idEstudiante,
                    'nombreEstudiante': infoEstudiante['nombre'],
                    'estado': infoEstudiante['estado']
                }
                entrenadorInfo['estudiantes'].append(estudianteInfo)
            
            listaEe.append(entrenadorInfo)
    
    return listaEe

def mostrarTabla(listaEe):
    for item in listaEe:
        print(f"\nRuta: {item['ruta']}")
        print(f"ID Trainer: {item['idTrainer']}, Nombre Trainer: {item['nombreTrainer']}")
        print("Estudiantes:")
        
        if not item['estudiantes']:
            print("   No hay estudiantes asignados.")
        else:
            tablaEstudiantes = []
            for estudianteInfo in item['estudiantes']:
                tablaEstudiantes.append([estudianteInfo['idEstudiante'], estudianteInfo['nombreEstudiante'], estudianteInfo['estado']])
            
            headers = ["ID Estudiante", "Nombre Estudiante", "Estado"]
            print(tabulate(tablaEstudiantes, headers=headers, tablefmt="grid"))





