# 🏗️ Crear un Proyecto

## Abrir TwinCAT XAE

- Buscar en el menú de inicio de Windows la aplicación **TwinCAT XAE Shell**.

![Acceso a TwinCAT XAE desde el menú Inicio](./img/open-tc3-xae-start-menu.png){ width="400px" }

- También es accesible desde la barra de tareas (junto al reloj de Windows).
    - Hacer clic derecho en :material-mouse-right-click: **TwinCAT** y seleccionar **TwinCAT XAE (TcXAEShell)**.

![Icono de TwinCAT XAE en la barra de tareas](./img/open-tc3-xae-taskbar.png){ width="300px" }

Tras cargar la aplicación se muestra la pantalla inicial de la aplicación.

![Ventana principal de TwinCAT XAE](./img/tc3-xae-main-window.png){ width="600px" }

## Crear un Proyecto TwinCAT 3

### Seleccionar el Tipo del Proyecto

- Seleccioanr el tipo de proyecto: **TwinCAT XAE Project (XML format)**
- En el menú de la aplicación: **File** > **New** > **Project**.
- En la página de inicio: **Open** > **New Project** > **New TwinCAT Project...**.

 ![Selección del tipo de proyecto TwinCAT](./img/tc3-xae-new-project.png){ width="400px" }

??? info "Parámetros"
    - **Name** = nombre del proyecto TwinCAT.
    - **Location** = carpeta donde se alojará la solución.
    - **Solution name** = nombre de la solución (normalmente, el mismo que el nombre del proyecto).
    - **Create directory for solution** = **SI**/**NO** (creará la solución dentro de una carpeta con el nombre de la solución).
    - **Create new Git repository** = **SI**/**NO** (inicia el control de versiones con Git).

 Se mostrará la nueva solución «vacía».

 ![Solución TwinCAT recién creada](./img/tc3-xae-empty-twincat-project.png){ width="600px" }

### Ocultar Configuraciones

Para despejar el panel de exploración de la solución, ocultar las configuraciones innecesarias.

- Hacer clic derecho en :material-mouse-right-click: **[configuración]** y seleccionar **Hide [configuración] Configuration**.

![Menú contextual para ocultar una configuración](./img/tc3-xae-hide-configuration-command.png){ width="200px" }

!!! note "Recomendación"
    - Ocultar las configuraciones que no se van a utilizar: `MOTION`, `SAFETY`, `C++`, `VISION`, `ANALYTICS`.
    - Mantener las configuraciones **SYSTEM**, **PLC** e **I/O**.

![Configuraciones ocultas en el explorador de la solución](./img/tc3-xae-configuration-hidden.png){ width="300px" }

## Crear un Proyecto PLC

1. Para crear un nuevo proyecto PLC, dentro de un proyecto TC.

    - Hacer clic derecho en :material-mouse-right-click: **PLC** > **Add New Item**.

    ![Menú para añadir un elemento al proyecto PLC](./img/tc3-xae-plc-add-new-item.png){ width="200px" }

2. En la ventana emergente, seleccionar **Standard PLC Project**, asignarle un nombre al proyecto PLC y pulsar **Add**.

    ![Ventana para crear un proyecto PLC](./img/tc3-xae-plc-add-new-item-window.png){ width="400px" }

    ??? info "Proyecto Estándar"
        Al selecionar un proyecto PLC estándar se aplica una plantilla predeterminada que incluye:

        - Una tarea tiempo real `PlcTask` con un tiempo de ciclo de 10 ms.
        - Un programa `MAIN` vinculado a la tarea `PlcTask`.
        - Un conjunto de librerías básicas: Tc2_Standard, Tc2_System y Tc3_Module.
        - Un conjunto estructurado de carpetas (DUTs, GVLs, POUs, VISUs).

    Tras la creación, se muestra el nuevo proyecto PLC en el panel del explorador de la solución.

    ![Proyecto PLC recién creado en el explorador](./img/tc3-xae-blank-plc-project.png){ width="300px" }

    ??? info "Descripción"
        - **Project** = código fuente estructurado bajo la norma IEC 61131-3.
        - **Instance** = instancias de las variables de E/S del proyecto para la vinculación con los canales de E/S del sistema.

    Y si se despliega su contenido, se muestra la estructura de carpetas y nodos que contiene.

    ![Árbol expandido del proyecto PLC](./img/tc3-xae-plc-project-expanded.png){ width="300px" }

    ??? info "Descripción"
        - **External Types** = declaración de tipos de datos complejos e interfaces que provienen de bibliotecas externas.
        - **References** = listado de bibliotecas vinculadas al proyecto.
        - **DUTs** (*Data Unit Types*) = declaración de los tipos de datos de usuario.
        - **GVLs** (*Global Variable Lists*) = listas de variables globales.
        - **POUs** (*Program Organization Units*) = conjunto de módulos que componen el proyecto.
        - **VISUs** = visualizaciones, interfaces gráficas.
        - **PlcTask** = llamada al programa de ejecución cíclica.

