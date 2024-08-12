import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

acao = input("Digite o código da ação desejada: ")

dados = yfinance.Ticker(acao).history(start="2020-01-01", end="2020-12-31")
fechamento = dados.Close

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

destinatario = "tjlira07@gmail.com"
assunto = "Análise do Projeto 2020"


# para concatenar informacoes dentro da mensagem é so colcoar o f antes das aspas e as chaves, 
# para chamar as variaveis criadas.
mensagem = f"""
Prezado gestor, 

Seguem as análises solicitadas da ação {acao}:

Cotação máxima: R${maxima}
Cotação Mínima: R${minima}
Valor médio: R${valor_medio}

Qualquer dúvida, estou à disposição!

Atte.
"""

# abrir o navegador e ir para o gmail
webbrowser.open("www.gmail.com")
time.sleep(3)

# configurando uma pausa de 3 segundos
pyautogui.PAUSE = 3

# clicar no botão escrever
pyautogui.click(x=2963, y=216)

# digitar o email do destinatário e teclar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar o assunto do email e teclar TAB
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# clicar no btão enviar

pyautogui.click(x=3377, y=993)

# Fechar o g-mail
pyautogui.hotkey("alt", "f4")

print("Email enviado com sucesso!")