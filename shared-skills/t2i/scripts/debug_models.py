# -*- coding: utf-8 -*-
import requests
import json

url = "https://modelscope.cn/api/v1/dolphin/models"
headers = {"Content-Type": "application/json"}
payload = {
    "PageSize": 30,
    "PageNumber": 1,
    "SortBy": "Default",
    "Target": "",
    "Criterion": [
        {"category": "support_pai_model_gallery", "predicate": "contains", "values": ["deploy"]},
        {"category": "tasks", "predicate": "contains", "values": ["text-to-image-synthesis"], "sub_values": []}
    ],
    "SingleCriterion": [
        {"category": "inference_type", "DateType": "int", "predicate": "equal", "IntValue": 1}
    ]
}

response = requests.put(url, headers=headers, json=payload)
data = response.json()

models = data.get("Data", {}).get("Model", {}).get("Models", [])
for m in models:
    print("Model:", m.get("Name"))
    print("  BackendSupport:", json.dumps(m.get("BackendSupport", {}), indent=2))
    print()
