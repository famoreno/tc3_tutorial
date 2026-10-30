---
icon: fontawesome/solid/display
---

# :fontawesome-solid-circle-info: Crear una HMI

## :fontawesome-solid-circle-info: Introducción

> Una **Interface Hombre-Máquina** (`HMI` ➔ *Human-Machine Inferface*) es el componente de un sistema de automatización que permite a los operarios interactuar con los procesos industriales de manera visual.

Entre las funciones principales de un HMI se encuentran:

- Monitorizar del estado del proceso en tiempo real.
- Controlar el proceso permitiendo arrancarlo, detenerlo, establecer y modificar parámetros de su funcionamiento, ...
- Gestionar alarmas y notificando los fallos.
- Registrar datos que permitan analizar el rendimiento y evaluar la producción.

Para desarrollar estas interfaces de usuario en TwinCAT 3, Beckhoff ofrece principalmente dos tecnologías de visualización nativas integradas en su ecosistema, diseñadas para distintas necesidades de complejidad, rendimiento y arquitectura.

### TwinCAT 3 PLC HMI

Es la solución de visualización clásica de TwinCAT. Está basada en CODESYS v3 y se encuentra integrada directamente dentro del entorno de desarrollo del PLC. Se puede ejecutar localmente (TF1800), mostrándose en una pantalla conectada directamente al propio PC Industrial de Beckhoff o puede renderizarse en HTML5 (TF1810) para visualizarse remotamente en un navegador web.

- Se «programa» utilizando el editor gráfico nativo de CODESYS integrado en Visual Studio (TwinCAT XAE).
- Se configura fácilmente porque todas las variables del proyecto PLC son accesibles de forma directa.
- Ideal para paneles locales, proyectos sencillos o desarrollos rápidos sin salir del entorno de programación.
- Cuenta con una colección suficiente de elementos estándar de control (formas, botones, barras, histogramas, alarmas, gestión básica de usuarios, ...).

### TwinCAT 3 HMI

Es la nueva generación de interfaces basados en web de Beckhoff, es una plataforma de visualización moderna y avanzada, orientada a arquitecturas modulares, multidispositivo y de alta personalización.

- Integrada en Visual Studio (TwinCAT XAE).
- Se crea como un proyecto independiente al del PLC.
- Arquitectura basada en el TwinCAT HMI Server (TF2000).
- Utiliza tecnologías Web estándar (HTML5, JavaScript y CSS).
- Aunque se diseña de manera visual mediante "arrastrar y soltar", permite añadir código personalizado y animaciones CSS avanzadas.
- Utiliza una arquitectura Cliente-Servidor. El servidor de HMI puede comunicarse simultáneamente con múltiples PLCs (mediante el protocolo ADS de Beckhoff u OPC UA) y servir la interfaz a múltiples pantallas de forma independiente.

!!! note
    Adicionalmente, gracias al protocolo abierto TwinCAT ADS, TwinCAT 3 ofrece la posibilidad de desarrollar HMI externos utilizando cualquier lenguaje de programación de terceros como C#, .NET, C++, o frameworks web como React/Angular, comunicándose directamente con las variables del PLC.

---

--8<-- "docs/contenidos/procedimientos/hmi/includes/tc3-plc-hmi.md"

---
