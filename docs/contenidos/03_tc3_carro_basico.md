# 🛒 Carro Básico (TwinCAT 3)

<!-- 
!!! info "Info"
    Enlace al repositorio en Github [![Github Logo](../images/_resource/github_logo.svg){width=15px}](https://github.com/vetorres-uma/TC3_Carro_Basico)
-->

## 📝 Descripción Funcional

El **carro va y viene** es un móvil que se desplaza longitudinalmente entre los extremos izquierdo y derecho de un tramo de vía.

![Esquematico del Carro Básico](../images/03_tc3_carro_basico/Carro_Basico_Esquematico.png){width=300px}

### Elementos constituyentes

La **parte operativa** del carro básico está constituida por los siguiente dispositivos:

- Un **motor** con dos señales de mando (izquierda y derecha)
- Un par de **sensores finales de carrera** (izquierdo y derecho)

La **parte de relación** consiste en un panel de operador básico compuesto únicamente por:

- Un **pulsador de marcha**.
- Una **lámpara de marcha**.

### Descripción del proceso

El funcionamiento del carro básico es como sigue.

1. El carro se pone en marcha hacia la derecha cuando se acciona el pulsador de marcha. 
1. Cuando el carro alcanza el final de carrera derecha invierte el sentido de la marcha.
1. El carro se detiene al alcanzar, de nuevo,  el final de carrera izquierda (posición inicial).

- **Condición inicial**: carro detenido sobre el final de carrera izquierda.

### Modalidades

1. **Carro pulsado**. El carro inicia un viaje de ida y vuelta, únicamente, cuando estando en su posición inicial se acciona el pulsador de marcha.
1. **Carro temporizado**. El carro se detiene durante un determinado tiempo sobre el final de carrera derecha antes de iniciar el camino de regreso hacia su posición inicial.
1. **Carro limitado**. El carro realiza un determinado número de viajes de ida y vuelta (tarea) cada vez que, estando en su posición inicial, se acciona el pulsador de marcha.
1. **Carro señalizado**. La lámpara de marcha se enciende de forma permanente para indicar que el carro está en funcionamiento y parpadea para indicar que el carro está en reposo.

### Entradas y salidas

| Nombre | Tipo | Origen | Descripción |
| :--- | :--- | :--- | :--- |
| `PM` | `BOOL` | Input | Pulsador de Marcha |
| `FCI` | `BOOL` | Input | Final de Carrera Izquierda |
| `FCD` | `BOOL` | Input | Final de Carrera Derecha |
| `LM` | `BOOL` | Output | Lampara de Marcha |
| `MI` | `BOOL` | Output | Marcha Izquierda |
| `MD` | `BOOL` | Output | Marcha Derecha |

---

### Especificación funcional

Las siguientes especificaciones funcionales describen el comportamiento del carro (lógica de control) de una manera precisa utilizando los diagramas de relés y contactos y el lenguaje GRAFCET.

- [Diagrama de relés y contactos (PDF)](../../pdfs/Carro_Basico_DRC.pdf)
- [Diagrama grafcet (PDF)](../../pdfs/Carro_Basico_GRF.pdf)

---

### Implementación

Implementa el funcionamiento básico de este "famoso" problema de automatización del carro va y viene en sus diferentes modalidades (básico, pulsado, temporizado, limitado y **señalizado**). 

!!! warning "Importante"
    Puesto que el desarrollo es incremental, se incluye solo el código correspondiente al nivel superior, que incluye los anteriores.

Una de las característica más relevante de este proyecto didáctico es que se muestran diferentes formas de especificar e implementer un problema simple de automatización, empleando el lenguaje de especificación GRAFCET y usando diferentes lenguajes de programación de la norma IEC 61131-3 (`SFC` y `ST`).

- **GRF → [SFC / ST]**

---

## 💻 Requisitos del Sistema

### Software

- **IDE:** Microsoft Visual Studio / TwinCAT 3 XAE (Versión mínima recomendada: **3.1.4024.x**).
- **Lenguajes:** Texto Estructurado (ST) y Diagrama de Funciones Secuenciales (SFC).

---

## 🚀 Descarga

!!! info "Lenguaje"
    Se proporciona con implementaciones equivalentes en `ST` y en `SFC`.

**Para descargar, compilar y ejecutar este proyecto en el entorno de TwinCAT 3, seguir el siguiente procedimiento**.
<!-- 
**Para descargar, compilar y ejecutar este proyecto en el entorno de TwinCAT 3, seguir una de estas dos opciones:**

- Mediante el Campus Virtual
- Mediante GIT
-->

### Mediante el Campus Virtual

1. **Copiar** a tu equipo local el fichero 
    
    `CV → Automatización → ejemplos → 2_tc3_carro_basico → tc3_carro_basico.tnzip` 
    
    que hay en la carpeta del campus virtual.

2. **Seguir el procedimiento** descrito [aquí](../../contenidos/01_conceptos/#abrir-un-fichero-tnzip) para generar la **Solución** a partir del fichero.
<!-- 
### Mediante GIT

1. **Clonar el Repositorio:**

```bash
git clone https://github.com/vetorres-uma/TC3_Carro_Basico.git
```

2. **Abrir el Proyecto:** abra el archivo `.sln` (Solución) ubicado en la carpeta principal utilizando el entorno de ingeniería **TwinCAT XAE** (integrado en Visual Studio).
1. **Selección del Controlador:** seleccione el simulador (**UmRT_Default**) o controlador local (**Local**) o remoto (**Choose Runtime System...**).
1. **Activación de Configuración:** en el modo **Configuración**, active la configuración (**Activate Configuration**)) y reinicie TwinCAT en modo **Ejecución (Run Mode)**.
1. **Carga del Código:** en el entorno PLC, inicie la sesión y descargue el programa al PLC (**Login**).
1. **Poner el código en ejecución:** ejecute la lógica de control en el controlador (**Start**). Puede utilizar la visualización integrada en el proyecto PLC para facilitar la prueba.
-->
---

## 🔨 Explicación

!!! warning "Importante"
    El proyecto completo que se explica aquí se corresponde con la versión **señalizada** del carro va y viene.
    
    **Descarga el ejemplo para inspeccionar el código**.

**Para replicar la creación de la solución completa, seguir este procedimiento:**

!!! tip "Sugerencia"
    Pulsa en ➡️ para obtener más información sobre cómo realizar el paso especificado.

1. Crear una solución de TwinCAT3 con nombre `tc3_carro_basico` [➡️](../../contenidos/01_conceptos/#crear-proyecto-tc3)
2. Crear un proyecto PLC con nombre `carro_basico_PLC` [➡️](../../contenidos/01_conceptos/#crear-proyecto-plc)
3. **Escoger un lenguaje** para la implementación: `ST` o `SFC`. ==Aunque aquí expliquemos ambas versiones, en el curso habrá que replicar el correspondiente al lenguaje `SFC`==.
4. Crear un bloque funcional con ese lenguaje llamado `FB_Carro_basico_ST` o `FB_Carro_basico_SFC` [➡️](../../contenidos/01_conceptos/#crear-bloque-funcional)
5. Declarar las variables:
    
    ??? info "Comunes"
        - Control de maniobras: `ManiobrasSolicitadas` (total a realizar) y `ManiobrasPendientes` (contador).
        - Control de tiempo de espera: `TiempoEspera` (total a esperar) y `TiempoPendiente` (tiempo que queda).
        - Utilidades: `FlancoPulsadorMarcha (R_TRIG)` (detector de flanco de subida) y `BLK (F_Blink)` (señal booleana que conmuta de valor cada cierto tiempo).
        - Relativas al *hardware*: 
            - <span class="fondo-amarillo">**E**</span>: `i_FinalDerecha`, `i_FinalIzquierda`, `i_PulsadorMarcha` 
            - <span class="fondo-rojo">**S**</span>: `o_LamparaMarcha`, `o_MarchaDerecha`, `o_MarchaIzquierda`
    
    ??? info "Específicas para `ST`"
        - Control del estado: `Estado`: Variable de tipo `ENUM` que puede tomar los valores que identifican los estados posibles mostrados en el GRAFCET.
        - Temporizador: `TemporizadorEspera (TON)`

    ??? info "Específicas para `SFC`"
        - Ninguna. 
            - **No necesitamos una variable de estado**, porque viene implícito en el lenguaje. Además, TwinCAT 3 asocia una variable booleana a cada estado que indica si éste está activo: `[nombre_etapa].x` (ejemplo `S2.x`).
            - **Tampoco necesitamos el temporizador**, ya que TwinCAT 3 incorpora un temporizador asociado a cada etapa, al que se puede acceder mediante el código `[nombre_etapa].t` (ejemplo `S2.t`).
---

1. Escribir el código del **FB**:
    
    ??? info "`ST`"
        1. Se llama a los **FBs** de **utilidades**: `BLK`, `FlancoPulsadorMarcha` y `TemporizadorEspera`.
        2. Se implementa la **función de estado** usando esta estructura:
            ```pascal
            CASE Estado OF:
                <nombre_estado_1>:
                    IF <condicion_transicion> THEN
                        // accion a la salida
                        // cambio de estado
                    END_IF

                <nombre_estado_1>:
                    [...]
            END_CASE
            ```

            Ejemplo:
            ```pascal
            E_Reposo:
                IF i_FinalIzquierda AND FlancoPulsadorMarcha.Q THEN
                    IF ManiobrasPendientes = 0 THEN
                        ManiobrasPendientes := ManiobrasSolicitadas;
                    END_IF;
                    
                    Estado := E_MarchandoDerecha;
                END_IF;
            ```
            Nótese la relación entre los estados implementados y los presentes en el GRAFCET.
        
        3. Se implementa la **función de salida** que activa las salidas del sistema según el estado activo:
            ```pascal
            <salida> := <estado_correspondiente>
            ```
            
            Ejemplo:
            ```pascal
            o_LamparaMarcha := ((Estado = E_Reposo) AND BLK.Q) OR (Estado <> E_Reposo);
            ```

            Nótese aquí el uso de la salida de `BLK` para conseguir que `o_LamparaMarcha` alterne de valor en el estado de reposo (la lámpara parpadeará), y quede fija en cualquier otro estado.

    ??? info "`SFC`"
        4. La conversión de GRAFCET a lenguaje `SFC` es más directa que con `ST`, al ser un lenguaje gráfico que representa muy claramente la secuencia de estados por la que pasa el sistema.
            
            ![Código de carro básico SFC](../images/03_tc3_carro_basico/carro_basico_sfc.png){width=500px}
        
        5. El código incluye cinco tipos de acciones ([➡️](../../contenidos/01_conceptos/#asociar-acciones-a-etapas)):
              1. No memorizadas para activar salidas binarias (equivalencia directa con GRAFCET). **Ejemplo**: `o_MarchaDerecha`
              
              2. No memorizadas con llamada a acciones en `ST` (para acciones continuas condicionadas). **Ejemplo**: `a_LamparaMarcha`.
              3. Activas a la entrada (para acciones memorizadas a la entrada de la etapa). **Ejemplo**: `a_ManiobrasPendientes_calcular`.
              4. Activas a la salida (para acciones memorizadas a la salida de la etapa). **Ejemplo**: `a_ManiobrasPendientes_iniciar`.
              5. Acciones principales (para acciones continuas durante la activación de la etapa). **Ejemplo**: `a_FlancoMarcha`.
        6. Nótese el uso de la salida del **detector de flanco** en la primera transición. El código que llama al **FB** de `FlancoPulsadorMarcha` está incluido dentro de la acción principal del estado `S0`.
        7. Nótese el uso del **temporizador** implícito a la etapa `S2` (`S2.t`) para controlar la transición hacia la etapa `S3`.
        8. Nótese la **bifurcación** tras la etapa `S4` que dirige el flujo a `S0` o `S1` en función del valor de `ManiobrasPendientes`.
        9.  Nótese el uso de la **variable** `S0.x` en la acción `a_LamparaMarcha` para identificar si el estado `S0` está activo (`S0.x=TRUE`) o inactivo (`S0.x=FALSE`).
---

1. Diseñar la visualización añadiendo: [➡️](../../contenidos/01_conceptos/#crear-visualizacion)

    ![Imagen](../images/03_tc3_carro_basico/carro_basico_visu.png){width=400px}

    1. Rectángulos (*Rectangle*) para las etiquetas **Panel**, **Maniobras**, **Tiempos**, etc.
    2. Rectángulos (*Rectangle*) **no editables** para mostrar el valor de `ManiobrasPendientes` y `TiempoRestante`.

        ??? info "Parámetros"
            - Texts > Text = 
                - [%d] *Formato estilo printf que indica que se va a sustituir por un número entero*
                - [%t] *Formato estilo printf que indica que se va a sustituir por una variable tipo `TIME`* 
            - Text variables > Text variable = 
                - [`MAIN.Carro.ManiobrasPendientes`]
                - [`MAIN.Carro.TiempoRestante`]

    3. Rectángulos (*Rectangle*) **editables** para introducir el valor de `ManiobrasSolicitadas` y `TiempoEspera`.
        
        ??? info "Parámetros"
            - Añadir el siguiente a los correspondientes a los rectángulos **no editables**:
            - Inputconfiguration 
                - OnMouseClick > Configure > Write a Variable. 
                    - *Aceptar cuadro de diálogo por defecto. El valor introducido se escribirá en la variable especificada en Text Variable.*
        
     4. Rectángulos (*Rectangle*) para las variables booleanas correspondientes a la lámpara, pulsador, sensores final de carrera y activación de motores. **Tanto para mostrar su valor como para poder modificarlo.**

        ??? info "Parámetros"
            - Texts > Text = [**Pulsador**], [**Lampara**], , etc.
            - Color variables > Toggle color = [`MAIN.i_PulsadorMarcha`], [`MAIN.o_Lampara`], etc.
            - InputConfiguration
                - Toggle > Variable: [`MAIN.i_PulsadorMarcha`], [`MAIN.o_Lampara`], etc.
---

1. Declarar la variable `Carro` de tipo `FB_Carro_SFC` o `FB_Carro_ST` en el programa `MAIN`, según la versión a utilizar y llamar al código del **FB**.
    
    !!! info "Declaración"
        ```pascal
        PROGRAM MAIN
        VAR
            Carro: FB_Carro_SFC; // o Carro: FB_Carro_ST;
        END_VAR
        ```
    
    !!! info "Código"
        ```pascal
        Carro();
        ```

1.  Compilar y poner el programa en funcionamiento [➡️](../contenidos/01b_ejecucion.md).

---

## 🤝 Contribuciones

Este proyecto es utilizado con fines educativos. Las contribuciones, sugerencias o correcciones de errores son bienvenidas. Por favor, abra un *Issue* o envíe un *Pull Request* si desea contribuir.

---

## 🧑 Autor

- **Autor Principal:** Victor Torres ([@vetorres-uma](https://github.com/vetorres-uma>))
- **Revisor**: Francisco Ángel Moreno ([@famoreno](https://github.com/famoreno))

---

## ⚖️ Licencia

Este proyecto es de código abierto y está disponible bajo la **Licencia Pública General GNU (GPL)**.

- Consulte el archivo `LICENSE.md` para más detalles.