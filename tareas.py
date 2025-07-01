# Importar módulos.
import logging
from colorama import Fore
import pandas as pd
import funciones as f


def agregar_tarea(df_tareas):
    """
    Permite agregar nuevas tareas al Dataframe insertado como parámetro.
    La tarea nueva tendrá:
        - id
        - nombre
        - descripción,
        - prioridad,
        - estado
    df_tareas: es el DataFrame a explorar
    """

    while True:
        # Visualizar menú.
        print(Fore.BLUE + "-" * 50)
        print(Fore.GREEN + "¡Vamos a agregar esta tarea!")
        print(Fore.BLUE + "-" * 50)

        # Asignar id automáticamente.
        if df_tareas.empty:
            tarea_id = 1
        else:
            tarea_id = df_tareas["id"].max()+1

        # Preguntar al usuario la información de la tarea.
        tarea_nombre = input(Fore.YELLOW + "Nombre: ")

        print("Puedes colocar una descripción breve de tu tarea:")
        tarea_descripcion = input("Escribe aquí: ")

        # La prioridad de la tarea.
        print("¿Qué tan prioritaria es la tarea?")
        print("1: Alta\n"
            "2: Media\n"
            "3: Baja")
        seleccion = f.usuario_input_num(n_min=1, n_max=3, texto="Prioridad (1-3): ")
        if seleccion == 1:
            tarea_prioridad = "Alta"
        elif seleccion == 2:
            tarea_prioridad = "Media"
        else:
            tarea_prioridad = "Baja"

        # DataFrame de la nueva tarea.
        tarea_nueva = pd.DataFrame([
            {
                "id" : tarea_id,
                "nombre" : tarea_nombre,
                "descripción" : tarea_descripcion,
                "prioridad" : tarea_prioridad,
                "estado" : "pendiente"
            }
        ])

        # Agregar la tarea al DataFrame completo.
        df_tareas = pd.concat([df_tareas, tarea_nueva], ignore_index=True)

        # log.
        logging.info(f"Se creó una nueva tarea id:{tarea_id}, nombre:{tarea_nombre}")

        # Posibilidad de agregar otra tarea sin volver al menú.
        print(Fore.BLUE + "-" * 50)
        print(Fore.GREEN + "¿Quieres agregar otra tarea?")
        print("1: No, volver al menú\n"
            "2: Si, agregar nueva tarea")
        seleccion = f.usuario_input_num(n_min=1, n_max=2, texto=("Elegir: "))
                                        
        if seleccion == 2:
            continue
        if seleccion == 1:
            return df_tareas


def visualizar_tareas(df_tareas, solo_pendientes=False):
    """
    Muestra todas las tareas (en páginas de a 5).
    df_tareas: es el DataFrame a explorar.
    solo_pendientes: para filtrar las tareas y solo ver las pendientes.
    """

    logging.info(f"Se están visualizando las tareas")

    # Filtrar solo las pendientes si el parametro es True.
    if solo_pendientes == True:
        df_tareas = df_tareas[df_tareas["estado"] == "pendiente"]

    # Si no hay tareas que mostrar, salir.
    if df_tareas.empty:
        print(Fore.BLUE + "-" * 50)
        print(Fore.RED + "No hay ninguna tarea para visualizar")
        print(Fore.BLUE + "-" * 50)
        logging.warning(f"Se querían borrar tareas, pero no existe ninguna")
        return

    tareas_por_pagina = 5
    total_tareas = len(df_tareas)
    total_paginas = (total_tareas - 1) // tareas_por_pagina + 1
    pagina = 0

    while True:
        # Calcular tareas que se deben mostrar en la página actual.
        inicio = pagina * tareas_por_pagina
        fin = inicio + tareas_por_pagina
        
        logging.info(f"Visualizando página: {pagina+1}/{total_paginas}")

        # Mostrar tareas de la página actual.
        print(Fore.BLUE + "-" * 50)
        print(Fore.GREEN + f"Lista de Tareas, página:{pagina+1} de {total_paginas}")
        print(Fore.BLUE + "-" * 50)
        print(Fore.YELLOW + df_tareas.iloc[inicio:fin].to_string(index=False))

        # Opciones para navegar entre las páginas.
        print(Fore.CYAN + "[1] siguiente página")
        print("[2] anterior página")
        print("[3] salir")
        seleccion = f.usuario_input_num(n_min=1, n_max=3, texto="Elegir:")
        
        # Navegar entre las páginas.
        if(seleccion == 1):
            pagina += 1
            if pagina >= total_paginas:
                pagina = 0
        elif(seleccion == 2):
            pagina -= 1
            if pagina < 0:
                pagina = total_paginas -1
        
        else:
            break
    
    logging.info(f"Se dejó de visualizar las tareas")


