#### Carro Básico

!!! tip "Punto de Partida"
    Esta sección continúa el trabajo de la sección anterior, por lo que aprovecharemos la estructura existente para integrar en ella la implementación en ST.

1. Crear una nueva POU. [➡️](../../procedimientos/workflow/index.md#crear-una-pou)

    !!! warning "Parámetros POU"
        - *Nombre* ➔ `FB_Carro_GRF_ST`
        - *Type* ➔ `Function Block`
        - *Implementation Language* ➔ `Structured Text`

2. Cómo en la sección anterior, declarar todas las variables de entrada/salida del sistema en `FB_Carro_GRF_ST` como variables locales (`VAR_LOCAL`), e incluir una variable entera para contener el valor del estado actual (`Estado`). [➡️](../../procedimientos/workflow/index.md#declarar-una-variable)

    ```iecst {hl_lines="8"}
    FUNCTION_BLOCK FB_Carro_GRF_ST
    // Transcripción del grafcet (GRF -> ST)
    VAR_INPUT
    END_VAR
    VAR_OUTPUT
    END_VAR
    VAR
        Estado: UINT;

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
        - A diferencia de <span class="fondo-rojo-lang">SFC</span>, que gestiona las etapas de forma implícita mediante su propia sintaxis gráfica, en <span class="fondo-azul-lang">ST</span> es necesario declarar una variable numérica explícita para registrar el **estado activo** del sistema.
        - Esta forma de gestionar el estado es válida únicamente para máquinas de **estado concentrado**, en las que toda la actividad del sistema reside en una única etapa, sólo tienen activa una etapa en cada instante.

3. Escribir el código <span class="fondo-azul-lang">ST</span> correspondiente al carro básico.

    ```iecst
    // FUNCION DE ESTADO
    CASE Estado OF
        0: // Reposo
            IF i_FinalCarreraIzquierda AND i_PulsadorMarcha THEN
                Estado := 1;
            END_IF;
        1: // Marcha Derecha
            IF i_FinalCarreraDerecha THEN
                Estado := 2;
            END_IF;
        2: // Marcha Izquierda
            IF i_FinalCarreraIzquierda THEN
                Estado := 0;
            END_IF;
    END_CASE;

    // FUNCION DE SALIDA
    o_MarchaDerecha := (Estado = 1);
    o_MarchaIzquierda := (Estado = 2);
    ```

    ??? info "Comentarios"
        - La estructura de selección múltiple `CASE`, permite evaluar elegantemente la **Función de Estado** expresada en el diagrama grafcet. Así, dependiendo del estado en el que se encuentre el sistemas ([0, 1, 2]) y los eventos de entrada (`i_FinalCarreraDerecha`, `i_FinalCarreraIzquierda`,... ) se calcula el nuevo estado asignando un nuevo valor a la variable `Estado`.
        - Las salidas se calculan, tal y como se especifica en el diagrama *grafcet*, a partir del estado (**Salidas Continuas**).

4. Añadir a `MAIN` la declaración de una nueva instancia `Carro` de tipo `FB_Carro_GRF_ST` y comentar la anterior.

    ```iecst {hl_lines="4"}
    PROGRAM MAIN
    VAR
        // Carro: FB_Carro_GRF_SFC;
        Carro: FB_Carro_GRF_ST;
    END_VAR
    ```

    ??? info "Comentarios"
        Al compartir ambos bloques funcionales las mismas variables de entrada y salida:

        - No es necesario volver a activar la configuración.
        - Las rutas de los enlaces de los objetos gráficos de la visualización con las variables del nuevo bloque funcional son los mismos. Por lo que se puede usar la misma visualización para probar ambos bloques funcionales (de forma alternativa).

5. Probar el programa desde la visualización accionando las entradas.
6. Cambiar la declaración de la variable `Estado`: entero (`UINT`) ➔ **tipo enumerado** implícito/local.

    ```iecst {hl_lines="8"}
    FUNCTION_BLOCK FB_Carro_GRF_ST
    // Transcripción del grafcet (GRF -> ST)
    VAR_INPUT
    END_VAR
    VAR_OUTPUT
    END_VAR
    VAR
        Estado: (E_INICIAL, E_MARCHA_DERECHA, E_MARCHA_IZQUIERDA);

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

7. Modificar la implementación sustituyendo los valores numéricos del estado por los correspondientes miembros del tipo enumerado (literales de enumeración).

    ```iecst {hl_lines="3-14 18-19"}
    // FUNCION DE ESTADO
    CASE Estado OF
        E_INICIAL:
            IF i_FinalCarreraIzquierda AND i_PulsadorMarcha THEN
                Estado := E_MARCHA_DERECHA;
            END_IF;
        E_MARCHA_DERECHA:
            IF i_FinalCarreraDerecha THEN
                Estado := E_MARCHA_IZQUIERDA;
            END_IF;
        E_MARCHA_IZQUIERDA: // Marcha Izquierda
            IF i_FinalCarreraIzquierda THEN
                Estado := E_INICIAL;
            END_IF;
    END_CASE;

    // FUNCION DE SALIDA
    o_MarchaDerecha := (Estado = E_MARCHA_DERECHA);
    o_MarchaIzquierda := (Estado = E_MARCHA_IZQUIERDA);
    ```

    ??? tip "Enumerados"
        - Puede observarse la evidente mejora semántica que produce la utilización de enumerados. No es lo mismo referirse a los distintos estados con un simple número (que no dice nada) que con un nombre descriptivo.
        - La utilización de enumerados hace innecesairo el uso de comentarios para aclarar el significado de los estados.
        - En estos casos, la utilización de enumerados se considera una buena práctica de código limpio.

#### Carro Pulsado

1. Modificar la parte de declaración.

    ```iecst {hl_lines="10-11"}
    FUNCTION_BLOCK FB_Carro_GRF_ST
    // Transcripción del grafcet (GRF -> ST)
    VAR_INPUT
    END_VAR
    VAR_OUTPUT
    END_VAR
    VAR
        Estado: (E_INICIAL, E_MARCHA_DERECHA, E_MARCHA_IZQUIERDA);

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
        - Añadir una instancia del bloque funcional `R_TRIG` de la librería estándar (`Tc2_Standard`) para la detección del flanco positivo del pulsador de marcha (`FlancoPulsadorMarcha`).
        - La librería `Tc2_Standard` se incluye automáticamente, al crear un proyecto PLC estándar.

2. Modificar la parte de implementación.

    ```iecst {hl_lines="4-5 7"}
    // FUNCION DE ESTADO
    CASE Estado OF
        E_INICIAL:
            // Acción principal
            FlancoPulsadorMarcha(CLK := i_PulsadorMarcha);

            IF i_FinalCarreraIzquierda AND FlancoPulsadorMarcha.Q THEN
                Estado := E_MARCHA_DERECHA;
            END_IF;
        E_MARCHA_DERECHA:
            IF i_FinalCarreraDerecha THEN
                Estado := E_MARCHA_IZQUIERDA;
            END_IF;
        E_MARCHA_IZQUIERDA: // Marcha Izquierda
            IF i_FinalCarreraIzquierda THEN
                Estado := E_INICIAL;
            END_IF;
    END_CASE;

    // FUNCION DE SALIDA
    o_MarchaDerecha := (Estado = E_MARCHA_DERECHA);
    o_MarchaIzquierda := (Estado = E_MARCHA_IZQUIERDA);
    ```

    ??? info "Comentarios"
        - Añadir la instrucción correspondiente a la invocación del detector de flanco `FlancoPulsadorMarcha(CLK := i_PulsadorMarcha)`.
        - Sustituir en la expresión de la condición de transición de la etapa `E_INICIAL` ➔ `E_MARCHA_DERECHA`, `PulsadorMarcha` por la salida de la instancia del bloque funcional que detecta los flancos positivos en la variable (`FlancoPulsadorMarcha.Q`).

3. Poner el programa en ejecución y comprobar, con la ayudad de la visualización, que no basta para iniciar la marcha con que el pulsador de marcha esté activado, sino que es necesario que se realice una acción de impulso.

#### Carro Temporizado

1. Modificar la parte de declaración.

    ```iecst {hl_lines="4 7 10 14"}
    FUNCTION_BLOCK FB_Carro_GRF_ST
    // Transcripción del grafcet (GRF -> ST)
    VAR_INPUT
        TiempoEspera: TIME := T#2S;
    END_VAR
    VAR_OUTPUT
        TiempoPendiente: TIME;
    END_VAR
    VAR
        Estado: (E_INICIAL, E_MARCHA_DERECHA, E_ESPERA, E_MARCHA_IZQUIERDA);

        // Bloques Funcionales
        FlancoPulsadorMarcha: R_TRIG;
        TemporizadorEspera: TON;

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
        - Añadir un parámetro de entrada `TiempoEspera` de tipo `TIME` en el bloque de declaración `VAR_INPUT`. Esto permite que este parámetro pueda ser modificado desde fuera del bloque funcional. Eventualmente, puede indicarse un valor inicial en su defecto (`T#2S`).
        - Añadir un parámetro de salida `TiempoPendiente` en el bloque de declaración `VAR_OUTPUT` para informar del tiempo de espera pendiente.
        - Añadir un nuevo miembro a la lista de literales de enumeración, correspondiente al estado de espera (`E_ESPERA`).
        - Añadir una instancia `TemporizadorEspera` del bloque funcional **Temporizador de Retardo a la Conexión** (`TON`) de la libreria estándar (`Tc2_standard`) para temporizar la espera.

    ??? note "Temporizaciones ST vs SFC"
        A diferencia de <span class="fondo-rojo-lang">SFC</span>, que gestiona automáticamene el tiempo que lleva activa una determinada etapa (`.t`), en <span class="fondo-azul-lang">ST</span> es necesario implentar esta temporización de forma explícita, por ejemplo, mediante una instancia de un temporizador.

2. Modificar la parte de implementación.

    ```iecst {hl_lines="2 15 17-25"}
    // BLOQUES FUNCIONALES
    TemporizadorEspera(IN := (Estado = E_ESPERA), PT := TiempoEspera);

    // FUNCION DE ESTADO
    CASE Estado OF
        E_INICIAL:
            // Acción principal
            FlancoPulsadorMarcha(CLK := i_PulsadorMarcha);

            IF i_FinalCarreraIzquierda AND FlancoPulsadorMarcha.Q THEN
                Estado := E_MARCHA_DERECHA;
            END_IF;
        E_MARCHA_DERECHA:
            IF i_FinalCarreraDerecha THEN
                Estado := E_ESPERA;
            END_IF;
        E_ESPERA:
            // Acción principal
            IF (TiempoEspera >= TemporizadorEspera.ET) THEN
                TiempoPendiente := TiempoEspera - TemporizadorEspera.ET;
            END_IF;

            IF TemporizadorEspera.Q  THEN
                Estado := E_MARCHA_IZQUIERDA;
            END_IF;
        E_MARCHA_IZQUIERDA:
            IF i_FinalCarreraIzquierda THEN
                Estado := E_INICIAL;
            END_IF;
    END_CASE;

    // FUNCION DE SALIDA
    o_MarchaDerecha := (Estado = E_MARCHA_DERECHA);
    o_MarchaIzquierda := (Estado = E_MARCHA_IZQUIERDA);
    ```

    ??? info "Comentarios"
        - Se añade la llamada al `TemporizadorEspera`.
        - Se modifica el estado futuro de `E_MARCHA_DERECHA`: `E_MARCHA_IZQUIERDA` ➔ `E_ESPERA`.
        - Se incluye el fragmento de código correspondiente al estado `E_ESPERA`. Este fragmento de código incluye, por un lado la evalución de la función de estado y, por otro, la acción principal asociada a la etapa `E_ESPERA` para calcular el tiempo de espera pendiente.

3. Proceder como en el apartador anterior probar el programa desde la visualización.

#### Carro limitado

1. Modificar la parte de declaración.

    ```iecst {hl_lines="4 9 12"}
    FUNCTION_BLOCK FB_Carro_GRF_ST
    // Transcripción del grafcet (GRF -> ST)
    VAR_INPUT
        TiempoEspera: TIME := T#2S;
        ManiobrasTotales: UINT := 1;
    END_VAR
    VAR_OUTPUT
        TiempoPendiente: TIME;
        ManiobrasPendientes: UINT;
    END_VAR
    VAR
        Estado: (E_INICIAL, E_MARCHA_DERECHA, E_ESPERA, E_MARCHA_IZQUIERDA, E_FINAL);

        // Bloques Funcionales
        FlancoPulsadorMarcha: R_TRIG;
        TemporizadorEspera: TON;

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
        - El parámetro entero de entrada `ManiobrasTotales` del bloque de declaración `VAR_INPUT` continene el valor del número total de maniobras deseadas. Eventualmente, puede indicarse un valor inicial en su defecto (`1`).
        - El parámetro entero de salida `ManiobrasPendientes`del bloque de declaración `VAR_OUTPUT` contiene el número de maniobras pendientes de realizar.
        - La lineral de enumeración `E_FINAL`, representa el estado correpondiente a la nueva etapa `S4`, en el que se calcula en nuevo valor de las maniobras pendientes y se decide si continuar con la siguiente maniobra o detenerse en la etapa inicial.

2. Modificar la parte de implementación.

    ```iecst {hl_lines="11-12 35-38 40 42-47"}
    // BLOQUES FUNCIONALES
    TemporizadorEspera(IN := (Estado = E_ESPERA), PT := TiempoEspera);

    // FUNCION DE ESTADO
    CASE Estado OF
        E_INICIAL:
            // Acción principal
            FlancoPulsadorMarcha(CLK := i_PulsadorMarcha);

            IF i_FinalCarreraIzquierda AND FlancoPulsadorMarcha.Q THEN
            // Acción de salida
            ManiobrasPendientes := ManiobrasTotales;

            Estado := E_MARCHA_DERECHA;
            END_IF;
        E_MARCHA_DERECHA:
            IF i_FinalCarreraDerecha THEN
                Estado := E_ESPERA;
            END_IF;
        E_ESPERA:
            // Acción principal
            IF (TiempoEspera >= TemporizadorEspera.ET) THEN
                TiempoPendiente := TiempoEspera - TemporizadorEspera.ET;
            END_IF;

            IF TemporizadorEspera.Q  THEN
                Estado := E_MARCHA_IZQUIERDA;
            END_IF;
        E_MARCHA_IZQUIERDA:
            IF i_FinalCarreraIzquierda THEN
                // Acción de entrada del siguiente estado
                IF (ManiobrasPendientes > 0) THEN
                    ManiobrasPendientes := ManiobrasPendientes - 1;
                END_IF;

                Estado := E_FINAL;
            END_IF;
        E_FINAL:
            IF (ManiobrasPendientes = 0) THEN
                Estado := E_INICIAL;
            ELSIF (ManiobrasPendientes > 0) THEN
                Estado := E_MARCHA_DERECHA;
            END_IF;
    END_CASE;

    // FUNCION DE SALIDA
    o_MarchaDerecha := (Estado = E_MARCHA_DERECHA);
    o_MarchaIzquierda := (Estado = E_MARCHA_IZQUIERDA);
    ```

    ??? info "Comentarios"
        - Se incluye la acción de salida de la etapa `E_INICIAL` (`S0`) para establecer el valor inicial de la cuenta de maniobras pendientes.
        - Se incluye la acción de entrada de la etapa `E_FINALAL` (`S4`) para decrementar el valor de la cuenta de maniobras pendientes.
        - Se modifica el estado futuro de `E_MARCHA_IZQUIERDA` (`S2`): `E_INICIAL` ➔ `E_FINAL`.
        - Se incluye el estado E_FINAL (`S4`), con su código correspondiente.

3. Probar el código desde la visualización.

#### Carro Señalizado

1. Incluir la librería `Util.lib` en las referencias (`References`) del proyecto.
2. Modificar l parte de declaración.

    ```iecst {hl_lines="17"}
    FUNCTION_BLOCK FB_Carro_GRF_ST
    // Transcripción del grafcet (GRF -> ST)
    VAR_INPUT
        TiempoEspera: TIME := T#2S;
        ManiobrasTotales: UINT := 2;
    END_VAR
    VAR_OUTPUT
        TiempoPendiente: TIME;
        ManiobrasPendientes: UINT;
    END_VAR
    VAR
        Estado: (E_INICIAL, E_MARCHA_DERECHA, E_ESPERA, E_MARCHA_IZQUIERDA, E_FINAL);

        // Bloques Funcionales
        FlancoPulsadorMarcha: R_TRIG;
        TemporizadorEspera: TON;
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
        - El bloque funcional `BLINK` de la librería `Util.lib`, se utilizará para implementar la intermitencia de la lámpara de marcha.

3. Modificar la parte de implementación.

    ```iecst {hl_lines="3 54"}
    // BLOQUES FUNCIONALES
    TemporizadorEspera(IN := (Estado = E_ESPERA), PT := TiempoEspera);
    Intermitencia(ENABLE := (Estado = E_INICIAL));

    // FUNCION DE ESTADO
    CASE Estado OF
        E_INICIAL:
            // Acción principal
            FlancoPulsadorMarcha(CLK := i_PulsadorMarcha);

            IF i_FinalCarreraIzquierda AND FlancoPulsadorMarcha.Q THEN
            // Acción de salida
            ManiobrasPendientes := ManiobrasTotales;

            Estado := E_MARCHA_DERECHA;
            END_IF;
        E_MARCHA_DERECHA:
            IF i_FinalCarreraDerecha THEN
                Estado := E_ESPERA;
            END_IF;
        E_ESPERA:
            // Acción principal
            IF (TiempoEspera >= TemporizadorEspera.ET) THEN
                TiempoPendiente := TiempoEspera - TemporizadorEspera.ET;
            END_IF;

            IF TemporizadorEspera.Q  THEN
                Estado := E_MARCHA_IZQUIERDA;
            END_IF;
        E_MARCHA_IZQUIERDA:
            IF i_FinalCarreraIzquierda THEN
                // Acción de entrada del siguiente estado
                IF (ManiobrasPendientes > 0) THEN
                    ManiobrasPendientes := ManiobrasPendientes - 1;
                END_IF;

                Estado := E_FINAL;
            END_IF;
        E_FINAL:
            IF (ManiobrasPendientes = 0) THEN
                Estado := E_INICIAL;
            ELSIF (ManiobrasPendientes > 0) THEN
                Estado := E_MARCHA_DERECHA;
            END_IF;
    END_CASE;

    // FUNCION DE SALIDA
    o_MarchaDerecha := (Estado = E_MARCHA_DERECHA);
    o_MarchaIzquierda := (Estado = E_MARCHA_IZQUIERDA);
    o_LamparaMarcha := (Estado <> E_INICIAL) OR Intermitencia.Q;
    ```

    ??? info "Comentarios"
        - Se incluye la llamada al bloque `Intermitencia` para activarlo en la etapa `E_INICIAL`.
        - Se calcula el valor de `o_LamparaMarcha`, para que sea encienda permanentemente cuando el carro está en marcha e intermitente cuando esté esperando la orden de marcha en la etapa inicial.

4. Probar el código desde la visualización.
