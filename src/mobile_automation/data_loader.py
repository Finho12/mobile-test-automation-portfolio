import csv
from pathlib import Path


def load_records(csv_path: str | Path) -> list[dict[str, str]]:
    """Carrega registros de teste de um CSV com cabeçalho record_id."""
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"Arquivo de dados não encontrado: {path}")

    with path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames or "record_id" not in reader.fieldnames:
            raise ValueError("O CSV precisa conter a coluna obrigatória 'record_id'.")

        records = []
        for row in reader:
            record_id = (row.get("record_id") or "").strip()
            if record_id:
                records.append({
                    "record_id": record_id,
                    "description": (row.get("description") or "").strip(),
                })

    return records
