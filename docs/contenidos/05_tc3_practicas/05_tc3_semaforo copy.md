# 🚦 Semáforo (ArduTC)

!!! info "Nota"
    Esta práctica **NO** es entregable.

## Ejemplo de apoyo

Utilice el ejemplo del [**carro básico**](../contenidos/03_tc3_carro_basico.md) como apoyo para entender la estructura del proyecto.

## Entregables

Ninguno.

## Descripción del proyecto

En esta práctica se implementará el control de un pequeño **semáforo físico** conectado a una placa **Arduino UNO** mediante una *shield* de prácticas. El Arduino actuará como terminal de entradas/salidas para un programa PLC ejecutado en **TwinCAT 3**, utilizando **ArduTC** como interfaz entre ambos.

El objetivo principal es que el alumno programe en TwinCAT 3 una **secuencia de control en lenguaje** {{SFC}} y compruebe su funcionamiento sobre un sistema físico de bajo coste.

El sistema dispone de:

- Un semáforo con tres luces: verde, amarilla y roja.
- Un pulsador para solicitar el cambio del semáforo.
- Una placa Arduino UNO y la *shield* de conexión.
- Un PC con TwinCAT 3 y ArduTC.

En esta segunda práctica, trataremos de aplicar los conocimientos obtenidos en el ejemplo del **carro básico**.

---

### Elementos constituyentes

La parte operativa está formada por:

- Una salida digital para la **luz verde**.
- Una salida digital para la **luz amarilla**.
- Una salida digital para la **luz roja**.
- Una entrada digital correspondiente al **pulsador de solicitud**.

La lógica de control se ejecutará íntegramente en el PLC de TwinCAT 3.  
El Arduino se utilizará únicamente como dispositivo físico de entrada/salida a través de ArduTC.

---

### Descripción funcional

El funcionamiento requerido será el siguiente:

1. Al iniciar el sistema, el semáforo debe permanecer en **verde**.
2. Mientras no se pulse el botón, el semáforo permanecerá indefinidamente en verde.
3. Cuando se accione el pulsador:
    - se registrará una solicitud de cambio;
    - el semáforo permanecerá todavía en verde durante un breve intervalo;
    - posteriormente pasará a amarillo;
    - después pasará a rojo.
4. El semáforo permanecerá en rojo durante un tiempo determinado.
5. Finalmente, volverá automáticamente a verde, quedando preparado para una nueva solicitud.
6. Las pulsaciones realizadas mientras el semáforo está ejecutando una secuencia de cambio no tendrán efecto.

Para esta práctica se utilizarán inicialmente los siguientes tiempos:

| Parámetro | Valor inicial |
| --- | ---: |
| Espera tras pulsar el botón | 2 s |
| Duración del amarillo | 2 s |
| Duración del rojo | 5 s |

Estos valores deberán declararse como parámetros del bloque funcional para poder modificarlos fácilmente.

### Entradas y salidas

| Nombre | Tipo | Origen | Descripción |
| --- | --- | --- | --- |
| `i_Pulsador` | `BOOL` | Input | Pulsador de solicitud de cambio |
| `o_Verde` | `BOOL` | Output | Luz verde del semáforo |
| `o_Amarillo` | `BOOL` | Output | Luz amarilla del semáforo |
| `o_Rojo` | `BOOL` | Output | Luz roja del semáforo |

!!! note "Asignación de pines"
    Los pines físicos del Arduino dependerán de la *shield* utilizada en el laboratorio.  
    La asociación entre estas variables de TwinCAT 3 y los pines reales se realizará posteriormente mediante **ArduTC**.

---

## Especificación funcional

La secuencia principal deberá implementarse utilizando {{SFC}}.

Se propone la siguiente secuencia:
TODO: Cambiarlo por una imagen.

```text
                         Pulsador
                            │
                            ▼
                  ┌──────────────────┐
                  │     S0_VERDE     │
                  │   Luz verde ON   │
                  └────────┬─────────┘
                           │ solicitud
                           ▼
                  ┌──────────────────┐
                  │    S1_ESPERA     │
                  │   Luz verde ON   │
                  └────────┬─────────┘
                           │ t >= T_espera
                           ▼
                  ┌──────────────────┐
                  │   S2_AMARILLO    │
                  │ Luz amarilla ON  │
                  └────────┬─────────┘
                           │ t >= T_amarillo
                           ▼
                  ┌──────────────────┐
                  │      S3_ROJO     │
                  │    Luz roja ON   │
                  └────────┬─────────┘
                           │ t >= T_rojo
                           └──────────────► S0_VERDE
```

