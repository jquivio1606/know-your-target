"""Herramienta para consultar security.txt.

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
def security_txt(dominio: str) -> str:
    """Busca y consulta security.txt en las ubicaciones habituales."""

    try:
        dominio = dominio.rstrip("/")
        rutas = [
            "/.well-known/security.txt",
            "/security.txt"
        ]

        errores = []

        for protocolo in ["https", "http"]:
            for ruta in rutas:
                url = f"{protocolo}://{dominio}{ruta}"

                req = urllib.request.Request(
                    url,
                    headers={"User-Agent": "aap-recon/1.0"}
                )

                try:
                    with urllib.request.urlopen(req, timeout=20) as r:
                        contenido = r.read(10000).decode("utf-8", "replace")

                    if contenido.strip():
                        return recortar(
                            f"Archivo encontrado: {url}\n\n{contenido}"
                        )

                    errores.append(f"{url}: archivo vacío.")

                except urllib.error.HTTPError as e:
                    if e.code == 404:
                        errores.append(f"{url}: no existe (404).")
                    else:
                        errores.append(f"{url}: error HTTP {e.code}.")

                except urllib.error.URLError as e:
                    errores.append(f"{url}: {e.reason}")

        return (
            f"No se encontró un security.txt accesible para {dominio}.\n"
            + "\n".join(errores)
        )

    except TimeoutError:
        return "ERROR: la consulta de security.txt superó el tiempo máximo."

    except Exception as e:
        return f"ERROR: no se pudo consultar security.txt: {e}"