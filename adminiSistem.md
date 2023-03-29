# Administracion de Sistemas
## Modificacion de discos Raids
    - aptitude install mdadm // Instalacion de mdadm para la administracion de discos
    - fdisk -l // Listado de discos
    - fdisk /dev/sdb // Creacion de particiones
    - n // Creacion de particion
    - p // Tipo de particion
    - 1 // Numero de particion
    - 2048 // Primer sector
    - 4096 // Ultimo sector
    - t // Cambio de tipo de particion
    - si queremos que sea linux Raid debemos poner fd // Tipo de particion a linux Raid
    - w // Guardar cambios
    - mdadm -Cv /dev/md1 -l1 -n2 /dev/sdb1 /dev/sdc1 // Creacion de Raid 1 con dos discos //l1 es Raid 1 y n2 es numero de discos
    - cat /proc/mdstat // Comprobacion de la creacion del Raid
    - mdadm --query /dev/md1 // Comprobacion de la creacion del Raid
    - mdadm --detail /dev/md1 // Comprobacion de la creacion del Raid con mas detalle
    - mkfs.ext4 /dev/md1 // Creacion de sistema de ficheros
    - mkdir /mnt/discoRaid // Creacion de directorio
    - mount /dev/md1 /mnt/discoRaid // Montaje del disco
    - ls -la /mnt/discoRaid // Comprobacion de la creacion del disco
    - ahora crear un disco de espera para el Raid
    - mdadm --add-spare /dev/md1 /dev/sdd1 // Creacion de disco de espera
    - mdadm --detail /dev/md1 // Comprobacion de la creacion del disco de espera
    - mdadm --fail /dev/md1 /dev/sdc1 // Fallo de disco
    - mdadm --remove /dev/md1 /dev/sdc1 // Eliminacion de disco
    - mdadm --add /dev/md1 /dev/sdc1 // Añadir disco

## LVM
    - aptitude install lvm2 // Instalacion de lvm2
    - pvcreate /dev/sde // Creacion de volumen fisico
    - pvs // Comprobacion de la creacion del volumen fisico
    - pvdisplay // Comprobacion de la creacion del volumen fisico
    - vgcreate sistemas /dev/sde // Creacion de grupo de volumenes
    - vgs // Comprobacion de la creacion del grupo de volumenes
    - vgdisplay // Comprobacion de la creacion del grupo de volumenes
    - lvcreate -L 5G -n volumen1 sistemas // Creacion de volumen logico // -L 5G es el tamaño del volumen logico y -n sistema es el nombre del volumen logico y sistemas es el grupo de volumenes
    - lvs // Comprobacion de la creacion del volumen logico
    - lvdisplay // Comprobacion de la creacion del volumen logico
    - mkfs.ext4 /dev/sistemas/volumen1 // Creacion de sistema de ficheros
    - mkdir /mnt/volumen1 // Creacion de directorio
    - mount /dev/sistemas/volumen1 /mnt/volumen1 // Montaje del volumen logico
    - ls -la /mnt/volumen1 // Comprobacion de la creacion del volumen logico
    - ls -l /dev/mapper // Comprobacion de la creacion del volumen logico
    - lvextend -L +5G /dev/sistemas/volumen1 // Aumento de tamaño del volumen logicoq
    - resize2fs /dev/sistemas/volumen1 // Aumento de tamaño del volumen logico
    - lvreduce -L -5G /dev/sistemas/volumen1 // Reduccion de tamaño del volumen logico
    - df -h // Comprobacion de la reduccion o aumento del volumen logico
        - lvremove /dev/sistemas/volumen1 // Eliminacion del volumen logico
        - vgremove sistemas // Eliminacion del grupo de volumenes
        - pvremove /dev/sde // Eliminacion del volumen fisico
    - vgextend sistemas /dev/sdf // Añadir volumen fisico al grupo de volumenes

### ahora creamos un volumen2 
    - lvcreate -L 5G -n volumen2 sistemas // Creacion de volumen logico // -L 5G es el tamaño del volumen logico y -n sistema es el nombre del volumen logico y sistemas es el grupo de volumenes


## Enjercicio
    - Crear un RAID 5 con 3 discos de 5G y un spare de 5G
    - fdisk -l // Listado de discos
    - fdisk /dev/sdg // Creacion de particiones
    - n // Creacion de particion
    - p // Tipo de particion
    - 1 // Numero de particion
    - 2048 // Primer sector
    - 4096 // Ultimo sector
    - t // Cambio de tipo de particion
    - si queremos que sea linux Raid debemos poner fd // Tipo de particion a linux Raid
    - w // Guardar cambios
    - repetir para los proximos discos sde y sdf
    - mdadm -Cv /dev/md5 -l5 -n3 /dev/sdg1 /dev/sdh1 /dev/sdi1 // Creacion de Raid 5 con tres discos //l5 es Raid 5 y n3 es numero de discos
    - cat /proc/mdstat // Comprobacion de la creacion del Raid
    - mdadm --query /dev/md5 // Comprobacion de la creacion del Raid
    - mdadm --detail /dev/md5 // Comprobacion de la creacion del Raid con mas detalle
    - mdadm --add-spare /dev/md5 /dev/sdj1 // Creacion de disco de espera
    - mdadm --detail /dev/md5 // Comprobacion de la creacion del disco de espera
    - mdadm --fail /dev/md5 /dev/sdh1 // Fallo de disco
    - mdadm --remove /dev/md5 /dev/sdh1 // Eliminacion de disco
    - mdadm --add /dev/md5 /dev/sdh1 // Añadir disco

## Ejercicio2
    - Tener 2 PVS cada uno de 15G
    - Crear 1 VG llamado PRACTICA
    - Crear un LVM de 11G llamado LUNES
    - Crear un LVM de 10G llamado EJERCICIO
    - Darle el formato EXT4 a ambos LVM y que se monten en /mnt/lunes y /mnt/ejercicio
    - Que se monten en el FSTAB

    - pvcreate /dev/sdk /dev/sdl // Creacion de volumen fisico
    - pvs // Comprobacion de la creacion del volumen fisico
    - vgcreate practica /dev/sdk /dev/sdl // Creacion de grupo de volumenes
    - vgs // Comprobacion de la creacion del grupo de volumenes
    - lvcreate -L 11G -n lunes practica // Creacion de volumen logico // -L 11G es el tamaño del volumen logico y -n lunes es el nombre del volumen logico y practica es el grupo de volumenes
    - lvs // Comprobacion de la creacion del volumen logico
    - mkfs.ext4 /dev/practica/lunes // Creacion de sistema de ficheros
    - mkdir /mnt/lunes // Creacion de directorio
    - mount /dev/practica/lunes /mnt/lunes // Montaje del volumen logico
    - ls -la /mnt/lunes // Comprobacion de la creacion del volumen logico
    - ls -l /dev/mapper // Comprobacion de la creacion del volumen logico
    - lvcreate -L 10G -n ejercicio practica // Creacion de volumen logico // -L 10G es el tamaño del volumen logico y -n ejercicio es el nombre del volumen logico y practica es el grupo de volumenes
    - lvs // Comprobacion de la creacion del volumen logico
    - mkfs.ext4 /dev/practica/ejercicio // Creacion de sistema de ficheros
    - mkdir /mnt/ejercicio // Creacion de directorio
    - mount /dev/practica/ejercicio /mnt/ejercicio // Montaje del volumen logico
    - ls -la /mnt/ejercicio // Comprobacion de la creacion del volumen logico
    - ls -l /dev/mapper // Comprobacion de la creacion del volumen logico
    - echo "/dev/practica/lunes /mnt/lunes ext4 defaults 0 0" >> /etc/fstab // Añadir al fstab
    - echo "/dev/practica/ejercicio /mnt/ejercicio ext4 defaults 0 0" >> /etc/fstab // Añadir al fstab
    - mount -a // Montaje de los volumenes logicos



