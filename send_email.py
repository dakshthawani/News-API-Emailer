import ssl
import smtplib
import os


def send_mail(message):
    username = "dakshthawani70@gmail.com"
    password = os.getenv("PASSWORD")
    user_email = "tanishkashukla45@gmail.com"
    host = 'smtp.gmail.com'
    port = 465
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, user_email, message)
