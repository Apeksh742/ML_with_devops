import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
sender_email = "Apekshagarwal369@gmail.com"
sender_password = "rj14sz7820"
receiver_email = "Apekshagarwal8@gmail.com"
s.login(sender_email, sender_password ) 
  
# message to be sent 
message = '''/
Subject: Build model_train failed
Hello, 
				Developer this is an email regarding your last commit. It seems that your model_train.py is not working properly please check it once and recommit.
			THANK YOU'''
  
# sending the mail 
s.sendmail(sender_email,receiver_email , message) 
  
# terminating the session 
s.quit() 
