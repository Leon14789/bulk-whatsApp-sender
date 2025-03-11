import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from data import textoDaMensagem, path_chromedriver



# Configurar o WebDriver do Chrome
service = Service(path_chromedriver)
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=/tmp/chrome-profile")  # Mantém a sessão do Chrome
driver = webdriver.Chrome(service=service, options=options)

# Carregar a tabela de contatos
contatos_df = pd.read_csv("contatos.csv")

# Mensagem que você deseja enviar
mensagem = textoDaMensagem 

# Abrir o WhatsApp Web
driver.get("https://web.whatsapp.com")
print("Escaneie o QR code do WhatsApp Web para continuar...")
time.sleep(15)  # Tempo para escanear o QR code

# Função para enviar a mensagem
def enviar_mensagem_whatsapp(telefone, mensagem):
    try:
        # Abrir o link direto do WhatsApp
        driver.get(f"https://web.whatsapp.com/send?phone={telefone}&text={mensagem}")
        time.sleep(10)  # Esperar a página carregar

        # Enviar a mensagem
        input_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        input_box.send_keys(Keys.ENTER)
        print(f"Mensagem enviada para {telefone} com sucesso!")
        time.sleep(10)  # Esperar 5 segundos entre cada envio
    except Exception as e:
        print(f"Erro ao enviar mensagem para {telefone}: {e}")

# Iterar sobre os contatos e enviar a mensagem
for index, contato in contatos_df.iterrows():
    nome = contato["Nome"]
    telefone = contato["Telefone"]
    
    # Personaliza a mensagem com o nome do contato
    mensagem_personalizada = mensagem.replace("pessoal", nome)
    
    # Envia a mensagem
    enviar_mensagem_whatsapp(telefone, mensagem_personalizada)

print("Todas as mensagens foram enviadas!")
driver.quit()