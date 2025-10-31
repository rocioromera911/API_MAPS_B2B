# API_MAPS_B2B
Este proyecto implementa un pipeline automatizado para la obtención y enriquecimiento de datos de constructoras, inmobiliarias y estudios de arquitectura en Argentina, combinando la API oficial de Google Places con técnicas de data enrichment y procesamiento web.
# 🏗️ Data Enrichment: Constructoras, Inmobiliarias y Arquitectos

## 📌 Descripción general

Este proyecto implementa un **pipeline automatizado de extracción y enriquecimiento de datos** para el sector de la **construcción, inmobiliarias y estudios de arquitectura** en Argentina.  

Utiliza la **API oficial de Google Places** para obtener información pública de empresas (nombre, dirección, teléfono y sitio web), y la complementa con técnicas de **email discovery** y **data enrichment** (Hunter.io, Apollo.io, etc.), generando una base estructurada y lista para análisis o marketing B2B responsable.

---

## ⚙️ Arquitectura del proyecto

┌──────────────────────┐
│ Google Places API │──► Dirección, teléfono, website
└──────────────────────┘
│
▼
┌──────────────────────┐
│ Extracción web │──► Email desde sitio web oficial
│ (BeautifulSoup) │
└──────────────────────┘
│
▼
┌──────────────────────┐
│ Enriquecimiento B2B │──► Emails y datos de contacto
│ (Hunter, Apollo, etc)│
└──────────────────────┘
│
▼
┌───────────────────────────┐
│ Base consolidada en Excel │──► contact_data.xlsx
└───────────────────────────┘

yaml
Copiar código

---

## 🧰 Tecnologías utilizadas

| Área | Herramienta / Librería |
|------|------------------------|
| Extracción de datos | **Google Places API** |
| Procesamiento HTTP | `requests` |
| Parsing HTML | `beautifulsoup4` |
| Limpieza / Exportación | `pandas`, `openpyxl` |
| Enriquecimiento opcional | **Hunter.io API**, **Apollo.io API** |
| Almacenamiento | `Excel (XLSX)` o `CSV` |

---

## 🚀 Características principales

✅ Cumple con los **Términos de Servicio de Google** (usa solo la API oficial).  
✅ Extrae automáticamente **nombre, dirección, teléfono y sitio web**.  
✅ Detecta correos electrónicos públicos en los sitios oficiales.  
✅ Exporta resultados a **Excel** con formato limpio y utilizable.  
✅ Permite integrar **APIs de enriquecimiento** (Hunter, Apollo, etc.).  
✅ Configurable por **ciudad, categoría y radio de búsqueda**.  

---

## 🧩 Estructura del repositorio

📂 data_enrichment_construccion/
├── buscar_contactos_maps.py # Script principal (Google Places + email scraping)
├── enrich_hunter_api.py # (opcional) Integración con Hunter.io
├── requirements.txt # Dependencias del proyecto
├── sample_output.xlsx # Ejemplo de salida generada
└── README.md # Documentación del proyecto

yaml
Copiar código

---

## 🔧 Instalación y uso

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tuusuario/data-enrichment-construccion.git
cd data-enrichment-construccion
2️⃣ Instalar dependencias
bash
Copiar código
pip install -r requirements.txt
3️⃣ Configurar API Key de Google
Crear una API Key en Google Cloud Console.

Activar el servicio Places API.

Reemplazar TU_API_KEY_AQUI en buscar_contactos_maps.py.

4️⃣ Ejecutar el script principal
bash
Copiar código
python buscar_contactos_maps.py
5️⃣ Revisar el resultado
Se generará un archivo:

Copiar código
contactos_cba.xlsx
con las columnas:

Categoría	Nombre	Dirección	Teléfono	Website	Email	Place_ID

🌐 Enriquecimiento adicional (opcional)
Podés ampliar los datos con herramientas de data enrichment B2B como:

Servicio	Qué hace	Plan gratuito
Hunter.io	Encuentra emails asociados a dominios	25 búsquedas/mes
Apollo.io	Emails y datos de decisión de empresas	plan free limitado
Lusha	Enriquecimiento de contactos B2B	5 créditos gratis
Snov.io	Búsqueda y verificación de emails	50 créditos free

Solo necesitás subir el Excel generado y configurar la búsqueda de correos a partir del campo Website.

🔒 Cumplimiento y ética
⚠️ Este proyecto no realiza scraping directo sobre Google Maps ni vulnera políticas.
Toda la información proviene de:

La API oficial de Google Places.

Sitios web públicos y accesibles de las empresas.

El uso de estos datos debe respetar las leyes de protección de datos y comunicación comercial (Ley 25.326 / LSSI / GDPR).
Solo se recomienda utilizar esta información para fines profesionales, institucionales o de análisis.

🌱 Próximas mejoras
Integración con Hunter.io API para enriquecer emails faltantes.

Dashboards de métricas (porcentaje con contacto completo).

Pipeline automatizado en n8n o Airflow.

Carga directa a CRM (HubSpot, Airtable o Notion).

👩‍💻 Autora
Rocío Romera
📊 Data Science & Automation Projects
💻 GitHub • 🌐 LinkedIn

