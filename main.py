# Importar módulos.
import logging
import os

from colorama import init, Fore
import pandas as pd

import funciones as f
import tareas as t

# Iniciar colorama.
init()

# Ruta a esta carpeta.
ruta_actual = os.path.dirname(os.path.abspath(__file__))

# Archivo .log para los registros.
ruta_log = os.path.join(ruta_actual, "gestor_de_tareas.log")
logging.basicConfig(
    filename=ruta_log,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


logging.info("Gestor de Tareas abierto")

# Archivo .csv donde se guardan las tareas.
ruta_csv = os.path.join(ruta_actual, "tareas.csv")
try:
    df_tareas = pd.read_csv(ruta_csv)
except:
    df_tareas = pd.DataFrame(columns=["id", "nombre", "descripción", "prioridad", "estado"])
    df_tareas.to_csv(ruta_csv, index=False)
    logging.info("No se encontró el .csv de tareas. Se creó uno nuevo")


def mostrar_menu():
    """
    Abre el menú principal del gestor de tareas.
    Desde este menú se accede a los submenús para agregar, visualizar, completar o eliminar las tareas.    
    """
    global df_tareas

    while True:
        # Visualizar menú.
        print(Fore.MAGENTA + "\n|--------- GESTOR DE TAREAS --------------|")
        print(Fore.CYAN + "|-- 1: Agregar tarea                      |")
        print(Fore.GREEN + "|-- 2: Ver todas las tareas               |")
        print(Fore.CYAN + "|-- 3: Marcar una tarea como completada   |")
        print(Fore.GREEN + "|-- 4: Eliminar una tarea                 |")
        print(Fore.CYAN + "|-- 5: Salir                              |")
        print(Fore.MAGENTA + "|-----------------------------------------|")

        # Esperar elección del usuario.
        seleccion = f.usuario_input_num(n_min=1, n_max=5)

        # Realizar la acción.
        # Agregar nueva tarea.
        if seleccion == 1:
            df_tareas = t.agregar_tarea(df_tareas)
            df_tareas.to_csv(ruta_csv, index=False)
            logging.info("Se actualizó el archivo tareas.csv")

        # Visualizar las tareas existentes.
        elif seleccion == 2:
            t.visualizar_tareas(df_tareas)

        # Marcar una tarea como completada.
        elif seleccion == 3:
            df_tareas = t.marcar_tarea_completada(df_tareas)
            df_tareas.to_csv(ruta_csv, index=False)
            logging.info("Se actualizó el archivo tareas.csv")

        # Eliminar una tarea.
        elif seleccion == 4:
            df_tareas = t.eliminar_tarea(df_tareas)
            df_tareas.to_csv(ruta_csv, index=False)
            logging.info("Se actualizó el archivo tareas.csv")

        # Salir del Gestor de Tareas.
        elif seleccion == 5:
            # Reordenar índices y actualizar el archivo .csv antes de salir.
            df_tareas = df_tareas.reset_index(drop=True)
            df_tareas["id"] = df_tareas.index + 1
            df_tareas.to_csv(ruta_csv, index=False)
            logging.info("Se actualizaron los id del archivo tareas.csv")
            
            print(Fore.BLUE + "-" * 50)
            print("Gestor de Tareas finalizado")
            logging.info("Gestor de Tareas cerrado")
            print(Fore.BLUE + "-" * 50)
            break

mostrar_menu()







