import smtplib

server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("manikantagowdab.1si15me078@gmail.com", "Manisit2019@")
server.sendmail("manikantagowdab.1si15me078@gmail.com","shashi.p.reddy434@gmail.com","Oata??")
server.quit()
'''You need to turn on the less security app to access the mail - Go to this link and select Turn On
https://www.google.com/settings/security/lesssecureapps'''