# импортируем все нужные библеотеки
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# сощдаем класс
class Parsing:
    def __init__(self,url:str,driver:str) -> None: # созлдаем объект
        self.url = url # прописываем все переменнные в нутри класса
        self.opp = webdriver.FirefoxOptions() # создаем опцию для веб драйвера
        self.driver = Service(driver)
        # self.opp.headless = False # прописываем методу headless параметр который обозначает что драйвер будет работать в фоновом режиме и мы его видеть не будем
        self.web = webdriver.Firefox(service= self.driver) # сощдаем веб драйвер и передаем ему нашу опцию
        self.web.get(self.url)

        
    

    # Сощдаем методы класса для прасинга 
    def one_teg(self, teg): # делаем метод который будет паристь только по одному названию тега
        element = self.web.find_element(By.TAG_NAME, teg)
        return element
        
                                               
    def all_teg_name(self,teg):# делаем метод который будет паристь все теги с один именем 
        elements = self.web.find_elements(By.TAG_NAME, teg)
        result = [i.text for i in elements]
        return result


    def paht_x(self,xpath):# делаем метод который будет паристь только один тег по его xpath(пути)
        element = self.web.find_element(By.XPATH, xpath)
        return element.text

    def classe(self,_class):# делаем метод который будет паристь тег по его классу
        element = self.web.find_element(By.CLASS_NAME, _class)
        return element.text

    def cliced(self,xpath):# делаем метод который будет восоздавать нажатие по какому то тегу при этом мы прописываем путь до этого тега(xpath)
        element = self.web.find_element(By.XPATH, xpath).click()


    def vvod(self,key:str,xpath:str):# делаем метод который будет восоздавать ввод в поле по его пути на этот тег(xpath)
        element = self.web.find_element(By.XPATH, xpath).send_keys(key)

    def clous(self):
        self.web.quit()

# точка входа проверям  класс на работо способность 
if __name__ == '__main__':
    reg = Parsing(url= 'https://news.microsoft.com/ru-ru/features/protect-yourself-online/', driver= '/geckodriver.exe')
    teg_pars_ib = ['3','5','8','10','11', '14','17','19']
    # result_pars_ib_teg_p = [reg.paht_x(f'/html/body/div[3]/div/main/div[1]/section[1]/div/p[{i}]') for i in teg_pars_ib] 
    result = reg.all_teg_name('h2')
    # print(result)
    # print(result_pars_ib_teg_p)
    result_2 = []
    for i in teg_pars_ib:
        result_2.append(reg.paht_x(f'/html/body/div[3]/div/main/div[1]/section[1]/div/p[{i}]'))
    # print(result_2)

    a = 0
    for i in result_2:
        print(f"{result[a]} '\n' {i}")
        a + 1
    