## CHMOD y CHOWN
### Permisos

Permisos del propietario
    - r: read
    - w: write
    - x: execute
Permisos del grupo
    - r: read
    - w: write
    - x: execute
Permisos de otros
    - r: read
    - w: write
    - x: execute

para cambiar los permisos de others usamos el comando:
    De manera numerica:
        chmod 007 (nombre del archivo o carpeta)
    De manera simbolica:
        chmod rwx (nombre del archivo o carpeta)
        chmod a+rwx (nombre del archivo o carpeta) (a es para todos los usuarios)
        chmod u+rwx (nombre del archivo o carpeta) donde + es para agregar permisos y - es para quitar permisos (u es para el usuario)
        chmod g+rwx (nombre del archivo o carpeta) (g es para el grupo)
        chmod o+rwx (nombre del archivo o carpeta) (o es para otros)
    
    chmod o=rwx * este comando es para dar permisos de lectura, escritura y ejecucion a todos los archivos y carpetas que esten en el directorio actual
    chmod a=rx (nombre del archivo o carpeta) este comando es para dar permisos de lectura y ejecucion al archivo o carpeta

    chown (nombre del usuario) (nombre del archivo o carpeta) este comando es para cambiar el propietario del archivo o carpeta
    chown (nombre del usuario):(nombre del grupo) (nombre del archivo o carpeta) este comando es para cambiar el propietario y el grupo del archivo o carpeta
    chgrp (nombre del grupo) (nombre del archivo o carpeta) este comando es para cambiar el grupo del archivo o carpeta
    

### Valores octales de los permisos
  Permiso   Valor octal   Descripcion
    ---         0:          no tiene permisos
    --x         1:          ejecutar
    -w-         2:          escribir
    -wx         3:          escribir y ejecutar
    r--         4:          leer
    r-x         5:          leer y ejecutar
    rw-         6:          leer y escribir
    rwx         7:          leer, escribir y ejecutar
## Comandos para ver los discos en linux
    - blkid (para ver los discos)// identificador de los discos
    - blkid -o list (para ver los discos)// identificador de los discos 
    - lsblk
    - fdisk -l
    - df -h // -h para verlo en human readable
    - top // para ver los procesos del sistema
    - free -h // para ver la memoria del sistema
    - mount // para ver los discos montados en el sistema
    - cat /etc/fstab // para ver los discos que se montan al iniciar el sistema 
    - cat /proc/mounts // para ver los discos que se montan al iniciar el sistema
    - cat /etc/mtab // para ver los discos que se montan al iniciar el sistema

## Comando para dar formato a los discos
    - fdisk /dev/sdc // para dar formato a los discos
    seguimos con los siguientes comandos:
    - m // para ver los comandos
    - n // para crear una nueva particion
    - p // para crear una particion primaria
    - 1 // para crear una particion primaria
    - tamano de la particion inicial // para crear una particion primaria
    - tamano de la particion final // para crear una particion primaria
    - p // para ver las particiones
    - w // para guardar los cambios
    - mkfs.ext4 /dev/sdc1 // para dar formato a la particion
    - file -s /dev/sdc1 // para ver la informacion del disco
    - mount /dev/sdc1 /mnt/(nombre_que_crees) // para montar el disco
    - ls -la /mnt/discoc/ // para ver los archivos del disco y debe aparecer el archivo lost+found para que el disco este montado correctamente
    - para montar automaticamente el disco al iniciar el sistema debemos agregar la siguiente linea al archivo /etc/fstab
    file sistem        mount point        type        options        dump        pass
    /dev/sdc1           /mnt/discoc         ext4        defaults        0           0

    # Tenemos un disco de 20GB y queremos crear 2 particiones de 10GB cada una
    - fdisk /dev/sda // para dar formato a los discos 
    - n // para crear una nueva particion
    - p // para crear una particion primaria
    - 1 // para crear una particion primaria
    - 1 // para crear una particion primaria
    - +10G // para crear una particion primaria
    - n // para crear una nueva particion
    - p // para crear una particion primaria
    - 2 // para crear una particion primaria
    - +10G // para crear una particion primaria
    - p // para ver las particiones
    - w // para guardar los cambios
    - mkfs.ext4 /dev/sda1 // para dar formato a la particion
    - mkfs.ext4 /dev/sda2 // para dar formato a la particion
    - file -s /dev/sda1 // para ver la informacion del disco
    - file -s /dev/sda2 // para ver la informacion del disco
    - mount /dev/sda1 /mnt/discoc/ // para montar el disco
    - mount /dev/sda2 /mnt/discod/ // para montar el disco
    - si queremos desmontar el disco usamos el comando umount /dev/sda1
    - ls -la /mnt/discoc/ // para ver los archivos del disco y debe aparecer el archivo lost+found para que el disco este montado correctamente

## Si hacemos mal en el /etc/fstab
    Lo que hacemos es editar el archivo /etc/fstab y comentamos la linea que agregamos y reiniciamos el sistema
    nano /etc/fstab
    y comenmtamos el disco que hayamos hecho mal 

## Encriptacion de Discos
    - cryptsetup luksFormat /dev/sda1
    - YES
    - escribimos la contraseña que queramos
    - cryptsetup luksDump /dev/sda1 reescribimos la contraseña
    - cryptsetup luksDump /dev/sda1 // para ver la informacion del disco
    - para anadir una nueva contrasena a este disco debemos ejecutar el siguiente comando
    - cryptsetup luksAddKey /dev/sda1   
    - ahora declaramos una variable para llamar al disco
    - blkid // para ver el identificador del disco
    - nano -c /etc/crypttab
    - escribimos la siguiente linea
    tarfet name     source device                                  key file   options //lo mas recomeble es usar espacios
    disk            UUID= 5166b645-1b5e-4df3-9037-97e7fee320d1     none       luks
    - cryptsetup luksOpen /dev/sda1 disk // para abrir el disco encriptado con su variable que declaramos
    - escribimos la contrasena
    - ls -l /dev/mapper/ // para ver los discos encriptados
    - mkfs.ext4 /dev/mapper/disk // para dar formato al disco encriptado
    - mkdir /mnt/cifrado // para crear una carpeta donde montaremos el disco encriptado
    - mount /dev/mapper/disk /mnt/cifrado // para montar el disco encriptado
    - ls -la /mnt/cifrado // para ver los archivos del disco encriptado
    - para montar el disco encriptado al iniciar el sistema debemos agregar la siguiente linea al archivo /etc/fstab
    file sistem        mount point        type        options                    dump        pass
    /dev/mapper/disk    /mnt/cifrado        ext4        errors=remount-ro           0           2


