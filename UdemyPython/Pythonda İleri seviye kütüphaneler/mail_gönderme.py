import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


mesaj=MIMEMultipart()

mesaj["From"] ="thesezerkahraman@gmail.com"
mesaj["To"] ="kaankahraman44@gmail.com"
mesaj["Subject"] ="Smtp Mail Gönderme Denemesi"

yazi="""

Smtp ile mail gönderiyorum.

Sezer Kahraman


"""

mesaj_govdesi=MIMEText(yazi,"plain")
mesaj.attach(mesaj_govdesi)

try:
    mail=smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("thesezerkahraman@gmail.com","laksz190544")
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    print("Mail basarıyla gönderildi")
    mail.close()
except:
    sys.stderr.write("Bir hata olustu")
    sys.stderr.flush()