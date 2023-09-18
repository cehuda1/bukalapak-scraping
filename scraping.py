from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import os
import time 

#global var
opsi = webdriver.ChromeOptions()
opsi.add_argument('--headless')
opsi.add_argument('--log-level=3')
servis = Service('chromedriver.exe')
driver = webdriver.Chrome(service=servis, options=opsi)

os.system("cls")
print('TOKOPEDIA WEB SCRAPING\n')
barang = input('Nama Produk: ')
halaman = input('Halaman: ')
os.system('cls')
print('Data sedang di proses ....')
time.sleep(3)

#url
base_url = f'https://www.bukalapak.com/products?page={halaman}&search[keywords]={barang}'

#selenium config(globar var)
driver.set_window_size(1300,800)
driver.get(base_url)
# driver.save_screenshot('coba.png')
global_content = driver.page_source
driver.quit()
data = BeautifulSoup(global_content,'html.parser')

#clear
i=0
os.system('cls')
print("Data Berhasil Di Datpatkan!")
time.sleep(2)

#looping
for area in data.find_all('div',class_="bl-flex-item mb-8"):
    product_name = area.find('a', class_="bl-link").get_text().strip()
    link = area.find('a', class_="bl-link")
    product_link = link["href"]
    product_price = area.find('p', class_='bl-text bl-text--semi-bold bl-text--ellipsis__1 bl-product-card-new__price').get_text().strip()
    product_rate = area.find('span', class_='bl-text bl-text--caption-12 bl-text--subdued bl-text--ellipsis__1').get_text().strip()
    product_loc = area.find('p', class_="bl-text bl-text--caption-12 bl-text--secondary bl-text--ellipsis__1 bl-product-card-new__store-location").get_text().strip()
    product_market = area.find('p',class_='bl-text bl-text--caption-12 bl-text--secondary bl-text--ellipsis__1 bl-product-card-new__store-name').get_text().strip()

#numbering product
    i+=1
       
#print result       
    print(f"\n[ Nomor: {i} ]")
    print("Nama : "+product_name)
    print("Link : "+product_link)
    print("Harga : "+product_price)
    print("Rating : "+product_rate)
    print("Lokasi : "+product_loc)
    print("Store : "+product_market+"\n")
    print("-------------------------------------------------------------- credit: @cehuda")
