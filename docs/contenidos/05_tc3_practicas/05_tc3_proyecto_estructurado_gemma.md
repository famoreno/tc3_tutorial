# ⚙️ Proyecto Estructurado + GEMMA

!!! info "Nota"
    Esta práctica es **entregable**.

- Esta sección describe un enfoque modular para estructurar proyectos de automatización en TwinCAT 3 utilizando Lenguaje Estructurado (`ST`) y Diagrama de Flujo Secuencial (`SFC`), que sigue parcialmente la guía GEMMA (*Guide d'Etude des Modes de Marche et d'Arrêt*) para la gestión de los modos de funcionamiento y parada de la máquina.
- La guía **GEMMA** es una herramienta metodológica que permite analizar los modos de funcionamiento de un sistema de automatización.
- EL **GDMMA** (Gráfico Descriptivo de los Modos de Marcha y Parada) resulta de aplicar la guía GEMMA a un sistema concreto. El GDMMA resultante es una **máquina de estados** que describe el funcionamiento general de un sistema de automatización.
- Beneficios del uso de la guía GEMMA:
    - **Estandarización y Lenguaje Común**: La guía GEMMA proporciona un marco estandarizado y reconocido para los modos de marcha y paro. Esto significa que diferentes ingenieros, técnicos de mantenimiento y operadores pueden entender rápidamente el comportamiento de la máquina, incluso si no participaron en su diseño original.
    - **Claridad en Operación y Mantenimiento**: Define explícitamente estados como "Parada en estado inicial" (`A1`), "Producción normal" (`F1`), "Parada de emergencia" (`D1`), etc. Estos estados son intuitivos para los operadores y facilitan la capacitación. Para mantenimiento, saber que la máquina está en un modo específico (ej. "Verificación sin orden" - `F4`) ayuda a diagnosticar problemas.
    - **Integración de la Seguridad desde el Diseño:** Los modos de defecto (`D`) y parada (`A`) están intrínsecamente ligados a la seguridad. El modo `D1` (Emergencia) es un pilar. La guía fuerza a pensar en cómo la máquina debe comportarse en situaciones anómalas y cómo volver a un estado seguro (`A6` - Puesta en estado inicial).
    - **Gestión Completa del Ciclo de Vida de la Operación:** La guía GEMMA no solo define los estados de producción, sino también los de preparación (`F2`), finalización (`F3`), y los diferentes tipos de paradas (`A1`, `A2`, `A4`). Esto cubre todo el espectro de cómo una máquina opera, desde el arranque hasta la parada completa.
    - **Facilita el Diseño de la Interfaz Hombre-Máquina (HMI):** Los modos GEMMA pueden mapearse directamente a la HMI, proporcionando al operador una visión clara y coherente del estado de la máquina y de las acciones permitidas en cada modo.
    - **Mejora la Modularidad y Reutilización del Código:** Al definir claramente las responsabilidades de cada modo, se fomenta un diseño de *software* más modular. Las lógicas específicas de cada modo (ej. la secuencia de producción en `F1`, la secuencia de reinicio en `A6`) pueden encapsularse en bloques de función separados.
    - **Análisis y Especificación Funcional más Rigurosos:** El uso del diagrama GEMMA en la fase de diseño obliga a un análisis exhaustivo de todos los posibles modos de operación y las transiciones entre ellos. Esto ayuda a identificar omisiones o comportamientos no deseados antes de la implementación.

## Ejemplo de apoyo

Utilice el ejemplo del [**carro extendido estructurado + gemma**](../04_tc3_carro_extendido/04_tc3_carro_extendido_estructurado_gemma.md) como apoyo para entender la estructura del proyecto.

## Entregables

- GRAFCET del proyecto estructurado en formato PDF.
- Programa TC3 con la lógica de control del proyecto en formato `.tnzip`.

!!! warning "Normas de entrega"
    Siga las instrucciones en [este documento](../../pdfs/0e_proyecto_automatizacion.pdf){target="_blank"} referidas al nombre del entregable.

## Funcionalidades

!!! warning "Atención"
    📃 Versión descargable [aquí](../../pdfs/Checklist_Func_Estructurado_Gemma.pdf){target="_blank"}.

El proyecto desarrollado debe tener implementar las siguientes funcionalidades (en <font color="red">rojo</font>, funcionalidades nuevas respecto a la versión estructurada simple):