Las etapas serán:

| Etapa | Función |
| --- | --- |
| `S0_VERDE` | Estado inicial. Semáforo verde y espera de una nueva solicitud. |
| `S1_ESPERA` | Mantiene el verde encendido durante un breve tiempo después de pulsar. |
| `S2_AMARILLO` | Enciende exclusivamente la luz amarilla. |
| `S3_ROJO` | Enciende exclusivamente la luz roja. |

Las transiciones serán:

| Transición | Condición |
| --- | --- |
| `S0_VERDE → S1_ESPERA` | Detección de una pulsación. |
| `S1_ESPERA → S2_AMARILLO` | `S1_ESPERA.t >= TiempoEspera` |
| `S2_AMARILLO → S3_ROJO` | `S2_AMARILLO.t >= TiempoAmarillo` |
| `S3_ROJO → S0_VERDE` | `S3_ROJO.t >= TiempoRojo` |

!!! info "Temporización en SFC"
    TwinCAT 3 monitoriza automáticamente el tiempo durante el que una etapa permanece activa. Puede consultarse mediante:

    ```iecst
    NombreEtapa.t
    ```

    Por tanto, para esta práctica no será necesario crear bloques `TON` para las temporizaciones principales.

---

## Requisitos del sistema

### Hardware

- PC compatible con TwinCAT 3.
- Arduino UNO.
- *Shield* de prácticas.
- Semáforo de tres luces.
- Pulsador.
- Cables Dupont.
- Cable USB.

### Software

- TwinCAT 3 XAE.
- TwinCAT 3 XAR.
- ArduTC.

### Lenguajes IEC 61131-3

- {{SFC}} para la implementación de la secuencia principal.
- {{ST}} únicamente para el programa principal y para pequeñas acciones auxiliares cuando sea necesario.

## Funcionalidades

!!! warning "Atención"
    📃 Versión descargable [aquí](../../pdfs/Checklist_Func_Semaforo.pdf){target="_blank"}.

El proyecto desarrollado debe tener las siguientes funcionalidades:

!!! info "Requeridas"
    1. Secuencia de producción normal.
    1. Visualización funcional.
    1. Modo automático.
    2. Parametrización de los tiempos.

## Componentes

- {{ST}} `MAIN`: programa principal.
    - {{SFC}} `FB_Semaforo`: lógica de control.
- `VISU_Semaforo`: interfaz gráfica

## Itinerario

!!! warning "Atención"
    La lista es *clickable* pero **NO** guarda el estado; si actualizas o entras/sales de la página se perderán las marcas.

    📃 Versión descargable [aquí](../../pdfs/Checklist_Itinerario_Semaforo.pdf){target="_blank"}.

### Creación del proyecto

- [ ] Crear una solución con el nombre: `XXX_tc3_semaforo_GYY` con `XXX` = iniciales de la asignatura, `YY` = número del grupo.
    - Menú `New → Solution`.
- [ ] Crear el proyecto PLC con nombre `Semaforo_PLC`.
    - **CD** sobre PLC, `New → Project`.
- [ ] Crear el bloque funcional `FB_Semaforo` en {{SFC}}.
    - **CD** sobre POUs, `New → POU → Function Block`.

### Declaraciones

- [ ] Declarar los tiempos necesarios como parámetros de entrada del **FB**: `TiempoEspera`, `TiempoAmarillo`, `TiempoRojo`.

    ```iecst
    VAR_INPUT
        TiempoEspera    : TIME := T#2S;
        TiempoAmarillo  : TIME := T#2S;
        TiempoRojo      : TIME := T#5S;
    END_VAR
    ```

    De esta forma los tiempos de funcionamiento podrán modificarse desde `MAIN` sin alterar la secuencia {{SFC}}.

    | Variable | Tipo | Descripción |
    | --- | --- | --- |
    | `TiempoEspera` | `TIME` | Tiempo que continúa en verde después de recibir la solicitud |
    | `TiempoAmarillo` | `TIME` | Duración de la fase amarilla |
    | `TiempoRojo` | `TIME` | Duración de la fase roja |

