# Mobile Test Automation — Python + Appium

Projeto de portfólio para demonstrar automação de testes mobile Android com Python, Appium, Selenium waits, dados externos em CSV, configuração por variáveis de ambiente e registro dos resultados.

> **Importante:** esta versão é uma refatoração de portfólio e uma base adaptável. Identificadores do aplicativo original, dados reais, UDID do aparelho e seletores específicos foram retirados. Antes de executar um fluxo contra um aplicativo, configure apenas um ambiente em que você tenha autorização para testar.

## O que o projeto demonstra

- Separação de configuração, dados, páginas e execução.
- Leitura de identificadores de teste por CSV.
- Seletores centralizados em um Page Object.
- Esperas explícitas em vez de depender somente de `sleep`.
- Tratamento de falhas por caso de teste.
- Exportação de resultados para CSV.
- Configuração local por `.env`, sem publicar identificadores do dispositivo.
- Testes unitários que podem rodar sem aparelho Android ou servidor Appium.

## Estrutura

```text
mobile-test-automation-portfolio/
├── data/
│   └── sample_records.csv
├── reports/
│   └── .gitkeep
├── screenshots/
│   └── .gitkeep
├── src/
│   └── mobile_automation/
│       ├── __init__.py
│       ├── config.py
│       ├── data_loader.py
│       ├── driver_factory.py
│       ├── page_objects/
│       │   ├── __init__.py
│       │   └── complaint_form_page.py
│       ├── reporting.py
│       └── runner.py
├── tests/
│   ├── test_data_loader.py
│   └── test_reporting.py
├── .env.example
├── .gitignore
├── pytest.ini
└── requirements.txt
```

## Requisitos

- Python 3.10 ou superior
- Android device/emulator com depuração USB ativada
- Appium Server 2.x instalado e iniciado
- Driver Appium UiAutomator2 instalado
- A aplicação Android de teste instalada no dispositivo

## Instalação

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Edite o `.env` e informe os valores do seu ambiente autorizado. Não comite o `.env`.

Inicie o Appium em outro terminal:

```powershell
appium
```

Confira se o Android está conectado:

```powershell
adb devices
```

## Executar testes unitários

```powershell
python -m pytest
```

Os testes unitários não precisam de Appium nem de dispositivo.

## Executar o fluxo mobile

Depois de configurar o `.env`, revise os seletores em `src/mobile_automation/page_objects/complaint_form_page.py` e adapte-os à aplicação de demonstração ou ao ambiente autorizado.

```powershell
$env:PYTHONPATH = "src"
python -m mobile_automation.runner
```

O fluxo é intencionalmente conservador: se um seletor ainda estiver como placeholder, a execução deve falhar com uma mensagem clara em vez de interagir com um elemento desconhecido.

## Dados de teste

O arquivo `data/sample_records.csv` contém identificadores fictícios. Para executar um teste autorizado, use dados de teste fornecidos ou aprovados pelo responsável pelo ambiente. Evite colocar dados pessoais reais em repositórios públicos.

## Relatórios

Cada execução gera um CSV com o número do teste, status, identificador usado e mensagem de erro, em `reports/`.