## comandos para navegar en linux:
    - cd /home // para ir a la carpeta home
    - ls // para ver los archivos y carpetas
    - ls -l // para ver los archivos y carpetas con sus permisos
    - ls -la // para ver los archivos y carpetas con sus permisos y los archivos ocultos
    - pwd // para ver en que directorio estoy
    - mkdir // para crear directorios
    - rmdir // para eliminar directorios vacios
    - rm // para borrar archivos
    - rm -rf // para borrar archivos y carpetas
    - rm -r // para borrar carpetas
    - rm -f // para borrar archivos    
    - cp // copiar
    - cp (nombre del archivo) (nombre del archivo copia) // para copiar un archivo
    - touch // para crear archivos
    - mv // para mover archivos
    - cat // para ver el contenido de un archivo
    - nano // para editar archivos
    - chmod // para cambiar los permisos de un archivo
    - chown // para cambiar el propietario de un archivo
    - chgrp // para cambiar el grupo de un archivo
    - ln // para crear enlaces simbolicos
    - tar -cvf comprimido1.tar /root/labo/clase2 // para comprimir archivos
    - tar cvjf comprimido2.tar.bz2 /root/labo/clase2 // para comprimir archivos con bzip2
        donde:
            - c: crear
            - v: verbose
            - j: bzip2
            - f: archivo
    - para comprimir archivos con gzip utilizando tar:
        tar -cvzf comprimido3.tar.gz /root/labo/clase2
     - para descomprimir un archivo con tar:
        tar -xvf comprimido1.tar
        donde:
            - x: extraer
            - v: verbose (para ver el proceso)
            - f: archivo (para indicar el archivo a descomprimir)
    - para ver el tamano de los archivos:
        - ls -l --block-size=M // para ver el tamaño de los archivos en megabytes
        - ls -l --block-size=G // para ver el tamaño de los archivos en gigabytes
        - ls -l --block-size=T // para ver el tamaño de los archivos en terabytes
   

    - change // para cambiar el nombre de un archivo
    - nano -c /etc/network/interfaces // configurar la ip de la maquina
        - auto ens33
        - allow-hotplug ens33
        - iface ens33 inet static
        - address
        - netmask
        - gateway
    - /etc/init.d/networking restart // reiniciar el servicio de red
    - tail -f /var/log/syslog // para ver los errores del sistema
    - dns => /etc/resolv.conf // para ver la configuracion de dns
        -nameserver 192.168.x.x
        -nameserver 8.8.4.4
        -nameserver 8.8.8.8
    y para reiniciar el servicio de dns:
        - sudo service networking restart
    - para borrar la cache 
        ip addr flush dev ens33
        si ya no nos aparece hacemos el restart del network manager
        - sudo service network-manager restart
    - shutdown -h now // para apagar la maquina
### para activar el modo root en la interfaz grafica en Debian debemos comentar la linea:
        #auth required pam_succeed_if.so user != root quiet_success
        esta ubicada en el archivo /etc/pam.d/gdm-password
### Y si solo se quiere arreglar el problema de sudoers se debe hacer lo siguiente:
    nano /etc/sudoers

    y anadimos la linea del usuario con el que estamos debajo del que dice root 
    - user  ALL=(ALL:ALL) ALL
    
    - Comando para activar y reiniciar ssh
        - sudo systemctl enable ssh
        - sudo systemctl restart ssh
        - para cambiar el puerto de ssh
            - sudo nano /etc/ssh/sshd_config
            - cambiar el puerto
            - sudo systemctl restart ssh
        - para que el usuario root pueda acceder por ssh
            - sudo nano /etc/ssh/sshd_config
            - PermitRootLogin yes
            - sudo systemctl restart ssh
    - Comando para ver los puertos abiertos
        - sudo netstat -tulpn
    
## Root
    root-superusuario-id es 0
    Que permisos tiene el root?
    - rwxrwxrwx donde rwx son los permisos de lectura, escritura y ejecucion para el propietario, grupo y otros.
    # Existen usuarios especiales si vemos en:
        cat /etc/passwd
        aca nos mostrara los usuarios del sistema, si contiene una x es por que existe en el /etc/shadow
        todos los usuarios tienen un id del 1 al 200
        ejemplo
        gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
        aca vemos que:
            - gnats es el nombre del usuario
            - x es el password del usuario o sea que esta en el /etc/shadow
            - 41 es el id del usuario
            - 41 es el id del grupo
            - Gnats Bug-Reporting System (admin) es el comentario del usuario
            - /var/lib/gnats es el directorio home del usuario
            - /usr/sbin/nologin es el shell del usuario

# Creacion de usuarios
    Para crear usuarios en linux debemos usar el comando:
        - sudo adduser nombre_del_usuario

# DHCP
    DHCP es un protocolo que se encarga de asignar direcciones IP a los equipos de una red.
    DHCP son las iniciales de Dynamic Host Configuration Protocol.

    Modos en DHCP
    - Asignacion manual: El administrador configura manualmente las direcciones IP del cliente en el Sevidor DHCP. Cuando la estacion de trabajo de cliente pide una direccion IP, el servidor mira la direccion MAC y procede a asignar la que configuro el administrador.

    - Asignacion automatica: Al cliente DHCP se le asigna una direccion IP cuando contacta por primera vez con el DHCP Server. El cliente mantendra la ip durante un tiempo determinado.

    - Asignacion dinamica: El cliente DHCP se le asigna una direccion IP cuando contacta por primera vez con el DHCP Server. El cliente mantendra la ip durante un tiempo determinado. Si el cliente no se comunica con el servidor durante un tiempo determinado, el servidor DHCP puede asignarle una nueva direccion IP.

# Configuracion de Servidores
    - aptitude search dhcp // para buscar paquetes
    - aptitude install isc-dhcp-server // para instalar el servidor dhcp
    - si queremos desinstalar el servidor dhcp
        - aptitude remove isc-dhcp-server
    - si nos sale error hacemos:
        - dpkg -s isc-dhcp-server // para ver si esta instalado
    - tail -f /var/log/syslog
    - cat /etc/default/isc-dhcp-server // para ver la configuracion del servidor dhcp
    - nano /etc/default/isc-dhcp-server // para editar la configuracion del servidor dhcp
    - en la linea INTERFACESv4="ens33" // para indicar la interfaz de red que va a usar el servidor dhcp
    - cp /etc/dhcp/dhcpd.conf /root/backup // para hacer una copia de seguridad del archivo de configuracion del servidor dhcp
    - nano /etc/dhcp/dhcpd.conf // para editar el archivo de configuracion del servidor dhcp
    cambiamos el:
        - option domain-name "example.org";
        - option domain-name-servers 8.8.8.8, 8.8.4.4;
        - en el default-lease-time pondremos el tiempo para semanas con 604800 // 7 dias * 24 horas * 60 minutos * 60 segundos
        - en el max-lease-time pondremos el tiempo para meses con 2419200 // 4 semanas * 7 dias * 24 horas * 60 minutos * 60 segundos
        - descomentamos:
            - authoritative; // para que el servidor dhcp sea el unico que pueda asignar direcciones ip
            - subnet (ponemos la red) netmask (ponemos la mascara de red) {
                range (ponemos el rango de ip) (ponemos el rango de ip);
                option routers (ponemos la ip del router);
                host (ponemos el nombre del host) {
                    hardware ethernet (ponemos la mac del host);
                    fixed-address (ponemos la ip del host);
                }
            }
        - /etc/init.d/isc-dhcp-server restart // para reiniciar el servidor dhcp
        - cat /var/lib/dhcp/dhcpd.leases // para ver las ips que se han asignado

    ## Configuracion de un cliente dhcp
    usaremos en esta ocacion el mini windows xp
    - ipconfig /all // para ver la configuracion de la ip
    - ipconfig /release // para liberar la ip
    - ipconfig /renew // para renovar la ip
    - si no tengo conexion con mi servidor dhcp 

