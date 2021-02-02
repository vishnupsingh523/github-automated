from selenium import webdriver
import time

# creating the driver
driver = webdriver.Chrome()
mainURL = "https://github.com/"

driver.get(mainURL)
signIn = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
signIn.click()

currentLink = driver.current_url
print("Current Link: ",currentLink)

username = driver.find_element_by_xpath('//*[@id="login_field"]')
username.send_keys('vishnupsingh523@gmail.com')

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys("Badshah7877@")


clickButton = driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[12]')
clickButton.click()
print("Signing in to the Github account.")

time.sleep(2)
print("Signed In successfully to the GITHUB Account.")
print("\nCurrent Link: ",driver.current_url)