## 💾 Guardar y mover proyectos

!!! warning "Importante"
    Se ha detectado que el sincronizar la carpeta del proyecto usando servicios como **Google Drive** está produciendo problemas a la hora de poder abrir los proyectos. Posiblemente esto se deba a que algunos ficheros no son sincronizados correctamente por Drive (por motivos desconocidos), lo que lleva a que, a la hora de abrir el proyecto, no se carguen los ficheros necesarios. 
    
    **Se recomienda, por tanto, no usar este método sino alguno de los otros.**

### Usando la carpeta completa

1. Es la manera más sencilla de llevarse un proyecto desde un equipo a otro.
2. Solo hay que copiar la carpeta raíz en un *pendrive* y pegar la carpeta en el equipo destino.

    ![Imagen](../images/01_conceptos/image%2017.png){width=132px}

4. Posteriormente, hacer **DCI** sobre el fichero de ***Solution*** (`.sln`) para que se abra de nuevo en TC3.

!!! warning "Importante"
    Si la carpeta ha sido comprimida para ser trasladada, hay que asegurarse de haber descomprimido la carpeta completa en el destino antes de abrir el proyecto.

### Guardando como `.tnzip`

!!! warning "Importante"
    La entrega final del proyecto deberá seguir este procedimiento.

1. Este proceso genera el mínimo tamaño posible para trasladar un proyecto.
2. Seleccionar `File → Save [nombre_del_proyecto] as Archive...`.
3. Seleccionar dónde guardar el proyecto, darle un nombre y asegurarse de que el formato es de tipo `.tnzip`.

#### Abrir un fichero `.tnzip`
Una vez movido el fichero `.tnzip` al equipo destino, para volver a abrir el proyecto, seguimos este procedimiento:

- Abrir TC3.
- Seleccionar `File → Open → Solution from Archive...`.
- Buscar el archivo `.tnzip`.
- Seleccionar (o crear si no existe) la carpeta donde queremos que se genere la *Solution*.
   
!!! tip "Sugerencia"
    En principio, se puede seleccionar siempre la misma carpeta cada vez que se repita este procedimiento.

!!! warning "Importante"
    Si al abrir el proyecto de nuevo y compilar obtienes errores no relacionados con el código que antes no tenías:

    - Cambiar el tipo de proyecto a TwinCAT RT (x86)
    - Recompilar
    - Volver a cambiar a TwinCAT RT (x64)
    - Volver a recompilar

### Usando GIT

TwinCAT3, al estar basado en Visual Studio, tiene compatibilidad directa con GitHub. 
Se recomienda seguir el tutorial en este video:

[PLC Programming using TwinCAT 3 - Version control](https://www.youtube.com/watch?v=1g6eYnlzKtA)

