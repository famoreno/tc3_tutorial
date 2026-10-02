# Arquitectura de Diseño

## Introducción

> La **Arquitectura de Diseño de Automatización** es la estructura organizativa de alto nivel que define cómo se descompone un sistema de control en componentes más sencillos, qué responsabilidad tiene cada módulo, cómo se representan y encapsulan la lógica y los recursos físicos, y mediante qué reglas e interfaces se comunican e interactúan entre sí para resolver el problema global de automatización de forma escalable, mantenible y robusta.

Cada arquitectura representa un paradigma de diseño que proporciona un modelo mental de cómo abordar la resolución de la implementación de la lógica de control de un automatismo y aporta soluciones distintas sobre la **Descomposición y Modularidad**, la **Asignación de Responsabilidades**, el **Nivel de Abstracción y Encapsulamiento** y el **Flujo de Información y Control:**.

En este curso se presentan varias arquitecturas que representan diferentes paradigmas con distintos niveles o modelos de abstracción: nomolítico, estructurado, jerárquico y funcional.

1.  **Monolítica:** Código "espagueti", toda la lógica en un únicolugar. Fácil realizar, pero difícil de mantener.
2.  **Estructurada:** Primera aplicación del aforismo «divide y vencerás» al distribuir la lógica de control en tareas independientes.
3.  **Jerárquica:** Se introduce del estándar industrial (GEMMA), que permite separar la producción normal del modo de funcionamiento.
4.  **Funcional:** La lógica de control de organiza en unidades funcionales que representa objetos mecatrónicos complejos y fácilmente reutilizables.

A medida que se avanza por esta jerarquía de arquitecturas aumenta la complejidad y se añaden capas de abstracción. A medida que se avanza por esta jerarquía se favorece el mantenimiento, A medida que se avanza por esta jerarquía se dispone de mecanismos más potentes que permiten abordar problemas más complejos. A medida que se avanza por esta jerarquía la arquitectura favorece el mantenimiento, la reutilización, la escalabilidad, la seguridad, la prueba, la puesta en marcha, el trabajo en equipo,...

Con fines pedagógicos estas arquitecturas se presentan en una progresión metodológica de cuatro niveles, que permite evaluar el impacto de cada una de ellas sobre el desarrollo de la lógica de control de un automatismo industrial.

---

## Arquitectura Monolítica

---

## Arquitectura Estructurada

---

## Arquitectura Jerárquica

---

## Arquitectura Funcional

---

<!---
Cuando enseño a programar plc con twincat utilizo una jerarquia de aproximaciones al problema de codificación de la lógica de control en los lenguajes de la norma iec 61131-3 que denomino jerarquías: monolítica (todo la lógica en un único grafcet, en un único fb), estructurada (la lógica se divide en grafcet de tareas y un grafcet coordinador de tareas, cada grafcet se corresponde con un fb en sfc), jerárquica (se introduce un elemento grafcet director a partir del gráfico GDMMA tras la aplicación de la guía gemma, que se corresponde con un FB  que codifica la correspondiente máquina de estados en ST) y finalmente funcional (en la que se pasa de "verbos/secuencias" a "objetos/unidades funcionales) en el que todo el sistemas se divide en unidades funcionales cada una de las cuales es responsable de una o varias secuencias y del "hardware" necesario para llevarlas a cabo, constituyendo cada unidad funcional un FB en ST que contiene un FB en SFC por cada secuencia, un FB en SFC para coordinar la ejecución de las secuencias,...)... es apropiado el nombre de estructura para referirse e estas formas de aproximación a la solución del problema de la automatización 

--->