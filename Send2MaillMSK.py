import smtplib
import pandas as pd
import pytz
import datetime
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def Send2Mail(FileName,sender_email, recipient_email, subject, body):
    #https://github.com/aws/aws-sdk-js/issues/893
    
    sender_password = "abcdefghijklmnop"  #COPIE E COLE ENTRE AS ASPAS A SUA SENHA DE API GERADA
    with open(FileName, 'rb') as f:
        image_part = MIMEImage(f.read())
    message = MIMEMultipart()        
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    html_part = MIMEText(body)
    message.attach(html_part)
    message.attach(image_part)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        datetime_br= datetime.now(pytz.timezone('America/Sao_Paulo'))                
        msgRESP = 'Enviado para: ' + str(recipient_email) + ' em: ' + str(datetime_br.strftime('%d/%m/%Y %H:%M:%S'))
        return msgRESP

def IsNiver(data):
  from datetime import datetime
  # storing the current time in the variable
  c = datetime.now()
  df = pd.to_datetime(data, format='%m/%d/%Y')
  d = pd.to_datetime(c,format='%Y-%m-%d')
  if df.month == d.month and df.day == d.day:
    return True
  else:
    return False