# apache2
    que es virtual host?
        es un servidor web que puede tener varios sitios web en un solo servidor
    como trabaja el hosting?
        el hosting es un servicio que permite a las personas o empresas tener un sitio web en internet
    - aptitude install apache2 // para instalar apache2
    - si queremos desis
    - ls /var/www/html // para ver los archivos de apache2
    - mkdir /var/www/sistemas.com/index.html // para crear un directorio
    - nano /var/www/sistemas.com/index.html // para crear un archivo html
    -   <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Mi pagina de prueba</title>
        </head>
        <body>
            holaaa
        </body>
        </html>
    - ls -l sites-available // para ver los sitios disponibles
    - ls -l sites-enabled // para ver los sitios habilitados
    - cp sites-available/000-default.conf /etc/apache2/sites-available/sistemas.com.conf // para copiar el archivo de configuracion
    - nano /etc/apache2/sites-available/sistemas.com.conf // para editar el archivo de configuracion
    - a2ensite sistemas.com.conf // para habilitar el sitio
    - /etc/init.d/apache2 restart // para reiniciar apache2
    - a2dissite 000-default.conf // para deshabilitar el sitio
    - /etc/init.d/apache2 restart // para reiniciar apache2
    - si queremos que una pagina se habra en aapache con un dominio
        - nano /etc/hosts // para editar el archivo hosts
        - reiniciamos apache2
    - si queremos cambiar el puerto de apache2
        - nano /etc/apache2/ports.conf // para editar el archivo de configuracion
        - cambiamos el puerto 80 por el puerto que queramos
        - /etc/init.d/apache2 restart // para reiniciar apache2
    - si no queremos que tengan acceso al index 
        - nano /etc/apache2/sites-available/sistemas.com.conf // para editar el archivo de configuracion
        - descomentamos la linea
            - <Directory "/var/www/sistemas.com">
                    Options -Indexes
            </Directory>    
        - /etc/init.d/apache2 restart // para reiniciar apache2
    - mkdir /var/archivosrestringidos // para crear un directorio
    - Ademas si ponemos el codigo siguiente:
    ErrorLog ${APACHE_LOG_DIR}/sistemas.com.log
    CustomLog ${APACHE_LOG_DIR}/sistemas.com.access.log combined
    <Directory "/var/www/sistemas.com">
        Options -Indexes
        AllowOverride none
        Order allow,deny
        Allow from all
        AuthName "Acceso restringido"
        AuthType Basic
        AuthUserFile /var/archivosrestringidos/restringidos
        Require valid-user
    </Directory>

    - htpasswd -c /var/archivosrestringidos/ restringidos // para crear un archivo de usuarios y contraseñas
    
# Nginx
    - aptitude install nginx // para instalar nginx
    - ls -l /etc/nginx // para ver los archivos de configuracion de nginx
    - ls -l /etc/nginx/sites-available // para ver los sitios disponibles
    - para levantar el servidor
        - /etc/init.d/nginx start
    - para reiniciar el servidor
        - /etc/init.d/nginx restart
    - para detener el servidor
        - /etc/init.d/nginx stop
    - mkdir /var/www/alpha.com // para crear un directorio
    - nano /var/www/alpha.com/index.html // para crear un archivo html
    -   <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Mi pagina de prueba</title>
        </head>
        <body>
            holaaa
        </body>
        </html>
    - cp /etc/nginx/sites-available/default /etc/nginx/sites-available/alpha.com // para copiar el archivo de configuracion
    - nano /etc/nginx/sites-available/alpha.com // para editar el archivo de configuracion
    -   server {
            listen 80;
            listen [::]:80;
            root /var/www/alpha.com;
            index index.html index.htm index.nginx-debian.html;
            server_name alpha.com www.alpha.com;
            location / {
                try_files $uri $uri/ =404;
            }
        }
    - ln -s /etc/nginx/sites-available/alpha.com /etc/nginx/sites-enabled/ // para crear un enlace simbolico
    - /etc/init.d/nginx restart // para reiniciar nginx
    - si queremos que una pagina se habra en nginx con un dominio
        - nano /etc/hosts // para editar el archivo hosts
        - reiniciamos nginx
    - si queremos cambiar el puerto de nginx
        - nano /etc/nginx/sites-available/alpha.com // para editar el archivo de configuracion
        - cambiamos el puerto 80 por el puerto que queramos
        - /etc/init.d/nginx restart // para reiniciar nginx
    - para quitar de sites-enabled
        - rm /etc/nginx/sites-enabled/alpha.com // para eliminar el enlace simbolico
        - /etc/init.d/nginx restart // para reiniciar nginx
    