### Crear una POU

1. Para añadir un nuevo POU.

    - Hacer clic derecho en :material-mouse-right-click: **POUs** > **Add** > **POU...**.

    ![Menú contextual para añadir un POU](./img/tc3-xae-add-pou-command.png){ width="400px" }

2. Cumplimentar los datos correspondientes en la ventana emergente **Add POU**.

    ![Ventana de creación de un POU](./img/tc3-xae-add-pou-window.png){ width="300px" }

    ??? info "Descripción"
        - **Name** = nombre del POU.
        - **Type** = tipo de POU (programa, bloque funcional o función).
        - **Implementation language** = lenguaje en el que se codificará el POU (CFC, FBD, IL, LD, SFC, ST, SC).

3. Se mostrará el nuevo POU «vacío».

    ![Editor con un POU vacío](./img/tc3-xae-blank-sfc-fb.png){ width="500px" }

## Implementar un POU

Al desplegar **POUs** se muestra la lista de módulos de programación (programas, bloques funcionales y funciones) del proyecto.

![Lista de POUs del proyecto](./img/tc3-xae-pou-list.png){ width="300px" }

Hacer clic en **POUs** > **[POU]** para abrir su contenido.

![Editor con un POU vacío](./img/tc3-xae-blank-sfc-fb.png){ width="500px" }

El contenido de un POU se muestra separado:

- En la ventana superior denominada `Parte de Declaración` se encuentra el **Encabezado del POU** y los **Bloques de Declaración**.
- En la ventana inferior denominada `Parte de Implementación` se muestra el código del POU en el lenguaje seleccionado.

### Declarar una Variable

Para crear una variable escribir su declaración siguiendo la siguiente sintaxis:

```iecst
Identificador [AT %Localización]: Type [:= ValorInicial];
```

1. **Identificador** (obligatorio). Es el nombre único de la variable dentro de su ámbito (scope).
2. **Localización** (opcional). La localización o **Ubicación Directa** establece la zona y la posición de memoria en la que se situará la variable.
    - Modificador de localización `AT`.
    - Dirección.

        ```iecst
        %[Área] [Tamaño] [Dirección]
        ```

        - `%`: prefijo de ubicación.
        - Área: `I` para entradas, `Q` para salidas y `M` para memoria interna (o de marcas).
        - Dirección:
            - Absoluta:

                ```iecst
                [Area][Tamaño][Dirección]
                ```

                - Tamaño [X/B/W/D/L]: prefijo que indica el tamaño de la variable (Bit/Byte/Palabra/Doble/Larga).
                - Dirección [palabra.bit]: posición de la variable en el área de memoria.

                ??? info "Ejemplo"
                    ```iecst
                    Pulsador AT %IX0.0: BOOL;
                    ```

            - Inespecificada: utilizando el carácter comodín `*`

                ??? info "Ejemplo"
                    ```iecst
                    Pulsador AT %*: BOOL;
                    ```

3. **Separador de tipo:** (obligatorio). Separa el nombre de la variable de su tipo.

4. **Tipo de dato**: Especifica principalmente el tamaño y el rango de la variable. Puede ser un tipo elemental (BOOL, INT, REAL, TIME,...), complejo (STRUCT, ENUM, ARRAY,...) o de usuario.
5. **Valor inicial**: Especifica el valor de la variable al iniciar el runtime. Si no se especifica tomará el valor predeterminado para ese tipo de variable.
6. **Delimitador ;** (obligatorio). Terminador de instrucción.  

### Ámbito de una Variable

