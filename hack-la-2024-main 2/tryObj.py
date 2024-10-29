from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import script
from script import Discussion
import time
import random


# Set up your WebDriver (Chrome in this example)
driver_path = "chromedriver.exe"  # Ensure you have the correct path to your ChromeDriver
service = Service(driver_path)  # Create a Service object
options = Options()

def new_discussion_spectate(discussiontitle, driver):
    driver.get('https://objection.lol/courtroom')
    driver.implicitly_wait(10)

    text_input = driver.find_element(by=By.XPATH,
                                     value='/html/body/div/div[1]/div[2]/main/div/div/form/div[1]/div[1]/div/div/div/div/input')
    text_input.send_keys("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b")
    text_input.send_keys(discussiontitle)

    text_input = driver.find_element(by=By.XPATH,
                                     value='/html/body/div/div[1]/div[2]/main/div/div/form/div[2]/div[2]/div/div/div/div[1]/input')

    discussion_code = text_input.get_attribute('value')
    print(discussion_code)

    submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[2]/main/div/div/form/div[4]/div/button')
    submit_button.click()

    spectate_button = driver.find_element(by=By.XPATH,
                                        value='/html/body/div/div[3]/div/div/form/div[3]/button[1]')
    spectate_button.click()

    return discussion_code
def post_user1(user, disc_code, driver):
    driver.get('https://objection.lol/courtroom/' + disc_code)
    driver.implicitly_wait(10)

    # Find and interact with the text input (example selector, modify as needed)
    # text_input = driver.find_element("id", "input-631")
    text_input = driver.find_element(by=By.XPATH,
                                     value='/html/body/div/div[3]/div/div/form/div[2]/div/div/div/div/div[1]/div/input')

    # Enter the argument
    # text_input.send_keys(argument)
    text_input.send_keys(user)

    # Simulate pressing "Enter" or clicking a button to submit (modify selector as needed)
    submit_button = driver.find_element(By.CSS_SELECTOR, '#app > div.v-dialog__content.v-dialog__content--active > div > div > form > div.v-card__actions > button:nth-child(3) > span')
    submit_button.click()
def post_user2(user, disc_code, driver):
    driver.get('https://objection.lol/courtroom/' + disc_code)
    driver.implicitly_wait(10)

    # Find and interact with the text input (example selector, modify as needed)
    # text_input = driver.find_element("id", "input-631")
    text_input = driver.find_element(by=By.XPATH,
                                     value='/html/body/div/div[3]/div/div/form/div[2]/div/div/div/div/div[1]/div/input')

    # Enter the argument
    # text_input.send_keys(argument)
    text_input.send_keys(user)

    # Simulate pressing "Enter" or clicking a button to submit (modify selector as needed)
    submit_button = driver.find_element(By.CSS_SELECTOR, '#app > div.v-dialog__content.v-dialog__content--active > div > div > form > div.v-card__actions > button:nth-child(3) > span')
    submit_button.click()

    characterChoice = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/main/div/div/div[1]/div[1]/div/div[2]/div[1]/div/div[3]')
    characterChoice.click()
    driver.implicitly_wait(10)
    character = driver.find_element(By.CSS_SELECTOR, value='#app > div.v-dialog__content.v-dialog__content--active > div > div > div > div.d-flex.flex-wrap.mt-4 > div:nth-child(2)')
    character.click()

def normal(driver):
    face_input = driver.find_element(by=By.XPATH,
                                     value='/html/body/div/div[2]/div[2]/main/div/div/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/img')
    face_input.click()

def desk(driver):
    face_input = driver.find_element(by=By.XPATH,
                                     value='/html/body/div/div[2]/div[2]/main/div/div/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/img')
    face_input.click()

def point(driver):
    face_input = driver.find_element(by=By.XPATH,
                                     value='/html/body/div/div[2]/div[2]/main/div/div/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div[3]/div/img')
    face_input.click()

# Function to open an instance of objection.lol and post an argument
def post_argument(argument, driver):
    # driver.get('https://objection.lol/courtroom/3792uz')
    driver.implicitly_wait(20)

    # Find and interact with the text input (example selector, modify as needed)
    # text_input = driver.find_element("id", "input-631")

    random_number = random.choice([1, 2, 3])

    if random_number == 1:
        normal(driver)
    elif random_number == 2:
        desk(driver)
    else:
        point(driver)

    text_input = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[2]/div/div[2]/textarea')
    text_input.click()

    # Enter the argument
    # text_input.send_keys(argument)
    text_input.send_keys(argument)

    # Simulate pressing "Enter" or clicking a button to submit (modify selector as needed)

    submit_button = driver.find_element(By.CSS_SELECTOR, '#app > div.v-application--wrap > div.container.pa-0.pa-lg-2.container--fluid > main > div > div > div.row.no-gutters > div:nth-child(1) > div > div:nth-child(4) > div:nth-child(2) > div > div > div:nth-child(2) > div > div.pl-1 > button')
    submit_button.click()


# Open two instances of Chrome with different options if needed

driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()
driver0 = webdriver.Chrome()

driver0.maximize_window()


# Post users and arguments from the course discussion
discussion = script.discussion_array[0]
user1 = discussion.get_user1()
user2 = discussion.get_user2()
discussiontitle = discussion.get_title()

disc_code = new_discussion_spectate(discussiontitle, driver0)
post_user1(user1, disc_code, driver1)
post_user2(user2, disc_code, driver2)

for i in range(0, len(discussion.get_messages()) - 1):
    if i % 2 == 0:
        post_argument(discussion.get_messages()[i], driver1)    # Argument 1 posted in browser 1
    else:
        post_argument(discussion.get_messages()[i], driver2)     # Argument 2 posted in browser 2

    time.sleep(5)                                           # Adding delay for timing (adjust as needed)


# Add more interactions if necessary, or let the drivers stay open to watch the results

# To keep the browsers open:
time.sleep(300)  # Adjust the time to keep the browser open before closing

# Close the browser windows when done
driver0.quit()

driver1.quit()
driver2.quit()