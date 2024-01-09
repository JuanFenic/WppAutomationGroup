from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import *
import time
from selenium.webdriver.common.keys import Keys
###SO FALTA CRIAR A INTERFACE GRAFICA COM TKINTER




options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())


print("nome do grupo:")
NomeGrupo = input() ##usa-se o nome do grupo
print("quantidade de participante a serem add:")
quantidade = int(input())
ListaDeContatos = []##Lista de contatos pra interar
print("nomes:")

for i in range(quantidade):
    nome = input()
    ListaDeContatos.append(nome)





nav = webdriver.Chrome(options=options,service=service)
nav.get("https://web.whatsapp.com")

time.sleep(50)


def automaticpt1(GroupName):
    nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
    nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(GroupName)
    nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
    nav.find_element('xpath', '//*[@id="main"]/header/div[2]/div[1]/div/span').click()

    time.sleep(3)

    nav.execute_script("window.scrollTo(0,1500)")
    

    time.sleep(2)


def automaticgroup(ContactsList):


    nav.find_element('xpath', '//*[@id="app"]/div/div[2]/div[5]/span/div/span/div/div/div/section/div[7]/div[2]/div[1]/div[2]/div/div').click()
    nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(ContactsList)

    time.sleep(0.5)

    nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)

    time.sleep(0.5)

    nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/span[2]/div/div/div/span').click()

    time.sleep(0.5)

    nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button[2]/div/div').click()

    time.sleep(0.5)

    element1 = nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button[1]/div/div')
    ##element2 = nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button[2]/div/div')

   


    
    if element1.is_displayed():
        element1.click()
    return
        


def LoopAddContat():
    for i in ListaDeContatos:
        automaticgroup(i)
        time.sleep(1)

automaticpt1(NomeGrupo)
LoopAddContat()