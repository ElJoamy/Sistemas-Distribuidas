# Coneptos
## Introduccion
    - Que es administracion de sistemas?
        Administracion de sistemas es el conjunto de actividades que se realizan para mantener un sistema informatico en funcionamiento. Estas actividades incluyen la instalacion, configuracion, mantenimiento, soporte y administracion de redes, hardware, software, datos, usuarios y recursos de una organizacion.
    
    -  Que son los repositorios en Linux?
        Los repositorios son un conjunto de paquetes de software que se encuentran en un servidor centralizado. Estos paquetes se pueden instalar en cualquier equipo que tenga acceso a internet.

    - Que es el active direcotry?
        Active Directory es un servicio de directorio de Microsoft que permite a los administradores de sistemas gestionar los recursos de una red de computadoras. Active Directory es un servicio de directorio de Microsoft que permite a los administradores de sistemas gestionar los recursos de una red de computadoras.

## Jerarquia de Linux
    Tenemos este jerarquia:
    - /bin -> Binarios esenciales del sistema
    - /boot -> Ficheros estaticos utilizados por el cargador de arranque
    - /dev  -> ficheros de dispositivos
    - /etc  -> ficheros de configuracion
    - /home -> directorio de los usuarios
    - /lib  -> librerias del sistema
    - /media -> montaje de dispositivos
    - /mnt -> montaje de dispositivos
    - /proc -> informacion del sistema
    - /root -> directorio del usuario root
    - /sbin -> binarios del sistema
    - /run -> ficheros de estado del sistema
    - /sys -> informacion del sistema
    - /tmp -> ficheros temporales
    - /usr -> ficheros de aplicaciones
    - /var -> ficheros variables
    - /srv -> ficheros de servicios
    - /opt -> ficheros de aplicaciones opcionales

## Sistemas de ficheros
    - FAT32
    - NTFS
    - EXT2
    - EXT3
    - EXT4
    - XFS
    - BTRFS

    -ext4: Es la ultima version de la familia de sistemas de ficheros ext. Sus principales ventajas radican en su eficiencia (menor uso de CPU, mejoras en la velocidad de lectura y escritura) y en la ampliacion de los limites de tamano de ficheros y de volumenes. ext4 es el sistema de ficheros por defecto en la mayoria de las distribuciones Linux.

    - XFS: Es un sistema de ficheros de alto rendimiento, orientado a servidores, que se ha desarrollado para sustituir a ext3. XFS es el sistema de ficheros por defecto en Red Hat Enterprise Linux 5 y 6. XFS es el sistema de ficheros por defecto en Red Hat Enterprise Linux 5 y 6.

    - OpenZFS: Es un sistema de ficheros de codigo abierto que se ha desarrollado para sustituir a ext3. OpenZFS es el sistema de ficheros por defecto en OpenSolaris y en OpenIndiana.

