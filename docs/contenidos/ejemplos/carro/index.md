---
title: Carro - Descripción
icon: fontawesome/solid/cart-shopping
---

# :fontawesome-solid-cart-shopping: Carro

## :fontawesome-solid-file-lines: Presentación

El proyecto **Carro** es una adaptación del clásico problema de automatización conocido como **«el carro va y viene»**, que básicamente consiste en un móvil que se desplaza longitudinalmente entre los dos extremos (izquierdo y derecho) de un tramo de vía.

![Esquemático del Carro](./img/carro-esquematico.png){ width="300px" .image-centered }
<figcaption>Figura 1: Representación Esquemática.</figcaption>

## Elementos Constituyentes

### Parte Operativa

- Un **motor** con dos señales de mando para la marcha (izquierda y derecha).
- Un par de **sensores finales de carrera** (izquierdo y derecho) para determinar su posición.

### Parte de Relación

Consiste en un panel de operador básico compuesto únicamente por:

- Un **pulsador de marcha**, para iniciar el funcionamiento.
- Una **lámpara de marcha**, para indicar el estado del sistema.

## :fontawesome-solid-gear: Descripción Funcional

El funcionamiento del **carro básico** es como sigue.

1. El carro se pone en marcha hacia la derecha cuando se acciona el pulsador de marcha.
2. Cuando el carro alcanza el final de carrera derecho, invierte el sentido de la marcha.
3. El carro se detiene al alcanzar, de nuevo, el final de carrera izquierdo.

**Condición inicial**: carro detenido sobre el final de carrera izquierdo.

## :fontawesome-solid-layer-group: Modalidades

El proyecto contempla diferentes variantes de complejidad progresiva.

1. **Carro Pulsado**. El carro inicia un viaje de ida y vuelta únicamente cuando, estando en su posición inicial, se realiza una pulsación sobre el pulsador de marcha.
2. **Carro Temporizado**. El carro se detiene durante un tiempo determinado ($T_{espera}$) sobre el final de carrera derecho antes de iniciar el regreso a su posición inicial.
3. **Carro limitado**. El carro realiza un determinado número de viajes de ida y vuelta (tarea) consecutivos cada vez que, estando en su posición inicial, se acciona el pulsador de marcha.
4. **Carro Señalizado**. La lámpara de marcha permanece encendida mientras el carro está en funcionamiento y parpadea cuando está en reposo.

## :fontawesome-solid-arrows-left-right: Entradas y Salidas

| Etiqueta | Tipo | Dirección | Descripción |
| :---: | :---: | :---: | :--- |
| `PM` | `Binario` | Entrada | Pulsador de Marcha |
| `FCI` | `Binario` | Entrada | Final de carrera izquierdo |
| `FCD` | `Binario` | Entrada | Final de carrera derecho |
| `LM` | `Binario` | Salida | Lámpara de Marcha |
| `MI` | `Binario` | Salida | Marcha Izquierda |
| `MD` | `Binario` | Salida | Marcha Derecha |

---

## :fontawesome-solid-brain: Especificación Funcional

Las siguientes especificaciones funcionales describen con precisión el comportamiento del carro (lógica de control) mediante **Diagramas de Relés y Contactos** y el lenguaje **GRAFCET**.

- :fontawesome-solid-file-pdf: [Diagrama de relés y contactos](./pdf/carro-drc.pdf).
- :fontawesome-solid-file-pdf: [Diagrama GRAFCET](./pdf/carro-grf.pdf).

---

## :fontawesome-solid-folder-tree: Estructura Simplificada del Repositorio

```text
TC3_Carro/
├── docs/
│   └── diagrams/
│       ├── carro-drc.pdf <-- Diagrama de Relés y Contactos (PDF)
│       └── carro-grf.pdf <-- Diagrama Grafcet (PDF)
└── src/
    ├── TC3_Carro.sln     <-- Solución de Visual Studio (TwinCAT XAE)
    └── TC3_Carro/        <-- Proyecto TwinCAT
        └── Carro_PLC/    <-- Proyecto PLC
```

---

## :fontawesome-solid-screwdriver-wrench: Implementación

El funcionamiento del carro va y viene (básico, pulsado, temporizado, limitado y señalizado) se implementa a partir de sus especificaciones (diagramas de relés y GRAFCET) mediante los lenguajes de programación de la norma **IEC 61131-3**: *Diagrama Ladder* ({{LD}}), *Sequential Function Chart* ({{SFC}}) y *Structured Text* ({{ST}}).

- DRC ➔ \[LD\]
- GRF ➔ \[SFC / ST / LD\]

!!! info "Paso a paso"
    Aprende a crear este proyecto desde cero en TwinCAT 3 siguiendo su **guía de implementación**. [:material-arrow-right-bold-box:](step-by-step.md)

---

## :fontawesome-solid-download: Código Fuente y Descarga

El código fuente completo de este proyecto está disponible en GitHub:

- :simple-github: **Repositorio:** [:material-link-variant: vetorres-uma/TC3_Carro](https://github.com/vetorres-uma/TC3_Carro)
- :simple-github: **Descargar:** [:material-download: archivo fuente `.zip`](https://github.com/vetorres-uma/TC3_Carro/archive/refs/heads/main.zip)

Los miembros de la **Universidad de Málaga** también pueden descargar el archivo comprimido de la solución (`.tnzip`) del proyecto desde el siguiente repositorio:

- :simple-googledrive: **Descargar:** [:material-download: solución comprimida `.tnzip`](https://drive.google.com/file/d/1-Gh4Smocq3HyR27G86v25gKdr8F6hRN4/view?usp=drive_link)

---
