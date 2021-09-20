import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
listener = sr.Recognizer()
#smtp==simple mail transfer protocol
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

 def send_email(receiver,subject,message):
     server = smtplib.SMTP('smtp.gmail.com',587)
     server.starttls()
     # tls == transport layer security
     server.login('soloranger21@gmail.com','password')
     email = EmailMessage()
     email['From']='soloranger21@gmail.com'
     email['To']= receiver
     email['Subject']= subject
     email.set_content(message)
     server.send_message(email)
 #diictionary of email list
email_list={
    'raktim': 'raktim20_ug@cse.nits.ac.in',
    'raja': 'rokuongo@gmail.com',


}


def get_email_info():
    talk('To whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver,subject,message)
    talk('Hey buddy, your email was sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()

get_email_info()