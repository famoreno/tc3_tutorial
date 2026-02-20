# Beckhoff

## La Empresa

**Beckhoff Automation GmbH & Co.** es un fabricante de tecnología de automatización con sede en Verl, en Renania del Norte-Westfalia (Alemania), y forma parte del Grupo Beckhoff. Fundada por **Hans Beckhoff en 1980**, la empresa implementa sistemas de automatización para la industria y la automatización de edificios.

Su característica esencial se materializó con el lanzamiento en **1986 del primer controlador industrial basado en PC del mercado**. Esta fue una idea radical en aquel entonces: utilizar la potencia y flexibilidad de un ordenador estándar, en lugar de los sistemas de control propietarios y cerrados que dominaban la industria. Este concepto, que llamaron **"PC-based Control"** (control basado en PC), se convertiría en la piedra angular de la empresa y en una revolución silenciosa para la automatización.

Además del uso de la tecnología de control basada en PC, desarrollada sobre la base de estándares abiertos, Beckhoff protagonizó en **2003 otro hito que revolucionó las comunicaciones industriales**: el desarrollo de **EtherCAT** (Ethernet for Control Automation Technology). Se trata de un bus de campo industrial en tiempo real basado en Ethernet, extremadamente rápido y preciso, que desde entonces se ha convertido en un estándar mundial para la automatización de alto rendimiento, gestionado por un consorcio internacional del que forman parte miles de empresas.

Manteniendo su espíritu pionero, Beckhoff ha continuado ampliando los límites de la tecnología con sistemas extraordinarios:

- **XTS (2011):** XTS (eXtended Transportation System), un sistema de transporte lineal con múltiples motores independientes (movers) que permiten un movimiento altamente dinámico y flexible en una sola pista.
- **XPlanar (2018):** Sistema de transporte planar que hace levitar y mover libremente productos sobre un mosaico de módulos, ofreciendo una flexibilidad sin precedentes.
- **MX-System (2024-2025):** Sistema que elimina la necesidad de armarios de control, integrando toda la electrónica y la fuente de alimentación en módulos robustos y resistentes, diseñados para ser montados directamente en la máquina.

### Interés Didáctico

Desde un punto de vista didáctico, Beckhoff presenta un ecosistema especialmente atractivo para su uso en entornos educativos y de formación. Esta idoneidad se sustenta en tres pilares fundamentales que, en conjunto, suponen una clara ventaja frente a otras filosofías de automatización:

1.  **Compromiso con los estándares abiertos:** A diferencia de los ecosistemas cerrados y propietarios que aún persisten en la industria, Beckhoff basa su tecnología en estándares internacionales. Esto no solo garantiza la interoperabilidad con otros sistemas, sino que permite al alumnado adquirir conocimientos y competencias universales, transferibles a múltiples entornos tecnológicos, en lugar de limitarse a aprender a manejar un único fabricante.
2.  **Acceso sin barreras para el aprendizaje (Política de licencias):** Su modelo de negocio permite a estudiantes, investigadores y desarrolladores trabajar con el entorno TwinCAT de forma completamente gratuita durante la fase de desarrollo y aprendizaje. El entorno de programación puede descargarse y ejecutarse sin ningún coste, eliminando la barrera económica que imponen otros fabricantes con licencias muy costosas, incluso para fines académicos.
3.  **Entorno de simulación integrado:** La posibilidad de ejecutar, depurar y validar código de control de manera virtual es clave en la docencia. Beckhoff permite probar proyectos completos de automatismo utilizando únicamente un PC, sin necesidad de disponer de hardware físico. Su potente emulador (Runtime) y simulador (UmRT_Default) integrados replican fielmente el comportamiento de los sistemas reales, facilitando la experimentación, el autoaprendizaje y la comprensión de conceptos complejos de una manera práctica, segura y accesible desde cualquier lugar.

---

## TwinCAT 2

En **1996**, Beckhoff presentó su plataforma software, **TwinCAT** (The Windows Control and Automation Technology). TwinCAT es un completo paquete para la automatización que incluye un software de desarrollo de aplicaciones para PLC y control numérico (CNC) y un **Runtime**, que convertía cualquier PC industrial en un potente controlador lógico programable (PLC) y controlador de movimientos en tiempo real. De esta forma, integraba la lógica de control con el mundo de la informática, permitiendo ejecutar código TwinCAT en tiempo real en cualquier ordenador con Windows y sentando las bases para el concepto de «Control Basado en PC».

### Componentes Principales

La arquitectura de TwinCAT 2 se articula en torno a tres aplicaciones clave que trabajan de forma conjunta:

