import os
def crearMenu():
    titulo= """
        ++++++++++++++++++++++++
        +       CAMPUS         +
        ++++++++++++++++++++++++
        """
    print(titulo)
    listMenu=[1,2,3,4,5,6]

    try:
        print(" 1.Campers \n 2.Agregar stack de rutas\n 3.Registro de Trainers\n 4.Matriculas \n 5.Reportes\n 6.Salir")
        1. 
        op=int(input('--'))

        if (op not in listMenu):
            os.system('cls')
            crearMenu()

    except:
        os.system('pause')
        crearMenu()
        
    else:
        return op