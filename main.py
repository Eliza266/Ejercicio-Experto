import modulos.camperModulo as camp
import modulos.menu as mp
import modulos.menuCamper as mc
import modulos.rutasModulo as rut
import modulos.trainer as tr
import modulos.matriculas as mt
import modulos.menuReportes as mr
import modulos.reportes as r
import json
if __name__=='__main__':

    #los estudiantes y trainers creados manualmente son solo para pruebas, si es de su gusto puede borrarlos 
    listaEe=[]
    campus = {
        'campers': {

            '123':{
                'id':'123',
                'nombre':'Juan',
                'apellidos':'hernandez',
                'direccion':'adhaskdahkj',
                'telefono':'3114562514',
                'estado':'Inscrito'

                },
            '445':{
                'id':'445',
                'nombre':'Lucas',
                'apellidos':'perez',
                'direccion':'adhaskdahkj',
                'telefono':'3114562514',
                'estado':'Aprobado'

                }
                ,
            '115':{
                'id':'115',
                'nombre':'Salomon',
                'apellidos':'perez',
                'direccion':'adhaskdahkj',
                'telefono':'3114562514',
                'estado':'Aprobado'

                }
            
        },
        'rutas': {
            'java':{ 
                'temas':{
                    'fundamentos': {},
                    'web': {},
                    'lengformal': {},
                    'bd': {},
                    'backend': {}
                    },
                'trainerAsignado':{
                    '357':{
                                'id':'357',
                                'nombre':'juan',
                                'area':'apolo',
                                'horario':'6-10',
                                'rutas':'java',
                                'nEstudiantes':1,
                                'estudiantes':{
                                    "445": {
                                        "id": "445",
                                        "nombre": "Lucas",
                                        "ruta": "java",
                                        "trainer": "357",
                                        "ingreso": "46",
                                        "finalizacion": "5453",
                                        "notas": {},
                                        "estado": ""
                                            }
                                }   
                            },
                    '159':{
                                'id':'159',
                                'nombre':'pedro',
                                'area':'artemis',
                                'horario':'10-2',
                                'rutas':'java',
                                'nEstudiantes':0,
                                'estudiantes':{}
                            }
                     }
                    },
            'nodejs': {
                'temas':{
                    'fundamentos': {},
                    'web': {},
                    'lengformal': {},
                    'bd': {},
                    'backend': {}
                    },
                'trainerAsignado':{}
            },
            'netcore': {
                'temas':{
                    'fundamentos': {},
                    'web': {},
                    'lengformal': {},
                    'bd': {},
                    'backend': {}
                    },
                'trainerAsignado':{}
            }
        },
        'areas': {
            'apolo': {
                'nombre': 'apolo',
                'horarios':{
                    '6-10':'ocupado',
                    '10-2':'libre',
                    '2-6':'libre'
                },
                'capacidad': 33
            },
            'artemis': {
                'nombre': 'artemis',
                'horarios':{
                    '6-10':'libre',
                    '10-2':'ocupado',
                    '2-6':'libre'
                },
                'capacidad': 33
            },
            'sputnik': {
                'nombre': 'sputnik',
                'horarios':{
                    '6-10':'libre',
                    '10-2':'libre',
                    '2-6':'libre'
                },
                'capacidad': 33
            }
        },

        }
        
    
    principal=True
    while principal:
        op=mp.crearMenu()
        if (op==1):
            #Modulos Campers
            principalReportes=True
            while principalReportes:
                opR=mc.crearMenuCamper()
                if (opR==1):
                    rcamper=True
                    while rcamper:
                        camp.regCampers(campus)
                        rcamper=bool(input('Ingrese S(si) si desea Agregar otro camper s(Si) o enter(No)'))
                elif (opR==2):
                    camp.registrarPrueba(campus)
                elif (opR==3):
                    camp.agregarNotas(campus)
                elif (opR==4):
                    principalReportes=False
            
        elif (op==2):
            stack=True
            while stack:
                rut.addRutas(campus)
                stack=bool(input('Ingrese S(si) si desea Editar otra Ruta s(Si) o enter(No)'))
            
        elif (op==3):
            rTrainer=True
            while rTrainer:
                tr.regtrainers(campus)
                rTrainer=bool(input('Ingrese S(si) si desea registrar otro Trainer s(Si) o enter(No)'))
            
        elif (op==4):
             mt.matriculas(campus)
        elif (op==5):
            #modulos Reportes
            listaEe = r.lista(campus)
            principalReportes=True
            while principalReportes:
                opR=mr.crearMenuReportes()
                if (opR==1):
                    r.CampersInscritos(campus)
                elif (opR==2):
                    r.CampersAprobados(campus)
                elif (opR==3):
                    r.MostrarTrainers(campus)
                elif (opR==4):
                   pass
                elif (opR==5):
                   r.mostrarTabla(listaEe)
                elif (opR==6):
                   pass
                elif (opR==7):
                   principalReportes=False
        elif (op==6):
            principal=False
    
    
    
    print(json.dumps(campus, indent=4))


