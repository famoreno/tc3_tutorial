# Tutorial de TwinCAT 3

Este repositorio contiene la documentación y los materiales del tutorial de TwinCAT 3, organizado como un sitio web estático con MkDocs y el tema Material for MkDocs.

## Descripción

El proyecto documenta conceptos, ejemplos y prácticas para trabajar con TwinCAT 3, incluyendo:

- fundamentos y presentación del ecosistema Beckhoff
- conceptos generales de programación y configuración
- ejecución y puesta en marcha de programas
- lenguajes de implementación
- ejemplos de automatización
- prácticas guiadas y proyectos de referencia

## Estructura del repositorio

- `mkdocs.yml`: configuración principal de MkDocs y navegación del sitio.
- `main.py`: script de soporte asociado al proyecto.
- `README.md`: documentación general del repositorio.
- `docs/`: contenido de la documentación.
  - `index.md`: página de inicio del tutorial.
  - `contenidos/`: módulos, capítulos y materiales didácticos.
  - `images/`: recursos gráficos e ilustraciones.
  - `javascripts/`: scripts personalizados para la web.
  - `stylesheets/`: estilos personalizados.
  - `overrides/`: personalización del tema Material.
  - `pdfs/`: documentos PDF generados o almacenados.
- `.github/`: configuración y automatizaciones del repositorio.
- `.gitignore`: reglas de exclusión de Git.

## Requisitos

Necesitarás Python 3 y las dependencias de MkDocs:

```bash
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install mkdocs mkdocs-material mkdocs-macros-plugin mkdocs-include-markdown-plugin
```

## Cómo visualizar la documentación localmente

1. Entra al directorio del proyecto.
2. Ejecuta el servidor de MkDocs:

   ```bash
   mkdocs serve
   ```

3. Abre en tu navegador:

   ```bash
   http://localhost:8000
   ```

## Cómo compilar el sitio

Para generar la versión estática del sitio:

   ```bash
   mkdocs build
   ```

El resultado se genera normalmente en la carpeta `site/`.

## Organización del contenido

La documentación está dividida en varias secciones:

- Presentación y contexto general
- Conceptos básicos de TwinCAT 3
- Ejecución de programas
- Lenguajes de implementación
- Ejemplos prácticos
- Casos de uso y prácticas
- Proyectos estructurados, monolíticos y jerárquicos

## Contribuciones

Las contribuciones son bienvenidas. Si quieres mejorar el contenido, corregir errores o añadir nuevos ejemplos, puedes abrir un *issue* o enviar un pull request.

---

© 2026 AutoISATeam TC3 Tutorial.
