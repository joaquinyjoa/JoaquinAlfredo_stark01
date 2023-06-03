from funciones import *

primer_menu = menu()
x = resultado(primer_menu)

if x == 8:
    segundo_menu = menu_01()
    y = resultado_01(segundo_menu)

os.system("pause")