import os
import socket
try:
    from selenium import webdriver
except ImportError:
    os.system("pip install selenium")
    from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import random
import string
try:
    import names
except ImportError:
    os.system("pip install names")
    import names
try:
    from barnum import gen_data
except ImportError:
    os.system("pip install barnum")
    from barnum import gen_data
try:
    from faker import Faker
except ImportError:
    os.system("pip install faker")
    from faker import Faker

from datetime import date
from random import choice


fake = Faker()

r = random.randint(100, 999)
a = 4
b = random.randint(100, 999)



url = 'https://www.paypal.com/pt/home/'
url1 = 'https://www.paypal.com/pt/merchantsignup/router/wps'
url2 = 'https://www.paypal.com/bizsignup/#/businessInfo'
url3 = 'https://www.paypal.com/businesswallet/money'
url4 = 'https://www.netflix.com/'
url5 = "https://www.netflix.com/signup/paypaloption"



def gen_phone():
    first = str(+351241)
    second = str(random.randint(1, 888)).zfill(3)

    last = (str(random.randint(1, 999)).zfill(3))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 999)).zfill(3))

    return '{}-{}-{}'.format(first, second, last)

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def by_id_keys(enterid,enterkeys):
    found = False
    while not found:
        try:
            element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, enterid))
            )
            found = True
        except NoSuchElementException:
            time.sleep(0.5)
        except TimeoutException:
            time.sleep(0.5)
        finally:
            found1 = False
            while not found1 and found == True:
                try:
                    element.send_keys(enterkeys)
                    found1 = True
                except ElementNotVisibleException:
                    time.sleep(0.5)
                except TimeoutException:
                    time.sleep(0.5)

def by_ref_click(enterloc,enterref):
    found = False
    while not found:
        try:
            element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((enterloc, enterref))
            )
            found = True
        except NoSuchElementException:
            time.sleep(0.5)
        finally:
            found1 = False
            while not found1 and found == True:
                try:
                    actions = ActionChains(driver)
                    actions.move_to_element(element).perform()
                    element.click()
                    found1 = True
                except ElementNotVisibleException :
                    time.sleep(0.5)
                except StaleElementReferenceException:
                    time.sleep(0.5)
                except TimeoutException:
                    time.sleep(0.5)

def postprocess():
    driver.get(url3)
    driver.get(url5)
    time.sleep(1)
    by_ref_click(By.ID, "simplicityPayment-CONTI-euft")
    time.sleep(1)
    by_id_keys("password",'Fucks@123')
    time.sleep(2)
    by_ref_click(By.ID,"btnLogin")
    time.sleep(1)
    # driver.get(url5)
    # # time.sleep(1)
    # # by_ref_click(By.XPATH, ".//*[contains(text(),'TRY 30 DAYS FREE')]")
    # # time.sleep(1)
    # # driver.execute_script("window.scrollBy(0,500)", "")
    # # by_ref_click(By.XPATH, ".//*[contains(text(),'PayPal')]")
    # time.sleep(1)
    # by_ref_click(By.ID, "simplicityPayment-CONTI-euft")
    # time.sleep(2)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    val = input("want to Exit: ")
    if (val == 'y'):
        driver.quit()

def add_card():
    driver.get(url3)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, ".//*[contains(text(),'Associar novo cartão')]"))
        )
    finally:
        element.click()

    time.sleep(1)
    by_id_keys("cardNumber", CCnum)
    time.sleep(0.5)
    by_id_keys("expDate", Exp)
    time.sleep(0.5)
    by_id_keys("verificationCode", Cvv)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, ".//*[contains(text(),'Associar cartão')]"))
        )
    finally:
        element.click()
        var = input("Continue :")
        time.sleep(2)
    driver.get(url5)
    time.sleep(1)
    by_ref_click(By.ID, "simplicityPayment-CONTI-euft")
    time.sleep(2)
    val = input("Want to Exit Or start Post Process ")
    if(val == 'y'):
        driver.quit()
    elif(val == 'pp'):
        postprocess()
    else:pass

