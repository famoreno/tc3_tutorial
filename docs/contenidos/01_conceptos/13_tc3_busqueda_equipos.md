
## 🌐 Búsqueda de controladores remotos

!!! tip "Recomendación"
    Hay un video de ejemplo en el Campus Virtual en `Automatización > Videos > TC3` con nombre `9_Runtime_Target_*.mkv`.

En esta sección explicaremos cómo buscar controladores remotos en la red del laboratorio y cómo escanear los terminales/canales que tienen conectados.

### Búsqueda en red

Si queremos utilizar un controlador remoto (PLC), lo primero que debemos hacer es buscarlo en la red local del laboratorio y establecer una conexión con él. Para ello, seguiremos este procedimiento:

- Desplegar `Target` y seleccionar `Choose Target System...`.
    
    ![Imagen](../images/01_conceptos/target_umrt_default.png){width=150px}

    ![Imagen](../images/01_conceptos/choose_target_system.png){width=400px}

    - Pulsar sobre `Search (Ethernet)`
        
        !!! warning "Importante"
            Aceptar si aparece el siguiente mensaje: *Searching for remote system only possible from local system. Change back to local system*.
        
        - Se abre el siguiente cuadro de diálogo:

            ![Imagen](../images/01_conceptos/add_route_dialog.png){width=400px}

        - Seleccionar `🔳 Advanced Settings`.
        - Pulsar sobre el botón `Broadcast Search`.
            - Seleccionar los adaptadores de red en el *popup*.

                ![Imagen](../images/01_conceptos/select_adapter.png){width=400px}

        - Seleccionar el PLC de la lista que aparezca.
        - Marcar `🔳 IP Address`
        - Pulsar en el botón `Add Route`.
        - En el *popup* que aparece (**Add Remote Route**):
            - Deseleccionar `🔲 Secure ADS`
            - Escribir: `User` el que corresponda (Administrator, por defecto).
            - Escribir: `Password` la que corresponda (1, por defecto).
        - Observar que aparece una `x` en la columna *Connected*.
        - Cerrar el cuadro de diálogo pulsando `Close`.
    
    - Ahora debería aparecer el controlador en el listado del cuadro de diálogo `Choose Target System`:
        - Seleccionar el controlador en la lista y pulsar `OK`.
    - Si aparece un *popup* indicando que es necesario cambiar la plataforma, pulsar en `Yes`.

### Escaneado del controlador

!!! warning "Importante"
    Para poder hacer este proceso, debemos asegurarnos que TwinCAT 3 está en modo configuración (*Configuration Mode*) y no en ejecución (*Run Mode*).

    ![Imagen](../images/01_conceptos/tc3_modes.png){width=150px}

Comenzamos por buscar los dispositivos de entrada/salida conectados al controlador. Para ello:

- En el explorador de la solución (`Solution Explorer`):
    - Seleccionar: `I/O > Device`.
    - Pulsar en el menú `TwinCAT > Scan (BD Scan)` (alternativamente, **CD** sobre `I/O Device` y pulsar `Scan`).
    - Aceptar el mensaje de que no todos los dispositvos pueden encontrarse automáticamente.
    - Seleccionar únicamente el dispositivo EtherCAT y pulsar `OK`.
    - Aceptar la búsqueda de *boxes* (terminales) pulsando `Yes`.
    - Aceptar la activación del modo *Free Run* pulsando `Yes`.

- Observar el arbol de I/O en el explorador de la solución.
- Desplegar el elemento `EK1200` y verificar que la lista de terminales se corresponde con la configuración del controlador (en su documentación).

    !!! info "Info"
        Tened en cuenta que el terminal `EL9011` es un elemento virtual.

### Comprobación de los terminales

Ahora vamos a comprobar alguno de los terminales de E/S para asegurarnos de que tenemos acceso a ellos. Usaremos un ejemplo en el que tendremos un programa con una variable de entrada `i_PulsadorMarcha` y una variable de salida `o_LamparaMarcha`.

El procedimiento a seguir es el siguiente:

- Buscar en el listado de E/S del controlador la entrada correspondiente al pulsador de marcha:
    - Localizar el **Terminal** y el **Canal** de entrada especificado.
    - Desplegar el contenido del **Canal** y hacer **DC** sobre su `Input`.
    - Seleccionar la pestaña *Online* y verificar que se corresponde con el pulsador:
        - Accionar el pulsador de marcha y observar el cambio de valor mostrado en la gráfica.
    
    !!! warning "Importante"
        Se recomienda seleccionar la pestaña *Variable* y **cambiar el nombre** de `Input` por el nombre de la variable asociada en el listado de E/S (por ejemplo, `i_PulsadorMarcha`). 
        
        Este paso **NO** vincula el terminal/canal con la variable sino que simplemente lo renombra para ayudarnos a localizarlo posteriormente durante el proceso de vinculación.

- Buscar en el listado de E/S del controlador la salida correspondiente a la lámpara de marcha:    
    - Localizar el **Terminal** y el **Canal** de salida especificado.
    - Desplegar el contenido del **Canal** y hacer **DC** sobre su `Output`.
    - Seleccionar la pestaña *Online* y verificar que se corresponde con la lámpara:
        - Pulsar `Write`.
        - Pulsar alternativamente `0`/`1` y comprobar que la lámpara se enciende y se apaga.
    
    !!! warning "Importante"
        Se recomienda seleccionar la pestaña *Variable* y **cambiar el nombre** `Output` por el nombre de la variable asociada en el listado de E/S (por ejemplo, `o_LamparaMarcha`). 
        
        Este paso **NO** vincula el terminal/canal con la variable sino que simplemente lo renombra para ayudarnos a localizarlo posteriormente durante el proceso de vinculación.

Una vez realizado esto, guardamos el proyecto.
