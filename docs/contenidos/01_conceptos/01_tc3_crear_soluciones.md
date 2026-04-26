## 🏗️ Crear soluciones en TC3

### Crear proyecto TC3

1. Abrir el *software* `Twincat XAE Shell`, desde el menú **Inicio** de Windows o desde el icono de la barra de programas en segundo plano que hay abajo a la derecha en la barra de tareas.
2. Seleccionar ***New TwinCAT Project***.

    ![Imagen](../images/01_conceptos/image.png){width=240px}

3. Seleccionar el tipo ***TwinCAT XAE Project (XML format)***.

    ![Imagen](../images/01_conceptos/image%201.png){width=384px}

4. Darle un nombre a la **Solución**, y seleccionar su ubicación (la que viene por defecto está bien). Dejar marcada la opción ***Create directory for solution***.

    ![Imagen](../images/01_conceptos/image%202.png){width=768px}

    !!! question "Ejemplo"
        `TC3_Lampara`  

5. Por defecto, tanto la **Solución** de Visual Studio como el proyecto de **TC3** tendrán el mismo nombre.

!!! note "Recomendación"
    Ocultar las secciones del proyecto que no se van a utilizar: `MOTION`, `SAFETY`, `C++`, `VISION`, `ANALYTICS`.
    Nos quedaremos solo con `SYSTEM`, `PLC` e `I/O`.

### Crear proyecto PLC

1. Una vez creado un proyecto de TC3, procedemos a crear un proyecto PLC.
2. Hacer **CD** sobre la sección `PLC` y seleccionar ***Add New Item***.
3. Seleccionar ***Standard PLC Project***, darle un nombre y pulsar ***Add***.  
    ![Imagen](../images/01_conceptos/image%203.png){width=384px}
        
    !!! question "Ejemplo"
        `Lampara_PLC`

1. En la sección de `SYSTEM > Tasks` aparecerá por defecto una nueva tarea `PLC Task` con sus parámetros por defecto (ej. 10 ms de ciclo).
2. En la sección `PLC` aparece el proyecto con dos secciones nuevas:
    1. `Project`
          1. `External Types`. Almacena definiciones de tipos de datos externos que provienen de fuentes externas al PLC.
          2. `References`. Listado de referencias a las librerías utilizadas en el proyecto.
          3. `DUTs`. Tipos de Dato de Usuario (*Data User Types*) (`ENUM`, `STRUCT`).
          4. `GVLs`. Listas de Variables Globales (*Global Variables Lists*).
          5. `POUs`. Unidades de Organización del Programa (Program Organization Units). Programas, bloques funcionales y funciones que implementaremos.
          6. `VISUs`. Visualizaciones creadas.
          7. Tarea creada (`PLCTask`) y programa `MAIN`
   
            ![Imagen](../images/01_conceptos/image%204.png){width=132px}
    
    2. `Instance`. Aquí aparecerán las variables en las imágenes de Entrada y Salida.
 
3. A partir de aquí se puede empezar a implementar el proyecto.

### Crear bloque funcional

Habitualmente, encapsularemos las funcionalidades del sistema en **bloques funcionales**. 
Un bloque funcional (**Function Block** o **FB**) es *módulo* de programa que encapsula **datos** y **comportamiento** para realizar una tarea concreta dentro del control de un PLC. 
A diferencia de una función simple, un bloque funcional **mantiene memoria interna entre ciclos de ejecución**, lo que permite modelar cosas que tienen estado, como temporizadores, contadores o el control de una estación. 
Se utiliza **creando una instancia** del bloque en el programa y llamándola en cada ciclo, pasando entradas y recibiendo salidas, mientras el bloque conserva sus variables internas para saber qué ocurrió en ciclos anteriores.

!!! warning "Importante"
    Nuestro `Ejemplo - Demo`, al ser solo un ejemplo sencillo, no hace uso de bloques funcionales, sino que implementa toda la funcionalidad en el programa principal, pero esto no será lo habitual.

Para crear un FB, seguimos este procedimiento:

1. Hacer **CD** sobre la sección `POUs`.
2. Seleccionar `Add → POU → Function Block`.
3. Darle un nombre significativo.
4. Seleccionar el lenguaje a utilizar. Normalmente utilizaremos `ST` o `SFC`.

### Instanciar bloque funcional

Para hacer uso del bloque funcional en un programa, deberemos **instanciar** dicho **FB** y llamar a la instancia:

!!! info "Declaración"
    ```pascal
    PROGRAM MAIN
    VAR
        Carro: FB_Carro;
    END_VAR
    ```
    
!!! info "Código"
    ```pascal
    Carro();
    ```

!!! tip "Nota"
    Un bloque funcional puede ser instanciado y usado dentro de otro bloque funcional.