def marcar_tarea_completada(df_tareas):
    """
    Permite marcar una tarea como completada.
    df_tareas: DataFrame con el listado de tareas a utilizar.
    """
    
    # Si no hay tareas, salir.
    if df_tareas.empty:
        print(Fore.RED + "No hay ninguna tarea")
        logging.warning(f"Se querían borrar tareas, pero no existe ninguna")
        return

    print(Fore.BLUE + "-" * 50)
    print(Fore.GREEN + "Menú para completar tareas")
    print(Fore.BLUE + "-" * 50)

    while True:
        # Elegir a qué tarea se le cambiará su estado.
        print(Fore.GREEN + "--Escribe el id de la tarea completada")
        print(Fore.YELLOW + "[0] Para consultar el listado")
        print("[-1] Para salir]")
    
        seleccion = f.usuario_input_num(n_min=-1, n_max=df_tareas["id"].max(), texto="id de la Tarea: ")

        if seleccion == 0:
            visualizar_tareas(df_tareas, solo_pendientes=True)
            continue
        
        # Cambiar estado de la tarea.
        if seleccion in df_tareas["id"].values:
            tarea_seleccionada = df_tareas[df_tareas["id"] == seleccion].index[0]
        
            if df_tareas.at[tarea_seleccionada, "estado"] == "completada":
                print(Fore.RED + "Esta tarea ya se encuentra completada")
                logging.warning("Se intentó completar una tarea que ya estaba completada")
            else:
                df_tareas.at[tarea_seleccionada, "estado"] = "completada"
                print(Fore.RED + f"La tarea id{seleccion} fue marcada como completada")
                logging.info(f"La tarea id:{seleccion} fue marcada como completada")

                print(Fore.BLUE + "-" * 50)
                return df_tareas
        else:
            print(Fore.RED + f"La tarea: [{seleccion}] no existe")
            logging.warning("Se intentó completar una tarea inexistente")


def eliminar_tarea(df_tareas):
    """
    Permite eliminar una tarea por su id, o borrar todas las completadas.
    df_tareas: DataFrame con las tareas.
    """
    
    # Si no hay tareas, salir.
    if df_tareas.empty:
        print(Fore.RED + "No hay ninguna tarea")
        logging.warning("Se intentó borrar tareas de un listado vacio")
        return df_tareas

    while True:

        logging.info("Menú para borrar tareas abierto")
        print(Fore.BLUE + "-" * 50)
        print(Fore.GREEN + "Menú para borrar tareas")
        print(Fore.BLUE + "-" * 50)
        # Opciones.
        print(Fore.GREEN + "--Escribe el id de la tarea a eliminar")
        print(Fore.YELLOW + "[0] Para consultar el listado")
        print("[-1] Para borrar todas las tareas completadas")
        print("[-2] Para salir")
    
        seleccion = f.usuario_input_num(n_min=-2, n_max=df_tareas["id"].max(), texto="id de la Tarea: ")

        # Si el usuario quiere, puede visualizar las tareas.
        if seleccion == 0:
            visualizar_tareas(df_tareas)
            continue

        # Confirmar selección para borrar todas las tareas completadas.
        if seleccion == -1:
            print(Fore.RED + "¿Estas seguro?")
            print("[1] SÍ     [2] NO")
            confirmar = f.usuario_input_num(n_min=1, n_max=2, texto="Confirmar: ")

            # Si se confirma, se borran todas las tareas completadas.
            if confirmar == 1:
                tareas_completadas = df_tareas[df_tareas["estado"] == "completada"]
                df_tareas = df_tareas[df_tareas["estado"] == "pendiente"]
                print(Fore.RED + f"Se borraron [{len(tareas_completadas)}] tareas completadas")
                logging.info("Se borraron todas las tareas completadas")
            else:
                print(Fore.RED + "Operación cancelada")
                logging.info("Operación cancelada")

            return df_tareas

        # Si el usuario decide volver al menú.
        if seleccion == -2:
            print(Fore.BLUE + "Regresando al menú")
            logging.info("Regresando al menú sin hacer cambios")
            return df_tareas

        # Si se quiere borrar una tarea específica.
        if seleccion in df_tareas["id"].values:
            
            tarea_seleccionada = df_tareas[df_tareas["id"] == seleccion].iloc[0]

            print(Fore.RED + f"Se eliminará la tarea: {tarea_seleccionada['nombre']}")
            print(Fore.YELLOW + "¿Estas seguro?")
            print("[1] SÍ     [2] NO")
            confirmar = f.usuario_input_num(n_min=1, n_max=2, texto="Confirmar: ")

            # Pedir confirmación para borrar tarea por id.
            if confirmar == 1:
                df_tareas = df_tareas.drop(df_tareas[df_tareas["id"] == seleccion].index)
                print(Fore.RED + "Tarea borrada")
                logging.info(f"Se eliminó la tarea id:{seleccion}")

            else:
                print(Fore.RED + "Operación cancelada")
                logging.info("Operación cancelada. Volver al menú")

            return df_tareas
        
        print(Fore.RED + f"La tarea: [{seleccion}] no existe")

