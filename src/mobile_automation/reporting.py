import csv
from datetime import datetime
from pathlib import Path
from typing import Iterable

from mobile_automation.config import PROJECT_ROOT

REPORTS_DIR = PROJECT_ROOT / "reports"


def write_results(results: Iterable[dict], output_path: str | Path | None = None) -> Path:
    """Exporta resultados de execução para CSV e retorna o caminho criado."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    path = Path(output_path) if output_path else (
        REPORTS_DIR / f"results_{datetime.now():%Y%m%d_%H%M%S}.csv"
    )
    rows = list(results)
    fieldnames = ["test_number", "status", "record_id", "message"]

    with path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    return path