## RAID
    RAID (Redundant Array of Independet Disks) los raids son un conjunto de discos que se unen para formar un solo disco virtual. Los discos que forman el raid se llaman discos miembros. Los discos miembros pueden ser de diferentes tamaños y pueden ser de diferentes tipos. Los discos miembros pueden ser de diferentes tamaños y pueden ser de diferentes tipos.

    Tipos de RAIDS:
    - RAID 0: Es un sistema de almacenamiento que combina dos o mas discos en un solo volumen. Los datos se dividen en bloques y se escriben en los discos de forma simultanea. El rendimiento de lectura y escritura es el doble que el de un solo disco. El rendimiento de lectura y escritura es el doble que el de un solo disco. 2 
    - RAID 1: Es un sistema de almacenamiento que combina dos o mas discos en un solo volumen. Los datos se dividen en bloques y se escriben en los discos de forma simultanea. El rendimiento de lectura y escritura es el doble que el de un solo disco. El rendimiento de lectura y escritura es el doble que el de un solo disco. 2
    - RAID 5: Es un sistema de almacenamiento que combina dos o mas discos en un solo volumen. Los datos se dividen en bloques y se escriben en los discos de forma simultanea. El rendimiento de lectura y escritura es el doble que el de un solo disco. El rendimiento de lectura y escritura es el doble que el de un solo disco. 3
    - RAID 6: Es un sistema de almacenamiento que combina dos o mas discos en un solo volumen. Los datos se dividen en bloques y se escriben en los discos de forma simultanea. El rendimiento de lectura y escritura es el doble que el de un solo disco. El rendimiento de lectura y escritura es el doble que el de un solo disco. 4
    - RAID 10: Es un sistema de almacenamiento que combina dos o mas discos en un solo volumen. Los datos se dividen en bloques y se escriben en los discos de forma simultanea. El rendimiento de lectura y escritura es el doble que el de un solo disco. El rendimiento de lectura y escritura es el doble que el de un solo disco.
    - RAID 50: Es un sistema de almacenamiento que combina dos o mas discos en un solo volumen. Los datos se dividen en bloques y se escriben en los discos de forma simultanea. El rendimiento de lectura y escritura es el doble que el de un solo disco. El rendimiento de lectura y escritura es el doble que el de un solo disco.
    - RAID 60: Es un sistema de almacenamiento que combina dos o mas discos en un solo volumen. Los datos se dividen en bloques y se escriben en los discos de forma simultanea. El rendimiento de lectura y escritura es el doble que el de un solo disco. El rendimiento de lectura y escritura es el doble que el de un solo disco.
    - RAID 100: Es un sistema de almacenamiento que combina dos o mas discos en un solo volumen. Los datos se dividen en bloques y se escriben en los discos de forma simultanea. El rendimiento de lectura y escritura es el doble que el de un solo disco. El rendimiento de lectura y escritura es el doble que el de un solo disco.

- Raid 
    referencia: https://www.mercadoit.com/blog/analisis-opinion-it/tipos-raid-y-sus-caracteristicas/
        -Que son los Raid?
            Es un sistema de almacenamiento de datos que combina dos o mas discos duros para crear un sistema de almacenamiento redundante. Los discos duros se combinan para proporcionar una mayor capacidad de almacenamiento, mayor velocidad de acceso a los datos y una mayor fiabilidad.
        - Tipos de Raid
            - Raid 0
                Nos ofrece tolerancia a fallos pero si mayor velocidad, algunos no consideran a esta configuracion como un RAID verdadero. Una configuracion RAID 0 con dos discos es hasta dos veces masa rapida que un solo disco duro.
                ejemplos de uso en: 
                    - Videojuegos
                    - Video
                    - Audio
                    - Imagen
                    - Base de datos
                    - Aplicaciones
            - Raid 1
                Tambien conocido como Mirror o espejo, este funciona anadiendo discos rigidos paralelos a los discos rigidos principales existentes en la computadora. De esta manera si por ejemplo una computadora posee 2 discos se puede anexar un disco rigido para cada uno, totalizando 4. los discos que fueron anadidos trabajan como una copia del primero.
                Nos ofrece tolerancia a fallos y velocidad, pero no mayor capacidad de almacenamiento. Una configuracion RAID 1 con dos discos es hasta dos veces mas rapida que un solo disco duro.
                SOLO INSTALAR EL SISTEMA OPERATIVO
            - Raid 5
                Este array ofrece tolerancia al fallo pero ademas optimiza la capacidad del sistema permitiendo una utilzacion de hasta 80% de la cpacidad del conjunto de discos.
                Este array ofrece tolerancia a fallos, velocidad y capacidad de almacenamiento. Una configuracion RAID 5 con tres discos es hasta tres veces mas rapida que un solo disco duro y puede perder un disco sin perder la informacion.
            - Raid 6
                Este array ofrece tolerancia al fallo pero ademas optimiza la capacidad del sistema permitiendo una utilzacion de hasta 80% de la cpacidad del conjunto de discos.
                Este array ofrece tolerancia a fallos, velocidad y capacidad de almacenamiento. Una configuracion RAID 6 minima con cuatro discos es hasta cuatro veces mas rapida que un solo disco duro y puede perder dos discos sin perder la informacion.
                el numero maximo de discos que se pueden utilizar en un array RAID 6 es de 18. No es recomendable tener tantos discos
                BDD, app web, app movil, app de escritorio
            - NO ES RECOMENDABLE TENER MAS DE 3 DISCOS EN UN RAID 5, PORQUE SE PUEDE PERDER LA INFORMACION DE LOS DISCOS QUE NO ESTAN EN EL RAID
            - NO ES RECOMENDABLE TENER MAS DE 4 DISCOS EN UN RAID 6, PORQUE SE PUEDE PERDER LA INFORMACION DE LOS DISCOS QUE ESTAN EN EL RAID 6
            - RAID: hardware y software
                - RAID hardware
                    Lo mas recomendable es que el RAID sea hardware, ya que es el mas rapido y el mas confiable. El RAID hardware es un sistema de almacenamiento que se encuentra integrado en la placa base de la computadora. Este tipo de RAID es el mas rapido y el mas confiable, pero tambien es el mas caro.
                    El RAID hardware es un sistema de almacenamiento que se encuentra integrado en la placa base de la computadora. Este tipo de RAID es el mas rapido y el mas confiable, pero tambien es el mas caro.
                - RAID software
                    El RAID software es un sistema de almacenamiento que se encuentra integrado en el sistema operativo de la computadora. Este tipo de RAID es el mas barato y el mas facil de instalar, pero tambien es el mas lento y el menos confiable.

    Si tenemos 6 discos y queremos utilizar raid 5 necesitamos 5 discos para almacenar datos y 1 disco para almacenar la informacion de paridad. Si tenemos 6 discos y queremos utilizar raid 6 necesitamos 4 discos para almacenar datos y 2 discos para almacenar la informacion de paridad.

