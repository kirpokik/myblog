from pathlib import Path

root = Path("public")
home = (root / "index.html").read_text(encoding="utf-8")
about = (root / "about" / "index.html").read_text(encoding="utf-8")
robots = (root / "robots.txt").read_text(encoding="utf-8")
sitemap = (root / "sitemap.xml").read_text(encoding="utf-8")

home_desc = "Personal blog by Kostiantyn Sorokin — indie app dev, MVP builder, retro gaming, and real notes from building startups and side projects."
about_desc = "About Kostiantyn Sorokin — indie app dev and MVP builder sharing notes on side projects, tech, retro gaming, and life."
default_img = "https://ksorok.in/images/og-default.png"

assert f'<meta name="description" content="{home_desc}">' in home, "home meta description not updated"
assert f'<meta property="og:description" content="{home_desc}">' in home, "home og description not updated"
assert f'<meta name="twitter:description" content="{home_desc}">' in home, "home twitter description not updated"
assert f'<meta property="og:image" content="{default_img}">' in home, "home default og image missing"
assert f'<meta name="twitter:image" content="{default_img}">' in home, "home default twitter image missing"
assert '<meta name="twitter:card" content="summary_large_image">' in home, "home twitter card not large image"
assert '<link rel="alternate" hreflang="en" href="https://ksorok.in/">' in home, "home hreflang en missing"
assert '<link rel="alternate" hreflang="x-default" href="https://ksorok.in/">' in home, "home hreflang x-default missing"
assert (root / "images" / "og-default.png").exists(), "default png not generated"

assert f'<meta name="description" content="{about_desc}">' in about, "about meta description not updated"
assert f'<meta property="og:description" content="{about_desc}">' in about, "about og description not updated"
assert f'<meta name="twitter:description" content="{about_desc}">' in about, "about twitter description not updated"
assert '<meta property="og:type" content="website">' in about, "about og:type is not website"
assert f'<meta property="og:image" content="{default_img}">' in about, "about default og image missing"
assert '<link rel="alternate" hreflang="en" href="https://ksorok.in/about/">' in about, "about hreflang en missing"
assert '<link rel="alternate" hreflang="x-default" href="https://ksorok.in/about/">' in about, "about hreflang x-default missing"
assert '"@type": "Person"' in about, "about Person schema missing"
assert '"@type": "BlogPosting"' not in about, "about should not emit BlogPosting schema"
assert '"datePublished"' not in about, "about Person schema should not emit article dates"

post_files = sorted((root / "posts").glob("*/index.html"))
assert post_files, "no generated posts found"
post_html = post_files[0].read_text(encoding="utf-8")
assert '<meta property="og:type" content="article">' in post_html, "post og:type article missing"
assert '"@type": "BlogPosting"' in post_html, "post BlogPosting schema missing"
assert '"datePublished"' in post_html, "post BlogPosting dates missing"

assert "<urlset" in sitemap and "https://ksorok.in/" in sitemap, "sitemap missing expected URLs"
assert "Sitemap: https://ksorok.in/sitemap.xml" in robots, "robots sitemap line missing"
print("SEO contracts passed")
