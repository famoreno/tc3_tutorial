---
title: Hola Mundo - Guía de Implementación
icon: fontawesome/solid/screwdriver-wrench
---

# :fontawesome-solid-screwdriver-wrench: Hola Mundo - Guía de Implementación

## :fontawesome-solid-circle-info: Introducción

El proyecto [**«Hola Mundo»**](../hola-mundo/index.md) nos permitirá dar nuestros primeros pasos en TwinCAT XAE, el entorno de ingeniería de Beckhoff para la configuración y el desarrollo de aplicaciones de automatización.

En esta guía se presenta el flujo de trabajo completo del desarrollo de un programa de PLC, desde la creación del proyecto hasta su puesta a punto sobre un ordenador embebido.

A continuación se muestra cómo replicar este proyecto paso a paso para implementar tu primer programa completo de PLC con TwinCAT 3 desde cero.

---

## :fontawesome-solid-bullseye: Objetivos

A lo largo de este proceso aprenderás a:

- Utilizar el entorno de ingeniería **TwinCAT XAE** de TwinCAT 3.
- Declarar variables de **memoria interna** (marcas).
- Declarar **variables de entrada y salida localizadas** con **mapeo dinámico**.
- Editar un sencillo fragmento de código en el lenguaje **Texto Estructurado (ST)** de la norma **IEC 61131-3**.
- Monitorizar y modificar (escribir/forzar) los valores de las variables en el modo de **Monitorización *online***.
- Monitorizar y modificar los valores de variables booleanas desde una visualización.
- Monitorizar y modificar los valores de variables numéricas desde una visualización.
- Desplegar (poner en marcha) un proyecto PLC.
    - Construir un proyecto.
    - Seleccionar un *runtime*.
    - Configurar la entrada/salida.
    - Vincular las variables de entrada/salida.
    - Transferir un proyecto.
    - Poner un programa en ejecución.
    - Validar un proyecto.

---

## :fontawesome-solid-list-check: Guía de Implementación

!!! tip "Sugerencia"
    Pulsa en :material-arrow-right-bold-box: para obtener más información sobre cómo realizar el paso especificado.

--8<-- "docs/contenidos/ejemplos/hola-mundo/includes/sobre-simulador.md"

---

--8<-- "docs/contenidos/ejemplos/hola-mundo/includes/sobre-controlador.md"

---

--8<-- "docs/contenidos/ejemplos/hola-mundo/includes/con-ardutc.md"

---
