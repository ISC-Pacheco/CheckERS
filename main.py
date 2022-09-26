import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size=(400,650)
KV='''
Screen:
    MDCard:
        size_hint:None,None
        size:300,550
        pos_hint: {"center_x":0.5,"center_y":0.5}
        elevation:10
        padding:65
        spacing:35
        orientation: 'vertical'
        MDIcon:
            icon:'android'
            icon_color: 75,75,75,75
            haling: 'center'
            font_size:180
        MDFillRoundFlatButton:
            id: encuestas
            text:"Encuestas"
            font_size:15
            pos_hint:{"center_x":0.5}
            on_press: app.encuestas()
        MDFillRoundFlatButton:
            id: asistencias
            text:"Asistencias"
            font_size:15
            pos_hint:{"center_x":0.5}
            on_press: app.asistencias()
        MDTextField:
            id:thepath
            hint_text: "Ruta del archivo .csv"
            line_color_normal: "red"
        MDFillRoundFlatButton:
            id: cerrarapp
            text:"Salir"
            font_size:15
            pos_hint:{"center_x":0.5}
            on_press: app.close()
        MDLabel:
            text: "CREATE BY: P4CH3C0"
            font_size:9
            halign: "center"
'''

class miBotencu(MDApp):
    dialog=None

    def build(self):
        self.theme_cls.theme_style= 'Dark'
        self.theme_cls.primary_palette= 'Indigo'
        self.theme_cls.accent_palette= 'Blue'

        return Builder.load_string(KV)

    def encuestas(self):
        driver = webdriver.Chrome('chromedriver.exe')
        driver.get("https://encuestasregresoseguro.com/")
        action = ActionChains(driver)
        select1 = driver.find_element("name", 'tipoEscuela').click()
        time.sleep(1)
        tipoEsc = driver.find_element("xpath", '//*[@id="tipoEscuela_id"]/option[3]').click()
        select1 = driver.find_element("name", 'tipoEscuela').click()
        select2 = driver.find_element("id", 'universidades').click()
        time.sleep(1)
        escuela = driver.find_element("xpath", '//*[@id="universidades"]/option[13]').click()
        select2 = driver.find_element("id", 'universidades').click()
        nick = "validacion_encuestas@vbravo.tecnm.mx"
        passw = "Val13_en"
        dni = driver.find_element("id", "DNI").send_keys(nick)
        passw = driver.find_element("name", "password").send_keys(passw)
        sendf = driver.find_element("id", 'botonEnviar').click()
        time.sleep(1)
        cerrar=driver.find_element("xpath",'/html/body/div/aside/section/div/div[2]/a')
        while cerrar!=True:
            try:
                activacamara = driver.find_element("xpath", '//*[@id="formbusqueda"]/div/div[3]/div/button[2]').click()# solicita activar camara //*[@id="formbusqueda"]/div/div[3]/div/button[2]
                time.sleep(5)
                confirmaacceso = driver.find_element("xpath", '/html/body/div[3]/div/div[3]/button[1]').click()#/html/body/div[3]/div/div[3]/button[1] confirma
                time.sleep(1)
                nuevo = driver.find_element("xpath",'/html/body/div[1]/div[2]/section/section[1]/div[3]/center/a').click() # pregunta si continua
                time.sleep(1)
            except:
                print("excepcion encontrada")#
                break

    def asistencias(self):
        thepath=''
        thepath=self.root.ids.thepath.text
        print(thepath)
        #En la siguiente linea es donde se cargan los datos del .ccv
        df = pd.read_csv(thepath)
        driver = webdriver.Chrome('chromedriver.exe')
        driver.get("https://encuestasregresoseguro.com/")
        action = ActionChains(driver)
        select1 = driver.find_element("name", 'tipoEscuela').click()
        #time.sleep(1)
        tipoEsc = driver.find_element("xpath", '//*[@id="tipoEscuela_id"]/option[3]').click()
        select1 = driver.find_element("name", 'tipoEscuela').click()
        select2 = driver.find_element("id", 'universidades').click()
        #time.sleep(1)
        escuela = driver.find_element("xpath", '//*[@id="universidades"]/option[13]').click()
        select2 = driver.find_element("id", 'universidades').click()
        nick = "asistencia_encuestas@vbravo.tecnm.mx"
        passw = "Asis13_en"
        dni = driver.find_element("id", "DNI").send_keys(nick)
        passw = driver.find_element("name", "password").send_keys(passw)
        sendf = driver.find_element("id", 'botonEnviar').click()
        time.sleep(1)
        for row, datos in df.iterrows():
            identificador = datos['Matricula']
            valida = driver.find_element("name", 'matricula').send_keys(identificador)
            buscar = driver.find_element("xpath", '//*[@id="formbusqueda"]/div/div[3]/div/button[1]').click()
            todook= {"method":"xpath","selector":"/html/body/div[3]/div/div[3]/button[1]"}
            nadaok= {"method":"xpath","selector":"/html/body/div[2]/div/div[3]/button[1]"}
            time.sleep(1)
            try:
                confirmaAsistencia = driver.find_element("xpath", '/html/body/div[3]/div/div[3]/button[1]').click()
                # time.sleep(1)
                escan = {"method": "xpath","selector": '/html/body/div[1]/div[2]/section/section[1]/div[3]/center/a'}
                nuevo_escaner = driver.find_element('xpath','/html/body/div[1]/div[2]/section/section[1]/div[3]/center/a').click()

            except:
                confirmaInacistencia = driver.find_element("xpath",'/html/body/div[2]/div/div[3]/button[1]').click()

    def close(self):
        MDApp.get_running_app().stop()
        Window.close()

miBotencu().run()
##create by:Pacheco