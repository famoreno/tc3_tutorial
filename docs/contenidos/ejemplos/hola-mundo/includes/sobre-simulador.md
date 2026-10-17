### Sobre el Simulador

Empecemos por <span class="objetivo-hito">utilizar el entorno de ingeniería TwinCAT XAE de TwinCAT 3</span> para crear nuestro primer proyecto con el entorno de ingeniería TwinCAT XAE.
<!--- todo: explicación, qué es TwinCAT XAE --->

Si tiene instalado TwinCAT 3 en su ordenador puede implementar el proyecto completo (código y visualización) y ejecutarlo en el simulador `UmRT_Default`.
<!--- todo: guía instalación TC3 --->
<!--- todo: explicación, qué es UmRT_Default --->

1. Abrir la aplicación **TwinCAT XAE**. [➡️](../../procedimientos/workflow/index.md#abrir-twincat-xae)
2. Crear una solución de TwinCAT 3 con nombre `TC3_Hola_Mundo`. [➡️](../../procedimientos/workflow/index.md#crear-un-proyecto-twincat-3)
3. Ocultar las configuraciones innecesarias para dejar el explorador de la solución lo más despejado posible. [➡️](../../procedimientos/workflow/index.md#ocultar-configuraciones)
4. Crear un proyecto PLC estándar con el nombre `Hola_Mundo_PLC`. [➡️](../../procedimientos/workflow/index.md#crear-un-proyecto-plc)

    ??? warning "Aviso"
        **Nota didáctica:** para facilitar la comprensión, en este primer ejemplo todo el código se implementa directamente dentro del **programa** principal (`MAIN`). Téngase en cuenta que esto se hace exclusivamente con fines pedagógicos. La buena práctica en programación industrial dicta que el `MAIN` debe actuar únicamente como punto de entrada y organizador del proyecto, mientras que la lógica de control debe residir en otras **Unidades de Organización del Programa** (`POUs`) —fundamentalmente **Bloques de Función** (`FB`)— que permiten modularizar, escalar y replicar fácilmente los comportamientos y las funcionalidades del sistema.

5. Localizar en el panel de **Explorador de la Solución** el programa `MAIN` bajo la carpeta `POUs` e incluir la línea de comentario inicial sobre el **encabezado del POU**.

    ```iecst
    // Hola Mundo de la Programación de PLC
    ```

6. <span class="objetivo-hito">Declarar la variable de memoria interna</span> `ContadorCiclos` como un entero sin signo `UINT` en el bloque `VAR` de la parte de declaración del programa `MAIN`. [➡️](../../procedimientos/workflow/index.md#declarar-una-variable)

    ```iecst
    PROGRAM MAIN
    VAR
        ContadorCiclos: UINT;
    END_VAR
    ```

    ??? info
        Según el estándar `IEC 61131-3` tipo de dato `UINT` representa un entero sin signo de 16 bits (0 a 65535).

7. <span class="objetivo-hito">Implementar un sencillo fragmento de código en el lenguaje Texto Estructurado (ST)</span> para a la gestión del contador de ciclos en la parte de implementación del programa `MAIN`.

    ```iecst
    ContadorCiclos := ContadorCiclos + 1;
    ```

8. <span class="objetivo-hito">Construir el proyecto</span> para obtener un archivo ejecutable [➡️](../../procedimientos/workflow/index.md#construir-el-proyecto)

    ??? warning "Aviso"
        Asegurarse antes de continuar de que el resultado de la construcción del proyecto mostrado en la ventana de mensajes no arroja errores.

9. Activar el simulador `UmRT_Default` para disponer de un *runtime* sobre el que ejecutar el código del proyecto. [➡️](../../procedimientos/workflow/index.md#activar-simulador)
10. <span class="objetivo-hito">Seleccionar como sistema destino</span> (**Target System**) el simulador `UmRT_Default`. [➡️](../../procedimientos/workflow/index.md#seleccionar-sistema-destino)
11. Activar la licencia temporal del runtime del sistema destino si es necesario. [➡️](../../procedimientos/workflow/index.md#activar-licencia)
12. Activar la configuración en el sistema destino.  [➡️](../../procedimientos/workflow/index.md#activar-la-configuracion)
13. <span class="objetivo-hito">Transferir el proyecto</span> conectándose (**Login**) al sistema destino. [➡️](../../procedimientos/workflow/index.md#transferir-el-proyecto)

    ??? info
        - Conectarse al sistema destino implica transferir el proyecto al runtime e iniciar la monitorización (sesión de depuración en tiempo real).
        - La comunicación para el intercambio de información entre el entorno de programación y el `runtime` tiene lugar, normalmente, a través del puerto `851` .

14. <span class="objetivo-hito">Poner el programa en ejecución</span> (**Run**). [➡️](../../procedimientos/workflow/index.md#arrancar-el-proyecto)
15. Observar cómo el valor de la variable `ContadorCiclos` se incrementa continuamente al ritmo de ejecución del ciclo básico del PLC (típicamente 10 ms), lo que prueba que el programa se está ejecutando.
16. Modificar el valor del contador de ciclos mediante forzado de variables (**Force values**, **Unforce values**, **Write values**). [➡️](../../procedimientos/workflow/index.md#forzar-variables)
17. Desconectarse del sistema destino (**Logout**) para continuar con la edición del programa. <!--- todo: incluir enlace a workout: desconetar --->

    ??? info
        Cuando nos desconectamos de un sistema destino abandonamos la monitorización, pero el programa sigue ejecutándose en el *runtime* del sistema destino. Como prueba podremos observar que, cuando nos volvamos a conectar, el contador de ciclos tendrá un valor diferente.

18. Crear una sencilla visualización para <span class="objetivo-hito">monitorizar y modificar el valor del dato numérico</span> del contador de ciclos. [➡️](../../procedimientos/hmi/index.md)

    ![Visualización Hola Mundo con el contador de ciclos](./img/v-hola-mundo-contador.png){ .screenshot }

    1. Rectángulo (*Rectangle*) para la etiqueta **Contador**.

        ??? note "Notas"
            - Texts > Text = Contador

    2. Rectángulo (*Rectangle*) para mostrar el valor de `ContadorCiclos`.

        ??? note "Notas"
            - Color > Normal state > Frame color = [0, 0, 0]
            - Color > Normal state > Fill color = [192, 192, 192]
            - Texts > Text = [%d]
                - *Formato estilo printf que indica que se va a sustituir por un número entero.*
            - Text variables > Text variable = [`MAIN.ContadorCiclos`]

    3. Rectángulo (*Rectangle*) para modificar el valor de `ContadorCiclos`.

        ??? note "Notas"
            - Color > Normal state > Frame color = [0, 0, 0]
            - Color > Normal state > Fill color = [255, 255, 255]
            - Texts > Text = [%d]
                - *Formato estilo printf que indica que se va a sustituir por un número entero.*
            - Text variables > Text variable = [`MAIN.ContadorCiclos`]
            - Inputconfiguration > OnMouseClick

    4. Botón (*Button*) para reiniciar el valor de la variable `ContadorCiclos`.

        ??? note "Notas"
            - Texts > Text = [**Reinicia**]
            - Inputconfiguration
                - OnMouseClick > Configure > Execute ST-Code = [`MAIN.ContadorCiclos := 0;`]

    ??? tip "Sugerencia"
        Los colores especificados para los elementos son simplemente un ejemplo, pueden ser escogidos libremente.

19. Volver a conectarse (**Login**) y comprobar que todos los elementos de la visualización funcionan correctamente.
20. Volver a desconectarse (**Logout**) e incluir en la parte de declaración del programa `MAIN` las variables `i_Pulsador` y `o_Lampara`.

    ```iecst
    PROGRAM MAIN
    VAR
        i_Pulsador: BOOL;
        o_Lampara: BOOL;
    END_VAR
    ```

    ??? info

        | Elemento | Tipo de componente | Descripción |
        | :---: | :---: | :--- |
        | `i_Pulsador` | **Identificador** | Identificador/Nombre de la variable |
        | `:` | **Separador** | Operador/Separador |
        | `BOOL` | **Tipo de dato** | Tipo de dato elemental (booleano) |
        | `;` | **Terminador** | Delimitador/Terminador de instrucción |

21. Incluir el código correspondiente a la activación de la lámpara en la parte de implementación del programa `MAIN`.

    ```iecst
    o_Lampara := i_Pulsador;
    ```

22. Construir (**Build**) nuevamente el proyecto para comprobar su corrección y generar las instancias de E/S.

    ??? warning "Aviso"
        Observa que si la compilación es correcta aparecen bajo el apartado `Hola_Mundo_PLC Instance` las instancias de las dos nuevas variables.

23. Incluir en la **visualización** los elementos correspondientes para <span class="objetivo-hito">monitorizar y modificar los valores de las variables booleanas</span> correspondientes al pulsador y la lámpara.

    ![Visualización Hola Mundo con el pulsador y la lámpara](./img/v-hola-mundo.png){ .screenshot }

    1. Botón (*Button*) para modificar el valor de `i_Pulsador`.

        ??? note "Notas"
            - Texts > Text = [**Pulsador**]
            - Inputconfiguration
                - Tap > Variable = [`MAIN.i_Pulsador`]

    2. Rectángulo (*Rectangle*) para mostrar el valor de la variable `o_Lampara`.

        ??? note "Notas"
            - Colors > Normal state > Frame color = [0, 64, 0]
            - Colors > Normal state > Fill color = [0, 64, 0]
            - Colors > Alarm state > Frame color = [0, 128, 0]
            - Colors > Alarm state > Fill color = [0, 128, 0]
            - Texts > Text = [**Lámpara**]
            - Color variables > Toggle color = [`MAIN.o_Lampara`]

    !!! tip "Sugerencia"
        Complete la visualización con los elementos que considere oportuno para mejorar su apariencia.

24. Conectarse nuevamente (**Login**) para <span class="objetivo-hito">validar el proyecto</span>.

    - Modificar los valores de las variables forzándolas (**Force values**, **Unforce values**, **Write values**).
    - Comprobar que los nuevos elementos de la visualización funcionan correctamente.

!!! success "¡Enhorabuena! 🎉"
    Has completado con éxito la primera parte de esta guía de implementación. Has puesto en marcha tu primer **proyecto de PLC** completo en **Texto Estructurado** con **TwinCAT 3** sobre el simulador **UmRT_Default**.