El bloque de declaración determina el ámbito y el alcance de la variable especificando quién y cómo puede acceder a la variable o parámetro.

   1.  `VAR ... END_VAR`: variables locales, internas al POU. Únicamente accesibles dentro del POU en el que se declaran.
   2.  `VAR_INPUT ... END_VAR`: parámetros de entrada. Pueden ser escritos desde el exterior.
   3.  `VAR_OUTPUT ... END_VAR`: parámetros de salida. Pueden ser leídos desde el exterior.
   4.  `VAR_IN_OUT ... END_VAR`: parámetros de entrada/salida por referencia. Punteros a variables externas que pueden leerse y escribirse dentro del POU.
   5.  `VAR_GLOBAL ... END_VAR`: variables globales (GVL). Accesibles desde cualquier POU del proyecto.
   6.  `VAR_STAT ... END_VAR`: variables estáticas. Variables locales que conservan su valor entre ciclos de ejecución.
   7.  `VAR_PERSISTENT ... END_VAR`: variables persistentes. Variables que conservan su valor incluso tras la pérdida de alimentación.

## Desplegar un Proyecto

El proceso de despliegue abarca la secuencia desde la validación del código fuente hasta la ejecución en tiempo real sobre el runtime  del sistema destino (*Target*).

### Seleccionar Sistema Destino

> El sistema destino (**Target System**) es el *runtime* de tiempo real sobre el que se ejecuta el código máquina del programa.

- Hay tres tipos de sistemas destino seleccionables:
    - **Local Target**: presente en el mismo ordenador en el que se está desarrollando el programa.
    - **Remote Target**: equipo físico remoto conectado por EtherCAT.
    - `UmRT_Default`: runtime que se ejecuta en modo usuario sin capacidades de tiempo real.
- Para seleccionarlo basta con elegirlo de la lista de runtimes disponibles en la barra de herramientas de TwinCAT.

![Lista de sistemas destino TwinCAT](./img/tc3-xae-target-system-list.png){ width="200px" }

#### Activar Licencia

- TwinCAT pone a disposición de aprendices y desarrolladores licencias de pruebas (*trial licenses*) que se solicitan cuando se intenta utilizar determinados servicios o funcionalidades.

    ![Ventana para generar una licencia de prueba](./img/tc3-xae-generate-trial-licenses-window.png){ width="300px" }

- Para activarlas se debe introducir el código de seguridad cuando sea solicitado.

    ![Ventana para introducir el código de seguridad](./img/tc3-xae-enter-security-code-window.png){ width="300px" }

#### Crear una Ruta

> En TwinCAT una ruta (route) es una conexión lógica entre dos entornos TwinCAT. Habitualmente se establece una ruta entre el entorno de ingeniería (TwinCAT XAE) en el que se desarrolla el proyecto y el runtime o entorno de ejecución (TwinCAT XAR) en el que se ejecuta el proyecto.

Una ruta sirve básicamente para establecer una relación de confianza entre ambos dispositivos (entorno de desarrollo y entorno de ejecución), para permitir, entre otras cosas, la transferencia de código y monitorización de vararibles.

- Seleccionar en la lista de sistemas destino **Choose Target System...**.

    ![Lista de sistemas destino](./img/lista-sistemas-destino.png){ width="200px" }

- En la ventana emergente **Choose Target System...**, pulsar **Search (Ethernet)...** para buscar sistemas TwinCAT en la red.
  
    ![Ventana inicial para elegir el sistema destino](<./img/choose-target-system-window-initial.png>){ width="400px" }

- Pulsar Aceptar si aparece el aviso TcXaeShell indicando que para buscar sistemas remotos debe hacerse desde el sistema local.
  
    ![Aviso para volver al sistema local antes de buscar rutas](./img/tcxaeshell-back-to-local.png){ width="300px" }

- En la ventana emergente **Select Adapter(s)**, seleccionar los dispositivos de red a través de los cuales se va a realizar la búsqueda y pulsar **OK**.

    ![Selección de adaptadores de red](./img/select-adapter-window.png){ width="300px" }

- Si la ventana emergente **Add Remote Route** aparece reducida, seleccionar **Advanced Settings** para mostrar todas las opciones.

    ![Ventana de ruta remota con opciones avanzadas](./img/add-remote-route-1.png){ width="400px" }

- Con todas las opciones disponibles, seleccionar **IP Address** y pulsar **Broadcast Search...**.

    ![Configuración de búsqueda de sistemas TwinCAT por difusión](./img/add-remote-route-2.png){ width="400px" }

- Se actualizará la lista de dispositivos TwinCAT encontrados. Seleccionar el sistema destino y pulsar **Add Route...**.

    ![Resultados de la búsqueda de sistemas TwinCAT](./img/add-remote-route-2.png){ width="400px" }

