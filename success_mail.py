import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
sender_email = "Apekshagarwal369@gmail.com"
sender_password = # "Enter your Password"
receiver_email = "Apekshagarwal8@gmail.com"
s.login(sender_email, sender_password ) 
  
# message to be sent 
message = '''\
Subject: Build Success
Hello, 
      Developer this is an email regarding your last commit. Your last commit was taken into consideration and based on that the trained model has given best accuracy .
Congratulations on your success.
			THANK YOU ...'''
  
# sending the mail 
s.sendmail(sender_email,receiver_email , message) 
  
# terminating the session 
s.quit() 
