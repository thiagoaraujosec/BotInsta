from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class IGBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(ChromeDriverManager().install())

    def loguearse(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        email = bot.find_element_by_name('username').send_keys(self.username)
        password = bot.find_element_by_name('password').send_keys(self.password)
        time.sleep(1)
        bot.find_element_by_name('password').send_keys(Keys.RETURN)
        time.sleep(3)

    def ganarSeguidores(self,cuentas,numeroParaSeguir):
        self.cuentas = cuentas
        bot = self.bot
        for user in cuentas:
            bot.get('https://instagram.com/' + user)
            time.sleep(2)
            bot.find_element_by_xpath('//a[@href="/' + user + '/followers/"]').click()
            time.sleep(1)
            for i in range(1,numeroParaSeguir):
                bot.find_element_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]').click()
    def unfollow(self,unfollowNumb):
        username = self.username
        self.unfollowNumb = unfollowNumb
        bot = self.bot
        bot.get('https://instagram.com/' + username)
        time.sleep(3)
        bot.find_element_by_xpath('//a[@href="/' + username + '/following/"]').click()
        time.sleep(2)
        for i in range(1,unfollowNumb):
            bot.find_element_by_xpath('//button[@class="sqdOP  L3NKy    _8A5w5    "]').click()
            time.sleep(1)
            bot.find_element_by_xpath('//button[@class="aOOlW -Cab_   "]').click()


arrayCuentas = []

def array(numm):   
    for i in range(num):
        user = input(f"Usuario {i}: ")
        arrayCuentas.append(user)
        print(arrayCuentas)


if __name__ == "__main__":
    print("""
    Coded by : Thiagous06
    """)
    username = input("Pon tu nombre de usuario : ")
    password = input("Pon tu contraseña : ")
    Bot = IGBot(username,password)
    Bot.loguearse()
    opc = input("""     Que eliges?\n1=Ganar Seguidores\n2=Dejar de Seguir a Todos los que sigues\n===> """)
    if opc == "1":
        num = int(input("Numero de cuentas a la que quieres seguir sus seguidores")) 
        array(numm=num)
        if num == arrayCuentas.__len__():
            Bot.ganarSeguidores(arrayCuentas,10)
    elif opc == "2":
        numm = int(input("A cuanta gente quieres dejar de seguir"))
        Bot.unfollow(numm)
    else:
        print("Ingrese un valor valido")
        exit()
