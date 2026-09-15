# 👋 Hola Mundo (TwinCAT 3)

## 📝 Descripción del Proyecto

Este proyecto es el **Hola Mundo** de la programación de **autómatas programables (PLC)**. 

El proyecto **Hola Mundo** se ha desarrollado en el entorno **TwinCAT 3** empleando el lenguaje **Texto Estructurado (ST)** conforme a la norma **IEC 61131-3**.

Hola Mundo es un proyecto mínimo y funcional, que muestra la declaración y el uso básico de variables booleanas y enteras, ubicadas en los espacios de memoria de marcas, imagen de entrada e imagen de salida. Cubriendo los elementos esenciales de programación del lenguaje ST de la norma **IEC 61131-3** para la programación de PLC.

![V_Hola_Mundo](../images/02_tc3_hola_mundo/V_Hola_Mundo.png)
<figcaption>Figura 1: Visualización del proyecto Hola Mundo.</figcaption>

Este proyecto incluye además, una **visualización** elemental que permite, mediante objetos gráficos, interactuar con las variables del proyecto. Utilizando **formas rectangulares**, para mostrar el valor de variables booleanas y numéricas, y **botones**, para modificar el valor de variables booleanas y numéricas.

---

## Estructura (simplificada) del Proyecto:

```text
TC3_Hola_Mundo/
├── TC3_Hola_Mundo.sln             <-- Solución de Visual Studio
└── TC3_Hola_Mundo/                <-- Proyecto TwinCAT
    └── Hola_Mundo_PLC/            <-- Proyecto PLC
        ├── POUs/
        │   └── MAIN.TcPOU         <-- Programa principal (Código ST)
        └── VISUs/
            └── V_Hola_Mundo.TcVISU <-- Visualización (Interfaz gráfica)
```

--- 

## Código

!!! info "Parte de Declaración"
    ```iecst
    // Hola Mundo de la Programación de PLC
    PROGRAM MAIN
    VAR
        ContadorCiclos: UINT;
        i_Pulsador AT %I*: BOOL;
        o_Lampara AT %Q*: BOOL;
    END_VAR
    ```

!!! info "Parte de Implementación"
    ```iecst
    ContadorCiclos := ContadorCiclos + 1;
    o_Lampara := i_Pulsador;
    ```

---

## Comentarios

- La interfaz del programa `MAIN` (cabecera y definición de variables) se define en la **Parte de Declaración**. 
- Los **comentarios** de una línea empiezan con `//`.
- La variable `ContadorCiclos` se declara como un entero sin signo (`UINT`).
- La variable `i_Pulsador` se declara como un **booleano** (`BOOL`) y se localiza dinámicamente en la **Imagen de Entrada** (`AT %I*`).
- La variable `o_Lampara` se declara como un **booleano** (`BOOL`) y se localiza dinámicamente en la **Imagen de Salida** (`AT %Q*`).
- La variable `ContadorCiclos` se incrementa indefinidamente una vez por **Ciclo Básico** de ejecución del PLC (10 ms).
- El código del módulo, en lenguaje ST, se incluyue en la **Parte de Implementación**.
- La variable de salida `o_Lampara` copia, continuamente, el valor de la variable de entrada `i_Pulsador`.
- El valor de la variable `ContadorCiclos` se muestra en rectángulo gris la visualización.
- El valor de la variable `ContadorCiclos` se se puede cambiar escribiéndolo en rectángulo blanco la visualización.
- La variable `ContadorCiclos` puede reiniciarse accionando el pulsador `Reinicia`.
- El valor de la variable `o_Lampara` se muestra con el cambio de color del rectángulo `Lampara` (verde claro = `FALSE`, verde oscuro = `TRUE`).
- El valor de la variable `i_Pulsador` cambia cuando se acciona el botón `Pulsador`.

---

## 📦 Código Fuente y Descarga

El código fuente completo de este proyecto **Hola Mundo**, está disponible en GitHub:

* :material-github: **GitHub:** [`vetorres-uma/TC3_Hola_Mundo`](https://github.com/vetorres-uma/TC3_Hola_Mundo)
* :material-github: **GitHub:** [:material-download: Descarga directa `.zip`](https://github.com/vetorres-uma/TC3_Hola_Mundo/archive/refs/heads/main.zip)

También puede descargarse el archivo comprimido de la solución (tnzip) del proyecto desde el siguiente repositorio:

* :material-google-drive: **Google Drive:** [:material-download: Descargar `.tnzip`](https://drive.google.com/file/d/1HiN3VGmpYH63-8s_RbQovNkcL4GJR9_5/view?usp=drive_link)

---
 