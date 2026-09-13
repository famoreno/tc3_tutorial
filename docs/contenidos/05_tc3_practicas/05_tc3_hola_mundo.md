# 👋 Práctica «Hola Mundo»

## Tarea
Replicar el ejemplo [**«Hola Mundo»**](../02_tc3_hola_mundo.md) para implementar nuestro primer programa de PLC con TwinCAT 3.

---

## Objetivos
- Familiarizarse con el entorno de desarrollo **TwinCAT XAE** de TwinCAT 3.
- Declarar variables de **memoria interna** (marcas).
- Declarar **variables localizadas** con **mapeo dinámico** de **entrada** y de **salida**.
- Implementar un fragmento de código sencillo en el lenguaje **Texto Estructurado (ST)** de la norma IEC 61131-3.
- Crear una **visualización** sencilla para mostrar y mofificar valores booleanos y numéricos.
- Construir un proyecto PLC.
- Vincular las instancias de las variables de entrada/salida a canales de entrada/salida.
- Desplegar (poner en marcha) un proyecto PLC.
- Validar un proyecto PLC.

---

## 🔨 Guía de implementación
A continuación se detallan los pasos necesarios para replicar completamente este proyecto.

!!! tip "Sugerencia"
    Pulsa en ➡️ para obtener más información sobre cómo realizar el paso especificado.

---

### Sobre el simulador (UmRT_Default)

