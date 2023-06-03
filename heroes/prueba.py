from data_stark import lista_personajes

for hero in lista_personajes:
    lista = []
    if hero['inteligencia'] == "":
        hero['inteligencia'] = "no tiene"
    lista.append(hero['inteligencia'])
    print(lista)