#### Carro Básico (GRAFCET a ST)

1. Añadir al proyecto un nuevo bloque funcional (`FB`) al proyecto `Carro_Basico_PLC`. [➡️](../../procedimientos/workflow/index.md#crear-una-pou)

    !!! warning "Parámetros POU"
        - Nombre ➔ `FB_Carro_GRF_ST`
        - Type ➔ `Function Block`
        - Implementation Language ➔ `Structured Text`

2. Copiar el bloque de declaración de variables locales (`VAR`) del FB anterior (`FB_Carro_GRF_SFC`), añadiendo una variable entera `Estado` para contener el valor del estado actual.

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

3. Escribir el código {{ST}} correspondiente al carro básico.

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

    ??? info "Implementación FB_Carro_GRF_ST"
        - La estructura de selección múltiple `CASE`, permite evaluar elegantemente la función de transición entre estados expresada en el diagrama grafcet. Así, dependiendo del estado en el que se encuentre el sistemas ([0, 1, 2]) y los eventos de entrada (`i_FinalCarreraDerecha`, `i_FinalCarreraIzquierda`,... ) se calcula el nuevo estado asignando un nuevo valor a la variable Estado.
        - Las salidas se calculan, tal y como se especifica en el diagrama grafcet, a partir del estado (**Salidas Continuas**).

4. Añadir a `MAIN` la declaración de una nueva instancia `Carro` de `FB_Carro_GRF_ST` y comentar la anterior.

    ```iecst {hl_lines="4"}
    PROGRAM MAIN
    VAR
        // Carro: FB_Carro_GRF_SFC;
        Carro: FB_Carro_GRF_ST;
    END_VAR
    ```

    ??? info "Implementación MAIN"
        Al compartir ambos bloques funcionales las mismas variables de entrada y salida:

        - No es necesario volver a activar la configuración.
        - Las rutas de los enlaces de los objetos gráficos con las variables son los mismos.

5. Repetir los pasos 10 a 16 de la sección anterior.
6. Probar el programa desde la visualización accionando las entradas.
7. Cambiar la declaración de la variable Estación a tipo enumerado implícito/local.

    ```iecst {hl_lines="8"}
    FUNCTION_BLOCK FB_Carro_GRF_ST
    // Transcripción del grafcet (GRF -> ST)
    VAR_INPUT
    END_VAR
    VAR_OUTPUT
    END_VAR
    VAR
        Estado: (E_REPOSO, E_MARCHA_DERECHA, E_MARCHA_IZQUIERDA);

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

8. Modificar la implementación sustituyendo los valores numéricos del estado por las etiquetas del tipo enumerado.

    ```iecst
    // FUNCION DE ESTADO
    CASE Estado OF
        E_REPOSO:
            IF i_FinalCarreraIzquierda AND i_PulsadorMarcha THEN
                Estado := E_MARCHA_DERECHA;
            END_IF;
        E_MARCHA_DERECHA:
            IF i_FinalCarreraDerecha THEN
                Estado := E_MARCHA_IZQUIERDA;
            END_IF;
        E_MARCHA_IZQUIERDA: // Marcha Izquierda
            IF i_FinalCarreraIzquierda THEN
                Estado := E_REPOSO;
            END_IF;
    END_CASE;

    // FUNCION DE SALIDA
    o_MarchaDerecha := (Estado = E_MARCHA_DERECHA);
    o_MarchaIzquierda := (Estado = E_MARCHA_IZQUIERDA);
    ```

    ??? Info "Enumerados"
        - Puede observarse la evidente mejora semántica que produce la utilización de enumerados. No es lo mismo referirse a los distintos estados con un simple número (que no dice nada) que con una etiqueta descriptiva.
        - La utilización de enumerados hace innecesairo el uso de comentarios para aclarar el significado de los estados.

#### Carro Pulsado (GRAFCET a ST)

1. Añadir en `FB_Carro_GRF_ST` la declaración de una instancia del bloque funcional `R_TRIG` de la librería estándar (`Tc2_Standard`) para la detección del flanco positivo del pulsador de marcha.

    ```iecst {hl_lines="10-11"}
    FUNCTION_BLOCK FB_Carro_GRF_ST
    // Transcripción del grafcet (GRF -> ST)
    VAR_INPUT
    END_VAR
    VAR_OUTPUT
    END_VAR
    VAR
        Estado: (E_REPOSO, E_MARCHA_DERECHA, E_MARCHA_IZQUIERDA);

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

2. Modifica en la parte de implementación de `FB_Carro_GRF_ST` el código:
    - Añadir la instrucción correspondiente a la invocación del detector de flanco `FlancoPulsadorMarcha(CLK := i_PulsadorMarcha)`.
    - Sustituir en la expresión de la condición de transición de la etapa `E_REPOSO` ➔ `E_MARCHA_DERECHA`, `PulsadorMarcha` por la salida de la instancia del bloque funcional que detecta los flancos positivos en la variable (`FlancoPulsadorMarcha.Q`).

    ```iecst {hl_lines="4-5 7"}
    // FUNCION DE ESTADO
    CASE Estado OF
        E_REPOSO:
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
                Estado := E_REPOSO;
            END_IF;
    END_CASE;

    // FUNCION DE SALIDA
    o_MarchaDerecha := (Estado = E_MARCHA_DERECHA);
    o_MarchaIzquierda := (Estado = E_MARCHA_IZQUIERDA);
    ```

3. Modificar, una vez más, el programa principal `MAIN` para que la instancia que se invoque ejecute el código de `FB_Carro_GRF_ST`, dejando sin comentar la acción correspondiente.

    ```iecst {hl_lines="4"}
    PROGRAM MAIN
    VAR
        // Carro: FB_Carro_GRF_SFC;
        Carro: FB_Carro_GRF_ST;
        // Carro: FB_Carro_GRF_LD;
    END_VAR
    ```

4. Poner el programa en ejecución y comprobar que no basta para iniciar la marcha con que el pulsador de marcha esté activado, sino que es necesario que se realice una acción de impulso.

#### Carro Temporizado (GRAFCET a ST)

1. Añadir en `FB_Carro_GRF_ST` la declaración:
    - Un parámetro de entrada `TiempoEspera` de tipo `TIME` en el bloque de declaración `VAR_INPUT`. Esto permitirá que este parámetro pueda ser modificado desde fuera del bloque funcional. Eventualmente, puede indicarse un valor inicial en su defecto (`T#2S`).
    - Un parámetro de salida `TiempoPendiente` en el bloque de declaración `VAR_OUTPUT` para informar del tiempo de espera pendiente.
    - Una nueva etiqueta `E_ESPERA` correspondiente al estado de espera.
    - Una instancia `TemporizadorEspera` del bloque funcional **Temporizador de Retardo a la Conexión** (`TON`) de la libreria estándar para temporizar la espera.

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
        Estado: (E_REPOSO, E_MARCHA_DERECHA, E_ESPERA, E_MARCHA_IZQUIERDA);

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

2. Modificar en la parte de implementación de `FB_Carro_GRF_ST` el código:
    - Añadir la llamada a TemporizadorEspera.
    - Modificar el estado futuro (E_MARCHA_IZQUIERDA ➔ E_ESPERA) de E_MARCHA_DERECHA
    - Incluir el fragmento de código correspondiente al estado E_ESPERA.

    ```iecst {hl_lines="2 15 17-25"}
    // BLOQUES FUNCIONALES
    TemporizadorEspera(IN := (Estado = E_ESPERA), PT := TiempoEspera);

    // FUNCION DE ESTADO
    CASE Estado OF
        E_REPOSO:
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
                Estado := E_REPOSO;
            END_IF;
    END_CASE;

    // FUNCION DE SALIDA
    o_MarchaDerecha := (Estado = E_MARCHA_DERECHA);
    o_MarchaIzquierda := (Estado = E_MARCHA_IZQUIERDA);
    ```

3. Proceder como en la sección anterior probar el programa desde la visualización.

---

#### Carro Computado (GRAFCET a ST)
