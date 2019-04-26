import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



from_address = "ralluri@itstrategists.com"
password = "Rakesh@Varma123"
receivers = ["narendra.kommoju@ggktech.com"]
msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = ','.join(receivers)
msg['Subject'] = "SUBJECT OF THE MAIL"

body = "YOUR MESSAGE HERE"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_address, password)
text = msg.as_string()
server.sendmail(from_address, receivers, text)
server.quit()