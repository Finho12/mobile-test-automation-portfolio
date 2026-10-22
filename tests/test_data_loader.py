import csv
import pytest

from mobile_automation.data_loader import load_records


def test_load_records_ignores_blank_ids(tmp_path):
    csv_file = tmp_path / "records.csv"
    csv_file.write_text(
        "record_id,description\nA-1,Primeiro\n ,Sem ID\nA-2,Segundo\n",
        encoding="utf-8",
    )

    assert load_records(csv_file) == [
        {"record_id": "A-1", "description": "Primeiro"},
        {"record_id": "A-2", "description": "Segundo"},
    ]


def test_load_records_requires_expected_header(tmp_path):
    csv_file = tmp_path / "invalid.csv"
    csv_file.write_text("id,name\n1,Exemplo\n", encoding="utf-8")

    with pytest.raises(ValueError, match="record_id"):
        load_records(csv_file)


def test_load_records_missing_file():
    with pytest.raises(FileNotFoundError):
        load_records("arquivo-que-nao-existe.csv")
