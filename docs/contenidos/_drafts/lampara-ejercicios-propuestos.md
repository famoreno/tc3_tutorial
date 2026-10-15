## :fontawesome-solid-puzzle-piece: Ejercicios Propuestos

A continuación se propone una serie de retos para profundizar en los conceptos fundamentales del lenguaje **Texto Estructurado (ST)** y la librería estándar IEC 61131-3.

Para la prueba se recomienda implementar una interfaz visual en cada ejercicio añadiendo los botones y elementos necesarios en una **visualización**.

---

### 1. Lámpara Memorizada

**Descripción:**

- La lámpara se enciende al accionar el pulsador de conexión (`i_PulsadorConexion`).
- La lámpara se apaga al accionar el pulsador de desconexión (`i_PulsadorDesconexion`).

??? tip "Pista para la solución"
    - Utiliza la [instrucción condicional IF ... THEN](https://infosys.beckhoff.com/english.php?content=../content/1033/tc3_plc_intro/2528275595.html){ target="_blank" }.
    - Piensa cuál de las dos condiciones debe prevalecer en caso de que se presionen ambos pulsadores al mismo tiempo (prioridad de activación o de desactivación).

---

### 2. Lámpara Conmutada

**Descripción:**

- La lámpara se enciende si, estando apagada, se acciona el pulsador (`i_Pulsador`).
- La lámpara se apaga si, estando encendida, se acciona el pulsador (`i_Pulsador`).

??? tip "Pista para la solución"
    - Utiliza el detector de flanco ascendente [`R_TRIG`](https://infosys.beckhoff.com/english.php?content=../content/1033/tcplclib_tc2_standard/74391563.html&id=){ target="_blank" } de la librería `Standard`.
    - Declara una instancia del bloque funcional detector de flanco ascendente (`Pulsación: R_TRIG;`).
    - Utiliza el [operador NOT](https://infosys.beckhoff.com/english.php?content=../content/1033/tc3_plc_intro/2528902283.html&id=){ target="_blank" } para la conmutación de la salida (`o_Lampara := NOT o_Lampara;`) cuando se produce un flanco en el pulsador (`Pulsacion.Q`).

---

### 3. Lámpara Temporizada

**Descripción:**

- La lámpara se enciende al accionar el pulsador (`i_Pulsador`).
- La lámpara se apaga transcurrido un cierto tiempo (por ejemplo, 5 segundos).

??? tip "Pista para la solución"
    - Utiliza el temporizador de retardo a la conexión [`TON`](https://infosys.beckhoff.com/english.php?content=../content/1033/tcplclib_tc2_standard/74406539.html&id=){ target="_blank" } de la librería `Standard`.
    - Declara una instancia del temporizador de retardo a la conexión (`Temporizador: TON;`).
    - Utiliza literales de tiempo con la sintaxis de formato de tiempo estándar de IEC (ejemplo: `T#5s`).
    - Parametriza el funcionamiento utilizando una variable (`TiempoEncendido`) que permita controlar la temporización desde la visualización.

---

### 4. Lámpara Computada

**Descripción:**

- La lámpara se enciende tras un determinado número de pulsaciones (`i_Pulsador`).
- La lámpara se apaga tras accionar el pulsador de reinicio (`i_PulsadorReinicio`).

??? tip "Pista para la solución"
    - Utiliza el bloque de contador de cuenta regresiva [`CTD`](https://infosys.beckhoff.com/english.php?content=../content/1033/tcplclib_tc2_standard/74398987.html&id=){ target="_blank" } de la librería `Standard`.
    - Declara una instancia de contador decreciente (`Contador: CTD;`).
    - Parametriza el funcionamiento utilizando una variable (`ManiobrasTotales`) que controle el contador desde la visualización.

---

### 5. Lámpara Intermitente

**Descripción:**

- La lámpara parpadéa de forma continua.

??? tip "Pista para la solución"
    - Utiliza un temporizador de retardo a la conexión (`Temporizador: TON;`) para controlar el tiempo de conmutación.
    - Cuando finalice el temporizador invierte el estado de la lámpara (`o_Lampara := NOT o_Lampara;`).
    - Parametriza el funcionamiento utilizando una varible (`TiempoParpadeo`) que permita controlar el temporizador desde la visualización.

---
