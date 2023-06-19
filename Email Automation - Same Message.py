import smtplib
import pandas as pd  # install pandas using pip install in CMD
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
email_list = pd.read_csv("emaillist.csv")
all_emails = email_list['Email']
all_names = email_list['Names']

from_addr = 'xyz@gmail.com' # add the senders Email Address Here.
msg= MIMEMultipart()
msg['From'] = from_addr
msg['To']= ",".join(all_emails)
msg['subject']= 'Test Mail'

body="This my test programme for Email Automation project" # add body of the common message 

msg.attach(MIMEText(body, 'plain'))

email = "xyz@gmail.com" # Enter senders Email ID for Login to Gmail SMTP Server
password = "qwerty123" # Enter senders app password which is generated using google settings for the senders email.

mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login(email, password)
text = msg.as_string()
mail.sendmail(from_addr, all_emails, text)
print("message sent to "+ all_names+ " Succesfully")
mail.quit()