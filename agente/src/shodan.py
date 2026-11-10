"""Herramienta para consultar Shodan InternetDB.

Reglas que cumple:
- Sin shell: utiliza peticiones HTTPS.
- Con tiempo máximo.
- Salida recortada.
- Errores como texto.
"""

import json
import socket
import urllib.request
import urllib.error

from guard import protegida

MAX_CARACTERES = 3000


def recortar(texto: str, maximo: int = MAX_CARACTERES) -> str:
    if len(texto) <= maximo:
        return texto
    return texto[:maximo] + f"\n[... recortado: {len(texto) - maximo} caracteres más]"


@protegida(objetivo="dominio")
def shodan_dominio(dominio: str) -> str:
    """Consulta Shodan InternetDB para obtener información pública
    de las direcciones IP asociadas a un dominio.
    """

    try:
        # Resolver el dominio para obtener sus direcciones IP.
        ips = sorted({
            resultado[4][0]
            for resultado in socket.getaddrinfo(
                dominio, None, type=socket.SOCK_STREAM
            )
        })

        if not ips:
            return "No se encontraron direcciones IP para el dominio."

        lineas = [f"Dominio: {dominio}"]

        for ip in ips[:10]:
            url = f"https://internetdb.shodan.io/{ip}"

            req = urllib.request.Request(
                url,
                headers={"User-Agent": "aap-recon/1.0"}
            )

            try:
                with urllib.request.urlopen(req, timeout=20) as r:
                    datos = json.load(r)

                lineas.append(f"\nIP: {ip}")

                puertos = datos.get("ports", [])
                lineas.append(
                    "Puertos: " + (", ".join(map(str, puertos)) if puertos else "Ninguno")
                )

                hostnames = datos.get("hostnames", [])
                if hostnames:
                    lineas.append("Hostnames: " + ", ".join(hostnames))

                etiquetas = datos.get("tags", [])
                if etiquetas:
                    lineas.append("Etiquetas: " + ", ".join(etiquetas))

                vulnerabilidades = datos.get("vulns", [])
                if vulnerabilidades:
                    lineas.append(
                        "Vulnerabilidades: " + ", ".join(vulnerabilidades)
                    )

            except urllib.error.HTTPError as e:
                if e.code == 404:
                    lineas.append(f"\nIP: {ip} - Sin información en InternetDB.")
                else:
                    lineas.append(f"\nIP: {ip} - Error HTTP {e.code}.")

        return recortar("\n".join(lineas))

    except socket.gaierror:
        return f"ERROR: no se pudo resolver el dominio {dominio}."

    except urllib.error.URLError as e:
        return f"ERROR: no se pudo conectar con Shodan: {e.reason}"

    except TimeoutError:
        return "ERROR: la consulta a Shodan superó el tiempo máximo."

    except Exception as e:
        return f"ERROR: no se pudo realizar la consulta: {e}"
