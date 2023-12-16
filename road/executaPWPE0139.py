from selenium import webdriver
import pyautogui
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

driver = webdriver.Ie (executable_path=r"C:\webdriver\IEDriverServer_Win32_4.7.0\IEDriverServer.exe")
driver.maximize_window()
driver.get("http://172.22.4.248/")

sleep(5)


pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('enter')

sleep(5)
elements = driver.find_elements(By.TAG_NAME, "cmdConfirma")

for e in elements:
    print(e.text)

driver.quit()

