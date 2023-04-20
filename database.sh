#!/bin/bash

# Pedir dirección IP del servidor
read -p "Ingrese la dirección IP del servidor: " ip_servidor

# Establecer conexión SSH al servidor y crear el archivo tar
ssh root@$ip_servidor "tar -czvf /tmp/Archivos.tar.gz /home/joseph1/Archivos"

# Verificar si existe la carpeta de destino en la máquina principal y crearla si no existe
if [ ! -d /home/joseph/BackUp ]; then
  mkdir /home/joseph/BackUp
fi

# Copiar el archivo tar a la máquina principal y cambiarle el nombre si ya existe
scp root@$ip_servidor:/tmp/Archivos.tar.gz /home/joseph/BackUp/
if [ -f /home/joseph/BackUp/Archivos.tar.gz ]; then
  mv /home/joseph/BackUp/Archivos.tar.gz /home/joseph/BackUp/Archivos_$(date +%Y%m%d%H%M%S).tar.gz
fi

# Eliminar el archivo tar en el servidor
ssh root@$ip_servidor "rm /tmp/Archivos.tar.gz"