??? info "Requeridas"
    1. Evaluación de las condiciones iniciales.
    2. Evaluación de las condiciones de marcha.
    3. Secuencia automática de restauración de las condiciones iniciales.
    4. Secuencia de producción normal.
    5. Tratamiento mejorado de la falta de material (en dos etapas: **Silenciar** y **Continuar**).
    6. Visualización funcional <font color="red">con descripción de modo.</font>
    7. Modo manual correcto y adecuado (mandos directos) y automático.
    8. Modo de procesamiento por lotes (tarea).
    9. Modo ciclo a ciclo.
    10. Solicitud de parada a final de ciclo.
    11. Gestión de la tarea (maniobras solicitadas, pendientes y realizadas).
    12. Parametrización de todas las variables (tiempos y cantidades).
    13. Reinicio del estado <font color="red">mejorado</font> en las situaciones:
        1.  Botón en visualización.
        2.  <font color="red">Pulsación simultánea de pulsador de marcha y de parada durante un tiempo.</font>
        3.  <font color="red">Tras el desenclavamiento del pulsador de emergencia.</font>
    14. Pausa del estado.
    15. <font color="red">Uso de un método gestor de modos para el reinicio y la pausa.</font>
    16. <font color="red">Inicialización de `ManiobrasPendientes` al entrar en `F2`.</font>
    17. <font color="red">Uso del modo en los distintos métodos.</font>

??? info "Opcionales"
    1.  Normalización y escalado de las señales de entrada analógicas.
    2.  Secuencias paralelas.
    3.  Señalización mejorada:
        1.  Lámpara de alarma y lámpara de falta material intermitente en falta material.
        2.  Lámpara de parada intermitente para indicar parada pedida.
    4.  <font color="red">Temporizador para la desconexión automática por falta de actividad durante 5min.</font>

## Componentes

- `MAIN`: programa principal (`ST`)
    - `FB_Estacion`: contenedor principal (`ST`)
        - `FB_EstacionDirector`: gestor de los modos de funcionamiento (implementación del gráfico GDMMA) (`ST`).
        - `FB_EstacionCoordinador`: implementa el grafcet coordinador de tareas (`SFC`).
        - `FB_*`: implementa la lógica de control de la tarea; un bloque funcional por cada tarea (ej.: `FB_SituarPale`) (`SFC`).
- `VISU_Estacion`: interfaz gráfica

## Itinerario

!!! warning "Atención"
    Punto de partida: **proyecto de automatización estructurado simple**.

!!! warning "Atención"
    La lista es *clickable* pero **NO** guarda el estado; si actualizas o entras/sales de la página se perderán las marcas.

    📃 Versión descargable [aquí](../../pdfs/Checklist_Itinerario_Proyecto_Estructurado_Gemma.pdf){target="_blank"}.

- [ ] Crear un tipo `ENUM` para contener los modos de funcionamiento (`E_GEMMA`).
- [ ] Crear una lista de textos para contener las descripciones de los modos de funcionamiento (`TL_GEMMA`).
- [ ] Crear un director que implemente el gráfico **GDMMA** (`FB_EstacionDirector`).
- [ ] Incluir, inicialmente, únicamente los modos: **"Parada en el estado inicial"** y **"Producción normal"** (`A1`, `F1`).
- [ ] Incluir en la visualización la gestión de los modos de funcionamiento (etiqueta y descripción).
    - Utilizar textos dinámicos para la descripción.
- [ ] Integrar el director en `FB_Estacion`.
- [ ] Añadir, integrar y validar poco a poco nuevos modos (`FB_Estacion`, `FB_Director`, `VISU_Estacion`).
    - **"Verificación en desorden"** (modo manual) (`F4`).
    - **"Situando la PO en el estado inicial"** para recuperar las condiciones iniciales (`A6`).
        - Incluir la tarea `FB_EstacionRestaurar` que implemente la secuencia de restauración.
    - **"Parada de emergencia"** (`D1`).
    - **"Parada solicitada a final de ciclo"** (`A2`).
    - **"Secuencia de preparación"** (`F2`).
        - Incluir la tarea `FB_EstacionPreparar` que implemente la secuencia de preparación.
    - **"Secuencia de cierre"** (`F3`).
        - Incluir la tarea `FB_EstacionFinalizar` que implemente la secuencia de finalización.
