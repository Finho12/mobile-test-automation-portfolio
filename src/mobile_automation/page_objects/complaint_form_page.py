from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy

from mobile_automation.config import settings


class ComplaintFormPage:
    """Page Object de exemplo; substitua os seletores pelos do app autorizado."""

    # Placeholders deliberados: configure os seletores após inspecionar o app.
    OPEN_FORM_ACCESSIBILITY_ID = "CONFIGURAR_SELETOR_ABRIR_FORMULARIO"
    NEXT_BUTTON_ACCESSIBILITY_ID = "CONFIGURAR_SELETOR_PROXIMO"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.wait_seconds, poll_frequency=0.2)

    def _require_configured_selector(self, selector: str) -> None:
        if selector.startswith("CONFIGURAR_"):
            raise NotImplementedError(
                "Há seletores placeholder. Configure os seletores do app de teste "
                "em complaint_form_page.py antes de executar o fluxo."
            )

    def open_form(self) -> None:
        self._require_configured_selector(self.OPEN_FORM_ACCESSIBILITY_ID)
        button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, self.OPEN_FORM_ACCESSIBILITY_ID)
            )
        )
        button.click()

    def click_next(self) -> None:
        self._require_configured_selector(self.NEXT_BUTTON_ACCESSIBILITY_ID)
        button = self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, self.NEXT_BUTTON_ACCESSIBILITY_ID)
            )
        )
        button.click()
