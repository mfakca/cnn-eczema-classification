# Gerekli kütüphanelerin içe aktarılması
from selenium import webdriver
import time
import urllib.request
import os
from selenium.webdriver.common.keys import Keys


# Web driver kurulumu (Ben chromium kullandım.)
browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

# Google'a bağlanır.
browser.get("https://www.google.com/")

# Search textbox'a erişir.
search = browser.find_element_by_name("q")


# Aranacak metni yazıp enter'a basar.
search.send_keys("eczema skin",Keys.ENTER)

# Görseller sekmesine geçer. (İngilizce kullanıyorsanız "Images" olarak değiştirebilirsiniz.)
elem = browser.find_element_by_link_text("Görseller")
elem.get_attribute("href")
elem.click()


value = 0

# 20 defa scroll atar ve görselleri toplar.
for i in range(20):
   browser.execute_script("scrollBy("+ str(value) +",+1000);")
   value += 1000
   time.sleep(3)
   
elem1 = browser.find_element_by_id("islmp")
sub = elem1.find_elements_by_tag_name("img")
 

# Belirtilen isimde dosya yoksa oluşturur, varsa geçer.  
try:
    os.mkdir("eczema_skin")
except FileExistsError:
    pass
    
count = 0

# Linkleri toplanan görselleri indirir ve belirtilen dosyaya kaydeder.
for i in sub:
    src = i.get_attribute('src')
    try:
        if src != None:
            src  = str(src)
            print(src)
            count+=1
            urllib.request.urlretrieve(src, os.path.join('eczema_skin','image'+str(count)+'.jpg'))
        else:
            raise TypeError
    except TypeError:
        print('fail')
