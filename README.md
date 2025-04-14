# Linux Filesystem Simulado

## Descripción
Este proyecto simula un pequeño sistema de archivos estilo Linux, soportando los siguientes comandos:

- `cd <ruta>`: navega entre directorios.
- `touch <nombre>`: crea un archivo.
- `ls`: lista archivos y directorios.
- `mkdir <nombre>`: crea un directorio.
- `pwd`: muestra la ruta actual.

El sistema soporta rutas relativas y absolutas (para el comando `ls`).
El sistema no soporta que un archivo y un directorio se llamen igual dentro del mismo directorio.
Lo demás está explicado en los comentarios de la solución.

## Cómo ejecutarlo

Desde la terminal, dentro del proyecto: `python main.py`