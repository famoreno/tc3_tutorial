### GRAFCET ➔ SFC

<span class="objetivo-hito">Implementemos un diagrama grafcet en el lenguaje SFC</span>

#### Carro Básico

1. Abre la aplicación **TwinCAT XAE**. [➡️](../../procedimientos/workflow/index.md#abrir-twincat-xae)
2. Crea una solución de TwinCAT 3 con nombre `TC3_Carro_Basico`. [➡️](../../procedimientos/workflow/index.md#crear-un-proyecto-twincat-3)
3. Oculta las configuraciones innecesarias para dejar el explorador de la solución lo más despejado posible. [➡️](../../procedimientos/workflow/index.md#ocultar-configuraciones)
4. Crea un proyecto PLC estándar con el nombre `Carro_Basico_PLC`. [➡️](../../procedimientos/workflow/index.md#crear-un-proyecto-plc)
5. Crea una nueva **Unidad de Organización de Programa (POU)** de tipo **Bloque Funcional**. [➡️](../../procedimientos/workflow/index.md#crear-una-pou)

    !!! note "Parámetros POU"
        - *Name* ➔ `FB_Carro_GRF_SFC`
        - *Type* ➔ `Function Block`
        - *Implementation Language* ➔ `Sequential Function Chart (SFC)`

6. Declara todas las **variables de entrada/salida** del sistema en `FB_Carro_GRF_SFC` como variables locales (`VAR_LOCAL`). [➡️](../../procedimientos/workflow/index.md#declarar-una-variable)

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

7. Escribe el código <span class="fondo-rojo-lang">SFC</span> correspondiente al carro básico.

    ![FB_Carro_GRF_SFC Basico](./img/fb-carro-grf-sfc-basico.png){ .screenshot }
    ??? info "Comentarios Código"
        - En la transición `S0` ➔ `S1`, `i_FinalCarreraIzquierda` es la **condición inicial** y `i_PulsadorMarcha` es el evento que dispara la transición.
        - La **Condición Inicial** es la condición material (estado de los sensores) que se debe cumplir para iniciar la secuencia de funcionamiento con seguridad.

8. Declara en `MAIN` una instancia `Carro` de `FB_Carro_GRF_SFC`.

    ```iecst {hl_lines="3"}
    PROGRAM MAIN
    VAR
        Carro: FB_Carro_GRF_SFC;
    END_VAR
    ```

9. Escribe en `MAIN` el código, una sola línea con la invocación a la instancia `Carro`.

    ```iecst
    Carro();
    ```

10. Construye el proyecto (**Build**) para generar un archivo ejecutable. [➡️](../../procedimientos/workflow/index.md#construir-el-proyecto)
11. Si no se dispone de ningún sistema destino (local o remoto) con un *runtime* sobre el que ejecutar el código, activar el simulador `UmRT_Default`. [➡️](../../procedimientos/workflow/index.md#activar-simulador)
12. Selecciona el sistema destino (**Target System**) sobre el que se vaya a ejecutar el programa (`UmRT_Default`). [➡️](../../procedimientos/workflow/index.md#seleccionar-sistema-destino)
13. Activa la licencia temporal del *runtime* del sistema destino si es necesario. [➡️](../../procedimientos/workflow/index.md#activar-licencia)
14. Activa la configuración en el sistema destino (**Activate Configuration**).  [➡️](../../procedimientos/workflow/index.md#activar-la-configuracion)
15. Conéctate (**Login**) al sistema destino para transferir el proyecto. [➡️](../../procedimientos/workflow/index.md#transferir-el-proyecto)
16. Pon el programa de PLC en ejecución (**Run**). [➡️](../../procedimientos/workflow/index.md#arrancar-el-proyecto)
17. Prueba el programa forzando las variables de entrada en el modo de **Monitorización *Online***. [➡️](../../procedimientos/workflow/index.md#forzar-variables)

    ![FB_Carro_GRF_SFC Basico Online](./img/fb-carro-grf-sfc-basico-online.png){ .screenshot }
    ??? info "Monitorización Online"
        En el modo **Monitorización *Online*** se muestra:

        - En la parte de declaración ➔ el valor de las variables.
        - En la parte de implementación ➔ las etapas y transiciones activas .

18. Crea una visualización mínima `V_Carro` que facilite la prueba.

    ![V_Carro Basico](./img/v-carro-basico.png){ .screenshot }
    ??? info "Visualización"
        - La visualización debe disponer al menos de:
            -  Un elemento gráfico para mostrar y modificar el valor de cada sensor.
            -  Un elemento gráfico para mostrar el valor de cada actuador.
        - Sin embargo, resulta conveniente, que tanto los objetos gráficos destinados a los sensores como a los actuadores permitan leer y escribir las señales correspondientes. De esta forma se facilitará la prueba cuando se ejecuta con el simulador (UmRt_Default) sin *hardware* asociado y se facilitará el modo manual cuando se ejecuta sobre un controlador con *hardware* asociado.
        - Conviene establecer un código de colores coherente para facilitar la interpretación y reducir la carga cognitiva del usuario.

19. Prueba el programa cambiando el valor de las entradas desde la visualización.

    ![V_Carro Basico Online](./img/v-carro-basico-online.png){ .screenshot }
    ??? info "Visualización en línea"
        Con la visualización en modo *Online* se puede:

        - Conocer el valor de las variables de salida por su color de desactivación/activación.
        - Modifica el valor de las variables de entrada pulsando sobre el objeto gráfico.

#### Carro Pulsado

<span class="objetivo-hito">Implementemos un detector de flancos en SFC</span>

1. Modifica la parte de declaración.

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

    ??? info "Comentarios"
        - Añade una instancia del bloque funcional `R_TRIG` de la librería estándar (`Tc2_Standard`) para la detección del flanco positivo del pulsador de marcha (`FlancoPulsadorMarcha`).
        - La librería `Tc2_Standard` se incluye automáticamente, al crear un proyecto PLC estándar.

2. Modifica el código de  `FB_Carro_GRF_SFC`

    ![FB_Carro_GRF_SFC Pulsado](./img/fb-carro-grf-sfc-pulsado.png){ .screenshot }

    !!! info "Comentarios"
        - Añade a `FB_Carro_GRF_SFC` una acción `a_FlancoPulsadorMarcha_Evaluar` (ST), en la que se invoque la ejecución del detector de flanco `FlancoPulsadorMarcha`.

            ```iecst
            FlancoPulsadorMarcha(CLK := i_PulsadorMarcha);
            ```

        - Incluye la acción `a_FlancoPulsadorMarcha_Evaluar` como acción principal (`Main action`) en la etapa inicial (`S0`), para que se ejecute continuamente (una vez por ciclo) mientras el sistema esté en la etapa inicial.
        - Sustituye en la expresión de la condición de transición de la etapa `S0` ➔ `S1`, `PulsadorMarcha` por la salida de la instancia del bloque funcional que detecta los flancos positivos en la variable (`FlancoPulsadorMarcha.Q`).

3. Pon el programa en ejecución y comprueba, con ayuda de la visualización, que no basta con mantener activado el pulsador de marcha: es necesario generar un pulso.

#### Carro Temporizado

<span class="objetivo-hito">Implementemos una temporización en SFC</span>

1. Modifica la parte de declaración.

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

    ??? info "Comentarios"
        - Añade un parámetro de entrada `TiempoEspera` de tipo `TIME` en el bloque de declaración `VAR_INPUT`. Esto permite que este parámetro pueda ser modificado desde fuera del bloque funcional. Eventualmente, puede indicarse un valor inicial en su defecto (`T#2S`).
        - Añade un parámetro de salida `TiempoPendiente` en el bloque de declaración `VAR_OUTPUT` para informar del tiempo de espera pendiente.

2. Modifica la parte de implementación.

    ![FB_Carro_GRF_SFC Temporizado](./img/fb-carro-grf-sfc-temporizado.png){ .screenshot }

    !!! info "Comentarios"
        - Añade una nueva etapa (`S2`), para representar el estado de espera, e incluir en su transición de salida la condición `S2.t > TiempoEspera`, equivalente a la condición de tiempo del diagrama grafcet `TE/X2`.

        - Añade a `FB_Carro_GRF_SFC` una acción denominda `a_TiempoPendiente_Calcular` (<span class="fondo-azul-lang">ST</span>), para calcular el tiempo de espera pendiente.

            ```iecst
            IF TiempoEspera >= S2.t THEN
                TiempoPendiente := TiempoEspera - S2.t;
            ELSE
                TiempoPendiente := T#0S;
            END_IF;
            ```
        -  Incluye la acción `a_TiempoPendiente_Calcular` como acción principal (**Main action**) en la etapa de espera (`S2`).

    ??? info "Programación Defensiva"
        - La condición defensiva `TiempoEspera >= S2.t` previene un **desbordamiento negativo (*underflow*)** en la resta, asegurando que el cálculo solo se realice cuando el resultado sea mayor o igual a cero.
        - Además, la estructura `ELSE` garantiza el **determinismo del PLC** al forzar explícitamente la variable a `T#0S`, evitando que `TiempoPendiente` retenga valores obsoletos de ciclos anteriores si la condición no se cumple.
        - La **Programación Defensiva** usada en su justa medida se considera una buena práctica de programación que favorece el **Código Limpio**.

3. Modifica la visualización.

    ![V_Carro Temporizado](./img/v-carro-temporizado.png){ .screenshot }

    ??? info "Comentario"
        Incluye en la visualización `V_Carro` un objeto gráfico para introducir el tiempo de espera deseado y otro para mostrar el tiempo pendiente.

4. Procede como en el apartado anterior para probar el programa desde la visualización.

#### Carro Limitado

<span class="objetivo-hito">Implementemos una cuenta en SFC</span>


1. Modifica la parte de declaración:

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

    ??? info "Comentarios"
        - El parámetro entero de entrada `ManiobrasTotales`, declarado en `VAR_INPUT`, contiene el número total de maniobras deseadas. Puedes establecer un valor inicial, por ejemplo, `1`.
        - El parámetro entero de salida `ManiobrasPendientes`, declarado en `VAR_OUTPUT`, contiene el número de maniobras pendientes.

2. Modifica el código:

    ![FB_Carro_GRF_SFC limitado](./img/fb-carro-grf-sfc-limitado.png){ .screenshot }

    !!! info "Comentarios"
        - Incluye una nueva etapa (`S4`) al final de la secuencia para evaluar si terminó la tarea.
        - Incluye una rama alternativa con salto atrás a la etapa `S4`.
        - Se regresa a la etapa inicial por la rama principal si terminó la tarea (`ManiobrasPendientes = 0`).
        - Se vuelve a la primera etapa de la secuencia (`S1`) si quedan maniobras por realizar (`ManiobrasPendientes > 0`).
        - Incluye una acción `a_ManiobrasPendientes_Reiniciar` para establecer el valor de la cuenta al iniciar la tarea y asociarla como acción a la salida a la etapa inicial (`S0`).

            ```iecst
            ManiobrasPendientes := ManiobrasTotales;
            ```

        - Incluye una acción `a_ManiobrasPendientes_Calcular` para decrementar el valor de la cuenta con la finalización de cada maniobra y asociarla como acción a la entrada a la etapa final (`S4`).

            ```iecst
            IF (ManiobrasPendientes > 0) THEN
                ManiobrasPendientes := ManiobrasPendientes - 1;
            END_IF;
            ```
3. Modifica la visualización.

    ![V_Carro Limitado](./img/v-carro-limitado.png){ .screenshot }

    ??? info "Comentarios"
    Incluye en la visualización `V_Carro` un objeto gráfico para introducir el número total de maniobras y otro para mostrar las maniobras pendientes.

4. Procede como en el apartado anterior para probar el programa desde la visualización.

#### Carro Señalizado

<span class="objetivo-hito">Implementemos una intermitencia en SFC</span>

1. Incluye la librería `Util.lib` en las referencias (`References`) del proyecto.
2. Modifica la parte de declaración.

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

    ??? info "Comentarios"
        - Añade una instancia `Intermitencia` del bloque funcional `BLINK` de la librería `Util`, que implementa una intermitencia.

3. Modifica la parte de implementación.

    ![FB_Carro_GRF_SFC Senalizado](./img/fb-carro-grf-sfc-senalizado.png){ .screenshot }

    !!! info "Comentarios"
        - Se incluye una acción `a_LamparaMarcha` para establecer el valor de `o_LamparaMarcha`, implementando tanto la acción condicionada a `BLK` en la etapa inicial (`SO`) como la acción continua en el resto de etapas.

            ```iecst
            Intermitencia(Enable := S0.x);

            o_LamparaMarcha := (S0.x AND Intermitencia.OUT) OR S1.x OR S2.x OR S3.x OR S4.x;
            ```

        - Incluye esta acción `a_LamparaMarcha` en todas las etapas tal y como figura en el diagrama grafcet.

4. Procede como en el apartado anterior para probar el programa desde la visualización.
