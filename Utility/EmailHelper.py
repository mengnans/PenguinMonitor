import urllib.request
import json
import smtplib
import time
import sys


class EmailHelper:

    @staticmethod
    def SendEmail(argReceiverAddress, argSubject, argContent):
        try:
            _server = smtplib.SMTP("smtp.gmail.com:587")
            _server.starttls()
            _server.login("penguinpi5887@gmail.com", "raspberryc")
            _message = 'Subject: {}\n\n{}'.format(argSubject, argContent)
            _server.sendmail("penguinpi5887@gmail.com", argReceiverAddress, _message)
            _server.quit()
            return True
        except:
            return False;

    @staticmethod
    def SendEmailToCS(argSubject, argContent):
        EmailHelper.sendEmail("rChansey5887@gmail.com", argSubject, argContent)
        EmailHelper.sendEmail("thundersmn@outlook.com", argSubject, argContent)
