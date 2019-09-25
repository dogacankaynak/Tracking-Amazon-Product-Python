'''
Created on 15 Eyl 2019

aþaðýdaki errorü araþtýr:
Traceback (most recent call last):
  File "test.py", line 8, in <module>
    from bs4 import BeautifulSoup , soup
ImportError: cannot import name 'soup' from 'bs4' (C:\Users\Hp\AppData\Local\Programs\Python\Python37-32\lib\site-packages\bs4\__init__.py)

C:\Users\Hp\workspace\pythonproject><
@author: Hp
'''
import requests

from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.de/COOAU-Unterwasserkamera-Fernbedienung-Wasserdicht-Stabilisierung/dp/B07RW4TBT8/ref=sr_1_1_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1N62AJ8Y6V0UR&keywords=camera&qid=1569432595&s=ce-de&sprefix=camera%2Caps%2C234&sr=1-1-spons&psc=1&smid=A3UXZQPQ4WNMU2&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExMlVMVkE2WjhIWDVFJmVuY3J5cHRlZElkPUEwNDQxMDU2MzJJRVA5MVY2MTgzTyZlbmNyeXB0ZWRBZElkPUEwOTY4NDM2MlA0TTlOQVg4RVNFRiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
def price_checking():
    
    page = requests.get(URL, headers =headers)

    soup = BeautifulSoup(page.content,'html.parser')

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id ="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])
    if(converted_price< 50):
        send_mail()
    #print(converted_price)
    #print(title)
    
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('kaynakdogacan@gmail.com','wnrjvujbxzoionae' )
    subject = 'PRICE FELL BELOW 50'
    body = 'Check the link => https://www.amazon.de/COOAU-Unterwasserkamera-Fernbedienung-Wasserdicht-Stabilisierung/dp/B07RW4TBT8/ref=sr_1_1_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1N62AJ8Y6V0UR&keywords=camera&qid=1569432595&s=ce-de&sprefix=camera%2Caps%2C234&sr=1-1-spons&psc=1&smid=A3UXZQPQ4WNMU2&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExMlVMVkE2WjhIWDVFJmVuY3J5cHRlZElkPUEwNDQxMDU2MzJJRVA5MVY2MTgzTyZlbmNyeXB0ZWRBZElkPUEwOTY4NDM2MlA0TTlOQVg4RVNFRiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('kaynakdogacan@gmail.com', 'dogacan.kynak@gmail.com', msg) 
    server.quit()
    
while(True):
    price_checking()
    time.sleep(86400)