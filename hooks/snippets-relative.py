# import re
# import posixpath

# def on_page_markdown(markdown, *, page, config, files):
#     """
#     Convierte las rutas de inclusión relativas al documento actual
#     (--8<-- "./ruta/archivo.md") en rutas relativas a la raíz del proyecto,
#     para que pymdownx.snippets las resuelva con base_path=["."].
#     """
#     # Patrón para detectar --8<-- "./algo" o --8<-- './algo'
#     pattern = r'(--8<--\s*["\'])(\./[^"\']+)(["\'])'

#     def replacer(match):
#         prefix = match.group(1)   # '--8<-- "'
#         rel_path = match.group(2) # './includes/sobre-simulador.md'
#         suffix = match.group(3)   # '"'

#         # Directorio del archivo Markdown actual (relativo a docs/)
#         page_dir = posixpath.dirname(page.file.src_uri)  # ej: 'contenidos/ejemplos/hola-mundo'

#         # Convertir './includes/...' -> 'docs/contenidos/ejemplos/hola-mundo/includes/...'
#         # (se normaliza para eliminar '..' y '.' innecesarios)
#         new_path = posixpath.normpath(
#             posixpath.join("docs", page_dir, rel_path)
#         )

#         return f"{prefix}{new_path}{suffix}"

#     return re.sub(pattern, replacer, markdown)

import re
import posixpath
import os


def on_page_markdown(markdown, *, page, config, files):
    docs_dir = config.get("docs_dir", "docs")
    if os.path.isabs(docs_dir):
        docs_dir = os.path.relpath(docs_dir, os.getcwd())
    docs_dir = docs_dir.replace(os.sep, "/").rstrip("/")

    pattern = re.compile(r'(--8<--\s*["\'])(\./[^"\']+)(["\'])')
    page_dir = posixpath.dirname(page.file.src_uri)

    def replacer(match):
        prefix, rel_path, suffix = match.group(1), match.group(2), match.group(3)
        new_path = posixpath.normpath(
            posixpath.join(docs_dir, page_dir, rel_path)
        )
        return f"{prefix}{new_path}{suffix}"

    return pattern.sub(replacer, markdown)
