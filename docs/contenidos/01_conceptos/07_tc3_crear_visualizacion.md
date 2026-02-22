## 🖥️ Crear visualización

- Hacer **CD** sobre la sección `VISUs`.

- Seleccionar `Add → Visualization` y pulsar en **Open** en la ventana *popup*.

    ![Imagen](../images/01_conceptos/image%2013.png){width=240px}

- En la parte derecha de la pantalla aparecerá la sección `Toolbox` donde, en la sección `Basic` aparecen las formas básicas. Arrastrar a la visualización los elementos que se quieran.

!!! warning "Importante"
    Si no aparece la sección, mostrarlo entrando en el **Menú** `View → Toolbox`

!!! note "Recomendación"
    Se recomienda utilizar **rectángulos** para crear botones tanto para las entradas como para las salidas.

### Botones para cambiar valores de variables

- Dibujar un rectángulo con el tamaño deseado.

- Escribir dentro la etiqueta que queramos que aparezca en el botón.

- Introducir la variable de tipo `BOOL` que queremos asociar a dicho botón. Dependiendo del comportamiento que queramos que tenga el botón, esta variable se introduce en una sección distinta dentro de `Properties → Input Configuration` (la pestaña `Properties` aparece a la derecha, normalmente combinada con `Toolbox`).

    - Si queremos que la variable cambie de valor **mientras** se pulsa el botón con el ratón pero vuelva a su valor anterior una vez soltado el ratón, introduciremos la variable en la sección `Tap`:

        ![Imagen](../images/01_conceptos/image%2014.png){width=240px}

    - Si queremos que la variable cambie de valor cada vez que pulsemos el botón lo introduciremos en la sección `Toggle` (el valor conmutará entre `TRUE` y `FALSE`):

        ![Imagen](../images/01_conceptos/image%2015.png){width=240px}
