from playwright.sync_api import sync_playwright
import pandas as pd
import time

consultas = [
    "constructoras Córdoba capital Argentina",
    "inmobiliarias Córdoba capital Argentina",
    "arquitectos Córdoba capital Argentina"
]

def scroll_panel(page):
    """Hace scroll en el panel lateral para cargar más resultados"""
    last_height = 0
    while True:
        page.evaluate("document.querySelector('div[role=\"feed\"]').scrollBy(0, 800)")
        time.sleep(1)
        new_height = page.evaluate("document.querySelector('div[role=\"feed\"]').scrollTop")
        if new_height == last_height:
            break
        last_height = new_height

def extraer_resultados(page):
    """Extrae los resultados visibles del panel lateral"""
    elementos = page.locator("div.Nv2PK.tH5CWc.THOPZb")
    data = []

    for i in range(elementos.count()):
        try:
            e = elementos.nth(i)

            nombre = e.locator("div.qBF1Pd.fontHeadlineSmall").inner_text() if e.locator("div.qBF1Pd.fontHeadlineSmall").count() > 0 else ""
            categoria = e.locator("div.W4Efsd span span").first.inner_text() if e.locator("div.W4Efsd span span").count() > 0 else ""
            direccion = e.locator("div.W4Efsd span span:nth-child(2)").first.inner_text() if e.locator("div.W4Efsd span span:nth-child(2)").count() > 0 else ""
            telefono = e.locator(".UsdlK").inner_text() if e.locator(".UsdlK").count() > 0 else ""
            sitio = e.locator("a[href^='http']").first.get_attribute("href") if e.locator("a[href^='http']").count() > 0 else ""
            rating = e.locator("span.MW4etd").inner_text() if e.locator("span.MW4etd").count() > 0 else ""
            descripcion = e.locator("div.ah5Ghc span").inner_text() if e.locator("div.ah5Ghc span").count() > 0 else ""
            link_maps = e.locator("a[href*='/maps/place/']").first.get_attribute("href") if e.locator("a[href*='/maps/place/']").count() > 0 else ""

            # Mostrar en terminal
            print(f"🏢 {nombre}")
            print(f"   🏷️ {categoria} | ⭐ {rating}")
            print(f"   📍 {direccion} | 📞 {telefono}")
            print(f"   🌐 {sitio}")
            print(f"   📝 {descripcion}")
            print(f"   🔗 {link_maps}\n")

            data.append({
                "Nombre": nombre,
                "Categoría": categoria,
                "Dirección": direccion,
                "Teléfono": telefono,
                "Sitio web": sitio,
                "Rating": rating,
                "Descripción": descripcion,
                "Link Google Maps": link_maps
            })
        except Exception as err:
            print("❌ Error al leer un resultado:", err)
    return data

def main():
    resultados = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        for consulta in consultas:
            print(f"\n🔎 Buscando: {consulta}")
            page.goto("https://www.google.com/maps", timeout=60000)
            time.sleep(2)

            page.fill("input#searchboxinput", consulta)
            page.click("button#searchbox-searchbutton")
            time.sleep(5)

            scroll_panel(page)
            resultados_parciales = extraer_resultados(page)
            print(f"🧾 {len(resultados_parciales)} resultados encontrados para '{consulta}'\n")
            resultados.extend(resultados_parciales)

        browser.close()

    df = pd.DataFrame(resultados)
    df.to_excel("resultados_maps.xlsx", index=False)
    print("✅ Resultados guardados en 'resultados_maps.xlsx'")

if __name__ == "__main__":
    main()
