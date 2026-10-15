# Tutorial de TwinCAT 3

Material didáctico para aprender y enseñar automatización industrial con TwinCAT 3. El tutorial combina fundamentos, procedimientos, ejemplos y prácticas, con referencias a los lenguajes IEC 61131-3 y a GRAFCET.

El contenido evoluciona de forma continua; algunas páginas pueden estar incompletas.

**Sitio publicado:** [Tutorial de TwinCAT 3](https://famoreno.github.io/tc3_tutorial/)

## Contenidos

La navegación del sitio se organiza en cuatro áreas:

- **Fundamentos:** conceptos, normas y arquitecturas de automatización.
- **Procedimientos:** flujos de trabajo para desarrollar con TwinCAT 3.
- **Ejemplos:** soluciones guiadas y acotadas.
- **Prácticas:** retos y proyectos para aplicar lo aprendido.

Consulta el [índice del tutorial](docs/index.md) para explorar las páginas disponibles. La estructura y el estado de cada sección se reflejan en la navegación del sitio.

## Desarrollo local

Se necesita Python 3. Desde la raíz del repositorio, crea y activa un entorno virtual.

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux o macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instala las dependencias empleadas para publicar el sitio:

```bash
python -m pip install --upgrade pip
python -m pip install mkdocs mkdocs-material mkdocs-macros-plugin mkdocs-include-markdown-plugin mkdocs-git-revision-date-localized-plugin
```

Inicia el servidor de desarrollo:

```bash
mkdocs serve
```

Abre <http://127.0.0.1:8000/>. Para generar el sitio estático localmente, ejecuta `mkdocs build`; el resultado se guarda en `site/`, que no se versiona.

## Contribuir

Si encuentras un error o tienes una propuesta, puedes [abrir un issue](https://github.com/famoreno/tc3_tutorial/issues). Para enviar cambios, crea una rama y abre un *pull request*.

Antes de editar o enviar contenido, consulta [CONTRIBUTING.md](CONTRIBUTING.md), que reúne las convenciones editoriales, de estructura y de validación del proyecto.

---

## Licencia

- El código fuente PLC de los proyectos y los fragmentos IEC 61131-3 incluidos en la documentación, normalmente en bloques `iecst`, se distribuyen bajo la licencia **GNU General Public License, versión 3.0 (GPLv3)**.
- El texto explicativo y los recursos originales creados para el tutorial se distribuyen bajo la licencia **Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)**. Los bloques de código y los materiales de terceros quedan excluidos de esta licencia.

---

© 2026 AutoISATeam TC3 Tutorial.
