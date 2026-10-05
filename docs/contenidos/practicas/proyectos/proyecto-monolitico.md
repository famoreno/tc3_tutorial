# 🔲 Proyecto Monolítico

## 📋 Tarea

Implementar la lógica de control de un automatismo industrial utilizando la [**Arquitectura Monolítica**](../../fundamentos/arquitecturas/index.md#arquitectura-monolitica).

---

## 🎯 Objetivos

- Programar la lógica de control de un automatismo industrial en el lenguaje {{SFC}} utilizando la **arquitectura monolítica**.
- Implementar un **modo manual** básico.
- Garantizar inicios de producción seguros (**condición inicial** y **marcha autorizada**).
- Implementar un el modo de **funcionamiento por lotes**.
- Gestionar las **incidencias de material**.
- Implementar una **señalización básica** (alarma, marcha y material).
- Implementar **Interfaces Hombre-Máquina** básicos utilizando visualizaciones.
- Realizar la **puesta en marcha** de un automatismo industrial.

---

## 📝 Descripción funcional

Para el desarrollo de este proyecto se utilizará como caso de estudio el **Sistema Didáctico Modular de Ensamblaje Flexible (FMS-200)** de **SMC International Training**. Sin embargo, el procedimiento que se describe a continuación no depende de ningún equipo en concreto: los pasos, la metodología y los conceptos de programación en TwinCAT 3 son aplicables a cualquier otro sistema automatizado, maqueta, célula de fabricación o simulador equivalente.

Si no dispones del sistema FMS-200, puedes seguir igualmente la práctica sin disponer de ningún sistema concreto o adaptando las entradas/salidas y la configuración de hardware a tu propio sistema. El objetivo no es aprender a programar el sistema FMS-200, sino aprender a programar PLC con TwinCAT 3.

La descripción funcional del **Sistema Didáctico Modular de Ensamblaje Flexible (FMS-200)** de **SMC International Training**, que incluye las tablas de entradas/salidas, está disponible en el siguiente archivo.

- [FMS-200 Descripción Funcional (PDF).](./pdf/fms_200_descripcion_funcional.pdf){target="_blank"}

---

## 📂 Estructura simplificada del proyecto

```text
XXX_TC3_GYY/
├── XXX_TC3_GYY.sln                    <-- Solución de Visual Studio (TwinCAT XAE)
└── 01_FMS_20X_Monolitico/             <-- Proyecto TwinCAT
    └── Monolitico_PLC/                <-- Proyecto PLC
        ├── POUs/
        |   ├── FB_Estacion_SFC.TcPOU  <-- Lógica de control monolítica en SFC
        |   └── MAIN.TcPOU             <-- Programa principal
        └── VISUs
            └── V_Estacion.TcVIS       <-- Visualización
```

---

## 📋 Guía de implementación

!!! Info
    Para el desarrollo de esta práctica puede tomarse como referencia la versión **monolítica** del proyecto [«Carro Extendido»](../../ejemplos/carro_extendido/index.md).

#### Solución

- [ ] Abrir la aplicación **TwinCAT XAE**. [➡️](../../procedimientos/workflow/index.md#abrir-twincat-xae)
- [ ] Crear un **proyecto (solución) TwinCAT 3**. [➡️](../../procedimientos/workflow/index.md#crear-un-proyecto-twincat-3)
  
    !!! info "Parámetros"
        - Nombre de la solución ➔ `**XXX_TC3_GYY**` (`XXX` = asignatura, `YY` = grupo).
        - Nombre del proyecto ➔ `01_FMS_20X_Monolitico` (`X` = número de la estación del sistema FMS-200).

- [ ] Ocultar las **configuraciones** innecesarias para dejar el Explorador de la Solución lo más despejada posible. [➡️](../../procedimientos/workflow/index.md#ocultar-configuraciones)

#### Proyecto PLC

- [ ] Crear un **proyecto PLC estándar** con el nombre `Monolitico_PLC`. [➡️](../../procedimientos/workflow/index.md#crear-un-proyecto-plc)
- [ ] Crear una nueva **Unidad de Organización de Programa (POU)** de tipo **Bloque Funcional**. [➡️](../../procedimientos/workflow/index.md#crear-un-pou)

    !!! warning "Parámetros POU"
        - Nombre ➔ `FB_Estacion_SFC`
        - Type ➔ `Function Block`
        - Implementation Language ➔ `Sequential Function Chart (SFC)`

- [ ] Declarar las **variables de entrada/salida** necesarias en `FB_Estacion_SFC` como variables locales (`VAR_LOCAL`). [➡️](../../procedimientos/workflow/index.md#declarar-una-variable)

    !!! Info "Entradas/Salidas"
        - Consultar la tabla de entrada/salida de cada estación en la [descripción funcional.](./pdf/fms_200_descripcion_funcional.pdf){target="_blank"}
        - Utilizar el prefijo `i` para las variables de entrada (i_PulsadorMarcha).
        - Utilizar el prefijo `o` para las variables de salida (o_LamparaMarcha).

- [ ] Declarar una **instancia** `Estacion` del tipo `FB_Estacion_SFC` en la parte de implementación del programa `MAIN`.

    ```iecst
    PROGRAM MAIN
    VAR
        Estacion: FB_Estacion_SFC;
    END_VAR
    ```

- [ ] Invocar la ejecución de la **instancia** `Estacion` en la parte de implementación de `MAIN`.

    ```iecst
    Estacion();
    ```

- [ ] Construir el proyecto (**Build**) para generar un archivo ejecutable. [➡️](../../procedimientos/workflow/index.md#construir-el-proyecto)

    !!! Info "Construcción"
        - Verificar la ausencia de errores en el panel ***Error List***.
        - Verificar la correcta creación de la instancias de las variables de entrada/salidas bajo el apartado `Monolitico_PLC Instance` del proyecto `Monolitico_PLC`.

#### Entrada/Salida

- [ ] Buscar y seleccionar un controlador remoto (crear una ruta). [➡️](../../procedimientos/workflow/index.md#crear-una-ruta)
- [ ] Buscar dispositivos y terminales de entrada/salida. [➡️](../../procedimientos/workflow/index.md#buscar-dispositivos)
- [ ] Identificar, verificar y nominar las señales de entrada (ver tablas de entrada/salida en la [descripción funcional](./pdf/fms_200_descripcion_funcional.pdf){target="_blank"}). [➡️](../../procedimientos/workflow/index.md#identificar-entradas)
- [ ] Identificar, verificar y nominar las señales de salida (ver tablas de entrada/salida en la [descripción funcional](./pdf/fms_200_descripcion_funcional.pdf){target="_blank"}). [➡️](../../procedimientos/workflow/index.md#identificar-salidas)
- [ ] Vincular las señales con las instancias de las variables de entrada/salida. [➡️](../../procedimientos/workflow/index.md#vincular-variables)
- [ ] Desplegar el proyecto
    - [ ] Activar la configuración [➡️](../../procedimientos/workflow/index.md#activar-la-configuracion)
    - [ ] Transferir el proyecto. [➡️](../../procedimientos/workflow/index.md#transferir-el-proyecto)
    - [ ] Ponerlo en funcionamiento. [➡️](../../procedimientos/workflow/index.md#arrancar-el-proyecto)
- [ ] Monitorizar una variable de entrada. [➡️](../../procedimientos/workflow/index.md#monitorizar-variables)
- [ ] Forzar una variable de salida. [➡️](../../procedimientos/workflow/index.md#forzar-variables)

#### Visualización

- [ ] Crear la visualización básica (V_Estacion)
- [ ] Añadir un rectángulo para monitorizar y modificar el valor de cada una de las variables de e/s.

    !!! info "Parámetros"
        - Ajustar según corresponda los parámetros: *Position (Width, Height), Colors, Texts, Text properties, inputconfiguration (Toggle/Tap)*.

- [ ] Monitorizar el valor de una variable de entrada (pulsador de marcha) desde V_Estacion.
- [ ] Forzar el valor una variable de salida (lámpara de marcha) desde V_Estacion.

#### Modo Manual

- [ ] Mover la variable i_SelectorManual del bloque de declaración VAR al bloque de declaración VAR_OUTPUT

    ```iecst
    FUNCTION_BLOCK FB_Estacion_SFC
    VAR_OUTPUT
        i_SelectorManual AT %I*: BOOL;
    END_VAR
    ```

- [ ] Condicionar la ejecución de Estacion en MAIN al selector de modo.
  
    ```iecst
    IF NOT i_SelectorManual THEN
        Estacion();
    END_IF;
    ```

- [ ] Verificar la correcta monitorización y modificación de las señales de entrada y salida desde la visualización.

    ??? Info
        - Verificar que desde la visualización el estado de las variables de entrada cambian conforme lo hacen las señales correspondintes. Si se acciona el «pulsador de marcha», el rectángulo que informa del estado de la variable de entrada «pulsador de marcha» cambia de color.
        - Verificar que desde la visualización el estado de las señales de salidas cambian conforme lo hacen las variables correspondientes. Si se acciona el rectángulo que gobierna el estado de la variable «lampara de marcha» en la visualización, cambia el estado de la señal de la lámpara de marcha.

- [ ] Realizar un ciclo completo manualmente desde la visualización.

    ??? Info
        Utilizando los elementos de la visualización, realizar un ciclo completo de funcionamiento del sistema para comprobar que:

        - Todas las señales involucradas en el el proceso funcionan correctamente tanto en le *software* como en el *hardware*.
        - Se conoce perfectamente todos los pasos del proceso de producción.

#### «Camino Feliz»

- [ ] Implementar únicamente la secuencia principal directa.

    !!! Info  
        - No considerar ninguna otra condición de la secuencia que no sea lo que el sistema hace «normalmente».
        - No considerar los elementos de señalización.

- [ ] Considerar como condición para iniciar la secuencia la activación del pulsador de marcha.
- [ ] Implementar la secuencia «poco a poco», subsecuencia a subsecuencia, apenas unas etapas cada vez.

    !!! Info
        - Una subsecuencia es un conjunto de etapas que realizan una función «básica» con sentido.
        - Utilizar los finales de carrera, cuando estén presentes, como condición de movimiento finalizado.
        - Incluir temporizaciones parametrizadas cuando sea necesario (ausencia de sensores).
        - Mantener el «sentido físico», una etapa por cada situación que ocurra en la realidad.
        - Una etapa para hacer un movimiento, una etapa para deshacerlo.
        - Validar las subsecuencias conforme se incluyen.

- [ ] Añadir los parámetros del sistema (principalmente tiempos) a la visualización.

#### Condición Inicial

!!! Info "Condición Inicial"
    - La condición inicial, es la condición material de los sensores, que indica que el inicio de la producción es seguro.
    - La condición inicial incluye la posición de «reposo» conocida de cada actuador.
  
- [ ] Calcular la condición inicial en FB_Estación en una acción principal (a_CondicionInicial) asociada a la etapa inicial.
- [ ] Ampliar la condición de inicio de secuencia para evitar el inicio del ciclo no-seguro (si no se cumplen las condiciones iniciales).
- [ ] Mostrar el estado de la condición inicial en la visualización.

#### Falta/Exceso Material

- [ ] Añadir una condición de falta/exceso de material.

    !!! Info
        - Condición de falta material.
            - FMS-201: No hay base en el alojamiento del cargador.
            - FMS-202: No se detecta un rodamiento al intentar sacarlo de su alojamiento (i_PresenciaRodamiento).
            - FMS-205: No se detecta una tapa al intentar sacarla de su alojamiento (i_AlimentadorDelante).
            - FMS-206: No se detecta tornillo en el desplazador (i_PresenciaTornillo) tras intentar dispensarlo.
        - Condición de exceso de material.
            - FMS-208: La zona de almacenamiento está llena.

- [ ] Abandonar la secuencia normal ante la falta/exceso de material.
- [ ] Incluir una secuencia alternativa para atender la falta/execeso de material.
    - Indicar la situación activando la lámpara de material.
    - Esperar la acción correspondiente (reposición/desalojo) por parte del operario.
    - Esperar la autorización del operario para continuar (i_PulsadorMarcha).
- [ ] Tras la reanudación volver a verificar, en su caso, la presencia del material.

#### Pieza Correcta

- [ ] Crear la estrucuta de datos necesaria para determinar el tipo de pieza solicitada.
- [ ] Incluir en la visualización los elementos necesarios para establecer en la tarea el tipo de pieza solicitada.
- [ ] Determinar la corrección de la pieza actual utilizando una acción a la entrada (a_PiezaCorrecta) en la etapa que corresponda.

    !!! Info "Pieza Correcta"
        La pieza actual es correcta si cumple las condición para ser descargada.

        - FMS-201 ➔ está bien posicionada.
        - FMS-202 ➔ la pieza actual se corresponde con la pieza solicitada (tipo rodamiento).
        - FMS-205 ➔ la pieza actual se corresponde con la pieza solicitada (tipo tapa).
        - FMS-206 ➔ no ha lugar
        - FMS-208 ➔ no ha lugar

- [ ] Incluir una secuencia alternativa para atender la situación rechazando la pieza actual.
- [ ] Tras la acción correctora volver a la secuencia principal e intentarlo con la siguiente pieza.
- [ ] Incluir en la visualización un indicador de pieza correcta.

!!! Warning "FMS-205"
    La complejidad para determinar la corrección de la «pieza actual» en la estación de Inserción de la Tapa (FMS-205), aconseja que esta funcionalidad se introduzca en varias fases.

    - **Fase 1**
        - [ ] Crear las variables de intención (CargaTapa, VolteaTapa, RechazaTapa, DescargaTapa).
        - [ ] Incluir en la visualización los elementos gráficos necesarios para cambiar y mostrar el estado de estas variables.
        - [ ] Utilizar estas variables para establecer saltos hacia delante en la secuencia principal para eludir la ejecución de las subsecuencias correspondites.
        - [ ] Comprobar que la estación opera adecuadamente en función del valor de estas variables.

    - **Fase 2**
        - [ ] Crear la estrucura de datos necesaria para contener y mantener la información de las piezas contenidas en el plato divisor.
        - [ ] Incluir el código necesario para mentener esta información actualizada según la posición que las piezas ocupen en el plato divisor.
        - [ ] Comprobar que estos datos se corresponden, en funcionamiento, con el tipo de pieza situada en cada posición del plato.
    
    - **Fase 3**
        - [ ] Incluir en la visualización los elementos necesarios para establecer en la tarea el tipo de pieza solicitada.
        - [ ] Calcular el valor de las variables de intención en función del tipo de la pieza actual situda en cada posición del plato y el tipo de pieza solicitado.

    !!! Tip
        Se recomiendo posponer la segunda y tercera fase de implementación de esta funcionalidad hasta la finalización completa de la implantación del resto de funcionalidades básicas.

#### Tarea

- [ ] Incluir las variables UnidadesPendientes y UnidadesSolicitadas necesarias para gestionar la tarea.

    !!! info "Procesamiento por Lotes"
        - En el modo de procesameiento por lotes se denomina tarea (cantidad y tipo) al número de piezas/unidades de un determinado tipo que se desea producir.
        - En automatización es costumbre contabilizar las unidades pendientes mediante una cuenta regresiva.
        - La tarea se finaliza cuando no quedan unidades pendientes que procesar.

- [ ] Utilizar una acción a la salida (a_PiezasPendientes_Calcular) para actualizar la cantidad de unidades pendientes cada vez que finaliza el ciclo con éxito.
- [ ] Utilizar acción a la entrada (a_PiezasPendientes_Iniciar) para iniciar la cuenta de unidades pendientes al empezar la tarea.
- [ ] Iniciar la tarea únicamente si se cumplen las condiciones iniciales y, ademas, se ha establecido una tarea válida (MarchaAutorizada).

    !!! Info "Tarea Válida"
        Se considera una tarea válida si:

        - Hay demanda de producción ➔ el número de piezas solicitadas en mayor que 0.
        - El tipo de la pieza solicitado es válido ➔ el tipo de pieza solicitada se corresponde con algún tipo de pieza que la estación puede producir (cuando corresponda).

- [ ] Utilizar una acción principal a_MarchaAutorizada en la etapa inicial que incluya a_CondidionInicial y la condición de tarea válida.

#### Señalización Básica

- [ ] La lámpara de alarma se activa para avisar al operario de una anomalía.
    - El inicio de la producción no es seguro.
- [ ] La lámpara de marcha se activa para indicar al operarios que el sistema está en producción.

---

<!---
## Funcionalidades Adicionales

1.  Secuencia automática de restauración.
2.  Secuencia automática de preparación de la producción.
3.  Modo ciclo-a-ciclo
4.  Reinicio y pausa del sistemas.
5.  Normalización y escalado de señales de entrada analógicas.
6.  Secuencias paralelas.
--->