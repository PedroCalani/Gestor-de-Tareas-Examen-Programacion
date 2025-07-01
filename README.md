# Gestor-de-Tareas-Examen-Programacion

## 📝 Gestor de Tareas en Consola
Programa que hice en Python para gestionar tareas de forma simple.
El usuario puede agregar, visualizar, completar y eliminar tareas, todo desde la terminal.

## 🚀 Características
- Crear tareas con nombre, descripción y prioridad.
- Visualizar tareas por páginas.
- Marcar tareas como completadas.
- Eliminar tareas individuales o eliminar en un paso todas las completadas.
- Mantener un registro de acciones usando un archivo ".log".

## 📦 Requisitos
Este proyecto necesita Python 3 y las siguientes librerías que no vienen instaladas por defecto:
Pandas
Colorama

## Cómo usar
Cloná el repositorio o descargá los archivos.
Podés crear un entorno virtual para instalar los módulos en un ambiente aislado.
Instalá los módulos necesarios escritos en requirements.txt
Ejecutá main.py
Después de eso, el manejo en el programa se realiza mediante inputs, generalmente introduciendo valores númericos.

## Estructura del proyecto
- gestor_tareas/

----- main.py               # Menú principal.
  
----- tareas.py             # Funciones para agregar/ver/completar/eliminar tareas.

----- funciones.py          # Funciones generales (como verificar que un input sea correcto).

----- tareas.csv            # Archivo donde se guardan las tareas.

----- gestor_de_tareas.log  # Archivo donde se registan los logs.

----- requirements.txt      # Módulos necesarios.

----- README.md
