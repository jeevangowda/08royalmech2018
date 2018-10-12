import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#Next, log in to the server
server.login("jeevanggowda51@gmail.com", "55113300")
#Send the mail
msg = "Hello!" # The /n separates the message from the headers
server.sendmail("jeevanggowda51@gmail.com", "haripramod92@gmail.com", msg)
server.quit()