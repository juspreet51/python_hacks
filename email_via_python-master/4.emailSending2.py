import smtplib , webbrowser , getpass
def get_mail():
    servicesAvailable = ["gmail"]
    while True:
        mail_id = input("E-Mail: ")
        if '@' in mail_id and '.com' in mail_id:
            symbol_pos = mail_id.find("@")
            dotcom_pos = mail_id.find(".com")
            sp = mail_id[symbol_pos+1:dotcom_pos]
            if sp in servicesAvailable:
                return mail_id , sp
                break
            else:
                print("Service not provided for ",sp)
                print("")
                continue
        else:
            print("Invalie eMail Adress")
            continue
        
def set_smtp_domain(serviceProvider):
    if serviceProvider == 'gmail':
        return 'smtp.gmail.com'
    else:
        return 'Error!\n'

print()
#user_mail , sp = get_mail()
#smtpDomain = set_smtp_domain(sp)
#print(user_mail)

print("Welcome, Send mails through this Program")
print("Please Enter your email address and Password")
e_mail , serviceProvider = get_mail()
print("Your Service Provider is ",serviceProvider)
password=getpass.getpass("Password: ")

while True:
    try:
        smtpDomain = set_smtp_domain(serviceProvider)
        connection = smtplib.SMTP(smtpDomain)
        connection.ehlo()
        connection.starttls()
        connection.login(e_mail , password)
    except:
        if serviceProvider == 'gmail':
            print("Gmail Security Error")
            print("We are oopening up a page, Kid=ndly press Yes and allow the aoo to access gmail")
            answer=input("y/n?")
            if(answer == "yes"):
                webbrowser.open("https://myaccount.google.com/lesssecureapps")
            else:
                print("Retype Your Password:-\n")
                e_mail , serviceProvider = get_mail()
                password = getpass.getpass("Password:- ")
                continue
        else:
            print("Login Unsuuccessfull")
            print("Retype Your Password:-\n")
            e_mail , serviceProvider = get_mail()
            password = getpass.getpass("Password:- ")
            continue
    else:
        print("Login Successfull")
    break
    
            
    print("")
print("Please Type reciver's eMail:- ")
receiverAddress , receiverSP = get_mail()
print("Now Please Type Subject and Message")
Subject = input("Subject:- ")
Message = input("Message:- ")
connection.sendmail(e_mail , receiverAddress , ("Subject:- " + str(Subject) + "\n\n" + str(Message)))

print("eMaild Sent")
connection.quit()
