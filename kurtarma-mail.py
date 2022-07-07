import time
from pyrsistent import v
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from imap_tools import MailBox
from imap_tools import AND

options = uc.ChromeOptions()
options.add_argument("--incognito")
driver = uc.Chrome(options=options,use_subprocess=True) 
wait = WebDriverWait(driver, 20)
url = "https://accounts.google.com/"
security_url="https://myaccount.google.com/security"

def x():
    #  ---------- EDIT ----------o
    email = input("E-mail: ")
    password = input("Password: ")
    kurtarma_maili= input("Kurtarma maili: ")
    EMAIL="xx@gmail.com" #security mail address
    PASSWORD="webapppassword" #webapppassword
    SERVER="imap.gmail.com"
    #  ---------- EDIT ----------
    driver.get(url)
    #login
    wait.until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(f"{email}\n")
    wait.until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys(f"{password}\n")
    time.sleep(1)
    driver.get(security_url)
    #security page
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/c-wiz/div/div[2]/div/c-wiz/c-wiz/div/div[3]/div/div/c-wiz/section/div[5]/div/div/div[3]/div[2]/a/div'))).click()
    wait.until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys(f"{password}\n")
    #input mail
    kurtarma_input = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div/div[4]/div/form/div[2]/div[1]/div/div/label/input')))
    kurtarma_input.clear()
    kurtarma_input.send_keys(f"{kurtarma_maili}@gmail.com\n")
    time.sleep(7)
    kod=[]
    #check imap for code
    with MailBox(SERVER).login(EMAIL, PASSWORD, 'INBOX') as mailbox:
        for message in mailbox.fetch(AND(text="search query"),limit=2, reverse=True):
            text=message.text[55:][:30]
            x=(text.find("@gmail.com"))
            y=f"{text[:x]}@gmail.com"
            #found the code
            if y == email:
                print("Kod bulundu.")
                #kod.append(message.subject[24:])
                kod=message.subject[24:]
                print(kod)
            #couldn't find the code, trying again.
            else:
                print("Kod bulunamadı tekrar deneniyor.")
                time.sleep(5)
                with MailBox(SERVER).login(EMAIL, PASSWORD, 'INBOX') as mailbox:
                    for message in mailbox.fetch(AND(text="search query"),limit=2, reverse=True):
                        text=message.text[55:][:30]
                        x=(text.find("@gmail.com"))
                        y=f"{text[:x]}@gmail.com"
                        if y == email:
                            print("Kod bulundu.")
                            kod=message.subject[24:]
                            print(kod)

    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[11]/div[2]/div/div[1]/div/div[1]/div[2]/div/div/label'))).send_keys(f"{kod}\n")
x()
x()
x()
x()
x()
time.sleep(9999)