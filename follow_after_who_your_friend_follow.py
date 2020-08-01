from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import login


def get_info():
    global username
    global password
    global friend_instgram
    username = input('enter your instgram username\n')
    password = input('enter your instgram password\n')
    friend_instgram = input('enter friend instgram name\n')

class Login:
    def __init__(self, driver, username, password,  friend_instgram):     #save user info
        self.driver = driver
        self.username = username
        self.password = password
        self.url =  friend_instgram

    def signin(self):                                   #open instgram website
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        self.driver.maximize_window()                   #full screen
        time.sleep(1)

    def login_account(self):                           #connect to account
        self.driver.find_element_by_xpath("//input[@name=\"username\"]") \
            .send_keys(self.username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
            .send_keys(self.password)
        self.driver.find_element_by_xpath('//button[@type="submit"]') \
            .click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
            .click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
            .click()
        time.sleep(1)

    def start_following(self):
        scroll = 1                                   #flag variable to runing until scroll over
        number_of_following = 0                      #this variable to save success following
        self.driver.get("https://www.instagram.com/"+self.url)       #go to friend instgram
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]") \
        .click()                                       #go to following button
        time.sleep(1)
        array = []                                     #this array contains the names your friend following them
        while(i):                                       #keep going scroll until the end
            self.popup = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[2]'))) #take  catch the small window
         #   self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', self.popup)   #scroll 1 time
            scroll = self.driver.execute_script("""
                            arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                            return arguments[0].scrollHeight;  
                            """, self.popup)
            time.sleep(1)
            peoples = self.driver.find_elements_by_class_name('FPmhX')  #count the peopls

        for people in peoples:   #appends the name to array
            if people not in array:
                array.append(people.text)

        self.array = array    #save the array with names
        time.sleep(1)

        for i in self.array:   #all iteration go to follower page and follow him
            self.driver.get('https://instagram.com/' + i)      #this is the url + instgram name
            time.sleep(1)
            try:
                self.driver.find_element_by_xpath("//button[contains(text(), 'Follow')]") \
                    .click()                    #follow this pepole
                number_of_following +=1
                print("you follow after "+i+" Now!\n")
            except:
                continue
        print("finish following!\n")   #when loop end
        print("you following after" + str(number_of_following) + " people!\n")


driver = ""
username = ""
password = ""
friend_instgram = ""

def main():
    global driver
    print('script on...\n\n')
    get_info()
    driver = webdriver.Chrome("/Users/matan/Downloads/chromedriver.exe")
    print('driver loaded...\n\n')
    l = Login(driver, username, password, friend_instgram)
    l.signin()
    l.login_account()
    l.start_following()

if __name__ == '__main__':
    main()