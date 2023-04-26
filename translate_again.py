
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
# Make imports
import time
import clipboard
import os
from selenium import webdriver

def splitkeep(s, delimiter):
    split = s.split(delimiter)
    return [substr + delimiter for substr in split[:-1]] + [split[-1]]

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


import ebooklib
from ebooklib import epub
def epub2thtml(epub_path):    
    book = epub.read_epub(epub_path)
    chapters = []    
    for item in book.get_items():
      if item.get_type() == ebooklib.ITEM_DOCUMENT:
                chapters.append(item.get_content())    
    return chapters

from bs4 import BeautifulSoup


def chap2text(chap):
    output = ''    
    soup = BeautifulSoup(chap, 'html.parser')
    text = soup.find_all(text=True)
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)    
    return output

def thtml2ttext(thtml):
    Output = []
    for html in thtml:
        text =  chap2text(html)
        Output.append(text)
    return Output

def epub2text(epub_path):
   chapters = epub2thtml(epub_path)
   ttext = thtml2ttext(chapters)     
   return ttext

blacklist = [   '[document]',   'noscript', 'header',   'html', 'meta', 'head','input', 'script',   ]

e = epub2text("Babel 2.0 - Où va la traduction automatique (Thierry Poibeau [Poibeau, Thierry]) (Z-Library).epub")
e2 = ''.join(e)
e2b = e2.replace("et al.","et al ")
e3 = splitkeep(e2b, ".")

#from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
# Start a Selenium driver 
driver_path='/usr/local/bin/chromedriver'
driver = webdriver.Chrome(driver_path, options=options)

from itertools import islice
import pyperclip
import time

ebookpl = open("Babel_2_0.txt","a+")
counter_file = open("counter.txt","r")
counter_file2 = str(counter_file.readlines()).strip()
counter_fileb = open("counterb.txt","a")

#opt = Options()
#opt.headless = True
#driver = webdriver.Firefox(options=opt)
#driver.get("https://deepl.com")
deepl_url = 'https://www.deepl.com/pl/translator'
driver.get(deepl_url)
time.sleep(3)
counter = 0
counter_internal = 1



def get_output_textarea():
    output_box = driver.find_elements_by_class_name("lmt__inner_textarea_container")[1]
    return output_box.find_element_by_tag_name("textarea")

# Recipe from https://docs.python.org/2/library/itertools.html
def take(n, iterable):
    return list(islice(iterable, n))
#if __name__ == "__main__":

for group in chunker(e3, 10):
       counter = counter + 1
       print("Licznik wynosi: "+str(counter))
       if counter_internal % 30 == 0:
          print("Reloading.")
          time.sleep(2)
          driver.close()
          driver = webdriver.Chrome(driver_path, options=options)
          time.sleep(20)
          deepl_url = 'https://www.deepl.com/pl/translator'
          driver.get(deepl_url)
          time.sleep(60)
       lines = ''.join(group)
      #print(counter_file2)
       cstring = "counter"+str(counter)+"end"
       if cstring not in counter_file2:
        counter_internal = counter_internal + 1
        print("---- Nie Znaleziono licznika. Tłumaczę -----")
# Get the input_area 
#        input_css = 'div.lmt__inner_textarea_container textarea'
#        input_area = driver.find_element_by_css_selector(input_css)
#        input_area.clear() 
#        time.sleep(10)
#        input_area.send_keys(lines)
#        time.sleep(30)
#       print(lines)
        
        wprowadz = driver.find_element(By.CLASS_NAME, "lmt__inner_textarea_container")
        area = wprowadz.find_element(By.CLASS_NAME,"lmt__textarea")
        area.send_keys(Keys.CONTROL + "a")
        area.send_keys(Keys.DELETE)
        time.sleep(5)
        area.send_keys(lines)
        time.sleep(15)
# Get the output area
#       out1 = get_output_textarea().get_attribute("value")
        out0 = driver.find_elements(By.CLASS_NAME, "lmt__inner_textarea_container")
        area3 = out0[1].find_element(By.CLASS_NAME,"lmt__textarea")
        out1 =  area3.get_attribute("value")


#       #print(str(out1))
# Get content from clipboard
#       content = clipboard.paste()
        ebookpl.write(out1)
        counter_fileb.write("counter"+str(counter)+"end")
        os.system('cp counterb.txt counter.txt')
#       else:
#         break
       print("-----poza ifem---")

ebookpl.close()
counter_fileb.close()
