import ply.lex as lex
import ply.yacc as yacc
import re

# Tokens
tokens = ('AGREGA_RAMO','EXIMICION','AGREGA_NOTA','PASAR_RAMO','PROMEDIO','RAMO', 'NUMERO', 'ELIMINA_RAMO', 'VER_RAMOS')

# Definición de Tokens
t_NUMERO = r'\d+(\.\d*)?'
t_RAMO = r'[a-zA-Z_][a-zA-Z0-9_]*'

# Caracteres ignorados
t_ignore = ' \t\n'

#Lexer rules
def t_AGREGA_RAMO(t):
    r'agrega_ramo'
    return t

def t_AGREGA_NOTA(t):
    r'agrega_nota'
    return t

def t_EXIMICION(t):
    r'eximicion'
    return t

def t_PROMEDIO(t):
    r'promedio'
    return t
def t_PASAR_RAMO(t):
    r'pasar_ramo'
    return t

def t_ELIMINA_RAMO(t):
    r'elimina_ramo'
    return t

def t_VER_RAMOS(t):
    r'ver_ramos'
    return t


# def t_RAMO(t):
#     r'[a-zA-Z_][a-zA-Z0-9_]*'
#     t.type = 'RAMO'
#     t.value = t.value.lower() 
#     return t

def t_error(t):
    print(">:C")
    t.lexer.skip(1)



# Parser rules
def p_agregar_ramo(t):
    'command : AGREGA_RAMO RAMO'
    agregar_ramo(t[2])

def p_agregar_nota(t):
    'command : AGREGA_NOTA RAMO NUMERO NUMERO'
    try:
        agregar_nota(t[2], t[3], t[4])
    except LookupError:
        print("Agregue ramos primero!")

def p_calcular_eximicion(t):
    'command : EXIMICION RAMO NUMERO NUMERO'
    try:
        calcular_eximicion(t[2], t[3], t[4])
    except LookupError:
        print("Tiene que realizar otras acciones primero!")


def p_pasar_ramo(t):
    'command : PASAR_RAMO RAMO NUMERO'
    try:
        pasar_ramo(t[2], t[3])
    except LookupError:
        print("Tiene que realizar otras acciones primero!")

def p_calcular_promedio(t):
    'command : PROMEDIO RAMO'
    try:
        calcular_promedio(t[2])
    except LookupError:
        print("Tiene que realizar otras acciones primero!")
    

def p_eliminar_ramo(t):
    'command : ELIMINA_RAMO RAMO'
    eliminar_ramo(t[2])

def p_ver_ramos(t):
    'command : VER_RAMOS'
    ver_ramos()


def p_error(t):
    print(t)
    print(":'(")

ramos = {}

# Función para agregar un ramo a la base de datos
def agregar_ramo(ramo):
    ramos[ramo] = []
    print(f'El ramo {ramo} fue agregado exitosamente')

# Función para agregar una nota a un ramo
def agregar_nota(ramo, nota, porcentaje):
    ramos[ramo].append((float(nota), int(porcentaje)))
    print(f'La nota {nota} fue agregada exitosamente')

# Función para calcular el promedio del ramo
def calcular_promedio(ramo, retornar = False):
    notas = ramos[ramo]
    nota_ponderada_total = sum(nota[0] * nota[1] for nota in notas)
    peso_total = sum(nota[1] for nota in notas)
    promedio = nota_ponderada_total / peso_total
    if retornar == True:
        return promedio
    print(f"Promedio del ramo {ramo}: {promedio:.02f}")


# Función para calcular la nota requerida para eximirse
def calcular_eximicion(ramo, porcentaje, eximicion):
    promedio = calcular_promedio(ramo,True)
    nota_requerida = (float(eximicion) - float(promedio)*(1-(int(porcentaje)/100)))/(int(porcentaje)/100)


    if nota_requerida is None:
        print("Notas insuficientes para calcular la nota requerida para eximirse.")
    elif nota_requerida<=1:
        print("Felicidades, ya aprobaste el ramo!")
    elif nota_requerida >= 7:
        print("Esta complicada la cosa...")
    else:
        print(f"Nota minima requerida para eximirse en {ramo}: {nota_requerida:.02f}")

# Función para calcular la nota requerida para pasar el ramo
def pasar_ramo(ramo, porcentaje):
    calcular_eximicion(ramo,porcentaje,4)


# Función para eliminar un ramo
def eliminar_ramo(ramo):
    if ramo in ramos:
        ramos.pop(ramo)
        print(f'El ramo {ramo} se ha eliminado con exito')
    else:
        print(f'No se ha encontrado el ramo {ramo}')

# Funcion para ver todos los ramos agregados
def ver_ramos():
    for ramo in ramos.keys():
        print(f'--{ramo}')
 
"""
Entradas de prueba (ocupar solo minusculas)

AGREGA_RAMO Calculo
AGREGA_NOTA Calculo 4.5 30
AGREGA_NOTA Calculo 5.0 50
AGREGA_NOTA Calculo 3.5 20
EXIMICION Calculo 60 eximicion
PASAR_RAMO Calculo 70
PROMEDIO Calculo
"""
lexer=lex.lex()
parser=yacc.yacc()
while True:
    try:
        data = input()
    except EOFError:
        break
    parser.parse(data)
