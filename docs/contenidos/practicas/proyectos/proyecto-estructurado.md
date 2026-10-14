---
icon: fontawesome/solid/boxes-stacked
---

# :fontawesome-solid-boxes-stacked: Proyecto Estructurado

--8<-- "snippets/avisos.md:documento-en-construccion"
1. Crear un proyecto twinCAT nuevo (sobre la solución) 02_Estructurado
2. eliminar configuraciones
3. Crear un nuevo proyecto plc Estructurado_PLC
4. Crear dos carpetas (Estacion, Tareas)
5. Crear fb_Estacion ST en estacion
6. Copiar todas la variables del anterior
7. Colocar i_SelectorManual en su sitio
8. en main declarar y llamar a estacion
9. Copiar VISU
10. copy paste dispositivos
11. Deshabilitar monolitico
12. Definir las tareas-susbsecuencias-funcionalidades (verbos)
13. Añadir la pou de la primera taera en sfc
14. Añadir el interfaz de sincronización de la tarea ((Execute, Ack, Ready, Done))
15. Incluir los parametros correspondientes a los sensores y actuadores
16. Incluir el resto de parámetros necesarios con las adaptacions necesarias.
17. Crer la estructura vacía de la tarea Initial, End
18. Implementar el resto de la secuencia
19. Declarar una instancia de la tarea en Estación
20. Invocar la tarea con execute = Pulsador Marcha y entradas y salidas
21. escribir las lineas de las salidas
22. Verificar su buen funcionameinto.
23. Seleccionar sistemas destino
24. activar configuració
25. login
26. run
27. probar


**** copiar los dispositivos despues de compilar... para mantener los vinculos Copiar con los vínculos.
**** no entiendo porqué pero hay que volver a vincular las variables
**** Eliminar los parametros del sistemas de estación y dejarlos solo en las tareas?

Only unused, exclude disabled

1.  Implementar las tareas (funcionalidades)
            - Crea los bloques funcionales de cada tarea una por una
            - Dotar a cada bloque funcional de tarea de la estructura de rutina (Execute, Ack, Ready, Done)
            - Incluir en cada tarea un parámetro de entrada para cada sensor y un parámetro de salida para cada actuador que necesite para cumplir su función
            - Integrar cada tarea en la estación (declaración, invocación y parámetros de entrada y salida)
            - Validad cada tarea antes de iniciar la siguiente
            - El pulsador de marcha inicia la tarea seleccionada
        [ ] Crear un coordinador de tareas secuencial (FB_EstacionCoordinador)
            - Dotar al bloque funcional de coordinación de la estructura de rutina
            - Implementar únicamente la secuencia principal «directa»
            - El coordinador dispondrá de parámetros de entrada y salidas para comunicarse con cada tareas de forma que, al menos, tenga un parámetro de salida (imperativo) para dar la orden de ejecución de la funcionalidad y un parámetro de entrada (participio pasado) para recibir la respuesta de que la tarea se ha completado satisfactoriamente
            - Integrar el coordinador de tareas en la estación (declaración, invocación y parámetros de entrada y salida)
            - Integrar el coordinador con cada una de las tareas (parámetos de entrada/salida)
            - El pulsador de marcha inicia la ejecución del coordinador
        [ ] Incluir la gestión de las condiciones iniciales
        [ ] Incluir la gestión de la tarea           
        [ ] Incluir la gestión de la falta de material
        [ ] Incluir la gestión del tipo de pieza
        [ ] Incluir la gestión del panel de operador (señalización)