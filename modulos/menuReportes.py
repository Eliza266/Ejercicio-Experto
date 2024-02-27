import os
def crearMenuReportes():
    titulo= """
        ++++++++++++++++++++++++
        +       REPORTES       +
        ++++++++++++++++++++++++
        """
    print(titulo)
    listMenu=[1,2,3,4,5,6,7]

    try:
        print(" 1.Campers Inscritos \n 2.Campers Aprobados\n 3.Lista de Entrenadores\n 4.Estudiantes con Bajo Rendimiento \n5.Relacion Campers Ruta y Trainer \n 6.Campers que perdieron\n 7. Salir ")
        1. 
        opR=int(input('--'))

        if (opR not in listMenu):
            os.system('cls')
            crearMenuReportes()

    except:
        os.system('pause')
        crearMenuReportes()
        
    else:
        return opR