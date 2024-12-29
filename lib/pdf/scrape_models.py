import json
from pathlib import Path

class BaseScraper:
    def __init__(self, file_name: Path | str, rows: list[tuple[str, ...]]):
        self.file_name = file_name
        self.rows = rows
        self.structured = {}

    def structure(self):
        for index, row in enumerate(self.rows, start=1):
           self.structured[f"Page {index}"] = row

        path = Path("semi-structured-data")
        path = path / f"{self.file_name.stem}.json"
        with path.open("w") as semi_structured:
            json.dump(self.structured, semi_structured)
