# Proyecto_Salvaramos_AyC
Nuestro proyecto: Creamos un interprete para ayudar estudiantes a calcular sus promedios y posibilidades de eximicion en sus diferentes ramos.


Funciones/comandos: Lo primero seria agregar un ramo, esto se utiliza [agrega_ramo {RAMO}] , RAMO siendo la materia a agregar.
Luego se agregan notas junto con sus coeficientes con el formato [agrega_nota {RAMO} {NOTA} {PORCENTAJE}], PORCENTAJE siendo el peso de la nota y no es necesario agregar 
el simbolo '%' a PORCENTAJE y las notas deben llevar '.' no ',' si no son enteras.

Al agregar las notas se abren varias opciones como por ejemplo calcular el promedio [promedio {RAMO}], que entrega el promedio de un ramo 
o también se puede calcular la nota necesaria para eximirse de un examen con [eximicion {RAMO} {PORCENTAJE} {SELLO DE EXIMICION}].

Si lamentablemente el estudiante no logro eximirse y debe rendir el examen, puede utilizar el comando [pasar_ramo {RAMO} {PORCENTAJE}], PORCENTAJE siendo el peso del examen en la nota final.

Ejemplos de comandos:
agrega_ramo calculo
agrega_nota calculo 6 30
agrega_nota calculo 6 10
agrega_nota calculo 5.5 30
promedio calculo
eximicion calculo 30 5.5
pasar_ramo calculo 30