- A continuación se mostrará la ventana **Add Remote Route** para conectar con el sistema destino. Desmarcar la casilla **Secure ADS** si no se exige una conexión segura.
  
    ![Credenciales para una ruta remota segura](./img/add-remote-route-credentials-secure.png){ width="400px" }

- Introducir las credenciales de usuario y contraseña del |dispositivo seleccionado.

    ??? Info "credenciales"
        Con los ajustes de fábrica el usuario es `Administrator` y la contraseña `1`.

    ![Credenciales para una ruta remota no segura](./img/add-remote-route-credentials-non-secure.png){ width="400px" }

- Si la ruta se crea correctamente, aparecerá una `x` en el campo **Connected**, junto al nombre del sistema destino (CX-840BD9), en la ventana **Add Remote Dialog**.

    ![Ruta remota conectada en el diálogo](./img/add-remote-dialog-connected.png){ width="400px" }

- Tras cerrar la ventana **Add Remote Dialog** pulsando **Close**, seleccionar el sistema destino (CX-840BD9) en la lista y pulsar **OK**.

    ![Ventana para confirmar el sistema destino seleccionado](<./img/choose-target-system-window-final.png>){ width="300px" }

- Pulsar **Sí** en la ventana emergente **TcXaeShell** para permitir que el compilador genere código compatible con la plataforma del sistema destino si difiere de la plataforma actual.

    ![Confirmación para cambiar la plataforma de la solución](./img/tcxaeshell-change-solution-platform.png){ width="300px" }

!!! success "Resultado de la operación"
    Finalmente, nuevo sistema destino (CX-840BD9) y la versión de la plataforma (TwinCAT RT (x86)) aparecerán actualizados en la barra de botones de la aplicación.

    ![Sistema destino y plataforma seleccionados en TwinCAT](./img/target-on-button-bar-zoom.png){ width="600px" }

### Configurar Entrada/Salida

> Configurar la Entrada/Salida es el proceso mediante el cual se buscan los dispositivos y terminales presentes en el bus EtherCAT, se localizan, se verifican y se nominan los canales de entrada y salida, se vinculan las variables con los canales de entrada y salida y, finalmente se activa esta configuración en el sistema destino.

#### Buscar Dispositivos

- Poner el sistema en modo configuración pulsando **Restart TwinCAT (Config Mode)** en la barra de TwinCAT o seleccionando **TwinCAT** > **Restart TwinCAT (Config Mode)**.
- Buscar dispositivos en **I/O** > **Devices** del Explorador de la Solución y pulsar **Scan** en la barra de TwinCAT; alternativamente, hacer clic derecho en :material-mouse-right-click: **Device** > **Scan** o elegir **TwinCAT** > **Scan**.

    ![Menú contextual para buscar dispositivos](./img/command-scan-popup.png){ width="200px" }

    !!! success "Resultado de la operación"
        Tras unos instantes se mostrará la lista de dispositivos encontrados.

        ![Lista de dispositivos encontrados en el escaneo](./img/io-devices-found.png){ width="400px" }

- Seleccionar los dispositivos deseados (al menos el dispositivo `EtherCAT`) y pulsar **OK**.

    !!! success "Resultado de la operación"
        Los nuevos dispositivos aparecerán bajo **I/O** > **Devices** en el Explorador de la Solución.

        ![Dispositivos EtherCAT en el árbol de E/S](./img/io-device-list.png){ width="300px" }

- Autorizar, en la ventana emergente, la búsqueda de terminales (*boxes*).

    ![Confirmación para buscar terminales EtherCAT](./img/scan-for-boxes.png){ width="200px" }

    !!! success "Resultado de la operación"
        Tras unos instantes, los nuevos terminales aparecerán bajo el dispositivo correspondiente.

        ![Terminales detectados bajo el dispositivo EtherCAT](./img/io-boxes-list.png){ width="300px" }

- Activar el modo Free Run pulsando **Sí**.
  
    ![Confirmación para activar el modo Free Run](./img/activate-freerun.png){ width="200px" }

    ??? Info "Free Run"
        El modo Free Run es una función especial que permite leer el estado de las entradas y forzar o escribir valores en las salidas físicas sin necesidad de tener un programa (PLC) cargado o ejecutándose.

