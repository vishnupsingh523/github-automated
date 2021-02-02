from selenium import webdriver
from tkinter import *
import time

root = Tk()

root.geometry("400x400")


mainFrame = Frame(bd = 2)
mainFrame.pack(fill=Y)


def launchYoutube():
    driver = webdriver.Chrome()
    mainURL = "https://github.com/"

    driver.get(mainURL)
    signIn = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
    signIn.click()

    currentLink = driver.current_url
    print("Current Link: ", currentLink)

    username = driver.find_element_by_xpath('//*[@id="login_field"]')
    username.send_keys('vishnupsingh523@gmail.com')

    password = driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys("Badshah7877@")

    clickButton = driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[12]')
    clickButton.click()
    print("Signing in to the Github account.")

    time.sleep(2)
    print("Signed In successfully to the GITHUB Account.")
    print("\nCurrent Link: ", driver.current_url)

    driver.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/summary').click()

    time.sleep(5)
    dashboard = driver.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/details-menu/div[1]/a')
    dashboard.click()
    print("Moving to the dashboard.")

    def driverclose():
        print("Closing the Browser.")
        driver.close()
    Button(mainFrame, text = "CLose Youtube",command = driverclose).pack(side = BOTTOM)

Button(mainFrame, text= "YouTube",command = launchYoutube,padx= 2, pady = 2).pack()

root.mainloop()