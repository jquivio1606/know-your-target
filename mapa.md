# MAPA DE RECONOCIMIENTO - ROBLOX

**Fecha:** 30/10/2026

## 1. Resumen

Roblox Corporation es la empresa propietaria del dominio 'roblox.com', registrado desde el 30 de enero de 2004.

Se han encontrado direcciones IP relacionadas con Roblox dentro del rango '128.116.0.0 - 128.116.127.255', además de servicios que utilizan proveedores externos como Amazon Web Services.

En su página web se han identificado tecnologías como React, AngularJS, Redux, Cloudflare y Bootstrap, entre otras.

El correo de la empresa utiliza los servidores de Google y se han encontrado referencias a herramientas de soporte, comunicación, desarrollo y gestión de pagos.

Por último, las consultas realizadas en Shodan InternetDB muestran los puertos 80 y 443 en la IP principal, pero no aparecen vulnerabilidades registradas en los resultados consultados.

## 2. Dominios y subdominios

| Dominio o subdominio | IP | En alcance | Función aparente |
|---|---|---|---|
| 'roblox.com' | 128.116.102.3 | Si | Dominio principal de la organización. |
| 'games.api.roblox.com' | 128.116.21.3 | Si | Servicio relacionado con las API de juegos. |
| 'developer.roblox.com' | 13.224.83.28, 13.224.83.40, 13.224.83.73, 13.224.83.117 | Si | Página para desarrolladores, alojada mediante CloudFront. |
| 'devforum.roblox.com' | 3.174.170.92, 3.174.170.62, 3.174.170.18, 3.174.170.121 | Si | Foro de desarrolladores, alojado mediante CloudFront. |
| 'authorize.roblox.com' | 65.8.202.77, 65.8.202.128, 65.8.202.69, 65.8.202.40 | Si | Subdominio relacionado con la autorización. |

*Las direcciones de CloudFront pertenecen a infraestructura de Amazon y no necesariamente son exclusivas de Roblox. El alcance debe confirmarse antes de realizar pruebas.*

## 3. Infraestructura y servicios

### Dominio y DNS

- Dominio registrado el 30/01/2004.
- Empresa registradora: MarkMonitor Inc.
- Rango de IP identificado mediante WHOIS: '128.116.0.0 - 128.116.127.255'.
- Se han encontrado cuatro servidores DNS (nameservers) asociados al dominio.
- DNSSEC: ICANN y las consultas realizadas con 'dig' indican que la delegación no está firmada, mientras que Netcraft indica que está habilitado. Por tanto, hay una diferencia entre los resultados de las herramientas.

### Tecnologías utilizadas

Con Wappalyzer he podido identificar varias tecnologías en la web de Roblox:

- **Frameworks:** React 17.0.2, AngularJS 1.6.3 y Redux.
- **Librerías:** Lodash, jQuery Migrate y core-js.
- **Interfaz web:** Bootstrap 3.3.5.
- **Infraestructura:** Amazon Web Services y Amazon S3.
- **Servicios web:** Cloudflare y Envoy.
- **Protección frente a bots:** PerimeterX, Cloudflare Bot Management y Arkose Labs.
- **Gestión de errores:** Sentry.

Estas detecciones sirven como referencia, pero no confirman que todas estas tecnologías se utilicen en todos los servicios de Roblox.

### Correo electrónico y servicios externos

Los registros DNS MX muestran que Roblox utiliza los servidores de correo de Google:

- 'aspmx.l.google.com'
- 'alt1.aspmx.l.google.com'
- 'alt2.aspmx.l.google.com'
- 'alt3.aspmx.l.google.com'
- 'alt4.aspmx.l.google.com'

El registro SPF incluye Google y otros servicios autorizados para enviar correos desde el dominio.

También se han encontrado referencias a diferentes herramientas y proveedores externos, como:

- **Google:** correo electrónico.
- **Slack y Atlassian:** herramientas de comunicación y trabajo.
- **Zendesk:** soporte y atención al cliente.
- **Stripe:** gestión de pagos.
- **DocuSign:** firma de documentos.
- **Dropbox:** almacenamiento de archivos.

Además, aparecen registros de verificación relacionados con servicios como OpenAI, Anthropic y Cursor. Estos registros indican que el dominio está asociado a dichos servicios, aunque no permiten saber exactamente cómo se utilizan.

### Resultados de Shodan

La consulta de la IP principal '128.116.102.3' en Shodan InternetDB devuelve:

- Puertos: 80 y 443.
- Hostnames: 'roblox.com' y 'us-central-origin-px.roblox.com'.
- Vulnerabilidades registradas: ninguna.
- CPE: ninguno.