- Deshabilitar los dispositivos que no se vayan a utilizar: hacer clic derecho en :material-mouse-right-click: **[dispositivo]** y seleccionar **Disable**.

    ![Menú contextual para deshabilitar un dispositivo](./img/io-disable-device.png){ width="300px" }

    !!! success "Resultado de la operación"
        Los dispositivo deshabilitados quedan marcados.

        ![Dispositivos deshabilitados en el árbol de E/S](./img/io-disabled-devices.png){ width="300px" }

#### Identificar Entradas

!!! goal "Objetivo"
    Lo que se pretende en este paso es localizar, en la sección de entrada/salida (**I/O**) del árbol del Explorador de la Solución, los canales en los que están conectadas físicamente las señales de entrada, verificar su funcionamiento y ponerles un nombre, para posteriormente facilitar su vinculación a sus correspondientes variables del proyecto PLC.

- Hacer **doble clic** sobre el primer **canal** del primer **terminal** de entrada (`EL1008`) situado bajo **acoplador de bus virtual** `EK1200`.

    ![Canal de entrada del terminal EL1008](./img/io-el1008-input-channel.png){ width="300px" }

    ??? Info "Cabeceras de Bus"
        Una cabecera de bus, en el entorno Beckhoff, es cualqueir dispositivo, módulo físico o interfaz virtual, que actúa como punto de entrada, alimentación o pasarela de comunicación para un conjunto de terminales de entrada/salida subordinados.

        - **Acopladores**: cabeceras de bus físicas como el `EK1100`, que extiende el bus más alla del controlador.
        - **Cabeceras virtuales**: representan la interfaz con el bus interno del controlador (`EK1200`).
        - **Interfaces de Bus**: cambian las características del bus, como el `BK1250`, que permite la conexión de módulos con **bus K** en un bus **EtherCAT**.
        - **Maestros de Red**: cabeceras de buses de otros protocolos, como el `KL6211`, que actúa como maestro de bus **ASi**.

- Seleccionar la pestaña **Online**.

    ![Pestaña Online del canal de entrada](./img/io-input-channel-online.png){ width="300px" }

- Localizar, consultando la tabla de entrada/salida en la descripción funcional del sistema el dispositivo conectado a ese canal (por ejemplo, el pulsador de marcha). Activarlo y verificar en la pantalla que cambia de valor la señal mostrada.

    ![Canal de entrada activado en la vista Online](./img/io-input-channel-online-active.png){ width="300px" }

- Si se reflejan los cambios en la pantalla, queda verificada la correspondencia entre el canal y el dispositivo. Nombrar el canal con el nombre del dispositivo en el campo **Name** de la pestaña **Variable**.

    ![Nombre asignado al canal de entrada](./img/io-input-channel-variable.png){ width="300px" }

!!! note "🔄 Repetir"
    Repetir este proceso de identificación para todos los canales de entrada digitales y analógicos conectados.

!!! success "Resultado de la operación"
    Todos los canales de entrada del sistema nominados.

    ![Canales del terminal EL1008 con nombre](./img/io-el1008-tagged.png){ width="300px" }

#### Identificar Salidas

!!! goal "Objetivo"
    Lo que se pretende en este paso es localizar, en la sección de entrada/salida (**I/O**) del árbol del Explorador de la Solución, los canales en los que están conectadas físicamente las señales de salida, verificar su funcionamiento y ponerles un nombre, para posteriormente facilitar su vinculación a sus correspondientes variables del proyecto PLC.

- Hacer **doble clic** sobre el primer **canal** del primer **terminal** de salida (`EL2004`) situado bajo **acoplador de bus virtual** `EK1200`.

    ![Canal de salida del terminal EL2008](./img/io-el2008-output-channel.png){ width="300px" }

- Seleccionar la pestaña **Online**.

    ![Pestaña Online del canal de salida](./img/io-output-channel-online.png){ width="300px" }

- Consultar la tabla de entrada/salida de la descripción funcional para identificar el dispositivo conectado al canal (por ejemplo, la lámpara de marcha). Activarla desde TwinCAT escribiendo `1` en **Set Value Dialog**, que aparece al pulsar **Write**.

    ![Diálogo para escribir un valor en la salida](./img/io-set-value-dialog.png){ width="200px" }

- ...y verificar que el dispositivo físico conectado cambia de valor cuando cambia el valor de la señal mostrada en la pantalla.

    ![Canal de salida activado en la vista Online](./img/io-output-channel-online-active.png){ width="300px" }

