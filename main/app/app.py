from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import base64
import openpyxl
import os 
# Função para salvar o PDF em Base64
def gerar_pdf_base64(pdf_base64, nome_arquivo, pasta_destino):
    try:
        # Certifique-se de que a pasta existe
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        # Caminho completo do arquivo
        arquivo_pdf = os.path.join(pasta_destino, f"{nome_arquivo}.pdf")

        # Salvar o arquivo PDF
        with open(arquivo_pdf, "wb") as pdf_file:
            pdf_file.write(base64.b64decode(pdf_base64))
        print(f"PDF salvo como {arquivo_pdf}")
    except Exception as e:
        print(f"Erro ao salvar o PDF: {e}")

#Extraindo Dados Planilha
workbook = openpyxl.load_workbook("/home/rrxx/Projetos/Automacao_CAC/main/resources/plan.xlsx")
sheet = workbook['Planilha1']
# Definindo Preferências 
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-extensions')
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-browser-side-navigation')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)

# Open a new tab and navigate to the URL
print("Abrindo Site ...")
driver.execute_script("window.open('https://servicos.pf.gov.br/epol-sinic-publico/','_blank')")
print("Carregando 15s ...")
time.sleep(15)
# Switch to the new tab
print("Trocando janela...")
driver.switch_to.window(driver.window_handles[1])
print("Título da Aba :",driver.title)
# Get cookies
print("Coletando Cookies ....")
cookies_gov = driver.get_cookies()
# Capturar cookies do Selenium
cookies = driver.get_cookies()
# Converter cookies para o formato esperado pelo requests
time.sleep(5)
session_cookies = {cookie['name']: cookie['value'] for cookie in cookies}
for row in sheet.iter_rows(min_row=2,min_col=2):
    nome_func = row[0].value
    nome_mom = row[1].value
    cpf = row[2].value
    data_born = row[3].value
    data_born = str(data_born)
    # Remover pontos e traços do CPF
    cpf_formatado = cpf.replace(".", "").replace("-", "")
    # Formatar data de nascimento para o formato "yyyy/MM/dd"
    data_born_f = (f"{data_born[:10]}")

    payload = {
            "cpf": cpf_formatado,
            "nome": nome_func,
            "listaNacionalidade": [24],  # Valor fixo para exemplo
            "dtNascimento": data_born_f,
            "coPaisNascimento": 24,  # Valor fixo para exemplo
            "noUfNascimento": None,
            "noMunicipioNascimento": None,
            "ufNascimento": "DF",  # Valor fixo para exemplo
            "coMunicipioNascimento": "5300108",  # Valor fixo para exemplo
            "nomePai": None,
            "nomeMae": nome_mom,
            "documentoCac": []
        }
    # Cabeçalhos necessários (ajustar conforme necessário)
    headers_get = {
        "User-Agent": driver.execute_script("return navigator.userAgent;"),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    headers_post ={
        "Content-Type":"application/json",
        "User-Agent": driver.execute_script("return navigator.userAgent;"),
        "Accept": "application/json, text/plain, */*",
        "Accept-Language":"pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding":"gzip, deflate, br, zstd",
        "Origin":"https://servicos.pf.gov.br",
        "Referer":"https://servicos.pf.gov.br/epol-sinic-publico/",
        "Connection":"keep-alive",
    }
    time.sleep(5)
    print("Fazendo Requisição GET ....")
    # Fazer a requisição GET usando cookies do Selenium
    url = "https://servicos.pf.gov.br/sinic2-publico-rest/api/siteKey"
    response = requests.get(url, cookies=session_cookies, headers=headers_get)

    print("Status Code:", response.status_code)
    time.sleep(5)
    print("Fazendo Requisição POST ...")
    # Fazendo a requisição POST usando cookies do Selenium
    url_pdf = "https://servicos.pf.gov.br/sinic2-publico-rest/api/cac/gerar-cac-pdf"
    response_post = requests.post(url_pdf,cookies=session_cookies,headers=headers_post,json=payload)
    print("Status Code:", response_post.status_code)
    print("Convertendo de Base64")
    time.sleep(5)
    pdf_base64 = response_post.json().get("pdf")
    pasta = ("Pdfs")
    gerar_pdf_base64(pdf_base64,f"{nome_func}-{cpf}",pasta)