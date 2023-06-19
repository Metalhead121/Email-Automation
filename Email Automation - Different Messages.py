import smtplib
import pandas as pd # install pandas using pip install in CMD
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
email_list = pd.read_csv("emaillist.csv")
all_names = email_list['Names']
all_emails = email_list['Email']
all_subjects = email_list['Subject']
all_messages = email_list['Message']
for idx in range(len(all_emails)): 
    from_addr = 'xyz@gmail.com' # add the senders Email Address Here.
    msg= MIMEMultipart()
    msg['From'] = from_addr
    msg['To']= all_emails[idx]
    msg['subject']=all_subjects[idx]
    body=all_messages[idx]
    msg.attach(MIMEText(body, 'plain'))
    email = "xyz@gmail.com" # Enter senders Email ID for Login to Gmail SMTP Server
    password = "qwerty123" # Enter senders app password which is generated using google settings for the senders email.
    mail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    mail.ehlo()
    #mail.starttls()
    mail.login(email, password)
    text = msg.as_string()
    mail.sendmail(from_addr, all_emails[idx], text)
    print("message sent to "+ all_names[idx]+ " Succesfully")
    mail.quit()