- Si se reflejan los cambios en el dispositivo, queda verificada la correspondencia entre el canal y el dispositivo. Nombrar el canal con el nombre del dispositivo en el campo **Name** de la pestaña **Variable**.

    ![Nombre asignado al canal de salida](./img/io-output-channel-variable.png){ width="300px" }

!!! note "🔄 Repetir"
    Repetir este proceso de identificación para todos los canales de salida digitales y analógicos conectados.

!!! success "Resultado de la operación"
    Todos los canales de salida del sistema nominados.

    ![Canales del terminal EL2008 con nombre](./img/io-el2008-tagged.png){ width="300px" }

#### Vincular Variables

!!! goal "Objetivo"
    El proceso de vinculación (*linking*) en TwinCAT conecta variables lógicas declaradas en el código PLC (*software*) con los canales físicos de los módulos de E/S (**I/O Terminals**) configurados en la sección `I/O` del **Explorador de la Solución** (*hardware*).

!!! tip
    Aunque la vinculación de variables puede hacerse desde las instancias de las variables de entrada salida hacia los canales de entrada/salida o viceversa, suele ser mucho más sencillo y rápido hacerlo desde los canales.

##### Desde el Canal

- Hacer clic derecho en :material-mouse-right-click: **I/O** > **[canal]** > **Change Link...**. También se puede abrir su ventana con **doble clic** en **I/O** > **[canal]**, o pulsar **Linked to...** en **Variable**.

    ![Canal de entrada con acceso a la variable enlazada](./img/io-input-channel-variable.png){ width="300px" }

- Seleccionar la variable deseada en la ventana **Attach Variable** y pulsar **OK**.

    ![Selección de una variable para enlazar con el canal](./img/io-attach-variable-to-instance.png){ width="300px" }

!!! success "Resultado de la operación"
    El resultado de la vinculación aparece junto al botón **Linked to...** en la ventana del canal y cambia el símbolo asociado al canal y a la instancia de la variable ![Indicador de variable enlazada](./img/io-variable-linked-symbol.png){ .inline-icon }.

    ![Canal de entrada enlazado a una variable](./img/io-input-channel-variable-linked.png){ width="300px" }

!!! note "🔄 Repetir"
    Repetir este mismo proceso de vinculación para todas las señales de entrada/salida.

##### Desde la Instancia

- Hacer clic derecho en :material-mouse-right-click: **PLC** > **[proyecto]** > **Instance** > **[variable]** > **Change Link...**. También se puede abrir su ventana con **doble clic** sobre la variable, o pulsar **Linked to...** en **Variable**.

    ![Instancia de variable en el proyecto PLC](./img/io-input-instance-variable.png){ width="300px" }

- Seleccionar el canal deseado en la ventana **Attach Variable** y pulsar **OK**.

    ![Selección de un canal para enlazar con la variable](./img/io-attach-variable-to-channel.png){ width="300px" }

!!! success "Resultado de la operación"
    El resultado de la vinculación aparece junto al botón **Linked to...** en la ventana de la instancia y cambia el símbolo asociado a la instancia de la variable y al canal ![Indicador de variable enlazada](./img/io-variable-linked-symbol.png){ .inline-icon }

    ![Instancia de variable enlazada a un canal](./img/io-input-instance-variable-linked.png){ width="300px" }

!!! note "🔄 Repetir"
    Repetir este mismo proceso de vinculación para todas las señales de entrada/salida.

#### Activar Simulador

Para activar el simulador (`UmRT_Default`), ejecutar el *script* `Start.bat`, que suele encontrarse en `C:\TwinCAT\3.1\Runtimes\UmRT_Default\Start.bat`.

- ++win+r++ > `C:\TwinCAT\3.1\Runtimes\UmRT_Default\Start.bat` > ++enter++

    ![Cuadro Ejecutar de Windows con la ruta al simulador](./img/win-run-umrt-default.png){ width="200px" }

- Se abrirá una ventana de terminal que debe permanecer abierta mientras usemos el simulador

    ![Terminal del simulador UmRT_Default en ejecución](./img/win-umrt-default-terminal-window.png){ width="500px" }

- Entre otros datos en la ventana de terminal del simulador aparecen los comandos del simulador y su dirección `AmsNetId`

    | Comando | Descripción |
    | :---: | :--- |
    | `c` | Poner TwinCAT en modo configuración (**C**onfig) |
    | `r` | Poner TwinCAT en modo ejecución (**R**un) |
    | `s` | Informar del estado actual de TwinCAT (**S**tatus) |
    | `x` | Salir del simulador `UmRT_Default` (E**x**it) |

