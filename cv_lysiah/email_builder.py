import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from . import settings


def send(sender_address,receiver_address,sender_pass,mail_content,object_mail,to_me):
      
    try:
      workpath = os.path.dirname(os.path.abspath(__file__)) 
      #Setup the MIME
      print('sender email : '+sender_address)
      print("send email to")
      print(receiver_address)
      message = MIMEMultipart()
      message['From'] = sender_address
      message['To'] = receiver_address
      message['Subject'] = object_mail
      #The subject line
      #The body and the attachments for the mail
      message.attach(MIMEText(mail_content, 'plain'))
      if not to_me:   
         attach_file_name = '../static/imagecv/cv_lysiah.pdf'
         attach_file = open(os.path.join(workpath, attach_file_name), 'rb') # Open the file as binary mode
         #payload = MIMEBase('application', 'octate-stream')
         payload = MIMEBase('application', 'application/pdf')
         payload.set_payload((attach_file).read())
         encoders.encode_base64(payload) #encode the attachment
         #add payload header with filename
         payload.add_header('Content-Disposition', 'attachment', filename="cv-lysiah.pdf")
         message.attach(payload)
      #Create SMTP session for sending the mail
      session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
      session.starttls() #enable security
      session.login(sender_address, sender_pass) #login with mail_id and password
      text = message.as_string()
      session.sendmail(sender_address, receiver_address, text)
      session.quit()
      print('Mail Sent')
    except Exception as e:
      print("Errreur d'envoi de mail au visiteur")
      print(e)
      return False;
    return True;



def send_mail_to_client(emailreceiver,nom):

    object_mail='CV Lysiah Mengue conceptrice logiciel'
    mail_content = "Bonjour "+nom+" merci de m'avoir contacter. \nVeuillez trouver ci-joint mon  CV. \n\nCordialement.\n\n\nLysiah MENGUE\nConceptrice logiciel Python\nTel : +33614127301"
    return send(settings.MON_MAIL,emailreceiver,settings.MON_MOT_DE_PASSE,mail_content,object_mail,False);

def send_mail_to_me(nom,object_mail,mail_content,emailreceiver):
    mail_body = "Nom du visiteur : "+nom+"\nEmail du visiteur : "+emailreceiver+"\nContenu du mail : "+mail_content
    return send(settings.MON_MAIL,settings.MON_MAIL,settings.MON_MOT_DE_PASSE,mail_body,object_mail,True); 


