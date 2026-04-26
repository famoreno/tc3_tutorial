# 🚟 Proyecto Monolítico
!!! info "Nota"
    Esta práctica es **entregable** y es el nivel **mínimo** a alcanzar.

- Esta sección describe un enfoque **monolítico** para estructurar proyectos de automatización en TwinCAT 3, en el cual toda la lógica de control se concentra en un único *Program Organization Unit* (POU), típicamente un solo *Function Block*.
- La implementación monolítica ofrece algunas ventajas iniciales:
    - **Simplicidad inicial:** El desarrollador no necesita diseñar una arquitectura modular ni pensar en interfaces entre bloques.
    - **Rapidez en proyectos pequeños:** Permite obtener resultados funcionales de forma rápida cuando el alcance del sistema es limitado.
    - **Menor sobrecarga conceptual:** Es más fácil de comprender para principiantes que están empezando en programación de PLCs.
- Sin embargo, también presenta inconvenientes importantes a medida que el sistema crece:
    - **Escalabilidad reducida:** El bloque de control se vuelve demasiado grande y difícil de mantener.
    - **Poco control de alto nivel**: Una implementación monolítica dificulta el control de alto nivel del sistema (gestión de problemas, paradas completas, etc.).
    - **Menor flexibilidad:** No es sencillo reutilizar partes de la lógica en otros proyectos.
    - **Dificultad en depuración y pruebas:** Los errores afectan a todo el sistema, y no pueden aislarse fácilmente.
    - **Riesgo de errores encadenados:** Un cambio en una sección del código puede impactar de forma inesperada en otras.

## Ejemplo de apoyo
Utilice el ejemplo del [**carro extendido monolítico**](../contenidos/04_tc3_carro_extendido/04_tc3_carro_extendido_mono.md) como apoyo para entender la estructura del proyecto.

## Entregables
- GRAFCET del proyecto monolítico en formato PDF.
- Programa TC3 con la lógica de control del proyecto en formato `.tnzip`.

!!! warning "Normas de entrega"
    Siga las instrucciones en [este documento](../../pdfs/0e_proyecto_automatizacion.pdf){target="_blank"} referidas al nombre del entregable.

## Funcionalidades
El proyecto desarrollado debe tener las siguientes funcionalidades:

??? info "Requeridas"
    1. Evaluación de las condiciones iniciales.
    2. Evaluación de las condiciones de marcha.
    3. Secuencia automática de restauración de las condiciones iniciales.
    4. Secuencia de producción normal.
    5. Tratamiento de la falta de material.
    6. Visualización funcional.
    7. Modo manual (mandos directos) y automático.
    8. Modo de procesamiento por lotes (tarea).
    9. Modo ciclo a ciclo.
    10. Gestión de la tarea (maniobras solicitadas, pendientes y realizadas).
    11. Parametrización de todas las variables (tiempos y cantidades).
    12. Reinicio y pausa del estado.

??? info "Opcionales"
    1.  Normalización y escalado de las señales de entrada analógicas.
    2.  Secuencias paralelas.

(Versión descargable [aquí](../../pdfs/Checklist_Func_Monolitico.pdf){target="_blank"}).

## Componentes
- `MAIN`: programa principal (`ST`)
    - `FB_Estacion`: lógica de control (`SFC`)
- `VISU_Estacion`: interfaz gráfica

## Itinerario
!!! warning "Atención"
    La siguiente lista es *clickable* pero **NO** guarda el estado. Si actualizas o entras/sales de la página se perderán las marcas. Puedes obtener una versión imprimible de esta lista [**aquí**](../../pdfs/Checklist_Ruta_Monolitico.pdf){target="_blank"}.

