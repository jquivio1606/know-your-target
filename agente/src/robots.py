"""Herramienta para consultar el archivo robots.txt.

Reglas que cumple:
- Una herramienta, una tarea.
- Sin shell: utiliza peticiones HTTPS/HTTP.
- Con tiempo máximo.
- Salida recortada.
- Errores como texto.
"""

import urllib.request
import urllib.error

from guard import protegida

MAX_CARACTERES = 3000


def recortar(texto: str, maximo: int = MAX_CARACTERES) -> str:
    if len(texto) <= maximo:
        return texto
    return texto[:maximo] + f"\n[... recortado: {len(texto) - maximo} caracteres más]"


@protegida(objetivo="dominio")
def robots_txt(dominio: str) -> str:
    """Consulta el archivo robots.txt de un dominio."""

    try:
        dominio = dominio.rstrip("/")
        errores = []

        for protocolo in ["https", "http"]:
            url = f"{protocolo}://{dominio}/robots.txt"

            req = urllib.request.Request(
                url,
                headers={"User-Agent": "aap-recon/1.0"}
            )

            try:
                with urllib.request.urlopen(req, timeout=20) as r:
                    contenido = r.read(10000).decode("utf-8", "replace")

                if contenido.strip():
                    return recortar(f"URL: {url}\n\n{contenido}")

                return f"El archivo robots.txt de {dominio} está vacío."

            except urllib.error.HTTPError as e:
                if e.code == 404:
                    errores.append(f"{protocolo}: archivo no encontrado (404).")
                else:
                    errores.append(f"{protocolo}: error HTTP {e.code}.")

            except urllib.error.URLError as e:
                errores.append(f"{protocolo}: {e.reason}")

        return "No se pudo consultar robots.txt:\n" + "\n".join(errores)

    except TimeoutError:
        return "ERROR: la consulta de robots.txt superó el tiempo máximo."

    except Exception as e:
        return f"ERROR: no se pudo consultar robots.txt: {e}"