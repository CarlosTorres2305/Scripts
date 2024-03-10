import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def preencher_formulario():
    # Inicializar o driver do Chrome
    driver = webdriver.Chrome()

    try:
        # Navegar até a página do formulário
        driver.get("https://forms.office.com/r/7CCRzPy7L4")

        # Encontrar o campo de texto usando aria-labelledby
        #campo_texto = WebDriverWait(driver, 10).until(
        #    EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-labelledby*='QuestionId']"))
        #)

        campo_pergunta1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-labelledby*='QuestionId_r5876721cfdeb47d49582d3ac563f8537 QuestionInfo_r5876721cfdeb47d49582d3ac563f8537']"))
        )
        campo_pergunta1.send_keys("Seu Nome")

        # Encontrar e preencher a segunda pergunta (se estiver em sequência)
        campo_pergunta2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-labelledby*='QuestionId_rac714ed604ff4c409f9f00274d2d940f QuestionInfo_rac714ed604ff4c409f9f00274d2d940f']"))
        )
        campo_pergunta2.send_keys("SEU CPF")

        # Encontrar e preencher a terceira pergunta (se estiver em sequência)
        campo_pergunta3 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-labelledby*='QuestionId_r9a1b82a238b74c3db18c29b7ce6b7fa0 QuestionInfo_r9a1b82a238b74c3db18c29b7ce6b7fa0']"))
        )
        campo_pergunta3.send_keys("SEU TELEFONE")
        

        #Selecionar a opção 2 conforme CSS encontrado
        checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[value*='ALT T4 - 00h às 08h20 ( uber de ida)']"))
        )
        checkbox.click()

        
        #Enviar formulário
        botao_enviar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-automation-id='submitButton']"))
        )
        botao_enviar.click()

    finally:
        # Fechar o navegador no final 
        driver.quit()

# Chamar a função
preencher_formulario()
