import json
import urllib.request
from pathlib import Path


template = """---
title: "{title}"
---

{shortcode}
"""

BASE_URL = "https://cdn.statically.io/gh/dankkom/datasus-metadata/main/metadata"


index_json_url = BASE_URL + "/index.json"

with urllib.request.urlopen(index_json_url) as response:
    data = json.load(response)

for dataset, info in data["data"].items():
    print(dataset)
    path = Path("content", "dados", dataset + ".md")
    url = BASE_URL + f"/data/{dataset}.json"
    title = f"Dados: {dataset.upper()}"
    shortcode = "{{< remote-data-table \"" + url + "\" >}}"
    path.write_text(template.format(title=title, shortcode=shortcode), encoding="utf-8")

for dataset, info in data["auxiliary"].items():
    print(dataset)
    path = Path("content", "auxiliares", dataset + ".md")
    url = BASE_URL + f"/auxiliary/{dataset}.json"
    title = f"Auxiliares: {dataset.upper()}"
    shortcode = "{{< remote-files-table \"" + url + "\" >}}"
    path.write_text(template.format(title=title, shortcode=shortcode), encoding="utf-8")

for dataset, info in data["documentation"].items():
    print(dataset)
    path = Path("content", "documentacao", dataset + ".md")
    url = BASE_URL + f"/documentation/{dataset}.json"
    title = f"Documentação: {dataset.upper()}"
    shortcode = "{{< remote-files-table \"" + url + "\" >}}"
    path.write_text(template.format(title=title, shortcode=shortcode), encoding="utf-8")