def save_email():
    file1 = open("paypal_emails.txt", "a")  # append mode
    file1.write(emailtyped.lower() + "@gmail.com\n")
    file1.close()

    file1 = open("netflix_emails.txt", "a")  # append mode
    file1.write(emailtyped.lower() + "@jaqs.site\n")
    file1.close()

def worker():

    # driver.get('chrome://settings/')
    # driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.75)')

    # driver.execute_script("document.body.style.zoom='75%'")

    # driver.manage().deleteAllCookies()
    # driver.ExecuteChromeCommand("Storage.clearCookies", new Dictionary<string, object>())

    print("Creating Paypal\n")

    driver.get(url)

    driver.get(url1)

    # driver.set_page_load_timeout(int(100))
    # driver.set_script_timeout(int(100))



    by_id_keys("email", emailtyped.lower() + "@jaq.site")
    by_ref_click(By.ID, "continueButton")
    by_id_keys("password", 'Fucks@123')
    by_ref_click(By.ID, "continueButton")

    by_id_keys("firstName", names.get_first_name())
    by_id_keys("lastName", names.get_last_name())
    by_id_keys("businessLegalName", gen_data.create_company_name())
    by_id_keys("businessPhoneNumber", gen_phone())
    by_id_keys("businessAddress-address_line_1", fake.street_address())
    by_id_keys("businessAddress-postal_code", str(a) + str(r) + '-' + str(b))
    by_id_keys("businessAddress-admin_area_2", fake.city())

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    by_ref_click(By.XPATH, ".//*[contains(text(),'Li, autorizo e aceito')]")
    by_ref_click(By.XPATH, ".//*[contains(text(),'Aceitar e criar conta')]")

    time.sleep(6)

    # var = input("Conitnue: ")

    try:
        driver.implicitly_wait(10)
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[contains(@class,'component-wrapper SelectDropdown col-md-12')]"))
        )
    finally:
        element.click()
        driver.find_element_by_id('INDIVIDUAL-1').click()

    by_id_keys("merchantCategoryCode", 'Time')

    by_ref_click(By.XPATH, ".//*[contains(text(),'Timeshares')]")

    by_id_keys("businessCCStatementName", random_char(10))

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    by_ref_click(By.ID, "continueButton")

    by_id_keys("dateOfBirth-day", random.randint(1, 28))

    by_id_keys("dateOfBirth-year", random.randint(1960, 1999))

    time.sleep(0.5)

    driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div/div[2]/div/div[2]/form/div/div[3]/div/div/div/div/div/div/div/div[2]/div").click()

    driver.find_element_by_id('1-2').click()

    driver.execute_script("window.scrollBy(0,500)", "")

    by_ref_click(By.XPATH, ".//*[contains(text(),'Igual à morada da empresa')]")

    by_ref_click(By.XPATH, ".//*[contains(text(),'Igual ao telefone da empresa')]")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    by_ref_click(By.XPATH, ".//*[contains(text(),'Enviar')]")

    time.sleep(3)

    print("Paypal Created\n")

    # var = input("coninue: ")

    print("Adding Card\n")

    driver.get(url3)
    driver.get(url3)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, ".//*[contains(text(),'Associar novo cartão')]"))
        )
    finally:
        element.click()

    time.sleep(1)
    by_id_keys("expDate", Exp)
    time.sleep(0.5)
    by_id_keys("verificationCode", Cvv)
    time.sleep(0.5)
    by_id_keys("cardNumber", CCnum)
    time.sleep(1.5)
    print(CCnum + "-" + Cvv)
    by_ref_click(By.XPATH, '//*[@id="mainModal"]/div/div/div/div/div/div/div/form[1]/button')

    time.sleep(2.5)
    print("Card Added\n")
    print("Creating Netflix\n")

    driver.get(url4)

    by_id_keys("id_email_hero_fuji", emailtyped.lower() + "@jaqs.site")

    time.sleep(1.5)

    save_email()

    print("Emails Saved\n")

    by_ref_click(By.XPATH, ".//*[contains(text(),'TRY 30 DAYS FREE')]")

    time.sleep(1.5)

    by_ref_click(By.XPATH, '//*[@id="appMountPoint"]/div/div/div[2]/div/div[2]/button')

    by_id_keys("id_password", "0000")

    by_ref_click(By.XPATH, ".//*[contains(text(),'CONTINUE')]")

    time.sleep(1.5)

    by_ref_click(By.XPATH, ".//*[contains(text(),'SEE THE PLANS')]")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(1.5)

    by_ref_click(By.XPATH, ".//*[contains(text(),'CONTINUE')]")

    time.sleep(1.5)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(2)

    print("Netflix Created\n")

    by_ref_click(By.ID, "paypalDisplayStringId")

    time.sleep(1)
    print("YOUR TURN")
    by_ref_click(By.ID, "simplicityPayment-CONTI-euft")

    time.sleep(5)

    # by_id_keys("cardExpiry", Exp)
    # by_id_keys("cardCvv", Cvv)
    #
    # time.sleep(2.5)
    #
    # by_id_keys("cardNumber", CCnum)
    # print(CCnum + "-" + Cvv)
    #
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #
    # time.sleep(2)
    #
    #
    #
    # by_ref_click(By.ID, "cardAddButton")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    found = False
    try:
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, ".//*[contains(text(),'Aceitar e continuar')]"))
        )
        found = True
    except NoSuchElementException:
        time.sleep(0.1)
    finally:
        if (found == True):
            element.click()
        else:
            pass
        val = input("Want to Exit or Start Post Process or card add: ")
        if (val == 'y'):
            driver.quit()
        elif (val == 'pp'):
            postprocess()
        elif (val == 'cc'):
            add_card()


