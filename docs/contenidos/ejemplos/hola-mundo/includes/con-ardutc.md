### Con ArduTC

Si tienes instalada en tu ordenador la aplicación **ArduTC**, puedes ejecutar el proyecto sobre un *runtime* (local/remoto) o sobre el simulador (`UmRT_Default`) y utilizar una placa microcontroladora compatible como **Arduino UNO** como terminal de E/S. [:material-arrow-right-bold-box:](../../fundamentos/ardutc/index.md)

??? warning "Proyecto TwinCAT"
    - Tener preparado un controlador TwinCAT: runtime (local o remoto) o simulador (`UmRT_Default`).
    - Deshabilitar todos los dispositivos *hardware* incluidos en el apartado **I/O**.
    - Activar la configuración del proyecto sobre el controlador.
    - Cargar el proyecto PLC sobre el controlador.
    - Poner en ejecución el proyecto en el controlador.

??? warning "Placa Microcontroladora"
    - Cargar el código **Telemetrix** en la placa microcontroladora (Arduino UNO).
    - Preparar el montaje conectando un pulsador y un led a los pines digitales correspondientes.

1. Abre la aplicación **ArduTC**.
2. Carga los símbolos del proyecto TC en **ArduTC**. [:material-arrow-right-bold-box:](../../fundamentos/ardutc/index.md#cargar-simbolos)
3. Selecciona la placa **microcontroladora**. [:material-arrow-right-bold-box:](../../fundamentos/ardutc/index.md#seleccionar-placa-microcontroladora)
4. Vincula las variables de E/S del proyecto TC con los pines correspondientes de la placa **microcontroladora**. [:material-arrow-right-bold-box:](../../fundamentos/ardutc/index.md#vincular-variables)
5. Establece la dirección **AMS Net ID** y el **puerto de comunicaciones** del controlador TC en **ArduTC**. [:material-arrow-right-bold-box:](../../fundamentos/ardutc/index.md#configurar-comunicaciones)
6. Conecta **ArduTC**. [:material-arrow-right-bold-box:](../../fundamentos/ardutc/index.md#conectar)
7. Acciona el pulsador y verifica que se enciende el led.

!!! success ":fontawesome-solid-trophy: ¡Enhorabuena!"
    Has completado con éxito la última parte de esta guía de implementación.

    Has puesto en marcha tu primer **proyecto de PLC** completo en **Texto Estructurado** con **TwinCAT 3** utilizando una placa microcontroladora compatible (**Arduino UNO**) como terminal de entrada/salidas con TwinCAT a través de la aplicación **ArduTC**.
