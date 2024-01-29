from selenium import webdriver
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys

from webdriver_manager.chrome import ChromeDriverManager

if len(sys.argv) > 1:
    if sys.argv[1] == '-n':
        print('Enter student number')
        u = input()
        print('Enter password')
        p = input()

        ed_user = dict(

            username=u,
            password=p
        )
        temp = dict(
            ed_user
        )
        with open('loginInfo.yml', 'w') as file:
            yaml.dump(temp, file)
else:
    print('Assuming you have entered user info with -n')

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

with open('loginInfo.yml', 'r') as file:
    conf = yaml.safe_load(file)

u = conf['username']
p = conf['password']

driver = webdriver.Chrome(options=chrome_options)


def login(url, username, password):
    driver.get(url)
    driver.implicitly_wait(2)

    driver.find_element(By.ID, 'login-btn').click()
    driver.implicitly_wait(2)

    driver.find_element(By.ID, 'login').send_keys(username)
    driver.find_element(By.ID, 'submit').click()
    driver.implicitly_wait(2)

    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'submit').click()
    driver.implicitly_wait(2)
    driver.get('https://www.learn.ed.ac.uk/auth-saml/saml/login?apId=_175_1')



login('https://www.myed.ed.ac.uk/myed-progressive/', u, p)
print("Successfully logged in!")