## Velocidades de Discos Duros
    - 5400 RPM
    - 7200 RPM
    - 10000 RPM
    - 15000 RPM

    - 5400 RPM: Es la velocidad de rotacion de los discos duros. Los discos duros de 5400 RPM son los mas economicos y los mas lentos. Los discos duros de 5400 RPM son los mas economicos y los mas lentos.
    - 7200 RPM: Es la velocidad de rotacion de los discos duros. Es la velocidad de los discos duros para servidores y para ordenadores de sobremesa. Es la velocidad de los discos duros para servidores y para ordenadores de sobremesa.

## Que es LVM
    Logical Volume Manager (LVM) permite una capa de abstracion entre el sistema operativo y las particiones/discos que utiliza. En la administracion de discos tradicionales de un sistemas operativo se busca que los discos esten disponibles en (/dev/sa1, /dev/sda2, etc.).
    Con LVM los discos y particiones se puede abstraer de contener varios discos y particiones en un solo dispositivo. Los sistemas operativos no notara la diferencia entre un disco y un conjunto de discos.

    Tiene lasiguiente structura:
        - Disk Drive
            - Physical Volume
                - Phisical Partition
                    - Logical Volume
                        - Logical Partition

    ## Volumen fisico
        Es un disco o particion que se puede utilizar para crear un volumen logico. Un volumen fisico puede ser un disco duro, una particion o un conjunto de discos duros o particiones.
    ## Volumen group
        Es un grupo de volumenes fisicos que se pueden utilizar para crear un volumen logico. Un volumen group puede ser un disco duro, una particion o un conjunto de discos duros o particiones.

## En que casos se usaria LVM
    3 de 10
    2 de 20 o 30

