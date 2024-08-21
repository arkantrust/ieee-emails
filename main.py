# Enviar emails de bienvenida a nuevos miembros del IEEE ICESI

from members import get_all, Member
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
import ssl
import smtplib

load_dotenv()

email_sender = os.getenv('ADDRESS')
email_password = os.getenv('PASSWORD')
wpp_link = os.getenv('GROUP_LINK')
discord_link = os.getenv('DISCORD_LINK')

def send_email(member: Member):
  membership_msg = ""
  if not member.membership:
    membership_msg = """<p>
    Te animamos a considerar adquirir la membresía oficial del IEEE a través
      de su <a href=\"https://www.ieee.org/membership/join/index.html\" >sitio web</a>.
      Ser miembro te brindará acceso a recursos exclusivos y oportunidades de crecimiento profesional.
    </p>"""
  subject = f"¡Bienvenido a la Rama Estudiantil IEEE ICESI, {member.name}!"
  body = f"""
  <html>
  <body>
    <h2>Hola, {member.name}!</h2>
    <p>Es un placer darte la bienvenida a la <b>Rama Estudiantil del IEEE ICESI</b>. Estamos muy entusiasmados de tenerte como parte de nuestra pequeña comunidad.</p>
    {membership_msg}
    <p>Para mantenernos en contacto y coordinar actividades, te invitamos a unirte a nuestro <a href="{wpp_link}">grupo de WhatsApp</a> y <a href="{discord_link}">servidor de Discord</a>.</p>
    <p>¡Esperamos verte pronto en nuestras próximas reuniones y eventos!</p>
    <p>Saludos cordiales,<br>
    <b>David Dulce</b><br>
    Recursos Humanos y Relaciones Externas<br>
    ICESI IEEE Student Branch<br>
    +57 3505307859
  </body>
  </html>
  """

  html_msg = MIMEText(body, "html", "utf-8")
  html_msg["Subject"] = subject
  html_msg["From"] = email_sender
  html_msg["To"] = member.email

  context = ssl.create_default_context

  with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, member.email, html_msg.as_string())
  print('Se envió a: ' + member.email)

members = get_all()

for each in members:
  send_email(each)