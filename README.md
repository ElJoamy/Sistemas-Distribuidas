## particionado de discos
    nos vamos manual:
        empzamosprimero por:
            - primero nos vamos alprimer disco
                le ponemos crear una nueva tabla de particiones: si
                Elejimos el tipo de particionado: ms2
            - hacemos lo mismo con el disco 2

        - Entramos al que dice espacio libre
            le damos a crear una nueva particion 300MB 
            primaria
            principio
            utilizar como: volumen fisico para RAID
            le damos a se ha definido la particion

        hacemos lo mismo con el disco 2

        - nos entramos en el que dice espacio libre
            le damos a crear una nueva particion con lo que nos queda de disco
            primaria
            utilizar como: volumen fisico para RAID
            le damos a se ha definido la particion

        - Ahora nos vamos a RAID por software
            desea escribir los cambios en el disco: si
            crear un dispositivo MD
            RAID 1
            minimo 2 discos
            numero de dispositivos libres para el array RAID1: 0 // esto esel spare disk que no se usa
            Dispositivos RAID1: /dev/sda1 /dev/sdb1 // deben escoger los discos qu son del mismo tamano
            terminar
            y hacemos lo mismo con losotros discos
        
        - ahora nos vamos al disco 2 
            - 

        - configurar los volumenes cifrados
            - desea mantener: si
            - crear volumenes cifrados
            - escogemos el que esta cifrado
            - terminar
            - desea realmente borrar los datos de dispositivo RAID1: no
            - escribimos la contraseña
            - escribimos la contraseña de nuevo
            - nos entramos al disco encriptado y le cambiamos a lvm

        - configurar los volumenes logicos
            - desea mantener: si
            - crear grupo de volumenes
            - nombre del grupo de volumenes: servidor1
            - escogemos siempre el mas grande en este caso el encriptado
            - crear volumen logico
            - entramos al que pusiumos el nombre del grupo de volumenes
            - nombre del volumen logico: root
            - tamaño del volumen logico: 40GB
            - nombre del volumen logico: home
            - tamaño del volumen logico: 15GB
            - nombre del volumen logico: var
            - tamaño del volumen logico: 15GB
            - nombre del volumen logico: swap   
            - tamaño del volumen logico: loque quede
            - terminar

        - nos vamos a home
            - sistema de ficheros: ext4
            - etiqueta del sistema de ficheros: home

        - nos vamos a root
            - sistema de ficheros: ext4
            - etiqueta del sistema de ficheros: /

        - nos vamos a var
            - sistema de ficheros: ext4
            - etiqueta del sistema de ficheros: var
        
        - nos vamos a swap
            - sistema de ficheros: area de intercambio
            - etiqueta del sistema de ficheros: swap

        - finalizamos 
        - le ponemos si
        