## Tipos de Hipervisores
    - Tipo 1
        Un hipervisor simple (tipo 1) es una capa de software que instalamos directamente sobre un servidor fisico y su hardware subyacente.
        Ejemplos:
            - VMware ESXi
            - Proxmox
            - Citrix XenServer
        
    - Tipo 2
        Un hipervisor de host (tipo 2) es un software que se instala sobre un sistema operativo existente, como Windows o Linux.
        Ejemplos:
            - VMware Workstation
            - VMware Player
            - VirtualBox
            - Parallels Desktop
            - Hyper-V
    
    - KVM 
        KVM es un hipervisor de tipo 2 que se ejecuta sobre Linux. La mquina virtual basada en el nucleo es una tecnologia de virtualizacion que permite a los sistemas operativos invitados ejecutarse directamente en el nucleo del sistema operativo del anfitrion. Esto significa que los sistemas operativos invitados no necesitan un hipervisor para ejecutarse, lo que reduce la sobrecarga y mejora el rendimiento.
    
    - Open-VZ
        OpenVZ es un hipervisor de tipo 1 que se ejecuta sobre Linux. OpenVZ es un sistema de virtualizacion de contenedores que permite a los sistemas operativos invitados ejecutarse directamente en el nucleo del sistema operativo del anfitrion. Esto significa que los sistemas operativos invitados no necesitan un hipervisor para ejecutarse, lo que reduce la sobrecarga y mejora el rendimiento.
        => Un container es una maquina virtual que se ejecuta sobre el nucleo del sistema operativo del anfitrion. 

## Que es proxmox
    Proxmox VE esta disenado para explotar completamente la potencia y la flexibilidad de los procesadores modernos y las tecnologias de virtualizacion. Proxmox VE es un hipervisor de tipo 1 que se ejecuta sobre Linux. Proxmox VE es un sistema de virtualizacion de contenedores que permite a los sistemas operativos invitados ejecutarse directamente en el nucleo del sistema operativo del anfitrion. Esto significa que los sistemas operativos invitados no necesitan un hipervisor para ejecutarse, lo que reduce la sobrecarga y mejora el rendimiento.

    - caracteristicas
        * Configuracion y restauracion de maquinas virtuales

## Topologia truenas
    - https://jamboard.google.com/d/1fBsiLovSZbNzdDpfz42GabFGPZeoNDlKunC55YcOIvE/viewer
    
## copias de seguridad en proxmox
    - Guarda una copia de la maquina virtual (KVM o LXC) en un archivo
    
## CEPH - HIPERCONVERGENCIA
    - Que es ceph?
        Ceph es un sistema de almacenamiento de objetos distribuido, libre y de codigo abierto. Ceph ofrece almacenamiento de alta disponibilidad, escalabilidad y rendimiento. Ceph se puede utilizar para almacenar datos de objetos, archivos y bloques y se puede utilizar como un sistema de archivos distribuido.

    - ceph se divide en:
        + Ceph Monitor
        + Ceph Managers

    - CRUSH (Controlled Replication Under Scalable Hashing)
        CRUSH es un algoritmo de distribucion de datos que se utiliza para distribuir datos en un cluster de almacenamiento distribuido. 

    - VSAN (VMware Storage Area Network)
        VSAN es un sistema de almacenamiento de datos distribuido que se ejecuta sobre el hardware de almacenamiento de la infraestructura de la red de almacenamiento de VMware. VSAN es un sistema de almacenamiento de datos distribuido que se ejecuta sobre el hardware de almacenamiento de la infraestructura de la red de almacenamiento de VMware.
    
    - lo negativo de vsan es que cvuando t estas quedando sin espacion debes agregar un nuevo nodo de almacenamiento, lo cual es un proceso costoso y tedioso.

    - osd (object storage daemon)
        Un objeto de almacenamiento de objetos (OSD) es un proceso que almacena datos en un cluster de almacenamiento de objetos distribuido. Un OSD es un proceso que almacena datos en un cluster de almacenamiento de objetos distribuido.

## Que es un cluster 
    Este tipo desistemasse basa en la union devariosservidoresque trabajan comoside uno solo se tratase. Los sistemas cluster han evolucionado mucho desde su primera aparicion, ahora se pueden crear distintos tipos de cluser en fucion de lo que senecesita:
        - Union de Hardware
        - Union de Software
        - Altp rendimiento de bases de datos
    Que caracteristicas y que beneficios nos da los clusters?
        - Alta disponibilidad
        - Alta escalabilidad
        - Alto rendimiento
        - Equilibrio de carga
    
    Cual serian las partes mas importantes para crear un cluster?
        - Servidores
        - Software
        - Red
        - Almacenamiento
## Que es shadow?
    Shadow es un sistema de archivos que contiene informacion sobre las contrasenas de los usuarios del sistema.