- [ ] Declarar las variables de entrada y salida en el **FB** según la tabla de E/S del sistema. Declarar también el detector de flanco.

    ```iecst
    VAR
        // Entrada
        i_Pulsador   AT %I* : BOOL;

        // Salidas
        o_Verde      AT %Q* : BOOL;
        o_Amarillo   AT %Q* : BOOL;
        o_Rojo       AT %Q* : BOOL;

        // Utilidades
        FlancoPulsador : R_TRIG;
    END_VAR
    ```

    Las declaraciones `AT %I*` y `AT %Q*` permiten que TwinCAT trate estas variables como entradas y salidas del proceso.

    !!! info "Conexión con el *hardware*"
        Posteriormente, podrán ser asociadas a los pines del Arduino mediante ArduTC.

### Lógica de control

- [ ] Crear la lógica de control en `FB_Semaforo`:
    - [ ] Renombrar la etapa inicial por `S0_VERDE` y asociar la acción de activación de la luz verde: `o_Verde`.
        - **CD** sobre la etapa → `Insert action association` y especificar la acción.
    - [ ] Asociar a la etapa una acción memorizada para el control de flanco del pulsador:
        - [ ] Crear acción y escribir el código.
            - **CD** sobre el **FB** → `Add → Action` (nombre: `a_Pulsador`, lenguaje: {{ST}}).

            ```iecst
            FlancoPulsador(CLK := i_Pulsador);
            ```

        - [ ] Asociar la acción a la etapa.
            - **CD** sobre la etapa → `Insert action association` y especificar la acción.

    - [ ] Escribir la condición de la transición entre `S0_VERDE` y `S1_ESPERA`:

        ```iecst
        FlancoPulsador.Q
        ```

        La transición se producirá cuando se detecte el flanco de subida del pulsador.

    - [ ] Crear etapa `S1_ESPERA` y asociar la acción de activación de la luz verde: `o_Verde`.
        - **CD** sobre la transición anterior y `Insert step-transition after`.
    - [ ] Escribir la condición de la transición hacia `S2_AMARILLO`:

        ```iecst
        S1_ESPERA.t >= TiempoEspera
        ```

        El objetivo es simular que la solicitud ha sido recibida, pero que el cambio del semáforo no se produce instantáneamente. La transición se producirá cuando pase el tiempo de espera en esta etapa.

    - [ ] Crear etapa `S2_AMARILLO` y asociar la acción de activación de la luz verde: `o_Amarillo`.
        - **CD** sobre la transición anterior y `Insert step-transition after`.
    - [ ] Escribir la condición de la transición hacia `S3_ROJO`:

        ```iecst
        S2_AMARILLO.t >= TiempoAmarillo
        ```

        La transición se producirá cuando pase el tiempo de color amarillo en esta etapa.

- [ ] Crear etapa `S3_ROJO` y asociar la acción de activación de la luz verde: `o_Rojo`.
        - **CD** sobre la transición anterior y `Insert step-transition after`.
    - [ ] Escribir la condición de la transición hacia `S0_VERDE`:

        ```iecst
        S3_ROJO.t >= TiempoRojo
        ```

        La transición se producirá cuando pase el tiempo de color rojo en esta etapa.

### Visualización

Se puede realizar utilizando elementos gráficos sencillos de TwinCAT 3, por ejemplo círculos o lámparas para representar las tres luces del semáforo y el estado del pulsador.

- [ ] Crear un indicador para la **luz verde** asociado a `o_Verde`.
- [ ] Crear un indicador para la **luz amarilla** asociado a `o_Amarillo`.
- [ ] Crear un indicador para la **luz roja** asociado a `o_Rojo`.
- [ ] Crear un indicador del estado del **pulsador** asociado a `i_Pulsador`.

!!! note "Objetivo de la visualización"
    La visualización no sustituye al semáforo físico conectado mediante ArduTC. Su finalidad es facilitar la depuración y permitir comparar en tiempo real el estado interno del programa PLC con el comportamiento del hardware.

