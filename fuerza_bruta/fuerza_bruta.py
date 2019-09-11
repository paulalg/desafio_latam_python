from sys import argv as args
import string


def contar_iter(password):
    """Versión con dos bucles

    Itera por la cadena pasada contando la distancia para llegar a cada caracter.
    El bucle interno calcula la distancia a cada ascii.
    Se considera sólo cadenas en minúsculas, por requerimiento.
    """
    print("Contraseña: ", password)
    count = 0
    for i in password:
        for j in string.ascii_lowercase:
            count += 1
            if i == j:
                break
    print(count)


def contar_iter2(password):
    """Versión con str.index()

    Itera por la cadena pasada contando la distancia para llegar a cada caracter.
    La distancia se determina directamente utilizando el índice del caracter.
    Se considera sólo cadenas en minúsculas, por requerimiento.
    """
    print("Contraseña: ", password)
    count = 0
    for i in password:
        count += string.ascii_lowercase.index(i) + 1
    print(count)


def validate_input():
    """Validar entrada y devolver los parámetros para la solución
    """
    if len(args) is not 2:
        print("Ingrese una contraseña.")
        exit()
    else:
        return (str(args[1]).lower())


if __name__ == "__main__":
    password = validate_input()

    # Versión con dos bucles:
    contar_iter(password)

    # Versión con str.index():
    contar_iter2(password)
