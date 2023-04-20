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
        
## Cifrados 
    - creamos un directorio /home/cifrado
    - nos vamos a la carpeta cd /home/cifrado
    - touch archivo1
    - touch archivo2
    - touch archivo3
    - cp /etc/shadow archivo1
    - cp /etc/passwd archivo2
    - cp /var/log/syslog archivo3
    - ls
    - md5sum archivo1 // md5sum es para ver el hash del archivo 
    - md5sum archivo2
    - md5sum archivo3
    - cat /etc/passwd > /home/cifrado/password.txt
    - gpg --symmetric archivo1 // esto es para cifrar un archivo donde --symmetric es para cifrar un archivo
    - gpg -c archivo2 // esto es para cifrar un archivo donde -c es para cifrar un archivo
    - gpg -c --cipher-algo AES256 archivo3 // esto es para cifrar un archivo donde -c es para cifrar un archivo y --cipher-algo es para escoger el algoritmo de cifrado AES256
    - gpg -c --cipher-algo CAMELLIA128 password.txt
    - rm archivo1
    - rm archivo2
    - rm archivo3
    - rm password.txt
    - ahora mandamos por scp los archivos cifrados al servidor2
    - scp archivo1.gpg root@192.168.207.101:/home/destinocifrado

    

## generar claves
    - gpg --full-generate-key
    - 1
    - 1024
    - 2y
    - s
    - ponemos nombre y apellido: joseph meneses
    - ponemos el correo: joamysalguero1@gmail.com
    - ponemos comentario: llave para sistemas distribuidos
    - V
    - ponemos la contraseña: admin123
    - gpg -a --export joamysalguero1@gmail.com > joseph.gpg.asc
    - le ponemos todos los permisos: chmod 777 joseph.gpg.asc
    - ahora mandamos el archivo por scp al servidor2
    - gpg --import joseph.gpg.asc
    - cp /etc/passwd joseph_passwd
    - gpg -a -r (direccion del otro) --encrypt joseph_passwd
    - gpg joseph_passwd.asc


- otros comandos de cifrado son:
    - gpg
    - 3des
    - aes
    - blowfish
    - aes192
    - aes256
    - twofish
    - camellia128

    