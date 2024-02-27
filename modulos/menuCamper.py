import os
def crearMenuCamper():
    titulo= """
        ++++++++++++++++++++++++++++++++
        +       CAMPUS MENU CAMPERS    +
        ++++++++++++++++++++++++++++++++
        """
    print(titulo)
    listMenu=[1,2,3,4]

    try:
        print(" 1.Registrar Camper\n 2.Registrar Prueba de Ingreso\n 3.Agregar NOtas \n 4.Salir")
        1. 
        opC=int(input('--'))

        if (opC not in listMenu):
            os.system('cls')
            crearMenuCamper()

    except:
        os.system('pause')
        crearMenuCamper()
        
    else:
        return opC