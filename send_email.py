import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "manjhipawankumar26@gmail.com"
    password = "wlwjknmijcigfksy"

    receiver = "manjhipawankumar26@gmail.com"
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)



