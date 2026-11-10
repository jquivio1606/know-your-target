
# 3. Comparación entre mi reconocimiento y el agente

## 3.1 La comparación

Para comparar ambos reconocimientos he tenido en cuenta las técnicas utilizadas, los datos obtenidos y las diferencias entre los resultados.

| Dato | Lo encontré yo | Lo encontró el agente | ¿Coincide? | Observaciones |
|---|---|---|---|---|
| Fecha de creación del dominio | 30/01/2004 | 30/01/2004 | Sí |  |
| Fecha de expiración | 30/01/2027 | 30/01/2027 | Sí |  |
| Registrador | MarkMonitor Inc. | 292 (GoDaddy) | No | Existe una discrepancia importante. Mi consulta de ICANN identificó MarkMonitor, mientras que el agente indicó GoDaddy. |
| Servidores DNS (NS) | 4 servidores `nspx` | Los mismos 4 servidores | Sí |  |
| Registro A | 128.116.102.3 | 128.116.102.3 | Sí |  |
| Registros AAAA | No documenté el resultado | Sin registros IPv6 | No comprobable | En mi cuaderno no anoté el resultado de esta consulta. |
| Servidores de correo (MX) | Servidores de Google | Google Workspace | Sí |  |
| Registros TXT | SPF y verificaciones de servicios externos | Más de 20 servicios identificados | Parcial | Ambos detectaron registros de verificación, pero el agente presentó una clasificación más detallada. |
| Subdominios | Subfinder y crt.sh | 139 subdominios | Parcial | Utilicé dos fuentes para obtener subdominios, mientras que el agente presentó resultados de crt.sh. No tengo el recuento final deduplicado de mi búsqueda para hacer una comparación numérica exacta. |
| Infraestructura externa | CloudFront, S3 y Akamai | Infraestructura propia y nodos relacionados con Arkose Labs | Parcial | Ambos identificaron servicios e infraestructuras externas, aunque las conclusiones no son exactamente iguales. |
| Dirección IP adicional | Netcraft mostró 128.116.32.3 | Shodan mostró 128.116.30.3 | No | Se obtuvieron direcciones diferentes. Son resultados de consultas distintas y no se debe asumir que una de ellas sea incorrecta sin contrastarlas. |
| Puertos abiertos | 80 y 443 | 80 y 443 | Sí |  |
| robots.txt | Encontré directivas y varios sitemaps | Encontró 32 sitemaps y reglas de exclusión | Parcial | Ambos localizaron el archivo, pero el agente detalló más información. |
| security.txt | No se encontró en la ruta consultada | Sí encontró información de contacto | No | El agente encontró un archivo que mi consulta no localizó. Habría que comprobar la URL exacta y la respuesta obtenida. |
| Tecnologías web | React, Redux, AngularJS, Sentry, Cloudflare, AWS, Envoy, etc. | No aparece un análisis equivalente | No comprobable | El agente no incluyó resultados de Wappalyzer en su informe. |
| Google Dorks | Encontré resultados PDF y referencias a foros | No aparece en el informe | No comprobable | El agente no documentó búsquedas avanzadas en Google. |
| Wayback Machine | Encontré referencias históricas a varios recursos | No aparece en el informe | No comprobable | No realizó o no incluyó esta técnica en el informe. |
| Hunter.io | Observé un posible patrón de correo corporativo | No aparece en el informe | No comprobable | No se incluyó información equivalente. |
| Have I Been Pwned | Encontré resultados de filtraciones asociados a algunas direcciones consultadas | No aparece en el informe | No comprobable | El agente no documentó esta consulta. |

### Resumen de resultados

En mi reconocimiento hice 14 apartados de trabajo, incluyendo consultas WHOIS, ICANN, DNS, Subfinder, crt.sh, Netcraft, Wappalyzer, robots.txt, security.txt, Shodan, Google Dorks, Wayback Machine, Hunter.io y Have I Been Pwned.

El agente presentó resultados de 6 bloques principales de reconocimiento: WHOIS, DNS, subdominios, Shodan, robots.txt y security.txt.

Yo documenté más técnicas diferentes. El agente consiguió presentar un informe estructurado y reunir bastante información de forma automática, pero también dejó fuera técnicas que yo sí había utilizado, por no añadirlas en el agente.

## 3.2 Los fallos del agente

Al revisar el informe y las ejecuciones del agente, he identificado varios tipos de fallos. 

### 1. Omisiones