if __name__ == '__main__':
    i = socket.gethostname()
    today = date.today()
    d = today.strftime("%m/%d/%Y")
    print("------------Created By SNIPER-------------")
    f = open("cards.txt", "r")
    CC = f.readline()
    CCnum = CC[:16]
    Exp = "03/22"
    Cvv = CC[17:20]
    options = Options()
    # options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(options=options)
    emailtyped = names.get_first_name() + names.get_last_name() + \
                 str(random.randint(11111, 999999))
    # if(i == "Shitbrick" and d == "03/27/2021"):
    worker()
    # else:
    #     print("BOT EXPIRED")
# SourceCode = driver.execute_script('return document.body.innerHTM')
#
# if 'Aceitar e continuar' in SourceCode:
#
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#     try:
#         element = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable(
#                 (By.ID, "consentButton"))
#         )
#     finally:
#         element.click()
#
# elif 'O seu cartão foi recusado. Tente outro cartão' in SourceCode:
#     pass
#
#
#
#     # print('Card Already Added' + str(CCs))
#     # open('Result/paypalcardadded.txt', 'w', errors='ignore', encoding='utf-8').write(
#     #     Email + ':' + Password + '|IP:' + IP)
#
#
# elif 'Este cartão já foi adicionado a outra conta PayPal. Remova o cartão da outra conta ou tente outro cartão.' in SourceCode:
#     print('LIVE HIT' + str(CCs))
#     open('Result/paypalcardadded.txt', 'w', errors='ignore', encoding='utf-8').write(
#         Email + ':' + Password + '|IP:' + IP)
#
#
# elif 'Lamentamos, mas neste momento não é possível configurar os pagamentos pré-aprovados.' in SourceCode:
#     print('LIVE HIT' + str(CCs))
#     open('Result/paypalcardadded.txt', 'w', errors='ignore', encoding='utf-8').write(
#         Email + ':' + Password + '|IP:' + IP)

# O seu cartão foi recusado. Tente outro cartão
#
# consentButton


# time.sleep(1000)


