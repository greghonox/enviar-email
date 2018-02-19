#coding:utf-8
import smtplib

#credenciais
remetente = "origem@gmail.com"
senha = "senha"

#desativar a configuração de envio do google
#https://myaccount.google.com/lesssecureapps?hl=pt-BR&pli=1
# Informações da mensagem
destinatario = 'dest@gmail.com'
assunto      = 'Enviando email com python'
texto        = 'Esse email foi enviado usando python! :)'

# Preparando a mensagem
msg = '\r\n'.join([
  'From: %s' % remetente,
  'To: %s' % destinatario,
  'Subject: %s' % assunto,
  '',
  '%s' % texto
  ])

  # Enviando o email
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(remetente,senha)
server.sendmail(remetente, destinatario, msg)
server.quit()