Son datos o técnicas que yo sí utilicé durante el reconocimiento, pero que el agente no incluyó en su informe porque no estaban incorporadas en su configuración.

### 2. Errores

- **Registrador del dominio:** el agente indicó que el registrador era 292 (GoDaddy), mientras que en mi consulta de ICANN Lookup apareció MarkMonitor Inc. Es una discrepancia que debería comprobarse antes de dar el dato por válido.

### 3. Invenciones

- **Ubicación de Chicago:** no se aportó una consulta que confirmase que el servidor estaba físicamente en Chicago.
- **Infraestructura distribuida globalmente:** disponer de servidores DNS con diferentes extensiones de dominio no demuestra por sí solo cómo está distribuida físicamente toda la infraestructura.

### 4. Intentos fuera de alcance

Son consultas que el agente intentó realizar sobre dominios que no estaban autorizados y que fueron bloqueadas por el `scope-guard`.

Durante las pruebas se produjeron diferentes intentos:

| Herramienta | Objetivo solicitado | Resultado |
|---|---|---|
| `whois_dominio` | `rbx.com` | Bloqueado |
| `subdominios_crtsh` | `rbx.com` | Bloqueado |
| `whois_dominio` | `google.com` | Bloqueado |
| `dns_registros` | `google.com` | Bloqueado |
| `whois_dominio` | `guilded.gg` | Bloqueado |
| Varias consultas | `otraempresa.com` y `blog.empresa2.com` | Bloqueadas |

**Ejemplo de la traza:** durante las pruebas el agente intentó consultar `google.com` mediante WHOIS y DNS, pero el `scope-guard` rechazó las peticiones porque ese dominio no pertenecía al alcance autorizado.

También intentó consultar `guilded.gg`, que estaba expresamente excluido del alcance.

En este caso, el sistema de protección funcionó correctamente, ya que impidió que el agente continuara investigando dominios ajenos al objetivo.

## 3.3 Reflexión

### 1. ¿Qué hizo mejor el agente que tú, y qué hiciste mejor tú?

El agente fue mejor a la hora de organizar y presentar los resultados. Consiguió reunir información de varias herramientas y generar un informe estructurado, con tablas y categorías, sin tener que redactar manualmente cada apartado, mucho más rápido de lo que yo lo hice.

Por mi parte, creo que hice mejor el contraste de la información y la variedad de técnicas utilizadas. No me limité a consultar una sola fuente, sino que comparé resultados de WHOIS con ICANN, y otras herramientas, detectando discrepancias que el agente no destacó, como la diferencia entre el estado de DNSSEC indicado por ICANN y el mostrado por Netcraft.

En definitiva, el agente fue más rápido organizando la información, pero mi reconocimiento fue más amplio en cuanto a las técnicas utilizadas y prestó más atención a contrastar algunos resultados.

### 2. ¿Por qué falló donde falló? ¿Faltaba una herramienta, el prompt era ambiguo, el modelo interpretó mal una salida?

Creo que los pocos fallos que tuvo se produjeron por problemas de interpretación. 
Por ejemplo, relacionó el nombre de un servidor con una ubicación geográfica sin disponer de una comprobación suficiente. 

En cuanto a las herramientas, el agente usó todas las herramientas instaladas, pero para poder comparar mejor con mis apuntes debería haber añadido más herramientas, para hacer un informe más completo.

### 3. ¿Te fiarías del informe del agente sin revisarlo? ¿Qué tendrías que comprobar siempre?

No me fiaría completamente del informe sin revisarlo. Aunque es una herramienta útil para ahorrar tiempo y organizar información, puede omitir resultados, interpretar mal algunos datos o sacar conclusiones que no están suficientemente demostradas.

Antes de dar por válido un informe comprobaría:

- Que todos los dominios consultados pertenecen al alcance autorizado.
- Que los datos importantes, como direcciones IP, servidores DNS y registradores, coinciden con las fuentes originales.
- Que los subdominios encontrados realmente pertenecen al objetivo.
- Que las conclusiones sobre tecnologías, infraestructura y posibles servicios externos están respaldadas por evidencias.
- Que no se confunden datos históricos con información actual.
- Que las herramientas utilizadas han devuelto resultados reales y que el agente no ha inventado información.

En conclusión, utilizaría el agente como una ayuda para realizar el reconocimiento pasivo, pero no como sustituto de mi propia revisión. La información que genera debe contrastarse antes de incluirla en un informe definitivo.
