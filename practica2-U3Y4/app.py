from clases import *
from datetime import *
from funciones import *

while True:
    opcion = int(input("""-------MENU PRINCIPAL-------
            1. Ingresar Estadía
            2. Finalizar Estadía\n"""))
    if opcion == 1:
        ingresar_estadia()
    elif opcion == 2:
        patente = str(input("""------FINALIZAR ESTADÍA-------
            Ingrese la patente del vehículo: """))
        
        for estadia in Estadia.vehiculos_estadia:
            if estadia.get_nro_patente == patente and estadia.get_estado == "ACTIVO":
                # Calcular la cantidad de horas de la estadía
                importe = Precio.calcular_importe(2)

                print(f"Importe a abonar: ${importe:.2f}")
                confirmacion = int(input("¿Desea confirmar el pago? \n1. Sí\n 2. No: "))
                if confirmacion == 1:
                    estadia.set_estado = "PAGADO"
                    estadia.set_hora_salida = datetime.now()
                    print("Estadía finalizada y actualizada.")
                else:
                    print("Operación cancelada.")
                break
        else:
            print("No se encontró una estadía activa para la patente ingresada.")
    
    
