# Terminología

## TwinCAT 3
### TwinCAT XAE
### TwinCAT XAR

## Proyecto TwinCAT 3

La arquitectura de TwinCAT 3 dentro de Visual Studio presenta 3 niveles:

```text
  (1) SOLUCIÓN DE VISUAL STUDIO (.sln)
   │
   └──(2) PROYECTO TWINCAT SYSTEM MANAGER (.tcproj)
       │
       └─ Configuración de Hardware, EtherCAT y Tareas de Tiempo Real
           ├─ Licencias y Target System
           │
           └──(3) PROYECTO PLC (.plcproj)
               ├─ Código fuente IEC 61131-3 (POUs, GVLs, FBs)
               └─ Instancia de ejecución de código (Puerto 851)
```

1. **Solución Visual Studio** (.sln)
    - La solución es el contenedor principal dónde se agrupan y organizan todos los proyectos independientes que conforman el sistema.
    - Permite agrupar en ún mismo entorno proyectos de distinta naturaleza (C#, TwinCAT, HMI, ...).

2. **Proyecto TwinCAT** (.tcproj)
    - El proyecto TwinCAT contine la arquitectura del sistema TwinCAT.
    - Permite agrupar varios proyectos TwinCAT de diferente tipo (PLC, HMI Web, Safety,...).
    - Gestiona la configuración hardware del sistema:
        - System/Target: distribución de núcleos tiempo real.
        - Licencias
        - I/O: topología del bus EtherCAT (terminales, servos, ...).
        - Motion/NC/CNC: configuración de ejes (movimientos, codificadores, drivers,... )
        - Mapeo (`Linking`): tabla de vinculaciones de variables y canales de E/S.

3. **Proyecto PLC** (.plcproj)
    - El proyecto PLC contiene del código fuente de la lógica de control del sistemas según el estándar IEC 61131-3.
        - Módulos con el código del proyecto, denominados Unidades de Organización de Programas (POUs).
        - Tipos de datos de usuario (DUTs)
        - Lista de variables globales (GLV)
        - Interfaces gráficos integrados, denomindas visualizaciones (VISUs).
