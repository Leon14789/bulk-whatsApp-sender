<div align="center">

# 📱 Bulk WhatsApp Sender

![Automated WhatsApp Messaging](https://img.shields.io/badge/Python-3.x-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

</div>

## 📌 Descrição do Projeto
Este projeto automatiza o envio de mensagens personalizadas no WhatsApp utilizando **Python, Selenium e Pandas**. Foi desenvolvido para enviar mensagens em massa para uma lista de contatos, como ex-alunos de uma instituição de ensino, permitindo personalização (ex.: inclusão do nome do contato na mensagem).

Ideal para:
✅ Campanhas de marketing  
✅ Lembretes e notificações  
✅ Pesquisas de satisfação e muito mais!

---

## 🚀 Recursos

✔️ **Envio de mensagens personalizadas:** Inclui o nome do contato na mensagem.  
✔️ **Automação via WhatsApp Web:** Utiliza Selenium para controle do navegador.  
✔️ **Leitura de contatos via CSV:** Processa uma lista de contatos de um arquivo CSV.  
✔️ **Fácil configuração:** Basta ajustar o arquivo de contatos e a mensagem desejada.  

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python  
- **Bibliotecas:**  
  - Selenium: Automação do navegador  
  - Pandas: Manipulação de dados  
- **Ferramentas:**  
  - Google Chrome: Navegador utilizado para automação  
  - ChromeDriver: Ponte entre Selenium e Google Chrome  

---

## 📂 Estrutura do Projeto

```bash
whatsapp-message-sender/
├── enviar_mensagens.py   # Script principal de automação
├── contatos.csv          # Arquivo CSV com a lista de contatos
├── README.md             # Documentação do projeto
└── requirements.txt      # Lista de dependências do projeto
```

---

## ⚙️ Como Funciona

1️⃣ **Configuração do Ambiente:**  
   - Instale o Google Chrome e ChromeDriver.  
   - Configure o Selenium para controlar o navegador.

2️⃣ **Leitura dos Contatos:**  
   - O script lê os contatos de um arquivo CSV (`contatos.csv`) contendo os campos `Nome` e `Telefone`.

3️⃣ **Acesso ao WhatsApp Web:**  
   - O script abre o WhatsApp Web e aguarda o usuário escanear o QR code para autenticação.

4️⃣ **Envio das Mensagens:**  
   - Personaliza a mensagem com o nome do contato.
   - Abre uma conversa no WhatsApp Web.
   - Envia a mensagem automaticamente.

5️⃣ **Finalização:**  
   - Após o envio das mensagens, o navegador é fechado automaticamente.

---

## 🛠️ Passo a Passo para Execução

### 📌 Pré-requisitos
✅ Python 3.x  
✅ Google Chrome instalado  
✅ ChromeDriver compatível com a versão do Chrome

### 🔽 Instalação
```bash
git clone https://github.com/seu-usuario/whatsapp-message-sender.git
cd whatsapp-message-sender
pip install -r requirements.txt
```

### ⚙️ Configuração
1. **Prepare o arquivo `contatos.csv`:**
```csv
Nome,Telefone
João Silva,+5511999999999
Maria Souza,+5511888888888
```
2. **Edite o script `enviar_mensagens.py`:**
   - Ajuste o caminho do ChromeDriver.
   - Personalize a mensagem que deseja enviar.

### ▶️ Execução
```bash
python3 enviar_mensagens.py
```
📌 **Importante:** Escaneie o QR code no WhatsApp Web para autenticar e aguarde o envio das mensagens.

---

## 📞 Contato
📧 **Email:** [leonardoortizalves@gmail.com](mailto:leonardoortizalves@gmail.com)  


---

<div align="center">
  <b>🚀 Desenvolvido com Python para facilitar a automação de mensagens no WhatsApp!</b>
</div>

