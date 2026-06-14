from pathlib import Path
from xml.etree import ElementTree as ET

sitemap = Path("public/sitemap.xml")
root = ET.fromstring(sitemap.read_text(encoding="utf-8"))
ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
urls = [node.find("sm:loc", ns).text for node in root.findall("sm:url", ns)]

assert len(urls) >= 50, f"sitemap should include content pages, got only {len(urls)} URLs"
assert "https://ksorok.in/" in urls, "home page missing from sitemap"
assert "https://ksorok.in/about/" in urls, "about page missing from sitemap"
assert "https://ksorok.in/posts/how-to-stream-shared-folder-vlc/" in urls, "VLC post missing from sitemap"
assert "https://ksorok.in/posts/gemini-cli-setup-guide/" in urls, "Gemini CLI post missing from sitemap"
print("Sitemap contract passed")
