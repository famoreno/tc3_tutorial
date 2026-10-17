### Sobre un Controlador

Si dispone de un controlador de Beckhoff (ordenador embebido) puede probar el proyecto con entradas y salidas reales conectadas a sus terminales.

!!! warning "Aviso"
    Para probar el programa con un pulsador y una lámpara real es necesario:

    - Modificar y construir el programa.
    - Configurar la E/S: escanear, identificar y vincular canales de E/S.

1. Desconectarse (**Logout**), si se estaba conectado, del sistema destino actual.
2. <span class="objetivo-hito">Declarar variables de entrada/salida localizadas con mapeo dinámico</span> Modificar, en la parte de declaración del programa `MAIN`, la declaración de las variables `i_Pulsador` y `o_Lampara`.

    ```iecst
    PROGRAM MAIN
    VAR
        i_Pulsador AT %I*: BOOL;
        o_Lampara AT %Q*: BOOL;
    END_VAR
    ```

    ??? note "Notas"
        - Las **variables localizadas**, son aquellas a las que se le asigna explícitamente una dirección de memoria.
        - Situar las instancias de estas variables en las correspondientes imágenes de E/S (*Process Image*) mediante el uso del modificador `AT`, las convierte en **variables de entrada y salida**.
        - Si no se hiciera, el compilador situaría estas variables en el **espacio de memoria interna** (marcas) y no se generarían las correspondientes instancias de E/S y no podrían vincularse (*mapping*) a canales físicos de E/S del controlador.
        - El símbolo `%` es el prefijo de ubicación directa.
        - Las letras `I` y `Q` indican el área de memoria (entrada/salida).
        - El símbolo `*` es un comodín que indica que estas varaibles tienen un **mapeo dinámico**, lo que implica que será el compilador el encargado de asignarle una dirección (`palabra.bit`) concreta.

3. Construir (**Build**) y verificar la ausencia de errores.

    ??? tip "Sugerencia"
        Verificar que las variables `i_Pulsador` y `o_Lampara` aparecen instanciadas.

        ```text
            Hola_Mundo_PLC Instance/
            ├── PLCTask Inputs
            |   └── MAIN.i_Pulsador
            └── PLCTask Outputs
                └── MAIN.o_Lampara
        ```

4. Encontrar el nuevo sistema destino (**controlador remoto**) de Beckhoff presente en la red local, creando una ruta de acceso. [➡️](../../procedimientos/workflow/index.md#crear-una-ruta)
5. Seleccionar el **controlador remoto** como nuevo sistema destino. [➡️](../../procedimientos/workflow/index.md#seleccionar-sistema-destino)
6. Empezar la <span class="objetivo-hito">configuración de la entrada/salida</span> escaneando (**Scan**) la entrada/salida (**I/O**) en busca de dispositivos y terminales. [➡️](../../procedimientos/workflow/index.md#buscar-dispositivos)
7. Localizar, identificar, nominar y probar un canal de entrada digital para `i_Pulsador`. [➡️](../../procedimientos/workflow/index.md#identificar-entradas)
8. Localizar, identificar, nominar y probrar un canal de salida digital para `o_Lampara`. [➡️](../../procedimientos/workflow/index.md#identificar-salidas)
9. <span class="objetivo-hito">Vincular las instancias de las variables de entrada/salida a canales de entrada/salida</span> (**Link**), para enlazar las varables `i_Pulsador` y `o_Lampara` con los correspondientes canales recién identificados.[➡️](../../procedimientos/workflow/index.md#vincular-variables)

    ??? tip "Sugerencias"
        - Buscar en la lista de entradas y salidas de la **descripción funcional** del sistema una señal de entrada (preferiblemente un **pulsador**) y otra de salida (preferiblemente una **lámpara**).
        - **Desactivar** los dispositivos de entrada y salida que no se van a utilizar (todos menos el dispositivo denominado `EtherCAT`).

10. Activar la configuración (**Activate Configuration**) y reiniciar TwinCAT (**Restart TwinCAT System**) en el nuevo sistema destino. [➡️](../../procedimientos/workflow/index.md#activar-la-configuracion)
11. Conectarse para transferir el programa al controlador (**Login**). [➡️](../../procedimientos/workflow/index.md#transferir-el-proyecto)
12. Poner el programa en ejecución (**Start**). [➡️](../../procedimientos/workflow/index.md#arrancar-el-proyecto)
13. Comprobar que:
    - El contador de ciclos sigue incrementándose de forma continua.
    - Al accionar el pulsador físico se enciende la lámpara física.
14. Utilizar la visualización integrada en el proyecto PLC para facilitar la prueba:
    - Comprobar que, accionando el pulsador físico, cambia de estado la lámpara en la visualización.
    - Comprobar que accionando el botón de la visualización, **NO cambia de estado la lámpara**.

    ??? note "Notas"
        Esto se debe a que la ejecución del ciclo básico hace que el valor del pulsador **se actualice con el valor del pulsador físico** al inicio de cada ciclo básico de ejecución, sobreescribiendo el valor que fija el botón de la visualización.

!!! success "¡Enhorabuena! 🎉"
    Has completado con éxito la segunda parte de esta guía. Has puesto en marcha tu primer **proyecto de PLC** completo en **Texto Estructurado** con **TwinCAT 3** sobre un **controlador** real.

??? tip "Recomendación"
    - Para ejecutar el proyecto sobre un controlador real con terminales de E/S asociados es necesario antes de activar la configuración tener HABILITADOS los dispositivos de E/S que se vayan a utilizar.
    - Para ejecutar el proyecto sobre un runtime sin terminales de E/S asociados (como el simulador `UmRT_Default`) es necesario antes de activar la configuración tener DESHABILITADOS los dispositivos de E/S ya que no se van a utilizar.
    - Para conmutar la habilitación, expandir el contenido de **I/O** y en **Devices**:
        - **Doble clic** sobre el dispositivo y seleccionar lo que corresponda (Enable/Disable).
