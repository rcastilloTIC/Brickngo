#!/bin/bash

# Pide al usuario que introduzca el directorio sobre el que se quiere actuar
# Ask the user to enter the directory to operate on
echo "Por favor, introduce el directorio en el que quieres listar los archivos:"
echo "Please, enter the directory where you want to list the files:"
read DIRECTORIO

# Verifica que el directorio existe
# Verify that the directory exists
if [ ! -d "$DIRECTORIO" ]; then
  echo "El directorio no existe: $DIRECTORIO"
  echo "The directory does not exist: $DIRECTORIO"
  exit 1
fi

# Lista todos los archivos en la carpeta, elimina las extensiones y los guarda en una lista de Python
# List all files in the folder, remove extensions, and store them in a Python list
lista_python="["

for archivo in "$DIRECTORIO"/*; do
  # Obtén el nombre del archivo sin la extensión
  # Get the filename without the extension
  nombre_archivo=$(basename "$archivo")
  nombre_sin_extension="${nombre_archivo%.*}"
  
  # Añade el nombre a la lista de Python
  # Add the name to the Python list
  lista_python+="\"$nombre_sin_extension\", "
done

# Elimina la última coma y espacio, y cierra la lista
# Remove the last comma and space, and close the list
lista_python=${lista_python%, }
lista_python+="]"

# Muestra la lista en formato Python
# Display the list in Python format
echo "$lista_python"