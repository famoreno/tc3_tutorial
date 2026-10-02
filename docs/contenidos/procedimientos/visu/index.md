🚧 *Proximamente*

<!---
Para desarrollar interfaces de usuario (HMI) en TwinCAT 3, Beckhoff ofrece principalmente dos tecnologías de visualización nativas integradas en su ecosistema, diseñadas para distintas necesidades de complejidad, rendimiento y arquitectura: [1, 2] 
## 1. TwinCAT 3 PLC HMI (Basada en CODESYS v3)
Es la solución de visualización clásica y está integrada directamente dentro del entorno de desarrollo del PLC. [1, 2] 

* Cómo se denomina: Dependiendo del entorno de ejecución, se divide en TwinCAT 3 PLC HMI (si se ejecuta localmente en la pantalla del propio PC Industrial) o TwinCAT 3 PLC HMI Web (si se renderiza en HTML5 para visualizarse remotamente en un navegador web). Su suplemento técnico suele identificarse como TF1800 o TF1810. [1, 2] 
* Posibilidades y características:
* Se programa utilizando el editor gráfico nativo de CODESYS integrado en Visual Studio.
   * Su configuración es muy directa porque las variables del PLC se mapean de forma inmediata a los elementos gráficos.
   * Es ideal para HMIs sencillos o de nivel de máquina, paneles locales y proyectos donde se requiera un desarrollo rápido sin salir del entorno de programación del PLC.
   * Cuenta con elementos estándar de control (botones, barras, histogramas, alarmas, y gestión de usuarios básica). [1, 2, 3] 

## 2. TwinCAT 3 HMI (La nueva generación basada en Web)
Es la plataforma de visualización moderna y avanzada de Beckhoff, orientada a arquitecturas modulares, multidispositivo y de alta personalización. [4, 5] 

* Cómo se denomina: Se le conoce comercialmente como TwinCAT 3 HMI. El entorno de ingeniería se integra en Visual Studio (como un tipo de proyecto independiente al del PLC) y su arquitectura se basa en el TwinCAT 3 HMI Server (TF2000). [5, 6] 
* Posibilidades y características:
* Tecnología Web Estándar: Está desarrollado sobre tecnologías estándar como HTML5, JavaScript y CSS. Aunque se diseña de manera visual mediante "arrastrar y soltar", permite añadir código personalizado y animaciones CSS avanzadas.
   * Independencia de plataforma: Al ser 100% web, cualquier dispositivo con un navegador moderno (smartphones, tablets, paneles de operador de cualquier marca) puede visualizar el HMI de forma responsiva sin necesidad de instalar plugins.
   * Arquitectura Cliente-Servidor: El servidor de HMI puede comunicarse simultáneamente con múltiples PLCs (mediante el protocolo ADS de Beckhoff u OPC UA) y servir la interfaz a múltiples pantallas de forma independiente.
   * Extensibilidad y Soluciones Específicas: Ofrece gran flexibilidad para layouts complejos, gráficos dinámicos avanzados y extensiones específicas de la industria, como los paquetes recientes CNC HMI Base (TF5310) para interfaces avanzadas de control numérico con simulación 3D en tiempo real. [1, 5, 7, 8] 

------------------------------
## Resumen comparativo rápido

| Característica | TwinCAT 3 PLC HMI (TF1800) | TwinCAT 3 HMI (TF2000) |
|---|---|---|
| Tecnología base | Gráficos nativos de PLC (CODESYS) | HTML5, CSS y JavaScript |
| Ubicación del proyecto | Integrado dentro del proyecto de PLC | Proyecto independiente en Visual Studio |
| Complejidad del diseño | Baja-Media (Rápido y estructurado) | Alta (Altamente personalizable y corporativo) |
| Enfoque principal | Control local a pie de máquina | Sistemas multidispositivo, SCADAs y Web corporativa |

(Nota: Adicionalmente, gracias al protocolo abierto TwinCAT ADS, TwinCAT 3 ofrece la posibilidad de desarrollar HMI externos utilizando cualquier lenguaje de programación de terceros como C#, .NET, C++, o frameworks web como React/Angular, comunicándose directamente con las variables del PLC). [1] 
Si estás evaluando cuál utilizar para un proyecto, ¿podrías comentarme si el HMI se ejecutará en la misma pantalla del PC Industrial o si necesitas acceso remoto desde tablets/móviles? Así te puedo orientar sobre cuál te conviene licenciar.

[1] [https://www.reddit.com](https://www.reddit.com/r/PLC/comments/1ft1mqc/best_way_to_develop_hmi_for_beckhoff/?tl=es-es)
[2] [https://es.scribd.com](https://es.scribd.com/document/745815606/TwinCAT-PLC-HMI-Rev01)
[3] [https://industrialmonitordirect.com](https://industrialmonitordirect.com/es/blogs/knowledgebase/beckhoff-twincat-hmi-visualization-tutorial-for-beginners)
[4] [https://www.beckhoff.com](https://www.beckhoff.com/es-mx/support/training-offerings/tr7050/)
[5] [https://www.stech.es](https://www.stech.es/es/noticias/beckhoff-amplia-twincat-3-con-componentes-hmi-especificos-para-cnc-y-simulacion-integrada-en-tiempo-real)
[6] [https://www.beckhoff.com](https://www.beckhoff.com/es-es/support/training-offerings/twincat-hmi/)
[7] [https://www.youtube.com](https://www.youtube.com/watch?v=t76O2Fthrzc&t=112)
[8] [https://infoplc.net](https://infoplc.net/noticias/beckhoff-1/componentes-twincat-hmi-interfaces-usuario-especificas-cnc)

--->