### Construir el Proyecto

Construir una solución o un proyecto (**Build**):

- **Análisis Sintáctico y Estático:** El compilador analiza el código fuente (ST, SFC, etc.) verificando la sintaxis, compatibilidad de tipos de datos y reglas de la norma IEC 61131-3.
- **Generación de Código Máquina:** Traduce las POUs a instrucciones binarias optimizadas para la arquitectura del procesador del sistema destino (x86/x64).
- **Ámbito de Compilación:** Se puede construir o reconstruir la solución completa o solo uno de los proyectos de la solución.
- **Modo de ejecución:** Desde el menú **Build** > **Build Solution** (o **Build** > **[Nombre del proyecto]**), o mediante ++ctrl+shift+b++.

![Comando para compilar la solución TwinCAT](./img/tc3-xae-build-solution-command.png){ width="200px" }

- El resultado (mensajes, avisos y errores) de la construcción se muestra en el panel de errores (*Error List*).

### Activar la Configuración

Activar la configuración (**Activate Configuration**):

- **Carga de Hardware y Mapeo:** Transfiere al Kernel de tiempo real la configuración física de dispositivos, terminales,..., la asignación de tareas (*Tasks*) y las tablas de enrutamiento de E/S (`AT %I*`/`AT %Q*`).
- **Instanciación en el Kernel:** Reinicia el Kernel de TwinCAT en el sistema destino para aplicar los cambios de infraestructura e instanciar los servicios de memoria RAM necesarios.
- **Cambio de Estado:** Conmuta el sistema operativo de tiempo real a modo **RUN** (indicado por el icono de TwinCAT en verde en la barra de tareas).
- **Modo de ejecución:** Desde el menú **TwinCAT** > **Activate Configuration**, o pulsando **Activate Configuration** en la barra de herramientas.

![Ventana de confirmación para activar la configuración](./img/tc3-xae-activate-configuration-window.png){ width="200px" }

??? info "Boot Project"
    El **Boot Project** (proyecto de arranque) es la copia ejecutable compilada que se guarda en el almacenamiento no volátil del sistema destino. Permite que TwinCAT cargue y arranque automáticamente el programa PLC al encender o reiniciar el equipo, sin conectarse desde el entorno de desarrollo (XAE).

!!! warning "Importante"
    - **NO** activar la generación del **Boot Project** durante la fase de desarrollo.
    - Si el código del proyecto de arranque contiene un fallo grave de ejecución (como un bucle infinito en ST, una división por cero o un puntero nulo/inválido) y el Boot Project está activo, el runtime intentará ejecutar ese código defectuoso inmediatamente al arrancar. Esto provocará un colapso (crash) o bloqueo en bucle del runtime de tiempo real en cada reinicio.

