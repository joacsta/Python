import smtplib
from email.mime.text import MIMEText

senha = 'iiee qhaw cbas hxna'
lista_destinatarios = []

def menu():
    print(
    """
Olá!

Digite o email de cada pessoa que você deseja enviar o email em lote
    """)

def login():
    menu()
    usuario = input('primeiramente, qual o email do remetente?\n')
    servidor_smtp = 'smtp.gmail.com'
    porta = 587

    servidor = smtplib.SMTP(servidor_smtp, porta)
    servidor.starttls()
    servidor.login(usuario, senha)
    return usuario, servidor

def destinatarios():
    while True:
        entrada = input('adicione aqui os emails dos destinatarios\npara sair tecle [0]\n')
        if entrada == '0':
            break
        else:
            lista_destinatarios.append(entrada)

def escrever_email():
    usuario, servidor = login()
    destinatarios()

    assunto = input('Digite o assunto do email:\n')
    corpo = input('Digite o que estará escrito no corpo do email:\n')
    
    mensagem = MIMEText(corpo)
    mensagem['Subject'] = assunto
    mensagem['From'] = usuario
    mensagem['To'] = ','.join(lista_destinatarios)
    servidor.send_message(mensagem)

    print('\nemail enviado! encerrando...')
    servidor.quit()

escrever_email()