# Gestor-de-Tareas-Examen-Programacion

## 📝 Gestor de Tareas en Consola
Es una aplicación de consola escrita en Python que permite **gestionar tareas** de forma simple.
El usuario puede agregar, visualizar, completar y eliminar tareas, todo desde la terminal.

## 🚀 Características
- ✅ Agregar tareas con nombre, descripción y prioridad.
- 📋 Visualizar tareas por páginas (5 por pantalla).
- ✔️ Marcar tareas como completadas.
- 🗑 Eliminar tareas individuales o todas las completadas.
- 🧾 Registro de eventos y errores mediante `logging` en archivo `.log`.

## 📦 Requisitos
Este proyecto necesita Python 3 y las siguientes librerías:
Pandas
Colorama

## Cómo usar
Cloná el repositorio o descargá los archivos.
Instalá los módulos necesarios escritos en requirements.txt
Ejecutá main.py

## Estructura
gestor_tareas/
├── main.py               # Menú principal
├── tareas.py             # Funciones para agregar/ver/completar/eliminar tareas
├── funciones.py          # Funciones auxiliares (como verificar el input)
├── tareas.csv            # Archivo donde se guardan las tareas
├── gestor_de_tareas.log  # Archivo de logs generado automáticamente
├── requirements.txt      # Módulos necesarios
└── README.md
