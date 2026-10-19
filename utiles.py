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