- [ ] Crear una solución con el nombre apropiado (`XXX_TC3_GYY`, `XXX` = iniciales de la asignatura, `YY` = número del grupo).
- [ ] Crear el proyecto PLC (`FMS_20X_PLC`).
- [ ] Crear el bloque funcional `FB_Estacion` (`SFC`).
- [ ] Declarar las variables pertinentes en el **FB** según la tabla de entrada y salida de la estación.
- [ ] Declarar e invocar la instancia `Estacion` de `FB_Estacion` en el programa `MAIN`.
- [ ] Compilar.
- [ ] Buscar el *runtime* remoto.
- [ ] Configurar entrada/salida (dispositivos y terminales).
- [ ] Vincular variables.
- [ ] Activar la configuración.
- [ ] Transferir el proyecto (`Login`) y ponerlo en funcionamiento (`Start`).
- [ ] Monitorizar una variable de entrada (pulsador de marcha).
- [ ] Forzar una variable de salida (lámpara de alarma).
- [ ] Crear una visualización (`VISU_Estacion`) que permita monitorizar todas las entradas y activar todas las salidas.
- [ ] Probar una a una todas las entradas y salidas desde la visualización.
- [ ] Utilizar la visualización para activar el *hardware* manualmente y así **determinar la secuencia** de producción normal de la estación.
- [ ] Incluir la gestión básica del modo manual en el `MAIN`.
- [ ] Añadir la secuencia principal «directa» en el `FB_Estacion`.
    - [ ] Poco a poco: subsecuencia a subsecuencia.
    - [ ] Realizar un ciclo por activación del pulsador de marcha.
    - [ ] Incluir temporizaciones cuando sea necesario.
    - [ ] Definir una etapa por cada situación.
    - [ ] Validar las subsecuencias conforme se incluyen.
- [ ] Incluir las condiciones iniciales en `FB_Estacion` y `VISU_Estacion`.
- [ ] Añadir la estructura para la gestión del procesamiento por lotes en `FB_Estacion` y `VISU_Estacion`.
    - [ ] Unidades pendientes y solicitadas.
- [ ] Incluir la gestión de los elementos de señalización (lámparas y avisador sonoro).
- [ ] Incluir las secuencias alternativas.
    - [ ] Gestión de la falta de material en `FB_Estacion`.
    - [ ] Gestión del tipo de pieza en `FB_Estacion` y `VISU_Estacion`, si procede.
    - [ ] Secuencia de restauración de las condiciones iniciales en `FB_Estacion`.
- [ ] Incluir funcionalidades adicionales.
    - [ ] Funcionamiento ciclo-a-ciclo.
    - [ ] Reinicio (`SFCReset`).
    - [ ] Implementar la parada inmediata (`SFCPause`).
    - [ ] Secuencias paralelas (opcional).
    - [ ] Normalización y escalado de las señales analógicas, si procede (opcional).

<!-- 
1. Crear una solución con el nombre apropiado (`XXX_TC3_GYY`, `XXX` = iniciales de la asignatura, `YY` = número del grupo).
1. Crear el proyecto PLC (`FMS_20X_PLC`).
1. Crear el bloque funcional `FB_Estacion` (`SFC`)
1. Declarar las variables pertinentes en el **FB** según la tabla de entrada y salida de la estación.
1. Declarar e invocar la instancia `Estacion` de `FB_Estacion` en el programa `MAIN`.
1. Compilar.
1. Buscar el *runtime* remoto.
1. Configurar entrada/salida (dispositivos y terminales).
1. Vincular variables.
1. Activar la configuración.
1. Transferir el proyecto (`Login`) y ponerlo en funcionamiento (`Start`).
1. Monitorizar una variable de entrada (pulsador de marcha).
1. Forzar una variable de salida (lámpara de alarma).
1. Crear una visualización (`VISU_Estacion`) que permita monitorizar todas las entradas y activar todas las salidas.
1. Probar una a una todas las entradas y salidas desde la visualización.
1. Utilizar la visualización para activar el *hardware* manualmente y así **determinar la secuencia** de producción normal de la estación.
1. Incluir la gestión básica del modo manual en el `MAIN`.
1. Añadir la secuencia principal «directa» en el `FB_Estacion`
    - Poco a poco: subsecuencia a subsecuencia.
    - Realizar un ciclo por activación del pulsador de marcha.
    - Incluir temporizaciones cuando sea necesario.
    - Definir una etapa por cada situación.
    - Validar las subsecuencias conforme se incluyen.
