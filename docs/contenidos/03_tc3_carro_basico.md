# 🛒 Carro Básico (TwinCAT 3)

## 📝 Descripción Funcional

El proyecto **Carro Básico** resuelve el clásico problema de automatización conocido como **««el carro va y viene»»**, que consiste en un móvil que se desplaza longitudinalmente entre los dos extremos (izquierdo y derecho) de un tramo de vía.

![Esquemático del Carro Básico](../images/03_tc3_carro_basico/Carro_Basico_Esquematico.png){ style="display: block; margin: 0 auto; width: 300px;" }

<!-- <figcaption>Figura 1: Representación Esquemática.</figcaption> -->

### Parte Operativa

- Un **motor** con dos señales de mando para la marcha (marcha y marcha).
- Un par de **sensores finales de carrera** (izquierdo y derecho).

### Parte de Relación
 
 Consiste en un panel de operador básico compuesto únicamente por:

- Un **pulsador de marcha**, para iniciar el funcionamiento.
- Una **lámpara de marcha**, para indicar el estado del sistema.

## Descripción del proceso

El funcionamiento del carro básico es como sigue.

1.  El carro se pone en marcha hacia la derecha cuando se acciona el pulsador de marcha.
2.  Cuando el carro alcanza el final de carrera derecha invierte el sentido de la marcha.
3.  El carro se detiene al alcanzar, de nuevo, el final de carrera izquierda.

- **Condición inicial**: carro detenido sobre el final de carrera izquierda.

## Modalidades

El proyecto contempla diferentes variantes de complejidad progresiva:

1. **Carro pulsado**. El carro inicia un viaje de ida y vuelta, únicamente, cuando estando en su posición inicial se acciona el pulsador de marcha.
1. **Carro temporizado**. El carro se detiene durante un determinado tiempo ($T_{espera}$) sobre el final de carrera derecha antes de iniciar el camino de regreso hacia su posición inicial.
2. **Carro limitado**. El carro realiza un determinado número de viajes consecutivos de ida y vuelta (tarea) cada vez que, estando en su posición inicial, se acciona el pulsador de marcha.
3. **Carro señalizado**. La lámpara de marcha se enciende de forma permanente para indicar que el carro está en funcionamiento y parpadea para indicar que el carro está en reposo.

## ⇄ Entradas y salidas

| Nombre | Tipo | Origen | Descripción |
| :--- | :--- | :--- | :--- |
| `PM` | `BOOL` | Entrada | Pulsador de Marcha |
| `FCI` | `BOOL` | Entrada | Final de Carrera Izquierda |
| `FCD` | `BOOL` | Entrada | Final de Carrera Derecha |
| `LM` | `BOOL` | Salida | Lámpara de Marcha |
| `MI` | `BOOL` | Salida | Marcha Izquierda |
| `MD` | `BOOL` | Salida | Marcha Derecha |

---

## 📄 Especificación funcional

Las siguientes especificaciones funcionales describen el comportamiento del carro (lógica de control) de una manera precisa utilizando los **Diagramas de Relés y Contactos** y el lenguaje **GRAFCET**.

- [Diagrama de relés y contactos (PDF)](../../pdfs/Carro_Basico_DRC_Final.pdf)
- [Diagrama grafcet (PDF)](../../pdfs/Carro_Basico_GRF_Final.pdf)

---

## 📂 Estructura simplificada del repositorio

```text
TC3_Carro_Basico/
├── docs/
|   └── diagrams/
│       ├── Carro_Basico_DRC.pdf   <-- Diagrama de Relés y Contactos (PDF)
│       └── Carro_Basico_GRF.pdf   <-- Diagrama Grafcet (PDF)
└── src/
    ├── TC3_Carro_Basico.sln       <-- Solución de Visual Studio (TwinCAT XAE)
    └── TC3_Carro_Basico/          <-- Proyecto TwinCAT
        └── Carro_Basico_PLC/      <-- Proyecto PLC
```

--- 

## 💻 Implementación

Se implementa el funcionamiento del carro va y viene (pulsado, temporizado, limitado y señalizado), a partir de sus especificaciones (diagramas de relés y diagramas grafcet) utilizando diferentes lenguajes de programación de la norma IEC 61131-3: *Diagrama Ladder* (LD), *Sequential Function Chart* ({{SFC}}) y *Structured Text* ({{ST}}).

- DRC → [LD]
- GRF → [SFC / ST / LD]

---

## 📦 Código Fuente y Descarga

El código fuente completo de este proyecto **Carro Básico**, está disponible en GitHub:

- :material-github: **GitHub:** [`vetorres-uma/TC3_Carro_Basico`](https://github.com/vetorres-uma/TC3_Carro_Basico)
- :material-github: **GitHub:** [:material-download: Descarga directa `.zip`](https://github.com/vetorres-uma/TC3_Carro_Basico/archive/refs/heads/main.zip)

También puede descargarse el archivo comprimido de la solución (tnzip) del proyecto desde el siguiente repositorio:

- :material-google-drive: **Google Drive:** [:material-download: Descargar `.tnzip`](https://drive.google.com/file/d/1-Gh4Smocq3HyR27G86v25gKdr8F6hRN4/view?usp=drive_link)
