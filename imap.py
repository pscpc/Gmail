from imap_tools import MailBox
from imap_tools import AND

EMAIL="xx@gmail.com"
PASSWORD="webapppassword"
server="imap.gmail.com"
while True:
    with MailBox('imap.gmail.com').login(EMAIL, PASSWORD, 'INBOX') as mailbox:
        for message in mailbox.fetch(AND(text="search query"),limit=3, reverse=True): #search for query in mails
            text=message.text[55:][:30] #cut the mail part(you can customize)
            x=(text.find("@gmail.com")) #define the mail
            y=f"{text[:x]}@gmail.com" #adding @gmail.com at the and
            print(f"{y:25s}\t {message.subject[24:]}") #print the mail address and the code
    x = input("")
    if x == "":
        continue