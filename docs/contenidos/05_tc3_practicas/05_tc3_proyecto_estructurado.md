# 🗂️ Proyecto Estructurado

!!! info "Nota"
    Esta práctica es **entregable**.

- Esta sección describe un enfoque **modular** para estructurar proyectos de automatización en TwinCAT 3, utilizando *Function Blocks* (**FBs**) basados en *Sequential Function Chart* (`SFC`).
- Beneficios del Enfoque Modular:
    - **Claridad:** Cada **FB** realiza una tarea específica (ej. Cargar Base, Prensar Rodamiento).
    - **Reutilización:** Los **FBs** de tareas pueden ser reutilizados en otras estaciones o proyectos con lógica similar.
    - **Mantenimiento:** Los cambios se localizan en **FBs** específicos, reduciendo el riesgo de efectos secundarios.
    - **Testabilidad:** Cada **FB** puede probarse individualmente (si se diseña adecuadamente).
    - **Colaboración:** Diferentes desarrolladores pueden trabajar en distintos **FBs** simultáneamente.

## Ejemplo de apoyo

Utilice el ejemplo del [**carro extendido estructurado**](../04_tc3_carro_extendido/04_tc3_carro_extendido_estructurado.md) como apoyo para entender la estructura del proyecto.

## Entregables

- GRAFCET del proyecto estructurado en formato PDF.
- Programa TC3 con la lógica de control del proyecto en formato `.tnzip`.

!!! warning "Normas de entrega"
    Siga las instrucciones en [este documento](../../pdfs/0e_proyecto_automatizacion.pdf){target="_blank"} referidas al nombre del entregable.

## Funcionalidades

!!! warning "Atención"
    📃 Versión descargable [aquí](../../pdfs/Checklist_Func_Estructurado.pdf){target="_blank"}.

El proyecto desarrollado debe tener implementar las siguientes funcionalidades (en <font color="red">rojo</font>, funcionalidades nuevas respecto a la versión monolítica):

??? info "Requeridas"
    1. Evaluación de las condiciones iniciales.
    2. Evaluación de las condiciones de marcha.
    3. Secuencia automática de restauración de las condiciones iniciales.
    4. Secuencia de producción normal.
    5. Tratamiento mejorado de la falta de material <font color="red">(en dos etapas: **Silenciar** y **Continuar**)</font>.
    6. Visualización funcional.
    7. Modo manual <font color="red">correcto y adecuado</font> (mandos directos) y automático.
    8. Modo de procesamiento por lotes (tarea).
    9. Modo ciclo a ciclo.
    10. <font color="red">Solicitud de parada a final de ciclo.</font>
    11. Gestión de la tarea (maniobras solicitadas, pendientes y realizadas).
    12. Parametrización de todas las variables (tiempos y cantidades).
    13. Reinicio y pausa del estado.

??? info "Opcionales"
    1.  Normalización y escalado de las señales de entrada analógicas.
    2.  Secuencias paralelas.
    3.  <font color="red">Señalización mejorada:</font>
        1.  <font color="red">Lámpara de alarma y lámpara de falta material intermitente en falta material.</font>
        2.  <font color="red">Lámpara de parada intermitente para indicar parada pedida.</font>

## Componentes

- `MAIN`: programa principal (`ST`)
    - `FB_Estacion`: contenedor principal (`ST`)
        - `FB_EstacionDirector`: implementa el gestor de modos del sistema (`SFC`).
        - `FB_EstacionCoordinador`: implementa el grafcet coordinador de tareas (`SFC`).
        - `FB_*`: implementa la lógica de control de la tarea; un bloque funcional por cada tarea (ej.: `FB_SituarPale`) (`SFC`).
- `VISU_Estacion`: interfaz gráfica

## Itinerario

!!! warning "Atención"
    Punto de partida: **proyecto de automatización monolítico**.

!!! warning "Atención"
    La lista es *clickable* pero **NO** guarda el estado; si actualizas o entras/sales de la página se perderán las marcas.

    📃 Versión descargable [aquí](../../pdfs/Checklist_Itinerario_Proyecto_Estructurado.pdf){target="_blank"}.

- [ ] Renombrar `FB_Estacion` por `_FB_Estacion_Monolitico`.
- [ ] Crear un nuevo `FB_Estacion` (`ST`).
- [ ] Trasladar toda la parte de declaración de `_FB_Estacion_Monolitico` a `FB_Estacion`.
- [ ] Eliminar la invocación al proceso (`MAIN`).
- [ ] Eliminar la gestión del modo manual (`MAIN`).
- [ ] Implementar las tareas (funcionalidades).
    - Crear los bloques funcionales de cada tarea una por una (`FB_*`).
    - Dotar a cada bloque funcional de tarea de la estructura de rutina (`Execute`, `Ack`, `Ready`, `Done`) (`FB_*`).
    - Incluir en cada tarea un parámetro de entrada para cada sensor y un parámetro de salida para cada actuador que necesite para cumplir su función (`FB_*`).
    - Integrar cada tarea en la estación (declaración, invocación y parámetros de entrada y salida) (`FB_Estacion`).
    - Validar cada tarea antes de iniciar la siguiente, usando el pulsador de marcha para iniciar la tarea seleccionada (`FB_Estacion`, `FB_*`).
- [ ] Crear un coordinador de tareas secuencial (`FB_EstacionCoordinador`).
    - Dotar al bloque funcional de coordinación de la estructura de rutina.
    - Implementar únicamente la secuencia principal «directa».
    - El coordinador dispondrá de parámetros de entrada y salidas para comunicarse con cada tarea de forma que, al menos, tenga un parámetro de salida (indicado en imperativo) para dar la orden de ejecución de la funcionalidad y un parámetro de entrada (indicado en participio pasado) para recibir la respuesta de que la tarea se ha completado satisfactoriamente.
    - Integrar el coordinador de tareas en la estación (declaración, invocación y parámetros de entrada y salida) (`FB_Estacion`).
    - Integrar el coordinador con cada una de las tareas (parámetros de entrada/salida) en el `FB_Estacion`.
    - El pulsador de marcha inicia la ejecución del coordinador (`FB_Estacion`, `FB_EstacionCoordinador`).
- [ ] Incluir la gestión de las condiciones iniciales (`FB_Estacion`).
- [ ] Incluir la gestión de la tarea (`FB_Estacion`, `FB_EstacionCoordinador`).
- [ ] Incluir la gestión de la falta de material (`FB_*`).
- [ ] Incluir la gestión del tipo de pieza, si procede (`VISU_Estacion`).
- [ ] Incluir la gestión del panel de operador (señalización) (`FB_Estacion`).
- [ ] Implementar la parada solicitada a final de ciclo (`FB_Director`).
- [ ] Implementar la parada inmediata (`SFCPause`) con detención de los actuadores (según convenga) (`FB_Estacion`).
- [ ] Incluir funcionalidades adicionales.
    - Funcionamiento ciclo-a-ciclo (`FB_Estacion`).
    - Reinicio (`SFCReset`).
    - Secuencia de restauración (`FB_Director`, `FB_*`).
    - Secuencias paralelas (opcional) (`FB_EstacionCoordinador`).