- Si no se dispone de una licencia permanente, cada 7 días habrá que reactivar la licencia de prueba ... [➡️](#activar-licencia)
- Finalmente, es necesario confirmar el reinicio del sistema destino en modo ejecución.

![Ventana para confirmar el reinicio de TwinCAT en modo ejecución](./img/tc3-xae-restart-run-mode-window.png){ width="200px" }

### Transferir el Proyecto

Transferir un proyecto PLC (**Login**):

- **Conexión vía ADS:** Se establece la sesión de comunicación con la instancia del PLC a través del puerto de sistema ADS (por defecto, **Puerto ADS 851**).
- **Transferencia de Binarios:** Se descarga el código compilado (*Bytecode*) a la memoria RAM asignada a la instancia del PLC en el controlador.
- **Generación de Boot Project:** Eventualmente se crea el proyecto de arranque (*Create Boot Project*) en el almacenamiento no volátil del sistema destino para garantizar que el programa se cargue automáticamente tras una pérdida de alimentación.
- **Modo de ejecución:** Pulsar **Login** (atajo ++alt+f8++) en la barra de herramientas de TwinCAT PLC.

![Solicitud para crear el puerto ADS durante el inicio de sesión](./img/tc3-xae-login-create-port-window.png){ width="200px" }

??? info
    - La primera vez que se realice **Login** sobre un nuevo sistema destino, TwinCAT solicitará la creación del puerto para las comunicaciones entre el entorno de programación (**XAE**) y el sistema de ejecución (**XAR**) del sistema destino.
    - Si el código presente en el sistema destino difiere significativamente del código que se pretende enviar se solicita autorización para realizar un *Online Change* (cambio en caliente) o una descarga completa (*Cold/Origin Reset Download*).

### Arrancar el Proyecto

Arrancar o poner en ejecución un proyecto (**Start**):

- **Inicio del Bucle de Tiempo Real:** Inicia la ejecución del ciclo básico de funcionamiento (*Task Scan*) asignado en la `PlcTask`.
- **Procesamiento de Entradas/Salidas:** Se activa el ciclo determinista: lectura de la imagen de proceso de entradas (`%I*`), ejecución de las POUs (`MAIN`) y actualización de las salidas (`%Q*`).
- **Modo de ejecución:** Pulsar **Start** (atajo ++f5++) o seleccionar **PLC** > **Login** > **Start**.

### Monitorizar Variables

- Tras pasar a modo ejecución, en el entorno de programación, el código se muestra en modo **Monitorización *Online***.

    ![Código PLC con valores de variables en monitorización Online](./img/tc3-xae-monitoring-online.png){ width="500px" }

    !!! info
        El **Modo *Online*** o de **Monitorización *Online*** es el estado de conexión directa e interactiva entre el entorno de desarrollo (**TwinCAT XAE**) y el motor de tiempo real en ejecución (**TwinCAT XAR**/*Target System*).
        Esta herramienta de supervisión y depuración en tiempo real de TwinCAT 3 permite:

        - Visualizar directamente sobre el código fuente (ST, SFC, etc.) los valores actualizados que de las variables en la memoria RAM del controlador durante cada ciclo de escaneo (*Task Scan*).
        - Modificar mediante el forzado/escritura las variables en tiempo de ejecución.

### Forzar Variables

!!! info

    - **Escribir una variable:** modifica su valor, pero la variable puede cambiar por que lo exiga el código o por el cambio de una entrada.
    - **Forzar una variable:** modifica su valor y lo congela, de forma que no puede cambiar a pesar del código en ejecución o de la entrada.
    - **Persistencia:** Una variable forzada conserva el valor establecido hasta que se libera.

#### Cómo Se Hace

1. **Preparar el valor deseado**

     - Para forzar/escribir una variable, en primer lugar introducir el valor deseado en la columna **Prepared value**. Si la variable es de tipo BOOL, hacer doble clic en la celda correpondiente para conmutar entre los valores `TRUE`/`FALSE`.

2. **Ejecutar la acción correspondiente**

    - Para escribir una variable, seleccionar la opción del menú **PLC** > **Write values**, o pulsar el botón ![Escribir](./img/write-value-button.png){ .inline-icon } o simplemente pulsar ++ctrl+f7++.
    - Para forzar una variable, seleccionar la opción del menú **PLC** > **Force values**, o pulsar el botón ![Forzar](./img/force-value-button.png){ .inline-icon } o simplemente pulsar ++f7++.

    !!! success "Resultado de la operación"
        Las variables que están forzadas se muestran con una F sobre fondo rojo ![Forzadp](./img/forced-value-icon.png){ .inline-icon }.

        ![Variables forzadas](./img/tc3-xae-forced-values.png){ width="500px" }

    - Para liberar una variable, seleccionar la opción del menú **PLC** > **Unforce values**, o pulsar el botón ![Liberar](./img/unforce-value-button.png){ .inline-icon } o simplemente pulsar ++ctrl+shift+f7++.
    - Para modificar el valor de forzado de una única variable, hacer doble clic en la celda correspondiente a la variable en la columna **Prepared value** y seleccionar lo que corresponda en la ventana.

    ![Ventana para preparar el valor de una variable](./img/tc3-xae-prepare-value-window.png){ width="200px" }

---

<!--
## Codificar en Texto Estructurado
Codificar un SFC -> documento aparte
De grafcet a SFC, a ST, a LD
Explicación del ciclo básico y de las imágenes de entrada y salida (AT), el programa no lee directamente, sino que trabaja con una copia
Stop ejecución, reiniciar sistema reset cold y reset origin
Mostrar punto de declaración de una variable
Mostrar todas las apariciones de una variable
Crear una visualización paso a paso -> esto mejor en otro archivo
Depurar errores

align=center en imágenes
incluir títulos explícitos en los bloques info
dirección AMS 
puerto de comunicaciones

Instancia FB 

-->