import markdown
import os

md_folder = "country-guides"
html_folder = "country-guides-html"
os.makedirs(html_folder, exist_ok=True)

for filename in os.listdir(md_folder):
    if filename.endswith(".md"):
        with open(os.path.join(md_folder, filename), "r", encoding="utf-8") as f:
            html = markdown.markdown(f.read(), extensions=["tables", "fenced_code"])
        html_filename = filename.replace(".md", ".html")
        with open(os.path.join(html_folder, html_filename), "w", encoding="utf-8") as f:
            f.write(f"<html><head><meta charset='UTF-8'><title>{html_filename}</title></head><body>{html}</body></html>")

print("✅ HTML versions created in /country-guides-html/")
