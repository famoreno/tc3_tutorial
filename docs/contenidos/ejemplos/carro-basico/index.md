---
title: Carro Básico - Descripción
icon: fontawesome/solid/cart-shopping
---

# :fontawesome-solid-cart-shopping: Carro Básico

## :fontawesome-solid-file-lines: Descripción

El proyecto **Carro Básico** es una adaptación del clásico problema de automatización conocido como **«el carro va y viene»**, que consiste en un móvil que se desplaza longitudinalmente entre los dos extremos (izquierdo y derecho) de un tramo de vía.

![Esquemático del Carro Básico](./img/carro-basico-esquematico.png){ width="300px" .image-centered }
<figcaption>Figura 1: Representación Esquemática.</figcaption>

### Parte Operativa

- Un **motor** con dos señales de mando para controlar su movimiento:  **marcha derecha** y **marcha izquierda**.
- Un par de sensores:  **final de carrera izquierdo** y **final de carrera derecho**.

### Parte de Relación

 Consiste en un panel de operador básico compuesto únicamente por:

- Un **pulsador de marcha**, para iniciar el funcionamiento.
- Una **lámpara de marcha**, para indicar el estado del sistema.

## :fontawesome-solid-gear: Descripción Funcional

El funcionamiento básico del carro es como sigue.

1.  El carro se pone en marcha hacia la derecha cuando se acciona el pulsador de marcha.
2.  Cuando el carro alcanza el final de carrera derecha, invierte el sentido de la marcha.
3.  El carro se detiene al alcanzar, de nuevo, el final de carrera izquierdo.

**Condición inicial**: carro detenido sobre el final de carrera izquierdo.

## :fontawesome-solid-layer-group: Modalidades

El proyecto contempla diferentes variantes de complejidad progresiva.

1.  **Carro pulsado**. El carro inicia un viaje de ida y vuelta, únicamente, cuando estando en su posición inicial se acciona el pulsador de marcha.
2.  **Carro temporizado**. El carro se detiene durante un determinado tiempo ($T_{espera}$) sobre el final de carrera derecho antes de iniciar el camino de regreso hacia su posición inicial.
3.  **Carro limitado**. El carro realiza un determinado número de viajes consecutivos de ida y vuelta (tarea) cada vez que, estando en su posición inicial, se acciona el pulsador de marcha.
4.  **Carro señalizado**. La lámpara de marcha se enciende de forma permanente para indicar que el carro está en funcionamiento y parpadea para indicar que el carro está en reposo.

## :fontawesome-solid-arrows-left-right: Entradas y Salidas

| Nombre | Tipo | Origen | Descripción |
| :---: | :---: | :---: | :--- |
| `PM` | `Binario` | Entrada | Pulsador de Marcha |
| `FCI` | `Binario` | Entrada | Final de Carrera Izquierda |
| `FCD` | `Binario` | Entrada | Final de Carrera Derecha |
| `LM` | `Binario` | Salida | Lámpara de Marcha |
| `MI` | `Binario` | Salida | Marcha Izquierda |
| `MD` | `Binario` | Salida | Marcha Derecha |

---

## :fontawesome-solid-brain: Especificación Funcional

Las siguientes especificaciones funcionales describen el comportamiento del carro (lógica de control) de una manera precisa utilizando **Diagramas de Relés y Contactos** y lenguaje **GRAFCET**.

- [Diagrama de relés y contactos (PDF).](./pdf/carro_basico_drc.pdf)
- [Diagrama GRAFCET (PDF).](./pdf/carro_basico_grf.pdf)

---

## :fontawesome-solid-folder-tree: Estructura Simplificada del Repositorio

```text
TC3_Carro_Basico/
├── docs/
|   └── diagrams/
│       ├── Carro_Basico_DRC.pdf <-- Diagrama de Relés y Contactos (PDF)
│       └── Carro_Basico_GRF.pdf <-- Diagrama Grafcet (PDF)
└── src/
    ├── TC3_Carro_Basico.sln     <-- Solución de Visual Studio (TwinCAT XAE)
    └── TC3_Carro_Basico/        <-- Proyecto TwinCAT
        └── Carro_Basico_PLC/    <-- Proyecto PLC
```

---

## :fontawesome-solid-screwdriver-wrench: Implementación

Se implementa el funcionamiento del carro va y viene (pulsado, temporizado, limitado y señalizado), a partir de sus especificaciones (diagrama de relés y diagrama grafcet) utilizando diferentes lenguajes de programación de la norma IEC 61131-3: *Diagrama Ladder* ({{LD}}), *Sequential Function Chart* ({{SFC}}) y *Structured Text* ({{ST}}).

- DRC ➔ [LD]
- GRF ➔ [SFC / ST / LD]

!!! info "Guía de implementación"
    Para implementar  este proyecto desde cero en TwinCAT 3, seguir la **[Guía de implementación](step-by-step.md)**.

---

## :fontawesome-solid-download: Código Fuente y Descarga

El código fuente completo de este proyecto **Carro Básico**, está disponible en GitHub:

- :simple-github: **Repositorio:** [:material-link-variant: vetorres-uma/TC3_Carro_Basico](https://github.com/vetorres-uma/TC3_Carro_Basico)
- :simple-github: **Descargar:** [:material-download: Archivo fuente `.zip`](https://github.com/vetorres-uma/TC3_Carro_Basico/archive/refs/heads/main.zip)

Los miembros de la **Universidad de Málaga**, también pueden descargarse el archivo comprimido de la solución (tnzip) del proyecto desde el siguiente repositorio:

- :simple-googledrive: **Descargar:** [:material-download: Solución comprimida `.tnzip`](https://drive.google.com/file/d/1-Gh4Smocq3HyR27G86v25gKdr8F6hRN4/view?usp=drive_link)

---
