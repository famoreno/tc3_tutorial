#### Carro Básico

1. Abrir la aplicación **TwinCAT XAE**. [➡️](../../procedimientos/workflow/index.md#abrir-twincat-xae)
2. Crear una solución de TwinCAT 3 con nombre `TC3_Carro_Basico`. [➡️](../../procedimientos/workflow/index.md#crear-un-proyecto-twincat-3)
3. Ocultar las configuraciones innecesarias para dejar el explorador de la solución lo más despejado posible. [➡️](../../procedimientos/workflow/index.md#ocultar-configuraciones)
4. Crear un proyecto PLC estándar con el nombre `Carro_Basico_PLC`. [➡️](../../procedimientos/workflow/index.md#crear-un-proyecto-plc)
5. Crear una nueva **Unidad de Organización de Programa (POU)** de tipo **Bloque Funcional**. [➡️](../../procedimientos/workflow/index.md#crear-una-pou)

    !!! note "Parámetros POU"
        - *Name* ➔ `FB_Carro_GRF_SFC`
        - *Type* ➔ `Function Block`
        - *Implementation Language* ➔ `Sequential Function Chart (SFC)`

6. Declarar todas las **variables de entrada/salida** del sistema en `FB_Carro_GRF_SFC` como variables locales (`VAR_LOCAL`). [➡️](../../procedimientos/workflow/index.md#declarar-una-variable)

    ```iecst {hl_lines="8-16"}
    FUNCTION_BLOCK FB_Carro_GRF_SFC
    // Transcripción del grafcet (GRF -> SFC)
    VAR_INPUT
    END_VAR
    VAR_OUTPUT
    END_VAR
    VAR
        // Entradas
        i_PulsadorMarcha AT %I*: BOOL;
        i_FinalCarreraIzquierda AT %I*: BOOL := TRUE;
        i_FinalCarreraDerecha AT %I*: BOOL;

        // Salidas
        o_MarchaIzquierda AT %Q*: BOOL;
        o_MarchaDerecha AT %Q*: BOOL;
        o_LamparaMarcha AT %Q*: BOOL;
    END_VAR
    ```

    ??? info "Comentarios Declaración"
        - **Ocultamiento**: las variables de entrada y salida se declaran como **locales** (`VAR`) para ocultarlas, para protegerlas, para que no sean accesibles desde fuera del bloque funcional.
        - **Direccionamiento**: se declaran con el modificador `AT` para situarlas, según corresponda, en la **Imagen de Entrada** (`%I`) o en la **Imagen de Salida** (`%Q`). No se especifica la posición de memoria (`*`) para dejar que TwinCAT se encargue de asignarle una dirección. Cuando se construya el proyecto las instancias correspondientes a estas variables estarán disponibles en la sección `I/O` para ser vinculadas con las señales presentes en los canales de entrada y salida.
        - **Valor Inicial**: La variable `i_FinalCarreraIzquierda` se inicia a `TRUE`. Aunque sea totalmente innecesario e incluso contradictorio, ya que las variables de entrada tomarán en el primer ciclo el valor que le corresponda según la señal de entrada a la que estén vinculadas. Establecer el valor inicial de algunas variables de entrada puede ser conveniente, desde un punto de vista práctico, cuando se ejecuta el código sin *hardware* (UmRT_Default), ya que así, cada vez que se reinicie la ejecución no hay que escribir uno a uno el valor de las variables que forman parte de la condición inicial.

7. Escribir el código <span class="fondo-rojo-lang">SFC</span> correspondiente al carro básico.

    ![FB_Carro_GRF_SFC Basico](./img/fb-carro-grf-sfc-basico.png){ .screenshot }
    ??? info "Comentarios Código"
        - En la transición S0➔S1, `i_FinalCarreraIzquierda` es la **Condicion Inicial** y `i_PulsadorMarcha` es el evento que dispara la transición.
        - La **Condición Inicial** es la condición material (estado de los sensores) que se debe cumplir para iniciar la secuencia de funcionamiento con seguridad.

8. Declarar en `MAIN` una instancia `Carro` de `FB_Carro_GRF_SFC`.

    ```iecst {hl_lines="3"}
    PROGRAM MAIN
    VAR
        Carro: FB_Carro_GRF_SFC;
    END_VAR
    ```

9. Escribir en `MAIN` el código, una sola línea con la invocación a la instancia `Carro`.

    ```iecst
    Carro();
    ```

10. Construir el proyecto (**Build**) para generar un archivo ejecutable. [➡️](../../procedimientos/workflow/index.md#construir-el-proyecto)
11. Si no se dispone de ningún sistema destino (local o remoto) con un *runtime* sobre el que ejecutar el código, activar el simulador `UmRT_Default`. [➡️](../../procedimientos/workflow/index.md#activar-simulador)
12. Seleccionar el sistema destino (**Target System**) sobre el que se vaya a ejecutar el programa (`UmRT_Default`). [➡️](../../procedimientos/workflow/index.md#seleccionar-sistema-destino)
13. Activar la licencia temporal del *runtime* del sistema destino si es necesario. [➡️](../../procedimientos/workflow/index.md#activar-licencia)
14. Activar la configuración en el sistema destino (**Activate Configuration**).  [➡️](../../procedimientos/workflow/index.md#activar-la-configuracion)
15. Conectarse (**Login**) al sistema destino para transferir el proyecto. [➡️](../../procedimientos/workflow/index.md#transferir-el-proyecto)
16. Poner el programa de PLC en ejecución (**Run**). [➡️](../../procedimientos/workflow/index.md#arrancar-el-proyecto)
17. Probar el programa forzando las variables de entrada en el modo de **Monitorización *Online***. [➡️](../../procedimientos/workflow/index.md#forzar-variables)

    ![FB_Carro_GRF_SFC Basico Online](./img/fb-carro-grf-sfc-basico-online.png){ .screenshot }
    ??? info "Monitorización Online"
        En el modo **Monitorización *Online*** se muestra:

        - En la parte de declaración ➔ el valor de las variables.
        - En la parte de implementación ➔ las etapas y transiciones activas .

18. Crear una visualización mínima `V_Carro` que facilite la prueba.

    ![V_Carro Basico](./img/v-carro-basico.png){ .screenshot }
    ??? info "Visualización"
        - La visualización debe disponer al menos de:
            -  Un elemento gráfico para modificar el valor de cada sensor.
            -  Un elemento gráfico para mostrar el valor de cada actuador.
        - Sin embargo, resulta conveniente, que tanto los objetos gráficos destinados a los sensores como a los actuadores permitan leer y escribir las señales correspondientes. De esta forma se facilitará la prueba cuando se ejecuta con el simulador (UmRt_Default) sin *hardware* asociado y se facilitará el modo manual cuando se ejecutA sobre un controlador con *hardware* asociado.
        - Conviene establecer un código de colores coherente para facilitar la interpretación y disminuir la carga congnitiva del usuario.

19. Probar el programa cambiando el valor de las entradas desde la visualización.

    ![V_Carro Basico Online](./img/v-carro-basico-online.png){ .screenshot }
    ??? info "Visualización en línea"
        Con la visualización *Online* se puede:

        - Conocer el valor de las variables de salida por su color de desactivación/activación.
        - Modificar el valor de las variables de entrada pulsando sobre el objeto gráfico.

#### Carro Pulsado

1. Añadir en la declaración de `FB_Carro_GRF_SFC`:
    - Una instancia del bloque funcional `R_TRIG` de la librería estándar (`Tc2_Standard`) para la detección del flanco positivo del pulsador de marcha.

    ```iecst {hl_lines="8-9"}
    FUNCTION_BLOCK FB_Carro_GRF_SFC
    // Transcripción del grafcet (GRF -> SFC)
    VAR_INPUT
    END_VAR
    VAR_OUTPUT
    END_VAR
    VAR
        // Bloques Funcionales
        FlancoPulsadorMarcha: R_TRIG;

        // Entradas
        i_PulsadorMarcha AT %I*: BOOL;
        i_FinalCarreraIzquierda AT %I*: BOOL := TRUE;
        i_FinalCarreraDerecha AT %I*: BOOL;

        // Salidas
        o_MarchaIzquierda AT %Q*: BOOL;
        o_MarchaDerecha AT %Q*: BOOL;
        o_LamparaMarcha AT %Q*: BOOL;
    END_VAR
    ```

2. Modificar el código de  `FB_Carro_GRF_SFC`

    ![FB_Carro_GRF_SFC Pulsado](./img/fb-carro-grf-sfc-pulsado.png){ .screenshot }
    !!! info "Comentarios Código"
        - Añadir a `FB_Carro_GRF_SFC` una acción `a_FlancoPulsadorMarcha_Evaluar` (ST), en la que se invoque la ejecución del detector de flanco `FlancoPulsadorMarcha`.

            ```iesst
            FlancoPulsadorMarcha(CLK := i_PulsadorMarcha);
            ```

        - Incluir la acción `a_FlancoPulsadorMarcha_Evaluar` como acción principal (`Main action`) en la etapa inicial (`S0`), para que se ejecute continuamente (una vez por ciclo) mientras el sistema esté en la etapa inicial.
        - Sustituir `i_PulsadorMarcha` por `FlancoPulsadorMarcha.Q`, en la condición de la transición de salida de la etapa inicial.

3. Poner el programa en ejecución y comprobar que no basta para iniciar la marcha con que el pulsador de marcha esté activado, sino que es necesario que se realice una acción de impulso.

#### Carro Temporizado

1. Añadir en la parte de declaración de `FB_Carro_GRF_SFC`:
    - Un parámetro de entrada `TiempoEspera` de tipo `TIME` en el bloque de declaración `VAR_INPUT`. Esto permitirá que este parámetro pueda ser modificado desde fuera del bloque funcional. Eventualmente, puede indicarse un valor inicial en su defecto (`T#2S`).
    - Un parámetro de salida `TiempoPendiente` en el bloque de declaración `VAR_OUTPUT` para informar del tiempo de espera pendiente.

    ```iecst {hl_lines="4 7"}
    FUNCTION_BLOCK FB_Carro_GRF_SFC
    // Transcripción del grafcet (GRF -> SFC)
    VAR_INPUT
        TiempoEspera: TIME := T#2S;
    END_VAR
    VAR_OUTPUT
        TiempoPendiente: TIME;
    END_VAR
    VAR
        // Bloques Funcionales
        FlancoPulsadorMarcha: R_TRIG;

        // Entradas
        i_PulsadorMarcha AT %I*: BOOL;
        i_FinalCarreraIzquierda AT %I*: BOOL := TRUE;
        i_FinalCarreraDerecha AT %I*: BOOL;

        // Salidas
        o_MarchaIzquierda AT %Q*: BOOL;
        o_MarchaDerecha AT %Q*: BOOL;
        o_LamparaMarcha AT %Q*: BOOL;
    END_VAR
    ```

2. Modificar el código de `FB_Carro_GRF_SFC`:

    ![FB_Carro_GRF_SFC Temporizado](./img/fb-carro-grf-sfc-temporizado.png){ .screenshot }
    !!! Info "Código SFC"
        - Añadir una nueva etapa (`S2`) para representar el estado de espera e incluir en su transición de salida la condición `S2.t > TiempoEspera`, equivalente a la condición de tiempo del diagrama grafcet `TE/X2`.

        - Añadir a `FB_Carro_GRF_SFC` una acción denominda `a_TiempoPendiente_Calcular` (<span class="fondo-azul-lang">ST</span>), para calcular el tiempo de espera pendiente.

            ```iecst
            IF TiempoEspera >= S2.t THEN
                TiempoPendiente := TiempoEspera - S2.t;
            ELSE
                TiempoPendiente := T#0S;
            END_IF;
            ```
        -  Incluir la acción `a_TiempoPendiente_Calcular` como acción principal (**Main action**) en la etapa de espera (`S2`).

    ??? Info "Programación Defensiva"
        - La condición defensiva `TiempoEspera >= S2.t` previene un **desbordamiento negativo (*underflow*)** en la resta, asegurando que el cálculo solo se realice cuando el resultado sea mayor o igual a cero.
        - Además, la estructura `ELSE` garantiza el **determinismo del PLC** al forzar explícitamente la variable a `T#0S`, evitando que `TiempoPendiente` retenga valores obsoletos de ciclos anteriores si la condición no se cumple.
        - La **Programación Defensiva** usada en su justa medida se considera una buena práctica de programación que favorece el **Código Limpio**.

3. Incluir en la visualización `V_Carro` un objeto gráfico que permita introducir el tiempo de espera deseado y otro que informe del tiempo pendiente.

    ![V_Carro Temporizado](./img/v-carro-temporizado.png){ .screenshot }
4. Proceder como en la sección anterior para probar el programa desde la visualización.

#### Carro Computado

1. Añadir en la parte de declaración de `FB_Carro_GRF_SFC`:
    - Un parámetro entero de entrada `ManiobrasTotales` en el bloque de declaración `VAR_INPUT` para contener el valor del número total de maniobras deseadas. Eventualmente, puede indicarse un valor inicial en su defecto (`1`);
    - Un parámetro entero de salida `ManiobrasPendientes` en el bloque de declaración `VAR_OUTPUT` para contener el número de maniobras pendientes de realizar.

    ```iecst {hl_lines="4 8"}
    FUNCTION_BLOCK FB_Carro_GRF_SFC
    VAR_INPUT
        TiempoEspera: TIME := T#2S;
        ManiobrasTotales: UINT := 2;
    END_VAR
    VAR_OUTPUT
        TiempoPendiente: TIME;
        ManiobrasPendientes: UINT;
    END_VAR
    VAR
    // Bloques Funcionales
    FlancoPulsadorMarcha: R_TRIG;

    // Entradas
        i_PulsadorMarcha AT %I*: BOOL;
        i_FinalCarreraIzquierda AT %I*: BOOL := TRUE;
        i_FinalCarreraDerecha AT %I*: BOOL;

        // Salidas
        o_MarchaIzquierda AT %Q*: BOOL;
        o_MarchaDerecha AT %Q*: BOOL;
        o_LamparaMarcha AT %Q*: BOOL;
    END_VAR
    ```

2. Modificar el código:

    ![FB_Carro_GRF_SFC Computado](./img/fb-carro-grf-sfc-computado.png){ .screenshot }
    !!! info "Código SFC"
        - Incluir una nueva etapa (`S4`)al final de las secuencia para evaluar si terminó la tarea.
        - Incluir una rama alternativa con salto atrás a la primera etapa de la secuancia (`S1`).
        - Se regresa a la etapa inicial por la rama principal si terminó la tarea (`ManiobrasPendientes = 0`).
        - Se vuelve a la primera etapa de la secuencia (`S1`) si quedan maniobra por realizar (`ManiobrasPendientes > 0`).
        - Incluir una acción `a_ManiobrasPendientes_Reiniciar` para establecer el valor de la cuenta al iniciar la tarea y asociarla como acción a la salida a la etapa inicial (`S0`).

            ```iecst
            ManiobrasPendientes := ManiobrasTotales;
            ```

        - Incluir una acción a_ManiobrasPendientes_Calcular para decrementar el valor de la cuenta con la finalización de cada maniobra y asociarla como acción a la entrada a la etapa final (`S4`).

            ```iecst
            IF (ManiobrasPendientes > 0) THEN
                ManiobrasPendientes := ManiobrasPendientes - 1;
            END_IF;
            ```
3. Incluir en la visualización `V_Carro` un objeto gráfico que permita introducir el valor de las maniobras totales y otro que muestre las maniobras pendientes.

    ![V_Carro Computado](./img/v-carro-computado.png){ .screenshot }
4. Proceder como en la sección anterior para probar el programa desde la visualización.

#### Carro Señalizado

1. Añadir la librería `Util` a las referencias (`References`) del proyecto.
2. Añadir en la parte de declaración de `FB_Carro_GRF_SFC`:
    - Una instancia `Intermitencia` del bloque funcional `BLINK` de la librería `Util`, que implementa una intermitencia.

    ```iecst {hl_lines="13"}
    FUNCTION_BLOCK FB_Carro_GRF_SFC
    VAR_INPUT
        TiempoEspera: TIME := T#2S;
        ManiobrasTotales: UINT := 2;
    END_VAR
    VAR_OUTPUT
        TiempoPendiente: TIME;
        ManiobrasPendientes: UINT;
    END_VAR
    VAR
        // Bloques Funcionales
        FlancoPulsadorMarcha: R_TRIG;
        Intermitencia: BLINK;

        // Entradas
        i_PulsadorMarcha AT %I*: BOOL;
        i_FinalCarreraIzquierda AT %I*: BOOL := TRUE;
        i_FinalCarreraDerecha AT %I*: BOOL;

        // Salidas
        o_MarchaIzquierda AT %Q*: BOOL;
        o_MarchaDerecha AT %Q*: BOOL;
        o_LamparaMarcha AT %Q*: BOOL;
    END_VAR
    ```

3. Modificar el código:

    ![FB_Carro_GRF_SFC Senalizado](./img/fb-carro-grf-sfc-senalizado.png){ .screenshot }
    !!! info "Código SFC"
        - Incluir una acción `a_LamparaMarcha` para establecer el valor de `o_LamparaMarcha`, implementando tanto la acción condicionada a `BLK` en la etapa inicial (`SO`)como la acción continua en el resto de etapas.

            ```iecst
            Intermitencia(Enable := S0.x);

            o_LamparaMarcha := (S0.x AND Intermitencia.OUT) OR S1.x OR S2.x OR S3.x OR S4.x;
            ```

        - Incluir la acción `a_LamparaMarcha` en todas las etapas tal y como figura en el diagrama grafcet.

4. Proceder como en la sección anterior para probar el programa desde la visualización.