## Ahora haremos otra nueva pagina pero con el nombre beta.com y en el puerto 8585
    - mkdir /var/www/beta.com // para crear un directorio
    - nano /var/www/beta.com/index.html // para crear un archivo html
    -   <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Mi pagina de prueba</title>
        </head>
        <body>
            holaaa
        </body>
        </html>
    - cp /etc/nginx/sites-available/default /etc/nginx/sites-available/beta.com // para copiar el archivo de configuracion
    - nano /etc/nginx/sites-available/beta.com // para editar el archivo de configuracion
    -   server {
            listen 8585;
            listen [::]:8585;
            root /var/www/beta.com;
            index index.html index.htm index.nginx-debian.html;
            server_name beta.com www.beta.com;
            location / {
                try_files $uri $uri/ =404;
            }
        }
    - ln -s /etc/nginx/sites-available/beta.com /etc/nginx/sites-enabled/ // para crear un enlace simbolico
    - para borrar un enlace simbolico
        - rm /etc/nginx/sites-enabled/beta.com
    - nginx -t // para comprobar la sintaxis de los archivos de configuracion
    - /etc/init.d/nginx restart // para reiniciar nginx
    - si queremos que una pagina se habra en nginx con un dominio
        - nano /etc/hosts // para editar el archivo hosts
        - reiniciamos nginx
    - alias ng="/etc/init.d/nginx restart" // para crear un alias para reiniciar nginx
    - para ver los alias
        - alias -p // para ver los alias
    - aptitude install apache2-utils // para instalar apache2-utils para poder usar htpasswd
    - htpasswd -c /etc/nginx/.htpasswd user // para crear un archivo de usuarios y contraseñas
    - nano /etc/nginx/sites-available/alpha.com // para editar el archivo de configuracion
    - anadimos las siguientes lineas
        - access_log /var/log/nginx/alpha.com.access.log;
        - error_log /var/log/nginx/alpha.com.error.log;
        - location / {
            auth_basic "Restricted";
            auth_basic_user_file /etc/nginx/.htpasswd;
        }
    - si nos sale un error de unknown directive "acces_log" in /etc/nginx/sites-enabled/alpha.com
        - nano /etc/nginx/nginx.conf // para editar el archivo de configuracion
        - anadimos las siguientes lineas
            - include /etc/nginx/conf.d/*.conf;
            - include /etc/nginx/sites-enabled/*;

## samba
    Que es xamba
        - es un servicio para compartir archivos en windows, linux y mac
    - aptitude install samba // para instalar samba
    - cp /etc/samba/smb.conf /root/share/smb.conf.bak // para hacer una copia de seguridad del archivo de configuracion
    - nano /etc/samba/smb.conf // para editar el archivo de configuracion
    - ponemos el codigo debajo de la linea 
    -   [share]
        comment = Compartido
        path = /home/share //no hacer en root
        writable = yes
        browseable = yes
        # read only = no
        guest ok = yes
        guest only = yes
        directory mode = 0777
    
    - /etc/init.d/samba restart // para reiniciar samba
    - systemctl status samba // para ver el estado de samba
    
    - /etc/init.d/samba restart // para reiniciar samba
    - en el cliente de windows
        - en el explorador de windows
            - \\ip_del_servidor
            - usuario: guest
            - contraseña: guest
        - si al darle click a la carpeta nos dice que no tenemos permisos para obtener acceso a la carpeta
        en windows debemos ir a la carpeta
            - C:\Windows\System32\drivers\etc
            - abrir el archivo hosts
            - anadir la ip del servidor y el nombre del servidor en este caso share
                -
    - si queremos dar permiso a un usuario debemos hacer:
        - smbpasswd -a usuario // para dar permiso a un usuario
    - nano /etc/samba/smb.conf // para editar el archivo de configuracion
    -   [share]
        path = /root/share
        writable = yes
        browseable = yes
        guest ok = no
        guest only = no
        directory mode = 0777
        valid users = usuario
    - /etc/s/init.damba restart // para reiniciar samba
    - si queremos una carpeta para un usuario:
        - [usuario]
        - path = /home/usuario
        - read only = no
        - writable = yes
        - create mode = 0777
        - directory mode = 0777
        - valid users = usuario


    - en el cliente: Net use * \\ip_del_servidor\share /user:usuario contraseña  
    - nano /etc/samba/smb.conf // para editar el archivo de configuracion
    - interfaces = 127.0.0.0/8 192.168.215.0/24 ens33 // para dar permiso a una ip
    - ahora crearemos un grupo y lo anadiremos a la configuracion
    - nano /etc/samba/smb.conf // para editar el archivo de configuracion
    -   [finanzas]
        path = /home/finanzas
        writable = yes
        browseable = yes
        create mode = 0777
        directory mode = 0777
        valid users = @finanzas
        write list = @finanzas

    - mount - t cifs //ipdelwindows/carpeta -o username=usuario,password=contraseña /mnt/windows // para montar una carpeta de windows


## proftpd
    - aptitude install proftpd // para instalar proftpd
    - nano /etc/proftpd/proftpd.conf // para editar el archivo de configuracion
    - editamos las lineas 
        - UseIPv6 off
        - DefaultRoot   /home/user user // para que el usuario no pueda salir de su directorio
    - reiniciamos proftpd
        - /etc/init.d/proftpd restart
    
    - vamos a crear un usuario anonimo
        - cat /etc/passwd // para ver los usuarios
        - mkdir /home/anonimo // para crear un directorio
        - touch /home/anonimo/archivo1.txt // para crear un archivo
        - touch /home/anonimo/archivo2.txt // para crear un archivo
        - touch /home/anonimo/archivo3.txt // para crear un archivo
        - ls -la /home/anonimo // para ver los archivos
        - chown ftp.nogroup /home/anonimo // para cambiar el propietario y el grupo
        - nano -c /etc/proftpd/proftpd.conf // para editar el archivo de configuracion
        - anadimos las siguientes lineas
            - <Anonymous /home/anonimo>
                User ftp
                Group nogroup
                <Limit READ>
                    DenyAll
                </Limit>
                <Limit WRITE>
                    DenyAll
                </Limit>
            </Anonymous>
        - /etc/init.d/proftpd restart // para reiniciar proftpd
        - si queremos abrir desde filezilla con el usuario anonimo
            - servidor: ip_del_servidor
            - usuario: anonimo
            - contraseña: anonimo
        - si desde el cliente tratamos de mandar un archivo nos dara un error de permisos esto es por que no tenemos permisos de escritura en el directorio anonimo y no podemos crear un archivo en el, para solucionarlo
            - nano -c /etc/proftpd/proftpd.conf // para editar el archivo de configuracion
            - anadimos las siguientes lineas
                - <Anonymous /home/anonimo>
                    User ftp
                    Group nogroup
                    <Limit READ>
                        DenyAll
                    </Limit>
                    <Limit WRITE>
                        AllowAll
                    </Limit>
                </Anonymous>
            - /etc/init.d/proftpd restart // para reiniciar proftpd

    ## Ahora me voy a crear dos usuarios que pertenezcan al grupo administacion 
        - creamos el grupo
            - groupadd administracion
        - useradd -m -g administacion usuario1 // para crear un usuario
        - passwd usuario1 // para crear una contraseña
        - useradd -m -g administacion usuario2 // para crear un usuario
        - passwd usuario2 // para crear una contraseña
        - cat /etc/passwd // para ver los usuarios
        - cat /etc/group // para ver los grupos
    
    ## ahora crearemos una carpeta en /mnt/administracion y pondremos 3 archivos con touch (servicio.txt, backup.txt, passwprd.txt)
        - mkdir /mnt/administracion // para crear un directorio
        - touch /mnt/administracion/servicio.txt // para crear un archivo
        - touch /mnt/administracion/backup.txt // para crear un archivo
        - touch /mnt/administracion/password.txt // para crear un archivo
        - ls -la /mnt/administracion // para ver los archivos
        - chown administracion:administracion /mnt/administracion // para cambiar el propietario y el grupo
    
    ## ahora vamos a modificar el archivo de configuracion de proftpd para que acepte al grupo de administracion en la parte de de defaultroot sin tocar la parte de anonimo
        - nano -c /etc/proftpd/proftpd.conf // para editar el archivo de configuracion
        - anadimos las siguientes lineas
            - DefaultRoot   /home/user user
            - <Directory /mnt/administracion>
                <Limit READ>
                    DenyAll
                </Limit>
                <Limit WRITE>
                    AllowGroup administracion
                </Limit>
            </Directory>
        - /etc/init.d/proftpd restart // para reiniciar proftpd
        todos los permisos
        chmod 777 /mnt/administracion


## Proxy
    - que es un proxy server?
        - un proxy server es un servidor que se encarga de filtrar el trafico de red, es decir, que si un usuario quiere acceder a una pagina web, el proxy server se encarga de filtrar el trafico de red y de permitir o denegar el acceso a la pagina web
    - por defecto esta en el puerto 3128

    - aptitude install squid // para instalar squid
    - netstat -antp | grep squid // para ver los puertos que esta usando squid
    - cp /etc/squid/squid.conf /root/Documentos/squid.conf.bak // para hacer una copia de seguridad del archivo de configuracion
    - squid -k reconfigure // para reiniciar squid
    - squid -k parse // muestra el resumen de la configuracion que no esta comentada, ademas de que si en algun momento algo esta mal podemos revisar aqui
    - nano -c /etc/squid/squid.conf // para editar el archivo de configuracion
    - esitamos la siguientes lineas
        - cache_mgr webmaster@sistemas.com // para cambiar el correo del administrador esta en la lineas, esta en la linea 5968
        - http_port 3128 // para cambiar el puerto en la linea 1907
        - cache_dir ufs /var/spool/squid 100 16 256 // donde 100 es el tamaño del cache en megas, 16 es el numero de subdirectorios, 256 es el tamaño maximo de los archivos
    - squid -k parse // para ver si hay algun error en la configuracion
    - /etc/init.d/squid restart // para reiniciar squid
    - haremos un nano con ips
        - nano /etc/squid/ips // para crear un archivo
            - 192.168.207.128
    - nano -c /etc/squid/squid.conf // para editar el archivo de configuracion
        - en la linea de insert your own rules here linea 1400
        - acl permitidos src "/etc/squid/ips" // para crear una lista de ips permitidas
        - mas abajo en las lineas de http_access allow localhost
        - http_access allow permitidos // para permitir el acceso a las ips de la lista
    - para bloquear dominios o paginas web nos haremos un nano con los dominios
        - nano /etc/squid/denegadas // para crear un archivo
            - www.tiktok.com
            - www.facebook.com
            - .tiktok.com // poner un punto al principio para bloquear todos los subdominios
            - .facebook.com
            - para bloquear expresiones en un dominio 
                - www.facebook.com/.* // para bloquear todo lo que este despues de la barra
                - www.facebook.com/.*.php // para bloquear todo lo que este despues de la barra y que termine en .php
                - para bloquear todas las expresiones que tengan facebook
                    - .*facebook.*
    - para bloquear busquedas con ciertas expresiones
        - nano /etc/squid/buscador // para crear un archivo
            - .*facebook.*
            - .*tiktok.*
    - para solo tengan acceso a ciertas paginas inocentes
        - nano /etc/squid/permitidos // para crear un archivo
            - www.google.com
            - www.youtube.com
            - www.wikipedia.com
    - para bloquear expresiones que contengan gov,musica, edu,mx, store
        - nano /etc/squid/expresiones // para crear un archivo
            - .*gov.*
            - .*musica.*
            - .*edu.*
            - .*mx.*
            - .*store.*
        - nano -c /etc/squid/squid.conf // para editar el archivo de configuracion
        - en la linea de insert your own rules here linea 1400
        - acl urls url_regex "/etc/squid/urls"
        - acl expresiones url_regex "/etc/squid/expresiones"
        - http_access allow ips !



    - nano -c /etc/squid/squid.conf // para editar el archivo de configuracion
        - en la linea de insert your own rules here linea 1400
        - acl dominios dstdomain "/etc/squid/dominios" // para crear una lista de dominios bloqueados
        - acl expresiones url_regex "/etc/squid/expresiones" // para crear una lista de expresiones bloqueadas
        - acl inocentes dstdomain "/etc/squid/inocentes" // para crear una lista de dominios permitidos
        - acl para crear una lista de dominios no permitidos
            - acl buscador url_regex "/etc/squid/buscador" // para crear una lista de dominios no permitidos
        - mas abajo en las lineas de http_access allow localhost
        - http_access allow all inocentes // para permitir el acceso a las ips de la lista
        - http_access deny expresiones !permitidos // para denegar el acceso a las expresiones de la lista 
        - http_access deny dominios // para bloquear el acceso a las ips de la lista
    - squid -k parse // para ver si hay algun error en la configuracion
    - /etc/init.d/squid restart // para reiniciar squid
    - si queremos ver el trafico que esta pasando por el proxy de una ip con tail -f
        - tail -f /var/log/squid/access.log | grep 192.168.207.128 // para ver el trafico de una ip
        - tambien podemos usar iftop
            - aptitude install iftop // para instalar iftop
            - iftop -i ens33

    - para activar la funcion de squid en modo transparente
        - nano -c /etc/squid/squid.conf // para editar el archivo de configuracion
        - en la linea de Squid normally listens to port 3128 linea 1900 aproximadamente
        - http_port 3128 transparent // para activar el modo transparente

    - para permitir una ip en el proxy y denegarle busquedas con ciertas expresiones
        acl permitidos src "/etc/squid/permitidos" // para crear una lista de ips permitidas
        acl buscador url_regex "/etc/squid/buscador" // para crear una lista de dominios no permitidos
        acl dominios dstdomain "/etc/squid/dominios" // para crear una lista de dominios bloqueados
        // para permitir el acceso a las ips de la lista y denegarle expresiones y dominios en una linea
        http_access allow permitidos !buscador !dominios

    - para bloquear las busquedas por horario a una cierta ip
        - nano -c /etc/squid/squid.conf // para editar el archivo de configuracion
        - en la linea de insert your own rules here linea 1400
        - acl permitidos src "/etc/squid/permitidos" // para crear una lista de ips permitidas
        - acl buscador url_regex "/etc/squid/buscador" // para crear una lista de dominios no permitidos
        - acl dominios dstdomain "/etc/squid/dominios" // para crear una lista de dominios bloqueados
        - acl horario time 08:00-18:00 // para crear un horario de 8 a 6
        - http_access allow permitidos horario !buscador !dominios // para permitir el acceso a las ips de la lista y denegarle expresiones y dominios en una linea
        - http_access deny buscador // para denegar el acceso a las ips de la lista
        - http_access deny dominios // para bloquear el acceso a las ips de la lista

## pfsense
    version 2.6.0
    architecure amd64
    descargar de la pagina: https://www.pfsense.org/download/

## SOPHOS
    - sophos es un antivirus que se puede instalar en un servidor y que se encarga de escanear los archivos que se suben al servidor
    - sophos se puede instalar en un servidor windows o linux
    - lo podemos descargar de la pagina: https://www.sophos.com/en-us/products/free-tools/sophos-antivirus-for-linux.aspx
    o tambien en https://docs.sophos.com/nsg/sophos-firewall/18.5/Help/en-us/webhelp/onlinehelp/VirtualAndSoftwareAppliancesHelp/VMware/VMwareInstall/index.html
    - por que me aparece error de acceso a la pagina?
        - porque el servidor no tiene acceso a internet
        el puerto por defecto de sophos es el 4444

## SARG
    - Practico
        - 1 tener un servidor web
        - 2 instalar el .deb de sarg (dpkg -i sarg_2.3.0-1_all.deb)
        - 3 sarg -x // para ejecutar sarg
        - 4 /etc/sarg/sarg.conf (/var/www/html) // para ver la configuracion de sarg

    - sarg depende de libc6 (>= 2.34); sin embargo:
      La versión de `libc6:amd64' en el sistema es 2.31-13+deb11u5.
      sarg depende de libldap-2.5-0 (>= 2.5.4); sin embargo:
      El paquete `libldap-2.5-0' no está instalado.
    - para actualozar la libreria libc6
        - aptitude install libc6 // para instalar la libreria libc6
        - aptitude install libldap-2.5-0 // para instalar la libreria libldap-2.5-0
        - dpkg -i sarg_2.3.0-1_all.deb // para instalar sarg
        - sarg -x // para ejecutar sarg
        - /etc/sarg/sarg.conf (/var/www/html) // para ver la configuracion de sarg
        - dentro del conf debemos cambiar el directorio de salida de los reportes
            - OutputDir /var/www/html/sarg

    
    
    - sarg es un programa que nos permite ver el trafico que pasa por el proxy
    - sarg se puede instalar en un servidor windows o linux
    - lo podemos descargar de la pagina: https://pkgs.org/download/sarg
    - ap

## DNS
    - aptitude install bind9 // para instalar el servidor dns
    - aptitude install bind9utils // para instalar las utilidades de bind9
    - aptitude install dnsutils // para instalar las utilidades de dns
    - nano -c /etc/bind/named.conf.local // para editar el archivo de configuracion
    - declaramos la zona directa
        zone "juas.com" { 
                type master;
                file "/var/lib/bind/juas.com.zone";
        };
    - y ahora en el mismo declaramos la zona indirecta
        zone "207.168.192.in-addr.arpa" { 
            type master;
            file "/var/lib/bind/207.168.192.zone";
        };
    - cp db.local /var/lib/bind/juas.com.zone // para copiar el archivo de configuracion de la zona directa
    - nano -c /var/lib/bind/juas.com.zone // para editar el archivo de configuracion de la zona directa
    - borramos todo y dejamos de esta manera
            ;
            ; BIND data file for local loopback interface
            ;
            $TTL    604800
            @       IN      SOA     localhost. root.localhost. (
                                            



                                                                    )      

            @       IN      NS      localhost.
            @       IN      A       127.0.0.1
            @       IN      AAAA    ::1
    - Ahora lo ponemos de la siguiente manera
        @       IN      SOA     adminSistem.juas.com. root.adminSistem.juas.com. (
                2022113001 //fecha de modificacion
                1H // tiempo de refresco
                30M // tiempo de reintentos
                1W // tiempo de expiracion
                86400 // tiempo de vida de la cache
        ) 
        @       IN      NS      adminSistem.juas.com. // nombre del servidor dns
        adminSistem.juas.com.   IN      A       192.168.207.100 // ip del servidor dns
        www     IN      CNAME   adminSistem.juas.com. // creamos un alias para el servidor dns
    - cp /var/lib/bind/juas.com.zone /var/lib/bind/207.168.192.zone // para copiar el archivo de configuracion de la zona indirecta
    - nano -c /var/lib/bind/207.168.192.zone // para editar el archivo de configuracion de la zona indirecta
    - borramos las de abajo y dejamos de esta manera 
        @       IN      NS      adminSistem.juas.com.
        100     IN      PTR     adminSIstem.juas.com.
    - /etc/init.d/named restart // para reiniciar el servicio de dns
    - dig @127.0.0.1 SOA juas.com // para ver la zona directa
    - dig @127.0.0.1 A www.juas.com // para ver la zona directa
    - para saber que esta bien nos debe aparecer 
        ANSWER SECTION:
    - ahora tenemos que irnos a la carpeta de:
    - nano /etc/resolv.conf // para editar el archivo de configuracion
    - y poner de esta manera
        search juas.com
        nameserver 192.168.207.100
    - nano -c /etc/bind/name.conf.options // para editar el archivo de configuracion
    - y ponemos de esta manera
        forwarders {
                8.8.8.8;
         };

         y en la parte de auto le ponemos no
    - /etc/init.d/named restart // para reiniciar el servicio de dns
    - /etc/init.d/networking restart // para reiniciar el servicio de networking
    - y hacemos ping a google donde deberiamos tener respuesta de ping exitoso

## Ahora haremos un dns scundario
    - nano -c /var/lib/bind/juas.com.zone // para editar el archivo de configuracion de la zona directa
    - y ponemos de esta manera
        @       IN      SOA     adminSistem.juas.com. root.adminSistem.juas.com. (
                2022113001 //fecha de modificacion
                1H // tiempo de refresco
                30M // tiempo de reintentos
                1W // tiempo de expiracion
                86400 // tiempo de vida de la cache
        ) 
        @       IN      NS      adminSistem.juas.com.
        @       IN      NS      adminSistem2.juas.com.
        adminSistem.juas.com.   IN      A       192.168.207.100
        adminSistem2.juas.com.   IN      A       192.168.207.200
        ftp     IN      A   192.168.207.200
        www     IN      CNAME   adminSistem.juas.com.

    - nano -c /var/lib/bind/207.168.192.zone // para editar el archivo de configuracion de la zona indirecta
    - y ponemos de esta manera
        @       IN      NS      adminSistem.juas.com.
        @       IN      NS      adminSistem2.juas.com.
        100     IN      PTR     adminSIstem.juas.com.
        200     IN      PTR     adminSIstem2.juas.com.
    
    - ahora en otra maquina instalamos los 3 paquetes de dns
    - nano -c /etc/bind/named.conf.local // para editar el archivo de configuracion
    - y ponemos de esta manera
        zone "juas.com" {
            type slave;
            file "/var/lib/bind/juas.com.zone";
            masterfile-format text;
            masters { 192.168.207.100; };
        };

        zone "207.168.192.in-addr.arpa" {
            type slave;
            file "/var/lib/bind/207.168.192.zone";
            masterfile-format text;
            masters { 192.168.207.100; };
        };
    - /etc/init.d/named restart // para reiniciar el servicio de dns
    - nano /etc/resolv.conf // para editar el archivo de configuracion
    - y ponemos de esta manera
        search juas.com
        nameserver 192.168.207.100
        nameserver 192.168.207.200
    - nano -c /etc/bind/name.conf.options // para editar el archivo de configuracion
    - y ponemos de esta manera
        forwarders {
            8.8.4.4;
        };
        y en la parte de auto le ponemos no
    - /etc/init.d/named restart // para reiniciar el servicio de dns
    - /etc/init.d/networking restart // para reiniciar el servicio de networking
    - y luego hacemos una pagina en apache
    - mkdir /var/www/ftp // para crear la carpeta
    - nano -c /var/www/ftp/index.html // para editar el archivo de configuracion\
    - y ponemos de esta manera
        <html>
            <head>
                <title>HOLLAA</title>
            </head>
            <body>
                <h1>HOLAAA</h1>
            </body>
        </html>
    - cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/ftp.juas.com.conf
    - nano -c /etc/apache2/sites-available/ftp.juas.com.conf 
    - editamos de esta manera
        ServerAdmin webmaster@juas.com
        DocumentRoot /var/www/ftp
    - a2ensite ftp.juas.com.conf // para activar el sitio
    - /etc/init.d/apache2 restart // para reiniciar el servicio de apache
    - a2dissite 000-default.conf // para desactivar el sitio
    - /etc/init.d/apache2 restart // para reiniciar el servicio de apache

## PROXMOX
    - para mas invormacion revisar la documentacion oficial de proxmox https://pve.proxmox.com/wiki/Storage
### ZFS
    - ZFS es un sistema de archivos de código abierto que proporciona una amplia variedad de características, incluyendo volúmenes de almacenamiento encriptados, copias de seguridad en tiempo real, compresión de datos, snapshots y mucho más.



## NETDATA - github stacer - webmin - ntopng


## LVM THIN
    - LVM-THIN es un tipo de volumen lógico que permite crear volúmenes lógicos de almacenamiento de datos que se pueden expandir y contraer dinámicamente, sin necesidad de mover los datos.
    - abrimos proxmox y abrimos ssh
    - vgcreate storage /dev/sdb 
    - lvcreate -L 9G -n lvmgui storage // donde lvmgui es el nombre del volumen logico y storage es el volumen fisico
    - lvremove /dev/storage/lvmgui 
    - para quitar un vg
    - vgremove storage
    - en proxmox nos vamos datacenter y vamos a storage
    - anadimos lvm
        id = lvmgui
        volumen group = storage
    - y add

    ahora haremos el otro disco
    - vgcreate thin /dev/sdc 
    - lvcreate -L 14G -T -n lvmthin thin 
    - en proxmox nos vamos datacenter y vamos a storage
    - anadimos lvm-thin
        id = lvmthingui
        volumen group = thin
        thin pool = lvmthin
    - y add




    - ahora vamos a crear el directorio donde se montara el disco sdd1
    - primero creamos el disco
    - fdisk /dev/sdd // creamos la tabla de particiones
    - n // creamos la particion
    - p // para particion primaria
    - 1 // para la particion 1
    - w // para guardar los cambios
    - mkfs.ext4 /dev/sdd1 // para crear el sistema de archivos
    - mkdir /mnt/directorio // para crear el directorio
    - mount /dev/sdd1 /mnt/directorio // para montar el disco

### Ahora borramos local-lvm y lo convertimos en directorio
    - en proxmox borramos el local-lvm
    - en la consola para borrar definitivamente usamos
        lvremove /dev/pve/data
    - 

### Crearemos una carpeta compartoda en proxmox
    - en proxmox vamos a
        - Datacenter
        - Storage
        - Add
        - SMB/CIFS
            id = carpeta compartida
            server = ip
            Username = usuario
            Password = contraseña
            Share = carpeta
### ahora haremos un cluster
    - nos vamos a datacenter
        - cluster
            cluster name = nombre del cluster
            cluster network = ip del cluster
            cluster network = ip de la maquina (pa q no t pierdas es la ip del https)
    - ahora para que otros cluster se conecten a este le damos a join information
    - y copiamos el comando que nos da
    - ahora nos vamos a otro cluster y le damos a join cluster
    - y pegamos el comando que nos dio el otro cluster
    - la password es la que tenemos en el que creo
    - para verificar que todo este bien en la linea de comandos escribimos 
        - pvecm status

### ahora para crear un contenedor
    - le damos click derecho a sistemas
    - y le damos a create CT y ponemos todo lo que nosm pide
    - y le damos a create
    - ahora para migrar en frio el contenedor a otro cluster le damos click derecho al contenedor y le damos a migrate
    - escojemos el cluster y le damos a migrate

### para crear un cluster desde linea de comandos
    - pvecm create CLUSTER1 --link0 10.10.10.11,priority=20 --link1 192.168.207.150,priority=20 // para crear el cluster
    // donde el link0 es la ip de la maquina principal y el link1 es la ip de la maquina oficial
    - en el otro hacemos 
    - pvecm add 192.168.207.150 -link0 10.10.10.13 -link1 192.168.207.152 // para unir el cluster
    // al principal y luego con los secundarios




## Para cualquier configuracion de proxmox 
    - cat /etc/pve/storage.cfg
    - cat /etc/pve/corosync.conf // para ver la configuracion del cluster


## TRUENAS
    - en el truenas nos vamos a 
    - creamos un disco
    - storage
    - pools
    - creamos un pool
    - ponemos un nombre
    - mostramos los discos
    - le damos click al disco y lo mandamos al otro lado con la flecha
    - forzamos y confirmamos
    - creamos otra vez y le damos confirmar
    - 
    - vamos a servicios
    - le damos encender a ISCSI 
    - que encienda automaticamente y editamos
    - le damos wizard
    - nombre: iscsi-truenas
    - Device
    - create new
    - buscamos nuestro disco
    - le damos siguiente 
    - create new
    - le ponemos 0.0.0.0
    - next hasta el final y listo
    - en proxmox 
    - storage
    - add
    - iscsi
    - le ponemos el nombre
    - le ponemos la ip del truenas
    - y automaticamente les aparecera el disco que creamos 
    - add y listo
    - si queremos ver que todo esta bien en el cli escribimos
    - cat /proc/partitions
### ahora le vamos a dar su cantidad de disco al disco
    - en proxmos vamos a Datacenter
    - Storage
    - add
    - LVM
        ID: lvm-iscsi
        Base storage: ponemos el disco que guardamos
        Base volume: automatico aparecera el disco que le pusimos
        Volume group iscsigui
        le damos click en shared y add

### Migracion en caliente y almacenamiento compartido
    - cat /proc/partitions // para ver los discos
    - apt-get install open-iscsi parted lsscsi // para instalar los paquetes
    - iscsiadm -m discovery -t sendtargets -p 192.168.207.139 
    - iscsiadm -m node -o show // para ver los nodos
    - iscsiadm -m node --login // para logearse
    - cat /proc/partitions // para ver los discos
    - vgcreate iscsigui /dev/sdc // para crear el volumen
    - nos vamos al proxmox main
    - storage
    - LVM
    - add
    - le ponemos el nombre
    - y activamos la funcion de share
    - hacemos los mismos pasos en el segundo proxmox hasta el login
    - ahora creamos un container en el proxmox main
    - le damos a create CT
    - le ponemos un nombre
    - le damos a next
    - ponemos el template
    - en storage le ponemos el lvmgiscsi
    - tamano 7 y terminamos de confirgurar
    - le damos a create
    - ahora que esta creado lo encendemos la maquina
    - y vamos a hacer una migracion en caliente
    - le damos click derecho al contenedor
    - y le damos a migrate
    - escogemos nuestro otro proxmox
    - y le damos a migrate
    - ahora que esta migrado veremos que esta encendido aun y migro completamente

### Alta disponibilidad - HA
    - la alta disponibilidad minimamente requiere 3 nodos
    - pvecm status // para ver el estado del cluster
    - nos vamos a datacenter
    - HA
    - groups
    - creamos un grupo
        - escogemos los dos nodos
        - escogemos nofailback
    - creamos
    - nos vamos a HA 
    - add
        VM 100
        Max restarts 3 //formula para poner n+1 donde n es el numero de nodos que tenemos
        Max relocate 3 
        escogemos el grupo que creamos
        Request State started
    - add

    - ahora para simular una caida debemos hacer
    - ponerle power off a la maquina principal
    - pvecm expected 1 // para ver que solo queda un nodo
    - ahora para simular que se recupero
    - le damos power on a la maquina principal
    - nos aparece un error en nuestro lvmgscsi
    - para arreglarlo debemos hacer nuevamente el procedimiento de almacenamiento compartido
    - iscsiadm -m discovery -t sendtargets -p 192.168.207.139 // la ip debe ser del truenas
    - iscsiadm -m node --login // para logearse
    - y listo

### Replicacion - ZFS
    - replicacion es para hacer una copia de seguridad de nuestros datos en otro nodo
    - nos vamos a un nodo
    - DIsks
    - ZFS
        name zfspool
        destiqueamos el add storage
        marcamos un disco
        raid level single Disk
        compression on
        ashift 12
    - creamos
    - hacemos lo mismo en el siguiente nodo
    - ahora en datacenter
    - storage
    - add
    - ZFS
        id zfspool
        ZFS pool zfspool
        nodes proxmox1 proxmox2
    - add
    - ahora creamos un contenedor con zfspool y listo
    - para activar la replicacion debemos irnos a la maquina que creamos 
    - nos vamos a replicacion
    - le damos a add
        Target proxmox2
        Schedule */30
    - creamos
    - y ahora ya nos aparece el volumen en el nodo dos

