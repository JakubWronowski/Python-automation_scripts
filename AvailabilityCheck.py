import os
import requests 
import smtplib
import bs4

###PYTHON CODE CHECKING IF WEBSITE IS AVAILABLE###


#env variables exported 
e_addr = os.environ.get("E_ADRR")
p_word = os.environ.get("P_WORD")

#Sending notification via e mail if wbsite is down 
def notification_email():
    notification = smtplib.SMTP("smtp.gmail.com", 587)
    notification.starttls()
    notification.login(e_addr, pword)
    type_of_info = "Website is down. Actions required!"
    email_message = (f"Type: {type_of_info}")
    notification.sendmail("Sender e-mail", "Reciever e-mail", email_message) ### Replace Sender email and Reciever email with e-mail ids
    notification.quit()



websiteurl = "" ### Place for website URL

#finding out if webpage is available by checking its status_code 
is_available = requests.get(websiteurl, timeout=8)
if is_available.status_code != 200:
    notification_email()

#finding out if webpage is available by checking if specific content is displayed
inspect = bs4.BeautifulSoup(is_available.text, "html.parser")

#copy and paste selector of content 
content = inspect.select("") 

#if statment for veryfing if conten is on webpage
try:
    if content[0].text != "":   ###Place for website content
        notification_email()
except Exception as e:
    notification_email()


