from dataclasses import dataclass
import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


def _env_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "sim", "on"}


@dataclass(frozen=True)
class Settings:
    appium_server_url: str = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")
    android_udid: str = os.getenv("ANDROID_UDID", "")
    android_device_name: str = os.getenv("ANDROID_DEVICE_NAME", "Android")
    app_package: str = os.getenv("APP_PACKAGE", "")
    wait_seconds: int = int(os.getenv("WAIT_SECONDS", "10"))
    no_reset: bool = _env_bool("NO_RESET", True)
    first_name: str = os.getenv("TEST_FIRST_NAME", "Usuario")
    last_name: str = os.getenv("TEST_LAST_NAME", "Teste")
    document: str = os.getenv("TEST_DOCUMENT", "000000000")
    phone: str = os.getenv("TEST_PHONE", "11900000000")
    email: str = os.getenv("TEST_EMAIL", "teste@example.com")
    reference: str = os.getenv("TEST_REFERENCE", "Endereco de teste")
    additional_info: str = os.getenv(
        "TEST_ADDITIONAL_INFO", "Registro gerado para teste automatizado"
    )


settings = Settings()
