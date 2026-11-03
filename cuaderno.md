# Cuaderno de trabajo – Reconocimiento pasivo

**Fecha de trabajo:** 30/10/2026  
**Objetivo general:** `roblox.com`  
**Tipo de reconocimiento:** Pasivo.  
[**Alcance:** ./alcance.md](./alcance.md)

---

## 1. Consulta WHOIS

### Anotación 1 – Información de registro del dominio

- **Cuándo:** 30/10/2026, 17:27.
- **Objetivo:** `roblox.com` (alcance: pendiente de contrastar con el *scope* vigente).
- **Qué hice:** Consulté la información pública de registro del dominio mediante [Who.is](https://who.is/whois/roblox.com).
- **Qué salió:** La consulta identifica a Roblox Corporation como organización asociada al dominio. Indica como fecha de creación el 30/01/2004 y como fecha de expiración el 30/01/2027. También muestra información de direccionamiento IP y servidores de nombres.
- **Siguiente paso:** Contrastar los datos de registro y los servidores de nombres con ICANN Lookup.

## 2. ICANN Lookup

### Anotación 2 – Contraste de los datos del dominio

- **Cuándo:** 30/10/2026, 17:49.
- **Objetivo:** `roblox.com` (alcance: pendiente de contrastar con el *scope* vigente).
- **Qué hice:** Consulté el dominio en [ICANN Lookup](https://lookup.icann.org/en/lookup) para contrastar sus datos de registro.
- **Qué salió:** Coinciden las fechas de creación, actualización y expiración observadas en Who.is. La empresa registradora indicada es MarkMonitor Inc. y aparecen cuatro servidores de nombres: `nspx1.roblox.com`, `nspx2.roblox.net`, `nspx3.roblox.us` y `nspx4.roblox.co.uk`. ICANN muestra DNSSEC como «Unsigned».
- **Siguiente paso:** Comprobar los registros DNS del dominio con `dig` y revisar si la información sobre DNSSEC coincide con otras consultas.

## 3. Consultas DNS con dig

### Anotación 3 – Registros A, MX, NS y TXT

- **Cuándo:** 30/10/2026, 18:15.
- **Objetivo:** `roblox.com` (alcance: pendiente de contrastar con el *scope* vigente).
- **Qué hice:** Consulté distintos tipos de registros DNS mediante `dig +short`: A, MX, NS y TXT.
- **Qué salió:** El registro A consultado devolvió `128.116.102.3`. Los registros MX apuntan a servidores de Google. Los registros NS coinciden con los cuatro servidores de nombres vistos en ICANN. Los registros TXT incluyen información de SPF y verificaciones de servicios externos.
- **Siguiente paso:** Conservar únicamente los datos DNS relevantes para el reconocimiento y contrastar la información de DNSSEC con la obtenida en otras fuentes.

> Los valores completos de los registros TXT se omiten porque incluyen tokens de verificación que no son necesarios para explicar el resultado del reconocimiento.

## 4. Enumeración de subdominios con Subfinder

### Anotación 4 – Búsqueda de subdominios

- **Cuándo:** 30/10/2026, 18:34.
- **Objetivo:** Subdominios asociados a `roblox.com` (cada resultado debe comprobarse individualmente contra el *scope*).
- **Qué hice:** Ejecuté un script de Linux que utiliza `subfinder -d roblox.com -all -silent` para obtener subdominios y después comprueba sus registros DNS con `dig +short`. El script aplica un filtro para destacar nombres considerados interesantes. Archivo utilizado: `script-subfinder-subdominio.sh`.
- **Qué salió:** Se encontraron nombres relacionados con APIs, juegos, autenticación, desarrollo, moderación, documentación y distribución de contenido. Algunos resultados apuntan a infraestructuras externas, como Amazon CloudFront, Amazon S3 y Akamai. Otros nombres no devolvieron registros DNS.
- **Siguiente paso:** Comparar los resultados con los obtenidos mediante crt.sh, eliminar duplicados y comprobar en el *scope* qué activos están autorizados antes de continuar con ellos.
- **Dónde guardé los resultados:** `./subdominiosArchivos/interesantes-subfinder.txt` y `./subdominiosArchivos/resultados-totales-subfinder.txt`.

## 5. Enumeración de subdominios con crt.sh

### Anotación 5 – Búsqueda mediante certificados públicos

- **Cuándo:** 30/10/2026, 19:45.
- **Objetivo:** Nombres de dominio asociados a certificados de `roblox.com` (cada resultado debe comprobarse individualmente contra el *scope*).
- **Qué hice:** Consulté [crt.sh](https://crt.sh/?q=roblox.com) para localizar nombres incluidos en certificados digitales públicos. Después utilicé un script de Linux que obtiene los resultados en JSON, extrae los nombres de dominio, comprueba sus registros con `dig +short` y aplica un filtro. Archivo utilizado: `script-crtsh-subdominio.sh`.
- **Qué salió:** Se encontraron nombres que coinciden con los obtenidos mediante Subfinder y otros adicionales. Algunos resultados utilizan infraestructuras externas como Amazon CloudFront y Akamai. También aparecieron nombres relacionados con servicios de terceros y algunos nombres sin respuesta DNS.
- **Siguiente paso:** Comparar y deduplicar los resultados de ambas fuentes. Comprobar el alcance de cada activo y no realizar pruebas sobre nombres que no estén expresamente autorizados.
- **Dónde guardé los resultados:** `./subdominiosArchivos/interesantes_crtsh.txt` y `./subdominiosArchivos/resultados_crtsh.txt`.

## 6. Netcraft

### Anotación 6 – Información de infraestructura

- **Cuándo:** 30/10/2026, 20:35.
- **Objetivo:** `roblox.com` (alcance: pendiente de contrastar con el *scope* vigente).
- **Qué hice:** Consulté el informe público de [Netcraft](https://sitereport.netcraft.com/?url=https://roblox.com).
- **Qué salió:** Netcraft mostró la dirección IPv4 `128.116.32.3`, el servidor de nombres `nspx1.roblox.com`, el registrador MarkMonitor y señaló DNSSEC como habilitado. Este último dato no coincide con el estado «Unsigned» mostrado por ICANN ni con las consultas DNS realizadas, que no devolvieron registros DS ni DNSKEY para el dominio.
- **Siguiente paso:** Mantener la discrepancia anotada y no dar por confirmado el estado de DNSSEC sin una comprobación adicional y completa.

## 7. Wappalyzer

### Anotación 7 – Identificación de tecnologías web

- **Cuándo:** 30/10/2026, hora no registrada.
- **Objetivo:** Sitio web `roblox.com` (alcance: pendiente de contrastar con el *scope* vigente).
- **Qué hice:** Analicé las tecnologías detectables del sitio mediante Wappalyzer.
- **Qué salió:** La herramienta identificó tecnologías y servicios como React, Redux, AngularJS, Sentry, Cloudflare, Amazon S3, AWS, Envoy y Bootstrap, además de varias bibliotecas JavaScript.
- **Siguiente paso:** Conservar esta información como referencia tecnológica. No asumir que la detección confirma versiones instaladas en todos los componentes ni que exista una vulnerabilidad.

## 8. robots.txt

### Anotación 8 – Consulta de directivas para rastreadores

- **Cuándo:** 30/10/2026, 21:59.
- **Objetivo:** `https://www.roblox.com/robots.txt` (el sitio y las rutas mencionadas deben contrastarse con el *scope*).
- **Qué hice:** Consulté el archivo `robots.txt` del sitio para revisar las directivas públicas dirigidas a los rastreadores web.
- **Qué salió:** El archivo contiene directivas para todos los agentes de usuario y excluye del rastreo distintas rutas relacionadas con informes, publicidad, catálogo, errores, foros, juegos, herramientas, insignias y compras. También referencia varios sitemaps.
- **Siguiente paso:** Utilizar esta información únicamente como contexto del reconocimiento. Las rutas incluidas en `robots.txt` no se consideran automáticamente vulnerables ni autorizadas para realizar pruebas.

## 9. security.txt

### Anotación 9 – Búsqueda del archivo de contacto de seguridad

- **Cuándo:** 30/10/2026, hora no registrada.
- **Objetivo:** `https://roblox.com/.well-known/security.txt` (alcance: pendiente de contrastar con el *scope* vigente).
- **Qué hice:** Consulté la ruta estándar `/.well-known/security.txt` del dominio.
- **Qué salió:** En la consulta realizada no se encontró el archivo en esa ruta.
- **Siguiente paso:** No extraer conclusiones sobre la existencia de un canal de comunicación alternativo; continuar con las demás fuentes públicas previstas.

## 10. Shodan InternetDB

### Anotación 10 – Consulta de información pública de una IP

- **Cuándo:** 30/10/2026, hora no registrada.
- **Objetivo:** IP `128.116.102.3` (comprobar que la IP está incluida en el *scope* antes de cualquier comprobación adicional).
- **Qué hice:** Consulté la información disponible en Shodan InternetDB mediante el comando:
  
  ```bash
  curl -s https://internetdb.shodan.io/128.116.102.3
  ```

- **Qué salió:** La respuesta mostró los puertos 80 y 443, dos nombres de host asociados y ningún CVE listado en el resultado consultado.
- **Siguiente paso:** Registrar el resultado como información de reconocimiento. La ausencia de vulnerabilidades listadas no demuestra que el sistema esté libre de ellas. No realizar escaneos ni pruebas adicionales sin confirmar antes que la IP está en alcance.

## 11. Google Dorks

### Anotación 11 – Búsquedas de información indexada

- **Cuándo:** 30/10/2026, 21:03, 21:04, 21:05, 21:49, 21:50, 21:53.
- **Objetivo:** Contenido público indexado bajo `roblox.com` (las páginas y activos encontrados deben comprobarse contra el *scope*).
- **Qué hice:** Realicé búsquedas avanzadas en Google con los siguientes operadores:
  
  ```text
  site:roblox.com filetype:pdf
  site:roblox.com filetype:docx
  site:roblox.com inurl:api
  site:roblox.com inurl:login
  site:roblox.com intitle:index.of
  ```

- **Qué salió:** La búsqueda de PDF devolvió numerosos resultados; la de DOCX y la de `inurl:login` no devolvieron resultados en la consulta realizada. Las búsquedas `inurl:api` e `intitle:index.of` mostraron referencias a un foro de desarrolladores.
- **Siguiente paso:** Revisar únicamente resultados públicos que sean relevantes para el objetivo y estén dentro del alcance. No interpretar la aparición de una página en Google como prueba de exposición o vulnerabilidad.

## 12. Wayback Machine

### Anotación 12 – Consulta de recursos históricos

- **Cuándo:** 30/10/2026, 21:08.
- **Objetivo:** URLs históricas asociadas a `roblox.com` (comprobar el alcance antes de cualquier interacción con los recursos).
- **Qué hice:** Consulté el índice CDX de Wayback Machine mediante el comando:
  
  ```bash
  curl -s 'https://web.archive.org/cdx/search/cdx?url=roblox.com/*&collapse=urlkey&fl=original' | grep -iE 'api/|\.json'
  ```

- **Qué salió:** Aparecieron referencias históricas a recursos como `/.well-known/ai-plugin.json`, `/.well-known/assetlinks.json`, `/.well-known/gpc.json`, `503.json` y una ruta relacionada con informes de abuso.
- **Siguiente paso:** Conservar las referencias como contexto histórico. No asumir que esos recursos siguen existiendo o están activos actualmente.

## 13. Hunter.io

### Anotación 13 – Información pública sobre el patrón de correo

- **Cuándo:** 30/10/2026, 21:12 y 23:14.
- **Objetivo:** Dominio `roblox.com` (alcance: consulta pasiva de información pública del dominio).
- **Qué hice:** Consulté la información pública disponible en [Hunter.io](https://hunter.io/search/roblox.com), filtrando los resultados por el área de seguridad.
- **Qué salió:** La herramienta mostró alrededor de 1.861 resultados relacionados con 'roblox.com'. agrupados por departamentos y permitió observar un posible patrón de formato de correo corporativo: inicial del nombre seguida del apellido y el dominio `@roblox.com`.
- **Siguiente paso:** Conservar únicamente el patrón y los datos agregados que sean relevantes. No recopilar ni utilizar direcciones personales para contactar con empleados o probar accesos.

## 14. Have I Been Pwned

### Anotación 14 – Consulta de posibles filtraciones asociadas a correos

- **Cuándo:** 30/10/2026, 22:04.
- **Objetivo:** Información pública asociada al dominio `roblox.com` (consulta pasiva; los resultados individuales no se consideran objetivos de prueba).
- **Qué hice:** Consulté Have I Been Pwned para comprobar si las direcciones corporativas revisadas aparecían asociadas a filtraciones conocidas.
- **Qué salió:** En la consulta original se observaron resultados de filtraciones asociados a algunas direcciones revisadas y no se observaron resultados para las direcciones del área de seguridad consultadas. No se incluyen las direcciones individuales en este cuaderno porque no son necesarias para documentar el resultado general.
- **Siguiente paso:** Registrar el hallazgo de forma agregada y no intentar acceder a cuentas, reutilizar credenciales ni contactar con las personas afectadas.

---