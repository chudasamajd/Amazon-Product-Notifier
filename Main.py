from selenium import webdriver
from twilio.rest import Client

client = Client("AC562ba15f63f2262134034f0b7180a0ea","cafabd9e7f4ad8ffc15ed307acb2c615")
driver = webdriver.Chrome('C:/Users/91816/Downloads/chromedriver_win32/chromedriver.exe')
driver.get("https://www.amazon.in/dp/B08CFSS789/ref=cm_sw_r_wa_apa_i_.9MsFbJ5QHK36")
print(driver.title)
el = driver.find_element_by_tag_name('body')
str1=el.text 
if(str1.find("Currently unavailable.")!=-1):
    print("Its still not available")
else:
    client.messages.create(to=["+918160462101"],from_="+13153841419",body="Your Product is available on Amazon")

driver.close()
