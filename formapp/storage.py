import json
from pathlib import Path
from typing import Any


def save_submission(file_path: Path, payload: dict[str, Any]) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if file_path.exists():
        with file_path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
        if not isinstance(data, list):
            data = []
    else:
        data = []

    data.append(payload)

    with file_path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2)
