
# Google Maps Scraper – Análisis de Mercado y Consultoría de Negocios

## Descripción del Proyecto

Este proyecto es una **herramienta de scraping y análisis de Google Maps** desarrollada en **Python** utilizando **Playwright**.

Está diseñado para **consultoría y análisis de mercado**, permitiendo a empresas o analistas extraer información estructurada de negocios por categoría y ubicación, optimizando la toma de decisiones estratégicas.

El sistema permite:

* Automatizar búsquedas en Google Maps por **categorías y ubicación**.
* Extraer información relevante de cada negocio: nombre, categoría (tipo de empresa), dirección, teléfono, sitio web, calificación, descripción breve y link directo en Maps.
* Guardar los resultados en **Excel** para análisis posterior, reportes o dashboards.
* Mostrar **los resultados en tiempo real** durante la ejecución, facilitando la revisión inmediata.

Este proyecto puede integrarse como parte de un **servicio de consultoría de mercado** para:

* Identificar competidores en un sector específico.
* Mapear oportunidades de expansión por ubicación.
* Analizar calificaciones y reputación de empresas en línea.

---

## Tecnologías

* **Python 3.10+** – lenguaje principal.
* **Playwright** – automatización del navegador para scraping dinámico.
* **Pandas** – procesamiento y almacenamiento de datos.
* **OpenPyXL** – exportación a Excel.

---

## Instalación

1. Instalar Python 3.10+
2. Instalar librerías necesarias:

   ```bash
   pip install pandas openpyxl playwright
   ```
3. Inicializar Playwright para instalar navegadores:

   ```bash
   playwright install
   ```

---

## Uso

1. Configurar las búsquedas en `main.py`:

```python
consultas = [
    "constructoras Córdoba capital Argentina",
    "inmobiliarias Córdoba capital Argentina",
    "arquitectos Córdoba capital Argentina"
]
```

2. Ejecutar el script:

```bash
python main.py
```

3. El scraper abrirá el navegador, realizará scroll automático, y **mostrará en tiempo real los negocios encontrados**:

* Nombre del negocio
* Categoría (tipo de negocio)
* Dirección
* Teléfono
* Sitio web
* Calificación / Rating
* Descripción breve
* Link directo a Google Maps

4. Al finalizar, los resultados se guardan automáticamente en `resultados_maps.xlsx`.

---

## Estructura de Datos

| Columna          | Descripción                                   |
| ---------------- | --------------------------------------------- |
| Nombre           | Nombre del negocio                            |
| Categoría        | Tipo de negocio (Inmobiliaria, Constructora…) |
| Dirección        | Dirección física del negocio                  |
| Teléfono         | Número de contacto                            |
| Sitio web        | Página web del negocio                        |
| Rating           | Calificación en Google Maps                   |
| Descripción      | Mini reseña o descripción breve del negocio   |
| Link Google Maps | Link directo al perfil del negocio en Maps    |

---

## Valor para Consultoría y Análisis de Mercado

* **Mapeo de Competencia:** Identificación de competidores por zona y categoría.
* **Inteligencia Comercial:** Obtención de datos de contacto y reputación online.
* **Soporte a Estrategia:** Generación de reportes listos para dashboards y presentaciones.
* **Automatización y Escalabilidad:** Permite recolectar grandes volúmenes de datos de forma eficiente.

---

## Buenas Prácticas

* El scraping está diseñado para **uso ético y académico**, cumpliendo con las políticas de Google Maps.
* Evitar consultas masivas que puedan generar bloqueos.
* Los selectores pueden actualizarse periódicamente según cambios en la interfaz de Maps.

---
