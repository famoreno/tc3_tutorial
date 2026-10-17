### Con ArduTC

Si tiene instalado en su ordenador la aplicación **ArduTC**, puede ejecutar el proyecto sobre un runtime (local/remoto) o sobre el simulador (`UmRT_Default`) y utilizar una placa microcontroladora como **Arduino UNO** como terminal de E/S. [➡️](../../fundamentos/ardutc/index.md)

1. Preparar el proyecto TC
    - Tener preparado un controlador TC: runtime (local o remoto) o simulador (`UmRT_Default`).
    - Deshabilitar todos los dispositivo *hardware* incluidos en el apartato I/O.
    - Activar la configuración del proyecto sobre el controlador.
    - Cargar el proyecto PLC sobre el controlador.
    - Poner en ejecución el proyecto en el controlador.

2. Preparar la placa Arduino
    - Descargar **Telemetrix** en la placa Arduino.
    - Preparar el montaje correspondiente: un pulsador y un led conectados a los pines correspondientes.

3. Abrir al aplicación **ArduTC**.
4. Cargar los símbolos del proyecto TC en **ArduTc**. [➡️](../../fundamentos/ardutc/index.md#cargar-simbolos)
5. Seleccionar la placa **microcontroladora**. [➡️](../../fundamentos/ardutc/index.md#seleccionar-placa-microcontroladora)
6. Vincular las variables de E/S del proyecto TC con los pines corespondientes de la placa **microcontroladora**. [➡️](../../fundamentos/ardutc/index.md#vincular-variables)
7. Establecer la dirección **AMS Net ID** y el **puerto de comunicaciones** del controlador TC en **ArduTC**. [➡️](../../fundamentos/ardutc/index.md#configurar-comunicaciones)
8. Conectar **ArduTC**. [➡️](../../fundamentos/ardutc/index.md#conectar)
9. Accionar el pulsador y verificar que se enciende el led.

!!! success "¡Enhorabuena! 🎉"
    Has completado con éxito la última parte de esta guía de implementación. Has puesto en marcha tu primer **proyecto de PLC** completo en **Texto Estructurado** con **TwinCAT 3** utilizando una placa **Arduino UNO** como terminal de entrada/salidas a través de la aplicación **ArduTC**.
