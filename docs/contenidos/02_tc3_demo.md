# 👋 Demo (TwinCAT 3)

Enlace al repositorio en Github: [TC3_Demo](https://github.com/vetorres-uma/TC3_Demo)

## 📝 Descripción del Proyecto

El proyecto Demo pretende ser un **Hola Mundo** para **automatas programables (PLC)**. 

Es un proyecto mínimo y funcional, que muestra la declaración y el uso básico de variables booleanas y enteras, ubicadas en los espacios de memoria de marcas, imagen de entrada e imagen de salida. Cubriendo los elementos esenciales de programación de los lenguajes de la norma **IEC 61131-3** para la programación de PLC.

![Imagen](../images/02_tc3_demo/VISU_Demo.png){width=240px}

Este proyecto incluye además, una **visualización** elemental que permite interactuar con las variables del proyecto, con objetos gráficos. **Formas rectangulares** para mostrar el valor de variables booleanas y numéricas y **botones** para modificar el valor de variables booleanas y numéricas.

### Código

!!! info "Declaración"
    ```st
    PROGRAM MAIN
    VAR
        ContadorCiclos    : UINT; // Variable numérica en el espacio de marcas
        i_Pulsador AT %I* : BOOL; // Variable booleana en la imagen de entrada
        o_Lampara  AT %Q* : BOOL; // Variable booleana en la imagen de salida
    END_VAR
    ```

!!! info "Código"
    ```st
    // Uso de una variable numérica (se incrementa con cada ciclo de ejecución)
    ContadorCiclos := ContadorCiclos + 1;

    // Uso de variables de entrada y salida booleanas (copia la entrada en la salida)
    o_Lampara := i_Pulsador;
    ```

### Comentarios

- La variable `ContadorCiclos` se incrementa indefinidamente una vez por ciclo básico de ejecución del PLC (10 ms).
- La variable de salida `o_Lampara` copia, continuamente, el valor de la variable de entrada `i_Pulsador`.
- El valor de la variable `ContadorCiclos` se muestra en la visualización.
- La variable `ContadorCiclos` puede reinicarse si se acciona el pulsador `Reinicia`.
- El valor de la variable `o_Lampara` se muestra con el cambio de color del rectángulo `Lampara` (verde claro = `false`, verde oscuro = `true`).
- El valor de la variabale `i_Pulsador` cambia cuando se acciona el botón `Pulsador`.

---

## 💻 Requisitos del Sistema

### Software

- **IDE:** Microsoft Visual Studio / TwinCAT 3 XAE (Versión mínima recomendada: **3.1.4024.x**).
- **Lenguajes:** Texto Estructurado (ST).

---

## 🚀 Puesta en Marcha

Para descargar, compilar y ejecutar este proyecto en el entorno de TwinCAT 3, siga los siguientes pasos:

1. **Clonar Repositorio:**

```bash
    git clone https://github.com/vetorres-uma/TC3_Demo.git
```

2. **Abrir el Proyecto:** abra el archivo `.sln` (Solución) ubicado en la carpeta principal utilizando el entorno de ingeniería **TwinCAT XAE** (integrado en Visual Studio).
1. **Selección del Controlador:** seleccione el simulador (**UmRT_Default**) o controlador local o remoto (**Choose Runtime System**).
1. **Activación de Configuración:** en el modo **Configuración**, active la configuración (**Activate Configuration**) y reinicie TwinCAT en modo **Ejecución (Run Mode)**.
1. **Carga del Código:** en el entorno PLC, inicie la sesión y descargue el programa al PLC (**Login**).
1. **Poner el código en ejecución:** ejecute la lógica de control en el controlador (**Start**). Puede utilizar la visualización integrada en el proyecto PLC para facilitar la prueba.

---

## 🔨 Procedimiento operativo
1. Crear una solución de TwinCAT3 con nombre `tc3_demo` [➡️](../../contenidos/01_conceptos/#crear-proyecto-tc3)
2. Crear un proyecto PLC con nombre `demo_PLC` [➡️](../../contenidos/01_conceptos/#crear-proyecto-plc)
3. Declarar las variables
    ```st
        PROGRAM MAIN
        VAR
            ContadorCiclos    : UINT; // Variable numérica en el espacio de marcas
            i_Pulsador AT %I* : BOOL; // Variable booleana en la imagen de entrada
            o_Lampara  AT %Q* : BOOL; // Variable booleana en la imagen de salida
        END_VAR
    ```
4. Escribir el código
    ```st
        // Uso de una variable numérica (se incrementa con cada ciclo de ejecución)
        ContadorCiclos := ContadorCiclos + 1;

        // Uso de variables de entrada y salida booleanas (copia la entrada en la salida)
        o_Lampara := i_Pulsador;
    ```
5. Diseñar la visualización añadiendo: [➡️](../../contenidos/01_conceptos/#crear-visualizacion)
    
    ![Imagen](../images/02_tc3_demo/VISU_Demo.png){width=240px}
    
    1. Rectángulo (*Rectangle*) para la etiqueta **Contador**

        ??? info "Parámetros"
            - Texts > Text = Contador

    2. Rectángulo (*Rectangle*) para el valor de `ContadorCiclos`
   
        ??? info "Parámetros"
            - Color > Normal state > Frame color = [0, 0, 0]
            - Color > Normal state > Fill color = [255, 255, 255]        
            - Texts > Text = [%d] -> *Formato estilo printf*
            - Text variables > Text variable = [`MAIN.ContadorCiclos`]
   
    3. Botón (*Button*) para reiniciar el contador
        
        ??? info "Parámetros"
            - Texts > Text = [**Reinicia**]
            - Inputconfiguration               - 
                - OnMouseClick > Configure > Execute ST-Code = [`MAIN.ContadorCiclos := 0;`]
   
    4. Botón (*Button*) para el pulsador

        ??? info "Parámetros"
            - Texts > Text = [**Marcha**]
            - Inputconfiguration
               - Tap > Variable = [`MAIN.i_Pulsador`]
    
    5. Rectángulo (*Rectangle*) para la lámpara
        
        ??? info "Parámetros"
            - Color > Normal state > Frame color = [0, 64, 0]
            - Color > Normal state > Fill color = [0, 64, 0]       
            - Color > Alarm state > Frame color = [0, 128, 0]
            - Color > Alarm state > Fill color = [0, 128, 0]       
            - Texts > Text = [**Marcha**]
            - Color variables > Toggle color = [`MAIN.o_Lampara`]


6. Compilar el proyecto [➡️](../../contenidos/01_conceptos/#ejecutar-programa)
7. Seleccionar el controlador [➡️](../../contenidos/01_conceptos/#seleccionar-el-controlador)
8. Activar la configuración y reiniciar TwinCAT 3 en modo **Ejecución (Run Mode)** [➡️](../../contenidos/01_conceptos/#activar-la-configuracion)
9. **Cargar el código** en el entorno PLC: iniciar la sesión y descargar el programa al PLC (**Login**) [➡️](../../contenidos/01_conceptos/#transferir-y-ejecutar-el-programa)
10. **Poner el código en ejecución:** ejecutar la lógica de control en el controlador (**Start**) [➡️](../../contenidos/01_conceptos/#transferir-y-ejecutar-el-programa)
14. **Utilizar la visualización** integrada en el proyecto PLC para facilitar la prueba:
    1. Reiniciar el contador desde la visualización pulsando en el botón **Reinicia**.
    2. **Si se está ejecutando el programa en un controlador local** (emulador `Local` o simulador `UmRT`).
        - Cambiar el valor de la lámpara de marcha pulsando el botón de marcha en la visualización.
        - Alternativamente, escribe o fuerza las variables deseadas desde TwinCAT 3.
    3. **Si tienes asociadas las variables a terminales de E/S físicas** en un controlador remoto.
        - Comprobar en el programa `MAIN` que accionando el pulsador físico se enciende la lámpara.
        - Comprobar en la visualización que accionando el pulsador físico cambia de estado la lámpara.
        - Comprobar en la visualización que accionando el botón ni se enciende, ni cambia de estado la lámpara.

            !!! warning "Importante"
                La ejecución del ciclo básico hace que el valor del pulsador **se actualice con el valor del pulsador real** al inicio de cada ciclo.

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
