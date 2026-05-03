# Fuzzer de Directorios desde Básico a Profesional**

---

## **📌 Descripción**
Este proyecto es un **fuzzer de directorios** escalable, optimizado para pasar de un script básico a una herramienta profesional. Combina **concurrencia**, **manejo robusto de errores** y **flexibilidad** (cabeceras, timeouts, agentes de usuario) para escanear URLs de manera eficiente.

⚠️ **Advertencia**:
Este script **solo debe usarse en entornos controlados** (laboratorios, Bug Bounties con permiso explícito). Su uso en sistemas ajenos puede ser ilegal y detectado como un ataque.

---

## **⚙️ Características Pro**

### **1️⃣ Concurrencia (Rendimiento Óptimo)**
- **ThreadPoolExecutor**: Procesa múltiples URLs en paralelo (configurable con `-t/--threads`).
- **Ejemplo**: Con 20 hilos, 1000 URLs se escanean en minutos (vs. horas en serial).
- **Optimización**: `stream=True` en `requests` evita descargar cuerpos de respuesta innecesarios.

### **2️⃣ Manejo Robusto de Errores**
- **Silencio estratégico**: Ignora errores de conexión (`requests.RequestException`) para no detener el escaneo.
- **Excepciones controladas**:
  - `FileNotFoundError`: Diccionario no encontrado.
  - `KeyboardInterrupt`: Interrupción manual (Ctrl+C) con mensaje claro.
- **Timeouts**: Configurables (default: 5 segundos) para evitar bloqueos.

### **3️⃣ Flexibilidad Avanzada**
- **Cabeceras personalizadas**: User-Agent (`Pro-Fuzzer-Scanner/1.0`) para evitar bloqueos.
- **Redirecciones deshabilitadas**: `allow_redirects=False` evita seguimientos innecesarios.
- **Codificación segura**: `encoding='utf-8', errors='ignore'` para diccionarios como RockYou.

---

## **📂 Estructura del Proyecto**
```
fuzzer-pro/
├── fuzzer.py          # Script principal (versión profesional)
├── wordlist.txt       # Ejemplo de diccionario (opcional)
└── README.md          # Este archivo
```

---

## **🚀 Uso Básico (Nivel Pro)**

### **1. Instalación de Dependencias**
```bash
pip install requests tqdm
```

### **2. Ejecución**
```bash
python fuzzer.py http://ejemplo.com /ruta/a/diccionario.txt -t 50
```
- **Argumentos**:
  - `url`: URL base (ej: `http://target.com`).
  - `dict`: Ruta al diccionario (ej: `wordlist.txt`).
  - `-t/--threads`: Número de hilos (default: 20).

### **3. Salida**
- **Consola**: Muestra URLs encontradas (200/301) en tiempo real con `tqdm`.
- **Guardar resultados**: Añade `-o output.txt` para exportar a un archivo.

---

## **🔍 ¿Qué hace un Fuzzer de Directorios?**

### **🎯 Objetivos Clave**
1. **Descubrir contenido oculto**:
   - Paneles de admin (`/admin`, `/login`).
   - Archivos de respaldo (`.bak`, `.old`).
   - Directorios de desarrollo (`/dev`, `/test`).

2. **Detectar fugas de información**:
   - Archivos `.env` (contraseñas).
   - Carpetas `.git` o `.svn` (código fuente).
   - Logs del sistema (rutas internas, usuarios).

3. **Mapear la estructura del servidor**:
   - Carpetas como `/uploads` o `/scripts` (puntos de entrada para exploits).

4. **Automatizar el reconocimiento**:
   - Prueba miles de rutas por minuto (vs. manualmente).

---

## **🛠️ Mejoras Propuestas (Opcionales)**
- **📝 Exportar resultados**: Guardar en `output.txt` con:
  ```python
  with open("output.txt", "a") as f:
      f.write(f"[+] Encontrado (200): {url}\n")
  ```
- **🌐 Proxies**: Añadir soporte para `requests` con proxies (evitar bloqueos).
- **🔐 Autenticación**: Soporte para headers de autenticación (Bearer Token, Basic Auth).
- **📊 Estadísticas**: Contadores de respuestas (200, 301, 403, etc.).

---

## **📜 Ejemplo de Diccionario (`wordlist.txt`)**
```txt
admin
login
backup
config.php
.git
.env
uploads
test
dashboard
```

---

## **⚠️ Ética y Legalidad**
- **✅ Permiso**: Solo usa este script en sistemas donde tengas autorización escrita.
- **❌ Prohibido**: Escanear servidores sin consentimiento (ilegal en muchos países).
- **🔒 Alternativas legales**: Plataformas como Hack The Box o Bugcrowd.

---

## **📌 Créditos**
- **Autor**: Kaleth
- **Librerías**:
  - `requests` (HTTP requests).
  - `tqdm` (barras de progreso).
  - `concurrent.futures` (concurrencia).

---
**🔄 Versión**: 1.0 (Profesional)
**📅 Fecha**: [02/04/2026
