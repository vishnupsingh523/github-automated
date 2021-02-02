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
username.send_keys('Enter-your-own-id')

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys("Enter-yourOwnPassowrd")


clickButton = driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/input[14]')
clickButton.click()
print("Signing in to the Github account.")


time.sleep(2)
print("Signed In successfully to the GITHUB Account.")
print("\nCurrent Link: ",driver.current_url)

driver.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/summary').click()

time.sleep(5)
dashboard = driver.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/details-menu/div[1]/a')
dashboard.click()
print("We are in the profile dashboard.")