import json
from pathlib import Path


template = """---
title: "{title}"
---

{shortcode}
"""

with open("data/index.json") as f:
    data = json.load(f)

for dataset, info in data["data"].items():
    print(dataset)
    path = Path("content", "dados", dataset + ".md")
    title = f"Dados: {dataset.upper()}"
    dataset = dataset.replace("-", "_")
    shortcode = '{{< remote-files-table "data" "' + dataset.replace("-", "_") + '" >}}'
    path.write_text(template.format(title=title, shortcode=shortcode), encoding="utf-8")

for dataset, info in data["auxiliary"].items():
    print(dataset)
    path = Path("content", "auxiliares", dataset + ".md")
    title = f"Auxiliares: {dataset.upper()}"
    shortcode = (
        '{{< remote-files-table "auxiliary" "' + dataset.replace("-", "_") + '" >}}'
    )
    path.write_text(template.format(title=title, shortcode=shortcode), encoding="utf-8")

for dataset, info in data["documentation"].items():
    print(dataset)
    path = Path("content", "documentacao", dataset + ".md")
    title = f"Documentação: {dataset.upper()}"
    shortcode = (
        '{{< remote-files-table "documentation" "' + dataset.replace("-", "_") + '" >}}'
    )
    path.write_text(template.format(title=title, shortcode=shortcode), encoding="utf-8")
