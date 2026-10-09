---
icon: fontawesome/solid/sitemap
---

# :fontawesome-solid-sitemap: Arquitecturas de Diseño

---

## :fontawesome-solid-circle-info: Introducción

> Las **Arquitecturas de Diseño para la Automatización** son las estructuras organizativas de alto nivel que definen cómo se descompone un sistema de control en componentes más sencillos, qué responsabilidad tiene cada módulo, cómo se representan y encapsulan la lógica y los recursos físicos, y mediante qué reglas e interfaces se comunican e interactúan entre sí para resolver el problema global de automatización de un determinado sistema de forma escalable, mantenible y robusta.

Cada arquitectura representa un paradigma de diseño que proporciona el modelo mental de cómo abordar la resolución de la implementación de la lógica de control de un automatismo y aporta soluciones distintas sobre la **Descomposición y Modularidad**, la **Asignación de Responsabilidades**, el **Nivel de Abstracción y Encapsulamiento** y el **Flujo de Información y Control**.

En este tutorial se presentan las siguientes arquitecturas que representan diferentes paradigmas con distintos niveles o modelos de abstracción:

1.  **Monolítica:** código "espagueti", toda la lógica en un único lugar. Fácil realizar, pero difícil de mantener.
2.  **Estructurada:** primera aplicación del aforismo «divide y vencerás», se distribuye la lógica de control en diferentes tareas independientes.
3.  **Jerárquica:** se introduce del estándar industrial (GEMMA), que permite separar la producción normal del modo de funcionamiento.
4.  **Funcional:** la lógica de control de organiza en unidades funcionales que representan objetos mecatrónicos complejos, pero fácilmente reutilizables.

 > - A medida que se avanza por esta jerarquía de arquitecturas, **aumenta la complejidad** y se añaden capas de abstracción.
 > - A medida que se avanza por esta jerarquía, **se favorece el mantenimiento**.
 > - A medida que se avanza por esta jerarquía, se dispone de **mecanismos más potentes** que permiten abordar problemas más complejos.
 > - A medida que se avanza por esta jerarquía, se favorecen los **pilares fundamentales** del mantenimiento, la reutilización, la escalabilidad, la seguridad, la prueba, la puesta en marcha, el trabajo en equipo,...

Con fines pedagógicos estas arquitecturas se presentan en una progresión metodológica de cuatro niveles, que permite evaluar el impacto y las limitaciones de cada una de ellas sobre el desarrollo de la lógica de control de un automatismo industrial.

---

## :fontawesome-solid-cube: Arquitectura Monolítica

> La arquitectura monolítica consiste en especificar toda la lógica de control en un único diagrama, en codificar todo el comportamiento del sistema en un único módulo.

Evidentemente, esta aproximación presenta algunas ventajas iniciales:

- **Simplicidad inicial:** al estar todo el código en un único módulo, evidentemente no es necesario invertir ningún esfuerzo en estructurar el código en diferentes módulos, ni en elaborar los en interfaces entre módulos.
- **Rapidez de despliegue:** permite obtener resultados funcionales en pruebas de concepto o en sistemas de alcance limintado de forma rápida.
- **Menor sobrecarga conceptual:** al estar todo el código en un único módulo, al no existir abstracción ninguan, se puede seguir la evolución del estado del sistema con un esfuerzo mínimo.

Sin embargo, también presenta inconvenientes importantes, especialmente a medida que la dimensión del sistema a controlar o la funcionalidad requerida aumentan:

- **Escalabilidad reducida:** si el módulo se vuelve demasiado grande, resultando inmanejable y difícil de mantener.
- **Limitaciones funcionales**: en un único módulo puede resultar difícil o incluso imposible introducir funcionalidades avanzadas (gestión de fallos, paradas, etc.).
- **Imposibilidad de reutilización:** al estar toda la lógica de control en un único modulo la reutilzación es simplemente imposible.
- **Complejidad en la depuración:** cualquier error afecta lógicamente a todo el sistema.
- **Efectos secundarios inesperados:** Un cambio menor en una línea de código puede alterar el comportamiento de secciones no relacionadas dentro del mismo ciclo de ejecución.

!!! warning "Conclusión y Buenas Prácticas"
    La arquitectura monolítica solo es aconsejable en sistemas didácticos básicos o automatismos extremadamente sencillos. Tan pronto como el sistema se vuelve algo más complejo o requiera más de un modo de funcionamiento,... debe adoptarse una arquitectura con mayor potencial como la estructurada o la jerárquica.

---

## :fontawesome-solid-boxes-stacked: Arquitectura Estructurada

--8<-- "snippets/avisos.md:seccion-en-construccion"

---

## :fontawesome-solid-diagram-project: Arquitectura Jerárquica

--8<-- "snippets/avisos.md:seccion-en-construccion"

---

## :fontawesome-solid-puzzle-piece: Arquitectura Funcional

--8<-- "snippets/avisos.md:seccion-en-construccion"

---

<!---
Cuando enseño a programar plc con twincat utilizo una jerarquia de aproximaciones al problema de codificación de la lógica de control en los lenguajes de la norma iec 61131-3 que denomino jerarquías: monolítica (todo la lógica en un único grafcet, en un único fb), estructurada (la lógica se divide en grafcet de tareas y un grafcet coordinador de tareas, cada grafcet se corresponde con un fb en sfc), jerárquica (se introduce un elemento grafcet director a partir del gráfico GDMMA tras la aplicación de la guía gemma, que se corresponde con un FB  que codifica la correspondiente máquina de estados en ST) y finalmente funcional (en la que se pasa de "verbos/secuencias" a "objetos/unidades funcionales) en el que todo el sistemas se divide en unidades funcionales cada una de las cuales es responsable de una o varias secuencias y del "hardware" necesario para llevarlas a cabo, constituyendo cada unidad funcional un FB en ST que contiene un FB en SFC por cada secuencia, un FB en SFC para coordinar la ejecución de las secuencias,...)... es apropiado el nombre de estructura para referirse e estas formas de aproximación a la solución del problema de la automatización

--->
