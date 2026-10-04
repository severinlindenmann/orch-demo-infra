"""Demo infra check: every JSON file parses and every job carries tags.cost_center."""
import json
import pathlib
import sys

bad = []
for p in sorted(pathlib.Path(".").glob("*/*.json")):
    try:
        data = json.loads(p.read_text())
    except json.JSONDecodeError as e:
        bad.append(f"{p}: {e}")
        continue
    if p.parts[0] == "jobs" and not (data.get("tags") or {}).get("cost_center"):
        bad.append(f"{p}: tags.cost_center is required")
print("\n".join(bad) or "ok")
sys.exit(1 if bad else 0)
