from data_stark import lista_personajes
import os


def menu()-> int:
    os.system("cls")
    print("""
                        ***MENU 00 STARK*** 
            1. nombre de cada superhéroe
            2. nombre de cada superhéroe junto a altura del mismo
            3. el superhéroe más alto (MÁXIMO)
            4. el superhéroe más bajo (MÍNIMO)
            5. la altura promedio de los superhéroes (PROMEDIO)
            6. el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
            7. Calcular e informar cual es el superhéroe más y menos pesado.
            8. MENU 01
            9. SALIR    
          """)

    try:
        seleccion = int(input("seleccione uno de estos numeros: "))

    except ValueError:
        print("debes seleccionar un numero")
    else:
        while (seleccion <= 0 or seleccion >= 11):
            print(int(input("elige un numero entre 1 y 10: ")))

        return seleccion


def resultado(selec)->None:
    match(selec):
        case 1:
            a = nombres
            print(a)
        case 2:
            print(nombres_altruas)
        case 3:
            print(altura_max)
        case 4:
            print(altura_min)
        case 5:
            print(promedio_alturas)
        case 6:
            print(max_min)
        case 7:
            print(peso_max_min)
        case 9:
            salida = input("Desea salir? s/n: ")
            while salida == "s" or salida == "n":
                break

    return selec

def nombres_suepr(lista: list, key: str):
    list_nombres = []
    for heroe in lista:
        list_nombres.append(heroe[key])

    return list_nombres


def heroes_altura(lista: list, nombre: str, altura: str) -> list:
    agrupacion = []

    for hero in lista:
        agrupacion.append(([hero[nombre]],[float(hero[altura])]))
        
    return agrupacion


def hero_max(lista: list, nombre: str, altura: str):
    name_max = None
    flag_max = True
    for hero in lista:
        if flag_max or altura_max < float(hero[altura]):
            altura_max = float(hero[altura])
            name_max = hero[nombre]
            flag_max = False

    return name_max, altura_max


def hero_min(lista: list, nombre: str, altura: str):
    name_min = None
    flag_min = True
    for hero in lista:
        if flag_min or altura_min > float(hero[altura]):
            altura_min = float(hero[altura])
            name_min = hero[nombre]
            flag_min = False

    return name_min, altura_min


def hero_promedio(lista: list, altura: str):
    acumulador = 0
    contador = 0
    for hero in lista:
        acumulador += float(hero[altura])
        contador += 1

    promedio = acumulador / contador

    return promedio


def hero_peso(lista: list, nombre: str, peso: str,):
    name_max = None
    flag_max = True
    
    name_min = None
    flag_min = True

    for hero in lista:
        if flag_max or float(hero[peso]) > peso_max:
            peso_max = float(hero[peso])
            name_max = hero[nombre]
            flag_max = False

    for hero in lista:
        if flag_min or float(hero[peso]) < peso_min:
            peso_min = float(hero[peso])
            name_min = hero[nombre]
            flag_min = False

    return name_min, peso_min, name_max, peso_max

nombres = nombres_suepr(lista_personajes,"nombre")
nombres_altruas = heroes_altura(lista_personajes, "nombre", "altura")
altura_max = hero_max(lista_personajes, "nombre", "altura")
altura_min = hero_min(lista_personajes, "nombre", "altura")
promedio_alturas = hero_promedio(lista_personajes, "altura")
max_min = altura_max, altura_min
peso_max_min = hero_peso(lista_personajes, "nombre", "peso")
# ---------------------------------------------------------------------------------------------

def menu_01()-> int:
    print("""
                                    *** MENU 01 *** 
            1. el nombre de cada superhéroe de género M
            2. el nombre de cada superhéroe de género F
            3. el superhéroe más alto de género M
            4. el superhéroe más alto de género F
            5. el superhéroe más bajo de género M
            6. el superhéroe más bajo de género F
            7. la altura promedio de los superhéroes de género M
            8. la altura promedio de los superhéroes de género F
            9. el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems 3 al 6)
            10. cuántos superhéroes tienen cada tipo de color de ojos.
            11. cuántos superhéroes tienen cada tipo de color de pelo.
            12. cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, ‘No Tiene’).
            13. todos los superhéroes agrupados por color de ojos.
            14. todos los superhéroes agrupados por color de pelo.
            15. todos los superhéroes agrupados por tipo de inteligencia
        """)
    try:
        seleccion_01 = int(input("seleccione uno de estos numeros: "))
    except ValueError:
        print("debes seleccionar un numero")
    else:
        while (seleccion_01 <= 0 or seleccion_01 >= 16):
            print(int(input("elige un numero entre 1 y 10: ")))

        return seleccion_01


