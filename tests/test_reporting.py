import csv

from mobile_automation.reporting import write_results


def test_write_results_creates_csv(tmp_path):
    output = tmp_path / "results.csv"
    results = [
        {
            "test_number": 1,
            "status": "SUCCESS",
            "record_id": "DEMO-001",
            "message": "ok",
        },
        {
            "test_number": 2,
            "status": "ERROR",
            "record_id": "DEMO-002",
            "message": "erro simulado",
        },
    ]

    created = write_results(results, output)
    assert created == output

    with output.open(encoding="utf-8-sig", newline="") as file:
        rows = list(csv.DictReader(file))

    assert len(rows) == 2
    assert rows[0]["status"] == "SUCCESS"
    assert rows[1]["message"] == "erro simulado"
