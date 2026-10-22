import csv
def pedir_numero():
    comprobar=1
    while comprobar==1:
        try:
            resultado=int(input("Introduce un numero: "))
            return resultado
            
        except ValueError:
            print("Ha ocurrido un error introduce un numero")
            continue
#hay que hacer una funcion que escriba automaticamente en csv usando lo de la relacion 9 ej 4
def dar_alta(clientes):
    nombre=input("Introduce el nombre ")
    email=input("Introduce el email ")
    ciudad=input("Introduce el ciudad ")
    activo=input("Introduce el activo ")
    clientes.append({
        "nombre": nombre,
        "email": email,
        "ciudad": ciudad,
        "activo": activo,
    })
    def busqueda_por_texto(clientes):
        busqueda=input("Pon el nombre del cliente: ").strip().lower()
        encontrado=0
        for cliente in clientes:
            if busqueda in cliente["nombre"].lower():
                print("EL cliente esta en los archivos: ")
                encontrado=1
        if encontrado==0:
            print("no encontrado")



def desactivacion(clientes):
    busqueda=input("Pon el nombre del cliente: ").strip().lower()
    for cliente in clientes:
        if busqueda in cliente["nombre"].lower():
            print("EL cliente ha sido borrado: ")
            clientes.remove(cliente)
            encontrado=1
        if encontrado==0:
            print("no encontrado")
    


def listado(clientes):
    if clientes!=[]:
        for clave in clientes:
            print(f"El cliente {clave['nombre']} tiene de email {clave['email']} y es de la ciudad {clave['ciudad']} y está {clave['activo']}")
            
    else:
        print("No hay clientes registrados")

def guardado(clientes,Ruta):
    with open(Ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(
            archivo, fieldnames=["nombre", "email", "ciudad", "activo"])
        escritor.writeheader()
        escritor.writerows(clientes)
    return len(clientes)


def carga(Ruta):
    lista=[]
    with open(Ruta, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            lista.append({#cambiar segun lo que se pida al final esta parte es una plantilla
                "nombre": fila["nombre"],
                "email": fila["email"],
                "ciudad": fila["ciudad"],
                "activo": fila["activo"].strip().lower() == "true",
            })
    
        print("archivo leido correctamente")
    return lista