def resultado_01(seleccion_01):
    match(seleccion_01):
        case 1:
            print(nombres_M)
        case 2:
            print(nombres_F)
        case 3:
            print(altura_max_M)
        case 4:
            print(altura_max_F)
        case 5:
            print(altura_min_M)
        case 6:
            print(altura_min_F)
        case 7:
            print(promedio_M)
        case 8:
            print(promedio_F)
        case 9:
            print(asociacion)
        case 10:
            print(color_ojos)
        case 11:
            print(color_pelo)
        case 12:
            print(inteligencia)
        case 13:
            print(hero_ojos)
        case 14:
            print(hero_pelo)
        case 15:
            print(hero_inteligencia)

    return seleccion_01


def filtro_hero(lista: list, nombre: str, key: str, value: str):
    nombres = []
    for hero in lista:
        if hero[key] == value:
            nombres.append(hero[nombre])
    return nombres


def filtro_altura_max(lista: list, nombre: str, altura: str, key: str, value: str)->list:
    nombre_max = None
    flag_max = True
    for hero in lista:
        if flag_max or altura_max > float(hero[altura]) and hero[key] == value:
            nombre_max = hero[nombre]
            altura_max = float(hero[altura])
            flag_max = False
    return nombre_max, altura_max

def filtro_altura_min(lista: list, nombre: str, altura: str, key: str, value: str)->list:
    nombre_min = None
    flag_min = True
    for hero in lista:
        if flag_min or altura_min < float(hero[altura]) and hero[key] == value:
            nombre_min = hero[nombre]
            altura_min= float(hero[altura])
            flag_min = False
    return nombre_min, altura_min

def promedio_genero(lista: list, altura: str, key: str, value: str):
    acumulador = 0
    contador = 0
    for hero in lista:
        if hero[key] == value:
            acumulador += float(hero[altura])
            contador += 1
    promedio = acumulador / contador
    return promedio


def tipos(lista: list, key: str):
    agrupacion = []
    
    for hero in lista:
        if hero[key] == "":
            hero[key] = "no tiene"
        esta = False
        
        for valor in agrupacion:
            if hero[key] == valor:
                esta = True
                break
            if hero[key] == "":
                print("no tiene")
                
        if not esta:
            agrupacion.append(hero[key])
    return agrupacion

def hero_tipos(lista: list, key: str, nombre_key:str):
    agrupacion = []
    for hero in lista:
        if hero[key] == "":
            hero[key] = "no tiene"
        esta = False
        for valor in agrupacion:
            if hero[key] == valor:
                esta = True
                break
                
        if not esta:
            agrupacion.append(([hero[key]],[hero[nombre_key]]))
        
    return agrupacion



nombres_M = filtro_hero(lista_personajes, "nombre", "genero", "M")
nombres_F = filtro_hero(lista_personajes, "nombre", "genero", "F")
altura_max_M = filtro_altura_max(lista_personajes, "nombre","altura", "genero", "M")
altura_max_F = filtro_altura_max(lista_personajes, "nombre","altura", "genero", "F")
altura_min_M = filtro_altura_min(lista_personajes, "nombre","altura", "genero", "M")
altura_min_F = filtro_altura_min(lista_personajes, "nombre","altura", "genero", "F")
promedio_M = promedio_genero(lista_personajes, "altura", "genero", "M")
promedio_F = promedio_genero(lista_personajes, "altura", "genero", "F")
asociacion = altura_max_M,altura_max_F,altura_min_M,altura_min_F
color_ojos = tipos(lista_personajes, "color_ojos")
color_pelo = tipos(lista_personajes, "color_pelo")
inteligencia = tipos(lista_personajes, 'inteligencia')
hero_ojos = hero_tipos(lista_personajes, "color_ojos","nombre")
hero_pelo =hero_tipos(lista_personajes, "color_pelo","nombre")
hero_inteligencia = hero_tipos(lista_personajes, "inteligencia","nombre")

#--------------------------------------------------------------------------------------------------------