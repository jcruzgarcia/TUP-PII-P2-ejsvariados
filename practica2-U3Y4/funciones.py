from clases import *

def ingresar_estadia():
    patente = str(input("""------INGRESAR ESTADÍA-------
                    Ingrese la patente del vehículo: """))
    if patente in Estadia.vehiculos_estadia:
            print("La patente ya se encuentra registrada")
    else:
        estadia = Estadia(datetime.today(), patente, datetime.now(), None, None, "ACTIVO", False)
        Estadia.vehiculos_estadia.append(estadia)
        print("Patente registrada con éxito.")
        print(estadia)
        
def finalizar_estadia():
    pass