- **PLC Control:** Es el Entorno Integrado de Desarrollo (IDE) para la creación de programas de control. Soporta la totalidad de los lenguajes definidos en el estándar internacional **IEC 61131-3** (Texto Estructurado, Diagrama de Contactos, Diagrama de Funciones, etc.), ofreciendo un entorno completo para la programación, depuración y compilación del código de la aplicación.
- **System Manager:** Es la herramienta de configuración del sistema TwinCAT que permite la conexión (asociación o vinculación) de las variables de entradas y salidas de las tareas software con las señales físicas presentes en los buses de campo.
- **Runtime:** Es una aplicación informática que **emula el comportamiento de un autómata programable industrial (SoftPLC)** en un ordenador con Windows. El Runtime se encarga de ejecutar el ciclo básico de funcionamiento del programa de usuario, gestionar las comunicaciones en tiempo real y actualizar el estado de las entradas y salidas. Por esta razón, cualquier PC embebido de Beckhoff se suministra habitualmente con un Runtime preinstalado, convirtiéndolo de facto en un PLC industrial listo para ejecutar código IEC 61131-3.

### Versiones

TwinCAT 2 es un software propietario que actualmente se distribuye en dos paquetes principales:

- **Versión R3:** Este paquete está destinado a sistemas con Windows de **32 bits**. Incluye tanto el entorno de desarrollo completo como el Runtime. El entorno de desarrollo puede usarse de forma **gratuita, indefinida y con toda su funcionalidad**. El Runtime, por su parte, dispone de una licencia gratuita limitada a **30 días**, que puede renovarse de forma indefinida con la simple reinstalación del paquete.
- **Versión x64 Engineering:** Diseñada para sistemas operativos Windows de **64 bits**, contiene únicamente el entorno de desarrollo de TwinCAT 2, que al igual que en la versión R3, puede usarse de forma **gratuita, indefinida y con toda su funcionalidad**.

---

## TwinCAT 3

**TwinCAT 3** es la evolución del sistema de programación de Beckhoff, puesto a disposición del gran público a partir de **2012**. Al igual que su predecesor, es un completo paquete para la automatización que incluye un software de desarrollo de aplicaciones para PLC y control numérico y un Runtime que permite ejecutar en tiempo real código TwinCAT en cualquier ordenador con Windows.

TwinCAT 3 representa la evolución del concepto de SoftPLC hacia la **eXtended Automation (XA)**. A diferencia de TwinCAT 2, no es una aplicación independiente, sino que se integra como una extensión dentro de **Microsoft Visual Studio**, convirtiéndolo en un entorno de desarrollo (IDE) de primer orden.

En TwinCAT 3, las funciones que antes estaban separadas en diferentes aplicaciones (System Manager y PLC Control) se fusionan en una única herramienta integrada:

- **Engineering (XAE):** Es el entorno de configuración y programación. Puede integrarse en Visual Studio o en su versión aislada **TcXaeShell**, disfrutando de todas las prestaciones que ofrece un IDE profesional (depuración, control de versiones, etc.). TcXaeShell es una versión personalizada por Beckhoff del Shell de Visual Studio 2017.
- **Runtime (XAR):** Es el motor de ejecución en tiempo real. Se ejecuta en modo **kernel**, lo que le permite tomar el control de uno o varios núcleos del procesador (Multi-core) para garantizar que las tareas de automatización se ejecuten con **determinismo**, independientemente de la carga de trabajo de Windows.

Los componentes principales del IDE son:

- **Configuración de Sistema (System):** Donde se gestiona el hardware, la asignación de núcleos del procesador y las tareas (tasks).
- **Configuración de I/O:** Sustituye al antiguo System Manager. Aquí se escanean los buses de campo (siendo **EtherCAT el estándar nativo**) y se vinculan (mapean) las variables del PLC con las señales físicas.
- **PLC:** Entorno de programación basado en la norma IEC 61131-3. En TwinCAT 3, se introducen de lleno la **Programación Orientada a Objetos (POO)** y el uso de **Texto Estructurado (ST)** como lenguaje principal.

A diferencia de TwinCAT 2, cuyo Runtime sólo funciona en sistemas de 32 bits, TwinCAT 3 está diseñado para arquitecturas modernas de **64 bits**. Además del tradicional emulador (Runtime), dispone de un simulador (**UmRT_Default**) capaz de procesar código IEC, aunque sin las prestaciones de tiempo real del emulador.

### Modelo de Licencias

Uno de los grandes éxitos de TwinCAT 3 es su modelo de licencias, especialmente atractivo para el ámbito académico y de ingeniería:

- **Instalación Gratuita:** El entorno de desarrollo (XAE) es **completamente gratuito** y se puede instalar en cualquier PC para programar y configurar proyectos de forma indefinida.
- **Licencias de Prueba (Trial de 7 días):** TC3 permite generar licencias temporales de **7 días** para todas sus funciones (PLC, HMI, Motion, Safety, Vision). Estas licencias se pueden renovar de forma infinita simplemente introduciendo un código "Captcha".
- **Licencias Hardware:** Para entornos de producción, las licencias se adquieren de forma permanente y se vinculan al hardware (el PC embebido o un dongle USB).