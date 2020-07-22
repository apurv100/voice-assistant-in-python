import smtplib

sender = 'apurva.somu@gmail.com'
receivers = ['apurv.harsh08@gmail.com']

message = 'hekko just a test mssg'

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")