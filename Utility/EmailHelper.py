#! python3

import urllib.request
import json
import smtplib
import time
import sys


class EmailHelper:

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
   
   def SendEmailToCS(argSubject,argContent):
      sendEmail("rChansey5887@gmail.com", argSubject, argContent)
      sendEmail("thundersmn@outlook.com", argSubject, argContent)