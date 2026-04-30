# 👋 Demo (TwinCAT 3)

<!--
!!! info "Info"
    Enlace al repositorio en Github [![Github Logo](../images/_resource/github_logo.svg){width=15px}](https://github.com/vetorres-uma/TC3_Demo)
-->

## 📝 Descripción del Proyecto

El proyecto Demo pretende ser un **Hola Mundo** para **autómatas programables (PLC)**.

Es un proyecto mínimo y funcional, que muestra la declaración y el uso básico de variables booleanas y enteras, ubicadas en los espacios de memoria de marcas, imagen de entrada e imagen de salida. Cubriendo los elementos esenciales de programación de los lenguajes de la norma **IEC 61131-3** para la programación de PLC.

![Imagen](../images/02_tc3_demo/VISU_Demo.png){width=240px}

Este proyecto incluye además, una **visualización** elemental que permite interactuar con las variables del proyecto, con objetos gráficos. **Formas rectangulares** para mostrar el valor de variables booleanas y numéricas y **botones** para modificar el valor de variables booleanas y numéricas.

### Código

!!! info "Declaración"
    ```pascal
    PROGRAM MAIN
    VAR
        ContadorCiclos    : UINT; // Variable numérica en el espacio de marcas
        i_Pulsador AT %I* : BOOL; // Variable booleana en la imagen de entrada
        o_Lampara  AT %Q* : BOOL; // Variable booleana en la imagen de salida
    END_VAR
    ```

!!! info "Código"
    ```pascal
    // Uso de una variable numérica (se incrementa con cada ciclo de ejecución)
    ContadorCiclos := ContadorCiclos + 1;

    // Uso de variables de entrada y salida booleanas (copia la entrada en la salida)
    o_Lampara := i_Pulsador;
    ```

### Comentarios

- La variable `ContadorCiclos` se incrementa indefinidamente una vez por ciclo básico de ejecución del PLC (10 ms).
- La variable de salida `o_Lampara` copia, continuamente, el valor de la variable de entrada `i_Pulsador`.
- El valor de la variable `ContadorCiclos` se muestra en la visualización.
- La variable `ContadorCiclos` puede reiniciarse si se acciona el pulsador `Reinicia`.
- El valor de la variable `o_Lampara` se muestra con el cambio de color del rectángulo `Lampara` (verde claro = `FALSE`, verde oscuro = `TRUE`).
- El valor de la variable `i_Pulsador` cambia cuando se acciona el botón `Pulsador`.

---

## 💻 Requisitos del Sistema

### Software

- **IDE:** Microsoft Visual Studio / TwinCAT 3 XAE (Versión mínima recomendada: **3.1.4024.x**).
- **Lenguajes:** Texto Estructurado (ST).

---

## 🚀 Descarga

**Para descargar, compilar y ejecutar este proyecto en el entorno de TwinCAT 3, seguir el siguiente procedimiento**.
<!-- 
**Para descargar, compilar y ejecutar este proyecto en el entorno de TwinCAT 3, seguir una de estas dos opciones:**

- Mediante el Campus Virtual
- Mediante GIT
-->
### Mediante el Campus Virtual

1. **Copiar** a tu equipo local el fichero:

    `CV → Automatización → ejemplos → 1_tc3_demo → tc3_demo.tnzip`

    que hay en la carpeta del campus virtual.

2. **Seguir el procedimiento** descrito [aquí](../../contenidos/01_conceptos/#abrir-un-fichero-tnzip) para generar la **Solución** a partir del fichero.

3. **Compilar** y poner en marcha el proyecto siguiendo lo descrito [aquí](../contenidos/01b_ejecucion.md).

<!-- 
### Mediante GIT

1. **Clonar Repositorio:**

```bash
git clone https://github.com/vetorres-uma/TC3_Demo.git
```

2. **Abrir el Proyecto:** abra el archivo `.sln` (Solución) ubicado en la carpeta principal utilizando el entorno de ingeniería **TwinCAT XAE** (integrado en Visual Studio).
1. **Selección del Controlador:** seleccione el simulador (**UmRT_Default**) o controlador local o remoto (**Choose Runtime System**).
1. **Activación de Configuración:** en el modo **Configuración**, active la configuración (**Activate Configuration**) y reinicie TwinCAT en modo **Ejecución (Run Mode)**.
1. **Carga del Código:** en el entorno PLC, inicie la sesión y descargue el programa al PLC (**Login**).
1. **Poner el código en ejecución:** ejecute la lógica de control en el controlador (**Start**). Puede utilizar la visualización integrada en el proyecto PLC para facilitar la prueba.
-->
---

## 🔨 Explicación

**Para replicar la creación de la solución completa, seguir este procedimiento:**

!!! tip "Sugerencia"
    Pulsa en ➡️ para obtener más información sobre cómo realizar el paso especificado.

1. Crear una solución de TwinCAT3 con nombre `tc3_demo` [➡️](../../contenidos/01_conceptos/#crear-proyecto-tc3)
2. Crear un proyecto PLC con nombre `demo_PLC` [➡️](../../contenidos/01_conceptos/#crear-proyecto-plc)

    !!! warning "Importante"
        En este ejemplo no utilizaremos bloques funcionales (**FB**) sino que implementaremos toda la funcionalidad directamente en el programa `MAIN`.

3. Declarar las variables en el programa `MAIN` [➡️](../../contenidos/01_conceptos/#declaracion-de-variables)

    ```pascal
    PROGRAM MAIN
    VAR
        ContadorCiclos    : UINT; // Variable numérica en el espacio de marcas
        i_Pulsador AT %I* : BOOL; // Variable booleana en la imagen de entrada
        o_Lampara  AT %Q* : BOOL; // Variable booleana en la imagen de salida
    END_VAR
    ```

4. Escribir el código

    ```pascal
    // Uso de una variable numérica (se incrementa con cada ciclo de ejecución)
    ContadorCiclos := ContadorCiclos + 1;

    // Uso de variables de entrada y salida booleanas (copia la entrada en la salida)
    o_Lampara := i_Pulsador;
    ```

5. Diseñar la visualización añadiendo: [➡️](../../contenidos/01_conceptos/#crear-visualizacion)

    ![Imagen](../images/02_tc3_demo/VISU_Demo.png){width=240px}

    !!! tip "Sugerencia"
        Los colores especificados para los elementos son simplemente un ejemplo, pero pueden ser escogidos libremente.

    1. Rectángulo (*Rectangle*) para la etiqueta **Contador**

        ??? info "Parámetros"
            - Texts > Text = Contador

    2. Rectángulo (*Rectangle*) para el valor de `ContadorCiclos`

        ??? info "Parámetros"
            - Color > Normal state > Frame color = [0, 0, 0]
            - Color > Normal state > Fill color = [255, 255, 255]
            - Texts > Text = [%d]
                - *Formato estilo printf que indica que se va a sustituir por un número entero.*
            - Text variables > Text variable = [`MAIN.ContadorCiclos`]

    3. Botón (*Button*) para reiniciar el contador

        ??? info "Parámetros"
            - Texts > Text = [**Reinicia**]
            - Inputconfiguration
                - OnMouseClick > Configure > Execute ST-Code = [`MAIN.ContadorCiclos := 0;`]

    4. Botón (*Button*) para el pulsador

        ??? info "Parámetros"
            - Texts > Text = [**Pulsador**]
            - Inputconfiguration
                - Tap > Variable = [`MAIN.i_Pulsador`]

    5. Rectángulo (*Rectangle*) para la lámpara

        ??? info "Parámetros"
            - Colors > Normal state > Frame color = [0, 64, 0]
            - Colors > Normal state > Fill color = [0, 64, 0]
            - Colors > Alarm state > Frame color = [0, 128, 0]
            - Colors > Alarm state > Fill color = [0, 128, 0]
            - Texts > Text = [**Lámpara**]
            - Color variables > Toggle color = [`MAIN.o_Lampara`]

6. **Poner en marcha** el proyecto [➡️](../contenidos/01b_ejecucion.md)
7. **Utilizar la visualización** creada PLC para facilitar la prueba:
    1.  Reiniciar el contador desde la visualización pulsando en el botón **Reinicia**.
    2.  Cambiar el valor de la lámpara de marcha pulsando el **botón de marcha** en la visualización.
    3.  Alternativamente, **escribe o fuerza** las variables deseadas desde TwinCAT 3.

---

Ahora vamos a ejecutar el programa en un **controlador remoto** (por ejemplo, un PLC del laboratorio).

1. **Buscar** el controlador en la red, **escanear** los módulos y **probar** dos terminales/canales, uno de entrada y otro de salida. [➡️](../../contenidos/01_conceptos/#busqueda-de-controladores-remotos)

    !!! tip "Sugerencia"
        Abrir la hoja de cálculo con la lista de entradas y salidas del sistema FMS200, seleccionar la pestaña correspondiente a tu estación y escoger un **pulsador** de entre los elementos de entrada y una **lámpara** de entre los elementos de salida.

2. **Vincular** los terminales/canales correspondiente con las variables de E/S [➡️](../../contenidos/01_conceptos/#vinculacion-de-variables-y-es)
    2.  Variable de entrada `i_Pulsador`
    2.  Variable de salida `i_Lampara`

3. **Activar la configuración** y reiniciar TwinCAT 3 en modo **Ejecución (Run Mode)** [➡️](../../contenidos/01_conceptos/#activar-la-configuracion)
4. **Cargar el código** en el controlador (**Login**) [➡️](../../contenidos/01_conceptos/#transferir-y-ejecutar-el-programa)
5. Poner el código en **ejecución** (**Start**) [➡️](../../contenidos/01_conceptos/#transferir-y-ejecutar-el-programa)
6. Comprobar que, accionando el pulsador físico, se enciende la lámpara física.
7. **Utilizar la visualización** integrada en el proyecto PLC para facilitar la prueba:
    - Comprobar en la visualización que, accionando el pulsador físico, cambia de estado la lámpara.
    - Comprobar en la visualización que, accionando el botón de la visualización, **ni se enciende, ni cambia de estado la lámpara**.

        !!! warning "Importante"
            Esto se debe a que la ejecución del ciclo básico hace que el valor del pulsador **se actualice con el valor del pulsador físico** al inicio de cada ciclo, sobreescribiendo el valor que fija el botón de la visualización.

---

## 🤝 Contribuciones

Este proyecto es utilizado con fines educativos y de prueba. Las contribuciones, sugerencias o correcciones de errores son bienvenidas. Por favor, abra un *Issue* o envíe un *Pull Request* si deseas contribuir.

---

## 🧑 Autor

- **Autor Principal:** Victor Torres ([@vetorres-uma](https://github.com/vetorres-uma>))
- **Revisor**: Manuel Castellano ([@mcastellanoquero](https://github.com/mcastellanoquero))
- **Revisor**: Francisco Ángel Moreno ([@famoreno](https://github.com/famoreno))

---

## ⚖️ Licencia

Este proyecto es de código abierto y está disponible bajo la **Licencia Pública General GNU (GPL)**.

- Consulte el archivo `LICENSE.md` para más detalles.
