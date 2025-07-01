# Importar módulos.
import logging
from colorama import Fore


def usuario_input_num(n_min, n_max, texto="Ir a: "):
    """
    Se solicita al usuario mediante input un número.
    Y se verifica que ese número sea:
    - n_min: valor mínimo permitido.
    - n_max: valor máximo permitido.
    - texto: Texto que le explica al usuario que hacer.

    Devuelve un número entero elegido.
    """
    
    while True:
        seleccion_str = input(texto)
        # Se intenta convertir a entero.
        try:
            seleccion = int(seleccion_str)
        # Si falla, avisa para repetir el input.
        except:
            print(Fore.RED + "Escriba un número válido")
            logging.warning("Se introdujo un input no válido.")
            continue

        # Si se convirtió exitosamente, y es un número válido, lo devuelve.
        if n_min <= seleccion <= n_max:
            return seleccion
        
        # Si el número no está en el rango permitido, avisa y se repite el input.
        print(Fore.RED + "Escriba un número válido")
        logging.warning("Se introdujo un input no válido.")