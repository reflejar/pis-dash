#!/bin/bash

# Ejecutar el script Python
echo "Ejecutando el archivo 1_Actualizacion_Data_Escuelas.py..."
python3 1_Actualizacion_Data_Escuelas.py

# Verificar el estado de finalización del script Python
if [ $? -eq 0 ]; then
    echo "El script 1_Actualizacion_Data_Escuelas.py se ha ejecutado correctamente."
else
    echo "Error: El script 1_Actualizacion_Data_Escuelas.py ha fallado. Deteniendo ejecución."
    exit 1
fi

# Ejecutar el script R
echo "Ejecutando el archivo 2_Unir_Escuelas_Parcelas.R..."
Rscript 2_Unir_Escuelas_Parcelas.R

# Verificar el estado de finalización del script R
if [ $? -eq 0 ]; then
    echo "El script 2_Unir_Escuelas_Parcelas.R se ha ejecutado correctamente."
else
    echo "Error: El script 2_Unir_Escuelas_Parcelas.R ha fallado. Deteniendo ejecución."
    exit 1
fi


# Ejecutar los archivos Python en la carpeta "Inputs"
echo "Ejecutando el archivo 1_Agregar_poblacion.py..."
cd Inputs
python3 1_Agregar_poblacion.py

# Verificar el estado de finalización del primer script Python en la carpeta "Inputs"
if [ $? -eq 0 ]; then
    echo "El archivo 1_Agregar_poblacion.py se ha ejecutado correctamente."
else
    echo "Error: El archivo 1_Agregar_poblacion.py ha fallado. Deteniendo ejecución."
    exit 1
fi

echo "Ejecutando el archivo 2_Crear_zonas_excl_y_amort.py..."
python3 2_Crear_zonas_excl_y_amort.py

# Verificar el estado de finalización del segundo script Python en la carpeta "Inputs"
if [ $? -eq 0 ]; then
    echo "El archivo 2_Crear_zonas_excl_y_amort.py se ha ejecutado correctamente."
else
    echo "Error: El archivo 2_Crear_zonas_excl_y_amort.py ha fallado. Deteniendo ejecución."
    exit 1
fi

echo "Proceso completo."