### Ejecución del programa

- [ ] Abrir el programa `MAIN` y declarar una instancia:

    ```iecst
    PROGRAM MAIN
    VAR
        Semaforo : FB_Semaforo;
    END_VAR
    ```

- [ ] En el cuerpo del programa realizar la llamada:

    ```iecst
    Semaforo(
        TiempoEspera   := T#2S,
        TiempoAmarillo := T#2S,
        TiempoRojo     := T#5S
    );
    ```

- [ ] Compilar.
      - Menú `Build → Build Solution`.
- [ ] Seleccionar el controlador local o el emulador.
- [ ] Activar la configuración.
      - Menú `TwinCAT → Activate Configuration`
- [ ] Transferir el proyecto y ponerlo en funcionamiento.
      - Menú `TwinCAT → Login`. Menú `TwinCAT → Start`.

### ArduTC

Una vez que el programa PLC funcione correctamente, se conectará a la placa Arduino.

- [ ] Conectar el Arduino
      - Conectar la *shield*, el semáforo y el pulsador al Arduino UNO.
      - Conectar el Arduino al PC mediante USB.
      - Comprobar el puerto serie asignado por Windows.

- [ ] Abrir el proyecto en ArduTC
      - Iniciar ArduTC y seleccionar el proyecto/archivo de símbolos generado por TwinCAT 3.

      - Localizar las variables:

        ```text
        i_Pulsador
        o_Verde
        o_Amarillo
        o_Rojo
        ```

        !!! warning "Variables no visibles"
            Si alguna variable no aparece en ArduTC, comprobar que el proyecto PLC se ha compilado correctamente y que las variables físicas han sido declaradas con `AT %I*` o `AT %Q*`.

- [ ] Asociar las variables a los pines

      - Asignar cada variable de TwinCAT al pin correspondiente de la *shield*:

        | Variable TwinCAT | Tipo Arduino | Pin |
        | --- | --- | --- |
        | `i_Pulsador` | Digital Input | **según shield** |
        | `o_Verde` | Digital Output | **según shield** |
        | `o_Amarillo` | Digital Output | **según shield** |
        | `o_Rojo` | Digital Output | **según shield** |

      - Guardar la configuración y establecer la comunicación.

### Comprobación del funcionamiento

Una vez iniciado TwinCAT y establecida la conexión de ArduTC:

- [ ] Comprobar que inicialmente está encendida únicamente la luz verde.
- [ ] Pulsar brevemente el botón.
- [ ] Verificar que el verde permanece encendido durante `TiempoEspera`.
- [ ] Comprobar el cambio a amarillo.
- [ ] Comprobar el cambio a rojo.
- [ ] Verificar que, transcurrido `TiempoRojo`, vuelve automáticamente a verde.
- [ ] Volver a pulsar el botón y comprobar que se inicia una nueva secuencia.
- [ ] Pulsar el botón durante las fases amarilla y roja y verificar que estas pulsaciones no modifican la secuencia en curso.

## Autoevaluación

Una vez finalizada la implementación, responde a las siguientes preguntas:

1.  ¿Qué ventaja tiene utilizar una etapa independiente `S1_ESPERA` en lugar de pasar directamente de verde a amarillo al pulsar?
2.  ¿Qué ocurriría si se utilizase directamente `i_Pulsador` en la primera transición en lugar de un detector de flanco?
3.  ¿Qué representa la variable `S2_AMARILLO.t`?
4.  ¿Qué parte del sistema ejecuta realmente la lógica del PLC: Arduino, ArduTC o TwinCAT 3?
5.  ¿Qué ventaja aporta separar el programa PLC de la asignación física de pines realizada en ArduTC?

## Ampliaciones opcionales

Una vez completada la versión básica se pueden plantear las siguientes extensiones:

- Hacer parpadear la luz verde durante el último segundo anterior al amarillo.
- Memorizar una pulsación realizada durante la fase roja para atenderla posteriormente.
- Permitir modificar los tiempos desde una visualización de TwinCAT 3.
- Contabilizar el número total de solicitudes atendidas.
- Añadir un segundo semáforo y coordinar ambos mediante un único SFC.
