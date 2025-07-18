from app.main import app
import json, pathlib
p = pathlib.Path("openapi.json")
p.write_text(json.dumps(app.openapi(), indent=2))
print("Wrote", p)
