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
        country_title = html_filename.replace(".html", "").replace("-", " ").title()

        html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{country_title} HR Guide</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
  <style>
    body {{
      font-family: 'Inter', sans-serif;
      background: linear-gradient(to right, #e3f2fd, #fce4ec);
      color: #2c3e50;
      padding: 2rem;
      max-width: 900px;
      margin: auto;
    }}
    h1 {{
      font-size: 2rem;
      margin-bottom: 1rem;
    }}
    h2 {{
      color: #0078d4;
      margin-top: 2rem;
    }}
    a {{
      color: #0078d4;
      text-decoration: none;
    }}
    code, pre {{
      background: #f4f4f4;
      padding: 0.5rem;
      border-radius: 4px;
      display: block;
      overflow-x: auto;
    }}
    ul, ol {{
      margin-left: 1.5rem;
    }}
    .back-link {{
      margin-top: 2rem;
      display: block;
      font-weight: bold;
    }}
    .footer {{
      margin-top: 3rem;
      font-size: 0.9rem;
      color: #555;
      border-top: 1px solid #ccc;
      padding-top: 1rem;
    }}
  </style>
</head>
<body>
  <h1>{country_title} HR Compliance Guide</h1>
  {html}
  <a class="back-link" href="../index.html">← Back to Global Guide</a>
  <div class="footer">
    <p>👤 Author: Shubham Kadam | <a href="https://www.linkedin.com/in/shubh2r/" target="_blank">LinkedIn</a></p>
    <p>👥 Co-author: Hitika Rathod | <a href="https://www.linkedin.com/in/hitika-rathod-1074702a9/" target="_blank">LinkedIn</a></p>
  </div>
</body>
</html>
"""

        with open(os.path.join(html_folder, html_filename), "w", encoding="utf-8") as f:
            f.write(html_template)

print("✅ Professionally styled HTML versions created in /country-guides-html/")