### Backup
    - nos vamos a la maquina
    - backup 
    - backup now
        mode snapshot
        compression zstd
    - esto es para hacer un backup manual

### Tareas de Backup
    - nos vamos a datacenter
    - backup
    - add
        mode snapshot
        compression zstd
        schedule */1:00
    - esto es para hacer un backup automatico cada hora        

### proxmox backup server
    - nos vamos a storage / disks 
    - en este caso haermos directory
        disk escogemos el disco
        file system ext4
        name (debe estar sin espacios) backup1
    - create

### para unir a nuestro proxmox
    - en el proxmox backup server
    - dashboard
    - show fingerprint
    - copiamos 
    - nos vamos al proxmox
    - datacenter
    - storage
    - add
    - proxmox backup server
        id beckupserver
        server (ip del proxmox backup server)
        username root@pam
        Datastore backup1 (este debe ser el mismo que creamos en el proxmox backup server)
        namespace vacio
        fingerprint (este debe ser el mismo que copiamos del proxmox backup server)
    - creamos

    - ahora para probar crearemos 6 backups de la maquina que tengamos en el proxmox pero que el storage este en backupserver
    - si nos vamos al backup server veremos en datastore
    - backup1
    - content
    - veremos las backups que acabamos de hacer
    - lo bueno de esto es que podemos verificar que los backups estan bien y que no se corrompieron
    - simplemente le damos a la V. 
    - si todo salio bien en cada linea de backups veremos un check verde si esta bien y un check rojo si esta mal
    - si queremos restaurar un backup debemos irnos a algun nodo 
    - nos vamos a backupserver
    - backup
    - escogemos un snapshot
    - le damos a restore
    - en CT ID le ponemos el numero que queramos
    - y restore

