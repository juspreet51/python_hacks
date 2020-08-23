import smtplib
connection = smtplib.SMTP("smtp.gmail.com",587)
connection.ehlo()
connection.starttls()   #start encryption
connection.login('guest51user@gmail.com','12345abc!')
connection.sendmail('guest51user@gmail.com','guest51user@gmail.com','Subject: Hello \n\n A message')
print("Done")
connection.quit()