1. Abrir la aplicación TwinCAT XAE Shell
1. Crear una solución de TwinCAT 3 con nombre `TC3_Hola_Mundo` [➡️](../../contenidos/01_conceptos/#crear-proyecto-tc3)
1. Ocultar las configuraciones innecesarias
1. Crear un proyecto PLC estándar con el nombre `Hola_Mundo_PLC` [➡️](../../contenidos/01_conceptos/#crear-proyecto-plc)

    !!! warning "Importante"
        **Nota didáctica:** Para facilitar la comprensión, en este primer ejemplo todo el código se implementa directamente dentro del programa principal (MAIN). Téngase en cuenta que esto se hace exclusivamente con fines pedagógicos. La buena práctica en programación industrial dicta que el MAIN debe actuar únicamente como punto de entrada y organizador, mientras que la lógica de control debe residir en otras unidades de organización del programa (POUs) —fundamentalmente Bloques de Función (FB)— que permiten modularizar, escalar y replicar fácilmente los comportamientos y funcionalidades del sistema.

1. Localizar en el panel de **explorador de la solución** el programa `MAIN` bajo la carpeta `POUs` e incluir la línea de comentario inicial.

    ```iecst
    // Hola Mundo de la Programación de PLC
    ```

1. Declarar la variable entera `ContadorCiclos` en la parte de declaración del programa `MAIN`. [➡️](../../contenidos/01_conceptos/#declaracion-de-variables)

    ```iecst
    PROGRAM MAIN
    VAR
        ContadorCiclos: UINT; // Variable numérica en el espacio de marcas
    END_VAR
    ```

1. Escribir el código correspondiente a la gestión del contador de ciclos en la parte de implemantación del programa `MAIN`.

    ```iecst
    ContadorCiclos := ContadorCiclos + 1;
    ```

1. Construir el proyecto (**Build**) para generar un achivo ejecutable.

    !!! warning "Importante"
        Asegurarse antes de continuar de que el resultado de la construcción del proyecto no arroja errores.

2. Artivar el simulador **UmRT_Default** para disponer de un `runtime` sobre el que ejecutar el código.
3. Seleccionar UmRT_Default como sistema destino (**Target System**).
4. Activar la licencia temporal del runtime del sistema destino si es necesario.
5. Reiniciar el sistema destino en **RUN Mode**.
6. Activar la configuración en el sistema destino.
7. Conectarse (**Login**) al sistema destino para enviar el proyecto al runtime e iniciar la monitorización (sesión de depuración en tiempo real) creando el puerto de comunicación 851 para el intercambio de información entre el entorno de programación y el runtime.
8. Poner el programa de PLC en ejecujción (**Run**) 
9. Observar cómo el valor de la variable `ContadorCiclos` se incrementa continuamente al ritmo de ejecución del ciclo básico del PLC (típicamente 10 ms). 
10. Modificar el valor del contador de ciclos  
11. Desconectarse del sistema destino (**logout**) para continuar con la edición del programa.
12. Crear un visualización para monitorizar y actulizar el contador de ciclos [➡️](../../contenidos/01_conceptos/#crear-visualizacion)

    ![Imagen](../images/02_tc3_demo/VISU_Demo.png){width=240px}

    1. Rectángulo (*Rectangle*) para la etiqueta **Contador**.
   
        ??? info "Parámetros"
            - Texts > Text = Contador

    2. Rectángulo (*Rectangle*) para el valor de `ContadorCiclos`.

        ??? info "Parámetros"
            - Color > Normal state > Frame color = [0, 0, 0]
            - Color > Normal state > Fill color = [192, 192, 192]
            - Texts > Text = [%d]
                - *Formato estilo printf que indica que se va a sustituir por un número entero.*
            - Text variables > Text variable = [`MAIN.ContadorCiclos`]

    3. Rectángulo (*Rectangle*) para el valor de `ContadorCiclos`

        ??? info "Parámetros"
            - Color > Normal state > Frame color = [0, 0, 0]
            - Color > Normal state > Fill color = [255, 255, 255]
            - Texts > Text = [%d]
                - *Formato estilo printf que indica que se va a sustituir por un número entero.*
            - Text variables > Text variable = [`MAIN.ContadorCiclos`]
            - Inputconfiguration > OnMouseClick

    4. Botón (*Button*) para reiniciar el contador

        ??? info "Parámetros"
            - Texts > Text = [**Reinicia**]
            - Inputconfiguration
                - OnMouseClick > Configure > Execute ST-Code = [`MAIN.ContadorCiclos := 0;`]

    !!! tip "Sugerencia"
        Los colores especificados para los elementos son simplemente un ejemplo, pueden ser escogidos libremente.

13. Volver a conectarse y comprobar que todos los elementos de la visualización funcionan correctamente.
14. Volver a desconectarse e incluir en la visualización los elementos correspondientes al pulsador y la lámapra.

    1.  Botón (*Button*) para el pulsador

        ??? info "Parámetros"
            - Texts > Text = [**Pulsador**]
            - Inputconfiguration
                - Tap > Variable = [`MAIN.i_Pulsador`]

    2.  Rectángulo (*Rectangle*) para la lámpara

        ??? info "Parámetros"
            - Colors > Normal state > Frame color = [0, 64, 0]
            - Colors > Normal state > Fill color = [0, 64, 0]
            - Colors > Alarm state > Frame color = [0, 128, 0]
            - Colors > Alarm state > Fill color = [0, 128, 0]
            - Texts > Text = [**Lámpara**]
            - Color variables > Toggle color = [`MAIN.o_Lampara`]

15. Conectarse nuevamente y comprobar que los nuevos elementos de la visualización funcionan correctamente

!!! success "¡Enhorabuena! 🎉"
    Has completado con éxito la primera parte de la práctica y has puesto en marcha tu primer proyecto completo de PLC en Texto Estructurado con TwinCAT 3 sobre el simulador UmRT_Default.

---

### Sobre un controlador

1. Estando desconectado, seleccionar como nuevo sistema destino un **controlador remoto** de Beckhoff presente en la actual red local.


2. **Buscar** el controlador en la red, **escanear** los módulos y **probar** dos terminales/canales, uno de entrada y otro de salida. [➡️](../../contenidos/01b_ejecucion/#busqueda-de-controladores-remotos)

    !!! tip "Sugerencia"
        Buscar la lista de entradas y salidas de la **descripción funcional** del sistema una señal de entrada (preferiblemente un **pulsador**) y otra de salida (preferiblemente una **lámpara**).

3. **Vincular** los canales correspondientes con las variables de E/S. [➡️](../../contenidos/01b_ejecucion/#vinculacion-de-variables-y-es)
    1.  Variable de entrada `i_Pulsador`
    2.  Variable de salida `i_Lampara`

4. **Activar la configuración** y reiniciar TwinCAT 3 en modo **Ejecución (Run Mode)** [➡️](../../contenidos/01b_ejecucion/#3-activar-configuracion)
5. **Transferir el programa** al controlador (**Login**) [➡️](../../contenidos/01b_ejecucion/#4-transferir-programa)
6. Poner el código en **ejecución** (**Start**) [➡️](../../contenidos/01b_ejecucion/#5-ejecutar-programa)
7. Comprobar que:
    1. El contador de ciclos sigue incrementándose de forma continua.
    2. Al accionar el pulsador físico se enciende la lámpara física.

8. **Utilizar la visualización** integrada en el proyecto PLC para facilitar la prueba:
    1. Comprobar en la visualización que, accionando el pulsador físico, cambia de estado la lámpara.
    1. Comprobar en la visualización que, accionando el botón de la visualización, **ni se enciende, ni cambia de estado la lámpara**.

        !!! warning "Importante"
            Esto se debe a que la ejecución del ciclo básico hace que el valor del pulsador **se actualice con el valor del pulsador físico** al inicio de cada ciclo, sobreescribiendo el valor que fija el botón de la visualización.

!!! success "¡Enhorabuena! 🎉"
    Has completado con éxito la segunda parte de la práctica y has puesto en marcha tu primer proyecto completo de PLC en Texto Estructurado con TwinCAT 3 sobre un controlador real.

---