


#Once run, constantly checks email for new emails, and then scrapes email to find links and immediately click them 
#with a default browser. Currently set to check as many times as possible, but in execution should be restricted to pause frequently, 
#and only check once in a while, so as not to overload email server with requests. 






import poplib
from email import parser
import re
import email
import webbrowser
import getpass
import quopri
import time

def justDoIt():
    mail = poplib.POP3_SSL('pop.gmail.com')
    mail.user('enteremail@email.com')
    mail.pass_('enterpassword')
    if mail.stat()[1] > 0:
        print ("You have new mail.")
        #Get messages from server:
        messages = [mail.retr(i) for i in range(1, len(mail.list()[1]) + 1)]
        # Concat message pieces:
        messages =  (["\n".join(str(v) for v in mssg[1]) for mssg in messages])
        #Parse message intom an email object:
        messages = [email.message_from_string(mssg) for mssg in messages]
        #print (messages)
        #messages = str(messages)
        #print (messages)
            #messagesString = "\n".join(map(str, messages))
        messagesString = [str(goddamn) for goddamn in messages]
        #SmessagesString = [goddamn.strip("b\'") for goddamn in messagesString]
        messagesString = [goddamn.replace("b\'","") for goddamn in messagesString]
        messagesString = [goddamn.replace("\'","") for goddamn in messagesString]
        messagesString = "".join(messagesString)

        #print (messagesString)
        messagesString = str(quopri.decodestring(messagesString))

        #print(messagesString)
        urlResult = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|#|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', messagesString )
        if urlResult:
            urlResult = list(set(urlResult))
            for results in urlResult:
                #print (results)
                if ("launches") in results:
                    results = results.replace("\\r","\r")
                    results = results.replace("\r", "")
                    results = results.replace("\\n","\n")
  
                    results = results.replace("\\t","\t")

                    results = results.replace('\'',"")
                    results = results.replace('\"',"")
                    results = results.strip(">")
                    results = results.strip('>')
                    results = results.rstrip(".")
                    print (results)
                    #print (1)
                    webbrowser.open(results)
                
        else:
            print("no matches")
        mail.quit()        


#x = input("Email: ")
#y = getpass.getpass("Password: ")
counterGj = 1
while (counterGj ==1):
    justDoIt()

