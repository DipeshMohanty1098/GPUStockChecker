from tkinter import messagebox
from selenium import webdriver
import tkinter as tk
from selenium.common.exceptions import NoSuchElementException
import time
from email.message import EmailMessage
import smtplib

#driver
driver_path = 'C:/Users/eradi/OneDrive/Desktop/chromedriver'

url = 'https://rptechindia.in/nvidia-geforce-rtx-3060-ti.html'

#tkinter
root = tk.Tk()

w = root.title("Check GPU Stock")
tk.Label(root, text = 'GPU URL: ').grid(row = 0, column = 0)
url_input = tk.Entry(root, width=40)
url_input.grid(row=0, column=1)
tk.Label(root, text = 'Email(Only Gmail): ').grid(row = 1, column = 0)
email = tk.Entry(root,width=40)
email.grid(row=1, column=1)
tk.Label(root, text = 'Password(gmail): ').grid(row = 2, column = 0)
password = tk.Entry(root,width=40, show="*")
password.grid(row=2, column=1)
tk.Label(root, text = 'Script not running').grid(row = 4, column = 1)




def script():
    is_present = False
    tk.Label(root, text='Script running!').grid(row=4, column=1)
    if (url_input.get() == '' or password.get() == '' or email.get() == ''):
        messagebox.showerror("Error", "Please fill up all fields!")
    else:
        driver = webdriver.Chrome(executable_path=driver_path)
        driver.get(url_input.get())
        while(is_present == False):
            try:
                add_to_cart = driver.find_element_by_id('product-addtocart-button')
                print('In Stock!')
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login(email.get(), password.get())
                # message
                message = EmailMessage()
                email_input = email.get()
                message.set_content('Your GPU is now in Stock!! \nClick Below to Buy!\n\n\n\n{}'.format(url))
                message['Subject'] = 'YOUR GPU IS NOW IN STOCK!'
                message['From'] = email_input
                message['To'] = email_input
                server.send_message(message)
                server.quit()
                root.update()
                break
            except NoSuchElementException:
                root.update()
                is_present = False
                print('Out of Stock!')
                driver.refresh()
                time.sleep(5)
                root.update()
                continue


cal = tk.Button(root, text = 'Start Script', command = script)
cal.grid(row = 3,column = 1)

root.mainloop()