from random import randint as rand
from sys import argv as args

opciones = ['piedra', 'papel', 'tijera']


'''
Versión con lógica (optimizado)
'''
def ejecutar_ppt(usuario, pc):
    print("Usuario: ", usuario, "\nPC:\t ", pc)
    if usuario == pc:
        print("Empataste!")
    else:
        if (usuario == 'piedra' and pc == 'papel') or \
            (usuario == 'papel' and pc == 'tijera') or \
            (usuario == 'tijera' and pc == 'piedra'):
            print("Perdiste... :(")
        else:
            print("Ganaste!")

'''
Versión con diccionario
'''
def ejecutar_ppt2(usuario, pc):
    print("Usuario: ", usuario, "\nPC:\t ", pc)
    resultados = { ('piedra', 'piedra'): 'Empataste!',
                   ('piedra', 'papel'):  'Perdiste...',
                   ('piedra', 'tijera'): 'Ganaste!!!',
                   ('papel', 'piedra'):  'Ganaste!!!',
                   ('papel', 'papel'):   'Empataste!',
                   ('papel', 'tijera'):  'Perdiste...',
                   ('tijera', 'piedra'): 'Perdiste...',
                   ('tijera', 'papel'):  'Ganaste!!!',
                   ('tijera', 'tijera'): 'Empataste!'
                   }
    print(resultados[(usuario, pc)])

def validate_input():
    if len(args) is not 2 or args[1] not in opciones:
        print("Opción inválida!")
        print("Las opciones son: ", opciones)
        exit()
    else:
        return (args[1], opciones[rand(0, 2)])


if __name__ == "__main__":
    usuario, pc = validate_input()

    # Versión con lógica:
    # ejecutar_ppt(usuario, pc)

    # Versión con diccionario indexado por tupla():
    ejecutar_ppt2(usuario, pc)
