# encoding=utf8

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


class Mailer:

    def send(self,toaddr,subj,html):

        try:
            fromaddr = 'bindexservice@gmail.com'
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = ", ".join(toaddr)
            msg['Subject'] = subj
            msg.attach(MIMEText(html.encode('utf-8'), 'html','utf-8'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, "bindexfunds123")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()
        except Exception as e:
            print str(e)
            pass

    def sendError(self, html):
        toaddr = ['iman@bindexfund.com', 'ethan@bindexfund.com']
        subj = 'New 500 Error'
        self.send(toaddr,subj,html)

    def sendDBUpdate(self, html):
        toaddr = ['ethan@bindexfund.com', 'iman@bindexfund.com']
        subj = 'Database updated with new market data'
        self.send(toaddr,subj,html)