### TAREA DE CEPH - HIPERCONVERGENCIA
    - tarea
    - en cada nodo anadimos un disco de 25G o 30G
    - hacemos un cluster de 3 nodos
    - intalar ceph en cada nodo
    - en el nodo 1
    - ceph
    - debe instalarlo si 
    - pacific
    - start
    - una vez instalado
    - wizard 
    - le ponemos la misma ip
    - y listo
    - en los otros nodos hacemos lo mismo pero la ip sera automatica 

### CEPH - HIPERCONVERGENCIA
    - nos vamos al nodo 1
    - Ceph 
    - dato importante ir a monitor y tener a todos los nodos ahi para ello vamos estar ahi
    - y crear los nodos
    - hacemos lo mismo en manager
    - nos vamos a OSD
    - Create OSD
    - escogemos el disco y creamos
    - hacemos lo mismo en los otros nodos
    - nos vamos a ceph pool
    - creamos
        name CEPHPOOL
        size 3
        min size 2
        crush rule replicated_rule
        of pgs 128
        pgautoscale on
        add as storage chequeamos si
    - creamos
    - ahora creamos un contenedor en el cephpool
    - y si migramos se va de manera mas rapida
    - 


### ISCSI    
    - ISCSI es un protocolo de red que permite compartir dispositivos de almacenamiento entre diferentes equipos de una red.