Esto indica que Shodan tiene registrados servicios web HTTP y HTTPS en esa IP, pero no muestra vulnerabilidades conocidas en los datos consultados.

### Otros hallazgos web

- **robots.txt:** contiene rutas que se excluyen del rastreo de los buscadores y referencias a varios sitemaps.
- **security.txt:** no se ha encontrado en la ruta estándar consultada.
- **Google Dorks:** se han encontrado documentos PDF y resultados relacionados con el foro de desarrolladores.
- **Wayback Machine:** conserva referencias antiguas a rutas como '/.well-known/assetlinks.json', '/.well-known/gpc.json' y '/abusereport/api/comment'.

## 4. Correos y personas

Hunter.io ha mostrado alrededor de 1.861 resultados relacionados con 'roblox.com'. La herramienta permite consultar información sobre direcciones de correo, puestos de trabajo y departamentos de la empresa.

Se ha observado un posible formato para los correos corporativos: la inicial del nombre seguida del apellido completo y el dominio '@roblox.com'. No se puede asegurar que todas las direcciones sigan este patrón.

En los resultados filtrados por el puesto de Security aparecen contactos de diferentes departamentos:

- IT / Engineering: 17 resultados.
- Management: 1 resultado.
- Sales: 1 resultado.
- Legal: 4 resultados, uno de ellos marcado como decisor.
- Operations & Logistics: 2 resultados.
- Departamento desconocido: 1 resultado.

Por otra parte, Have I Been Pwned ha mostrado filtraciones antiguas relacionadas con algunas de las direcciones corporativas consultadas. En otras direcciones, como las relacionadas con el departamento de Security, no aparecieron resultados.

Esto puede servir para conocer posibles exposiciones de información, aunque aparecer en una filtración no significa que una cuenta esté actualmente comprometida ni que se conozca su contraseña.

## 5. Puntos de interés para la fase activa

Después de revisar toda la información, hay tres cosas que me parecen interesantes para investigar con más detalle en la siguiente fase:

### 1. Los subdominios y servicios web

Han aparecido distintos subdominios relacionados con Roblox, algunos vinculados a servicios web, foros y API. También he encontrado rutas relacionadas con estos servicios en Google y Wayback Machine.

Me centraría en conocer mejor para qué sirve cada uno y comprobar cuáles siguen activos, ya que pueden dar una idea de los distintos servicios que forman parte de la plataforma.

Además, durante las búsquedas con Subfinder y crt.sh han aparecido varios subdominios que no devuelven resultados DNS, como 'api.roblox.com', 'analytics.roblox.com', 'music.roblox.com' y 'www.jira.roblox.com'.

Me parece interesante investigar si alguno de estos subdominios se ha dejado de utilizar y ha quedado mal configurado. En algunos casos, este tipo de errores puede permitir realizar un *subdomain takeover*, es decir, que otra persona consiga utilizar un subdominio de la empresa.

De momento no se ha encontrado ningún caso confirmado, pero creo que merece la pena tenerlo en cuenta para la siguiente fase.

### 2. Los correos electrónicos y la información pública

En Hunter.io aparecen alrededor de 1.861 resultados relacionados con 'roblox.com'. Esto puede ser interesante para conocer mejor cómo se organizan los departamentos de la empresa, qué puestos de trabajo existen y qué formato suelen tener sus direcciones de correo.

También se han encontrado algunas direcciones que aparecen en bases de datos de filtraciones consultadas mediante Have I Been Pwned. Me gustaría investigar qué información se puede obtener de estas exposiciones y si afectan a cuentas corporativas. Esto no significa que se hayan descubierto contraseñas ni que las cuentas estén comprometidas, pero puede ayudar a conocer posibles riesgos relacionados con la exposición de datos.

### 3. Los servicios y puertos encontrados en Shodan

Con Shodan InternetDB he podido consultar información sobre algunas direcciones IP relacionadas con Roblox. En los resultados aparecen principalmente los puertos 80 y 443, utilizados habitualmente para servicios web HTTP y HTTPS.

También se han consultado algunas IP relacionadas con CloudFront, que es una infraestructura externa utilizada para distribuir contenido. Me parece interesante conocer mejor qué servicios hay detrás de estas direcciones y qué información pública se puede obtener sobre ellos.

En los resultados consultados no aparecen vulnerabilidades conocidas, aunque esto no significa que los servicios estén libres de fallos de seguridad. Además, habría que tener en cuenta qué sistemas pertenecen realmente a Roblox y cuáles son de proveedores externos antes de realizar cualquier prueba.