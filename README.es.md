# Professional Research MCP

[English](README.md) | [Português (Brasil)](README.pt-BR.md) | [Español](README.es.md)

Servidor MCP local para investigar profesionales, empresas y posibles stakeholders mediante **información pública indexada en la web**. Compatible con clientes MCP que admitan conexiones SSE locales.

**Instalación gratuita:** no requiere clave API, tarjeta de crédito ni cuenta de LinkedIn. Los proveedores de búsqueda pública pueden limitar o bloquear consultas.

> **No es una API oficial de LinkedIn ni una integración afiliada.** No accede a perfiles privados, conexiones, mensajes ni al feed de una cuenta.

## Elige cómo instalar

| Opción | Para quién | Pasos |
| --- | --- | --- |
| **Instalación fácil (recomendada)** | Principiantes | Instala [Python 3.11+](https://www.python.org/downloads/), descarga el proyecto con **Code → Download ZIP**, extrae los archivos y ejecuta **`install.bat`** (Windows) o **`install.command`** (macOS). No necesitas Git. |
| **Instalación manual** | Usuarios avanzados | Sigue los comandos de Terminal y Git en las secciones siguientes. |

**Detalles de la instalación fácil:** El archivo prepara el entorno Python, instala las dependencias e inicia el servidor. Mantén la ventana abierta y conecta tu cliente MCP a **`http://127.0.0.1:8000/sse`**. Vuelve a ejecutar el mismo archivo para iniciar el servidor otro día; también comprueba las dependencias. En macOS, Gatekeeper puede bloquear scripts descargados sin firma: revisa el código y usa la instalación manual si es necesario. Puede ser necesario dar permiso de ejecución (`chmod +x install.command`) o ejecutar `bash install.command` en Terminal. Los scripts no instalan Python automáticamente ni evitan las políticas de seguridad.

## Instalación para principiantes (sin Git)

Si nunca instalaste Python ni Git, **no necesitas instalar Git** para usar este proyecto.

1. Instala Python 3.11 o posterior desde el [sitio oficial](https://www.python.org/downloads/). En Windows, activa **Add python.exe to PATH** si aparece esa opción.
2. Abre el [repositorio del proyecto](https://github.com/caiqueescaler86/jouleandlinkedin), haz clic en **Code → Download ZIP**.
3. Extrae el ZIP en una carpeta fácil de encontrar, por ejemplo Documentos.
4. Abre la carpeta extraída `jouleandlinkedin-main`.
5. **Windows:** Haz clic en la barra de direcciones de la carpeta, escribe `powershell` y presiona Enter. Ejecuta los comandos **uno por uno**:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe server.py
```

Si `py` no funciona, prueba `python -m venv .venv`.

6. **macOS:** Abre Terminal, escribe `cd ` (con espacio), arrastra la carpeta extraída a Terminal y presiona Enter. Luego ejecuta:

```bash
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python server.py
```

7. Mantén la ventana abierta. Configura el cliente MCP con la URL **`http://127.0.0.1:8000/sse`**, según las instrucciones de abajo.

**Para volver a iniciar:** Abre la terminal en la carpeta del proyecto y ejecuta solamente el último comando (`server.py`). Para actualizar una instalación ZIP, descarga y extrae la última versión y repite la configuración en la nueva carpeta.

**Si hay problemas:** Después de instalar Python, cierra y vuelve a abrir la terminal. Verifica `py --version` (Windows) o `python3 --version` (macOS). Si tu equipo es administrado por una empresa, solicita ayuda a TI; no evites las restricciones de seguridad.

## Requisitos

- Windows con PowerShell o macOS con Terminal
- Python 3.11 o superior
- Git
- Cliente MCP compatible con servidores SSE locales
- Conexión a internet para las búsquedas públicas

Verifica las herramientas:

**Windows**
```powershell
py --version
git --version
```

**macOS**
```bash
python3 --version
git --version
```

Instala Python y Git si es necesario. En Windows, puedes usar `python` en lugar de `py` si no tienes el lanzador de Python.

## Instalación en Windows

Abre PowerShell y ejecuta los comandos **uno por uno**:

```powershell
git clone https://github.com/caiqueescaler86/jouleandlinkedin.git
cd jouleandlinkedin
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe server.py
```

Deja la ventana abierta. Mensaje esperado:

```text
INFO: Application startup complete.
INFO: Uvicorn running on http://127.0.0.1:8000
```

Para iniciarlo de nuevo, abre PowerShell en la carpeta del proyecto y ejecuta:

```powershell
.\.venv\Scripts\python.exe server.py
```

## Instalación en macOS

Abre Terminal y ejecuta:

```bash
git clone https://github.com/caiqueescaler86/jouleandlinkedin.git
cd jouleandlinkedin
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python server.py
```

Mantén Terminal abierto durante el uso. Para reiniciar: `./.venv/bin/python server.py`.

## Configuración del cliente MCP

Con el servidor Python en ejecución:

1. Abre un cliente MCP compatible con conexiones SSE locales.
2. Busca la sección de servidores o conectores MCP (el nombre varía según el cliente).
3. Agrega un servidor con estos datos:

| Campo | Valor |
| --- | --- |
| Nombre | Professional Research |
| URL | `http://127.0.0.1:8000/sse` |
| Transporte | SSE |
| Autenticación | Ninguna (solo desarrollo local) |

4. Guarda y habilita la conexión.
5. Comprueba que aparezcan las cuatro herramientas.

**Utiliza `127.0.0.1` en vez de `localhost`:**

```text
http://127.0.0.1:8000/sse
```

El cliente MCP debe ejecutarse en el mismo equipo o tener acceso explícito al servidor local. Un cliente exclusivamente en la nube no puede acceder automáticamente a `127.0.0.1` de tu computadora.

## Primera prueba

En el chat del cliente MCP:

```text
Usa research_professional para buscar referencias profesionales
públicas de "Nombre Apellido". Incluye las URL de las fuentes
y no inventes información.
```

```text
Usa map_stakeholders para identificar posibles responsables
de Marketing y CRM en Empresa Ejemplo en Brasil.
Incluye fuentes y señala los datos no verificados.
```

## Herramientas disponibles

| Herramienta | Función |
| --- | --- |
| `search_professionals(company, role, country, limit)` | Buscar profesionales por empresa, cargo y país |
| `research_professional(name, company)` | Investigar referencias públicas de una persona |
| `research_company(company, country)` | Buscar información pública de una empresa |
| `map_stakeholders(company, country, function)` | Identificar posibles stakeholders |

Los resultados son **referencias no verificadas**, no confirmaciones de identidad, empleo o autoridad de decisión.

## Solución de problemas

**No conecta:** Comprueba que el servidor Python esté activo y que la URL sea exactamente `http://127.0.0.1:8000/sse`. Si antes usabas `localhost`, vuelve a crear la conexión con `127.0.0.1`.

**Prueba SSE en Windows** (en otra ventana de PowerShell):

```powershell
curl.exe -N --max-time 5 http://127.0.0.1:8000/sse
```

Respuesta esperada:

```text
event: endpoint
data: /messages/?session_id=...
```

El timeout después de cinco segundos es normal porque SSE mantiene la conexión abierta. Esto valida el endpoint SSE, **no** toda la negociación MCP.

**Muchos `GET /sse 200 OK`:** El cliente podría estar reconectándose. HTTP 200 por sí solo no confirma una inicialización MCP correcta.

**`MCP error -32602: Invalid request parameters`:** Vuelve a conectar el cliente. Si continúa, recopila el error exacto y los logs.

**`Error: name 'clean' is not defined`:** Actualiza el repositorio; este error ya fue corregido. Reinicia el servidor.

**Sin resultados:** Los proveedores de búsqueda pública pueden limitar consultas o estar indisponibles. No significa necesariamente que falle la conexión MCP.

## Actualización

Detén el servidor con `Ctrl+C`.

**Windows**
```powershell
git pull
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe server.py
```

**macOS**
```bash
git pull
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python server.py
```

## Seguridad y limitaciones

- El servidor escucha en `127.0.0.1` de forma predeterminada. **No lo expongas públicamente sin autenticación.**
- Las búsquedas utilizan `ddgs`, no el acceso autenticado a LinkedIn.
- Verifica las fuentes y los cargos antes de tomar decisiones comerciales.
- Respeta los términos de los proveedores, las políticas corporativas y las leyes de privacidad aplicables.
