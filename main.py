from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException
import time
from email.message import EmailMessage
import smtplib

#driver
driver_path = 'C:/Users/eradi/OneDrive/Desktop/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
sender = 'dipeshmohanty0226@gmail.com'
receiver = ['dipeshmohanty0226@gmail.com']
url = 'https://rptechindia.in/nvidia-geforce-rtx-3060-ti.html'


#message
message = EmailMessage()
email =""
message.set_content('Your GPU is now in Stock!! \nClick Below to Buy! \n\n\n\n{}'.format(url))
message['Subject'] = 'YOUR GPU IS NOW IN STOCK!'
message['From'] = email
message['To'] = email


#check condition
is_present = False


driver.get(url)


while(is_present == False):
    try:
        add_to_cart = driver.find_element_by_id('product-addtocart-button')
        is_present = True
        print('In Stock!')
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("", "")
        server.send_message(message)
        server.quit()
        break
    except NoSuchElementException:
        is_present = False
        print('Out of Stock!')
        driver.refresh()
        time.sleep(5)
        continue