1. Incluir las condiciones iniciales en `FB_Estacion` y `VISU_Estacion`.
1. Añadir la estructura para la gestión del procesamiento por lotes en `FB_Estacion` y `VISU_Estacion`.
    - Unidades pendientes y solicitadas
1. Incluir la gestión de los elementos de señalización (lámparas y avisador sonoro).
1. Incluir las secuencias alternativas
    - Gestión de la falta de material en `FB_Estacion`.
    - Gestión del tipo de pieza en `FB_Estacion` y `VISU_Estacion`, si procede.
    - Secuencia de restauración de las condiciones iniciales en `FB_Estacion`.
1. Incluir funcionalidades adicionales.
    - Funcionamiento ciclo-a-ciclo.
    - Reinicio (`SFCReset`).
    - Implementar la parada inmediata (`SFCPause`).
    - Secuencias paralelas (opcional).
    - Normalización y escalado de las señales analógicas, si procede (opcional).

<!-- 
1. Añadir las variables que sean necesarias para la definición de la tarea (ej: `ManiobrasSolicitadas`, `RodamientoAlto`), la temporización (ej: `TiempoEspera`), etc.
2. Declarar e invocar la instancia `Estacion` de `FB_Estacion` en el programa `MAIN`.
3. Asociar las variables declaradas al *hardware* de la estación.
4. Diseñar una **visualización funcional completa** para la estación (inspirarse en la del ejemplo proporcionado del carro extendido).
5. Utilizar la visualización para activar el *hardware* manualmente y así **determinar la secuencia** de producción normal de la estación.
6. Definir el GRAFCET correspondiente a dicha secuencia.
7.  Implementar en `SFC` la funcionalidad especificada en el GRAFCET.
8.  Añadir las funcionalidades adicionales a las de producción normal:
    1.  Comprobación de las condiciones iniciales y órdenes de marcha.
    2.  Secuencia de restauración.
    3.  Gestión de falta material.
    4.  Gestión de la tarea (modos continuo, por lotes y ciclo a ciclo).
    5.  Pausa y Reset.
9.  Añadir las funcionalidades extra:
    1.  Normalización y escalado de las señales analógicas.
    
## Itinerario
Nivel 1: Monolítico (obligatorio)
    - Objetivo
        - Automatización de la estación FMS-20X (producción normal)
        - Aquitectura monolítica
            - Toda la funcionalidad en un único elemnto (FB_Estacion)
    - Componentes
        [ ] MAIN: programa principal (ST)
            [ ] FB_Estacion: lógica de control (SFC)
        [ ] Visu_Estacion: interfaz gráfica
    - Procedimiento
        [ ] Incluir la gestión básica del modo manual (MAIN)
        [ ] Añadir la secuencia principal «directa» (FB_Estacion)
            - Poco a poco: subsecuencia a subsecuencia
            - Un ciclo por activación del pulsador de marcha 
            - Incluir temporizaciones cuando sea necesario
            - Una etapa por cada situación
            - Validar las subsecuencias conforme se incluyen 
        [ ] Incluir las condiciones iniciales (FB_Estación y Visu_Estacion)
        [ ] Añadir la estructura para la gestión del procesamiento por lotes (FB_Estación y Visu_Estacion)
            - Unidades pendientes y solicitadas
        [ ] Incluir la gestión de los elementos de señalización
		[ ] Incluir las secuencias alternativas
			[ ] Gestión de la falta de material (FB_Estación y Visu_Estacion)
			[ ] Gestión del tipo de pieza (FB_Estación y Visu_Estacion)
			[ ] Secuencia de restauración de las condiciones iniciales
        [ ] Incluir funcionalidades adicionales
            - Funcionamiento ciclo-a-ciclo
            - Reinicio (SFCReset)
            - Secuencias paralelas (opcional)
        [ ] Añadir método proceso (m_Proceso) a FB_Estación
            - Invocar al método para que se ejecute en «background» (MAIN)
            - Implementar la parada solicitada a final de ciclo
            - Implementer el funcionamiento continuo
            - Trasladar la gestión de la señalización a proceso
            - Implementar la parada inmediata (SFCPause) con detención de los actuadores (según convenga)
-->
