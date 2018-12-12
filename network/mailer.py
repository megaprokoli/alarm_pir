import smtplib
from email.mime.text import MIMEText


class Mailer(smtplib.SMTP):

    def __init__(self, snd_addr, recv_addr, pwd, sock):
        super().__init__(sock[0], sock[1])

        self.snd_addr = snd_addr
        self.recv_addr = recv_addr

        self.starttls()
        self.login(self.snd_addr, pwd)  # TODO Error handling

        del pwd

    def send_msg(self, msg):
        message = MIMEText(msg)

        message["From"] = self.snd_addr
        message["To"] = self.recv_addr
        message["Subject"] = "ALARM"

        msg_full = message.as_string()

        self.sendmail(self.snd_addr, self.recv_addr, msg_full)

    def kill(self):
        self.quit()
