# Descripción general - Ejemplos TC3

Descripción completa de los ejemplos y qué se va añadiendo en cada paso.

## DEMO
- Programa: `tc3_demo` [➡️](../contenidos/02_tc3_demo.md)
- **El «hola mundo» de la automatización industrial**
    - Presentación del IDE TcXaeShell
    - Introducción a Beckhoff/TwinCAT
    - Introducción a IEC 1131-3
    - TwinCAT 3 *workflow*

??? abstract "Arquitectura"
    - **Ninguna**. Toda la funcionalidad implementada en `MAIN`.
    - `MAIN`

??? info "Contenidos"
    - Utilización de un `PRG`
    - Declaración de variables numéricas (`UINT`)
    - Declaración de variables booleanas (`BOOL`) en el espacio de entradas/salida (`AT`)
    - Lenguaje `ST` (asignación)
    - **Visualización**
        - Botones, Rectángulos
        - Mostrar y modificar el valor de variables booleanas y numéricas
        - Propiedades
            - *Position*
            - *Colors*
            - *Texts*
            - *Texts properties*
            - *Text variables*
            - *Inputconfiguration* (*Tap*)
            - *Inputconfiguration* (*OnMouseClick > Execute ST-Code*)
                
## CARRO BÁSICO
- Programa: `tc3_carro_basico` [➡️](../contenidos/03_tc3_carro_basico_v2.md)
- **Mi primera máquina de estados** 
    - Introducción al GRAFCET
    - Introducción al `SFC`
    - Codificación de máquinas de estado en `SFC` y `ST`

??? abstract "Arquitectura"
    - **Monolítica estricta**
        - Toda la lógica de control en un único elemento (`FB_Carro`)
        - `SFC` únicamente con elementos propios (transiciones y acciones)
    - `MAIN -> Carro`

??? info "Contenidos"
    - Creación de un **FB**
        - Parámetros de entrada y salida (`VAR_INPUT`, `VAR_OUTPUT`)
        - Variables locales (`VAR`)
        - Valores iniciales (literales)
    - Tipos de datos: `TIME`
    - Uso de enumerados locales
    - Operadores relacionales (`=`, `<>`)
    - Operadores lógicos (`AND`, `OR`)
    - Uso de **FB** de la librería STANDARD (`R_TRIG`, `TON`)
    - Uso de **FB** de usuario (`FB_Blink`)
        - Intermitencia de elementos de señalización
    - Lenguaje `ST`: `CASE`, `IF`
    - Lenguaje `SFC`: 
        - elementos: etapas, etapa inicial, trasiciones, acciones (continua, principal, entrada, salida), transiciones dependientes del tiempo, divergencias (ramas), saltos
        - acciones continuas condicionadas
        - Variables implícitas de etapa (`.x`, `.t`)
        - Procesamiento de un `SFC`: bifurcaciones (prioridad implícita)
    - **Visualización**
        - Mostrar y modificar variables de tiempo
        - Propiedades
            - *Absolute movement*
            - *State variable* (*Invisible*)

??? success "Funcionalidades"
    - Secuencias lineales, cíclicas, alternativas, utilización de flancos, tiempo y computo de eventos
    - Gestión de una tarea
    - Señalización continua e intermitente

## CARRO EXTENDIDO MONOLÍTICO (Lite)
- Programa: `tc3_carro_extendido_monolitico_lite` [➡️](../contenidos/04_tc3_carro_extendido.md)
- **Primera automatización real** 

??? abstract "Arquitectura"
    - **Monolítica estricta**
        - Toda la lógica de control en un único elemento (`FB_Estacion`)
        - `SFC` únicamente con elementos propios (transiciones y acciones)
    - `MAIN -> Estacion`

??? info "Contenidos"
    - `VAR_CONSTANT`
    - `ARRAY` (longitud fija)
    - Variables implícitas: indicadores `SFC` (`SFCPause`, `SFCReset`)
    - Procesamiento de un `SFC`: «final scan»
    - Tipos de datos: `REAL`
    - Semántica reforzada, uso de variables de estado (`SistemaPreparado`,...)
    - `SFC`: nada nuevo
    - Visualización
        - Elementos: *Polygon*, *Image Pool*, *Image*

??? success "Funcionalidades"
    - Evaluación de las condiciones iniciales
    - Evaluación de la condición de marcha
    - Secuencia de restauración
    - Modo manual
    - Modo automático (ilimitado/por lotes)
    - Tratamiento «básico» de la falta de material
    - Procesamiento de señales analógicas
    - Modo ciclo a ciclo
    - Pausa
    - Reinicio

??? failure "Limitaciones"
    - Implementación de modo manual correcta pero inadecuada
    - Entrada no segura al modo manual
    - Pausa no segura (sin detención de los actuadores no-limitados)
    - Carece de parada a final de ciclo
    - Requiere de variables auxiliares que «ensucian» la declaración de variables de `FB_Estacion`

<!-- TODO: REVISAR ESTO

## CARRO MONOLÍTICO Basic
- Programa: `tc3_carro_monolitico_basic` [➡️](../contenidos/03_tc3_carro_mono_basic.md)
- **Primera automatización real mejorada**

??? abstract "Arquitectura"
    - Monolítica extendida
        - Toda la lógica de control en un único elemento (`FB_Estacion`)
        - `SFC` con métodos
    - Paralelismo
    - `MAIN -> Estacion`
    
??? info "Contenidos"
    - `STRUCT`: declaración, valores iniciales y asignación (`ST_SensorAnalogicoParams`)
    - `ARRAY` (longitud variable)
    - `METHOD` (`m_Proceso`): ejecución en *background*
        - Aligera la lógica de control de la secuencia pricipal
        - Favorece el uso de indicadores internos `SFC` (`SistemaEnReposo`, `FinCiclo`,...) que limpian, enriquecen y facilitan la comprensión
        - Incorpora la gestión de la parada a final de ciclo
        - Libera a la secuencia de control de la gestión de la señalización
        - Gestiona adecuadamente las acciones críticas en la pausa
        - Resuelve el uso inadecuado de `i_SelectorManual`
    - Uso extensivo de funciones de usuario (`F_Map`, `F_Normalize`, `F_Scale`, `F_ScaleAnalogInput`)
        - simplifica, favorece la reutilización y enriquece semánticamente la lógica
    - `SFC`
        - Secuencias paralelas (etapas de espera)
    
??? success "Funcionalidades"
    - Semántica reforzada con indicadores internos y funciones
    - Implementación adecuada del modo manual
    - Entrada segura en el modo manual
    - Pausa segura
    - Implementación de parada solicitada a final de ciclo
    - Funcionamiento paralel
    - Favorece de la reutilización

??? failure "Limitaciones"
    - No hace comparación de estructuras
    - No utiliza `ARRAY` de `STRUCT`

-->