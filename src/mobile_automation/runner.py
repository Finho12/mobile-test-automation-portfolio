import random
import traceback
from pathlib import Path

from mobile_automation.config import PROJECT_ROOT
from mobile_automation.data_loader import load_records
from mobile_automation.driver_factory import create_driver
from mobile_automation.page_objects.complaint_form_page import ComplaintFormPage
from mobile_automation.reporting import write_results


def ask_test_quantity() -> int:
    while True:
        try:
            quantity = int(input("Quantas vezes deseja repetir o teste? "))
            if quantity > 0:
                return quantity
            print("Digite uma quantidade maior que zero.")
        except ValueError:
            print("Digite um número inteiro válido.")


def execute_case(driver, record: dict[str, str], test_number: int) -> dict:
    """Ponto central para o fluxo; complete as etapas específicas do app autorizado."""
    page = ComplaintFormPage(driver)
    page.open_form()

    # Integre aqui as etapas do cenário depois de configurar os Page Objects.
    # Não use coordenadas fixas quando houver seletores estáveis disponíveis.
    page.click_next()

    return {
        "test_number": test_number,
        "status": "SUCCESS",
        "record_id": record["record_id"],
        "message": "Fluxo de demonstração executado.",
    }


def main() -> None:
    quantity = ask_test_quantity()
    data_path = PROJECT_ROOT / "data" / "sample_records.csv"
    records = load_records(data_path)
    if not records:
        raise ValueError("O CSV não contém registros de teste válidos.")

    driver = create_driver()
    results = []
    try:
        for test_number in range(1, quantity + 1):
            record = random.choice(records)
            print(f"\n{'=' * 55}\nExecutando teste {test_number}/{quantity}")
            print(f"Registro selecionado: {record['record_id']}")
            try:
                results.append(execute_case(driver, record, test_number))
            except Exception as error:
                print(f"Falha no teste {test_number}: {type(error).__name__}: {error}")
                traceback.print_exc()
                results.append({
                    "test_number": test_number,
                    "status": "ERROR",
                    "record_id": record["record_id"],
                    "message": f"{type(error).__name__}: {error}",
                })
    finally:
        driver.quit()

    report_path = write_results(results)
    successes = sum(item["status"] == "SUCCESS" for item in results)
    failures = len(results) - successes
    print(f"\nExecução finalizada: {successes} sucesso(s), {failures} falha(s).")
    print(f"Relatório: {report_path}")


if __name__ == "__main__":
    main()
