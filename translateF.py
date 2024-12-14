
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# new set
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Make imports
import time
#import clipboard
import os
from selenium import webdriver
import sys, getopt
from bs4 import BeautifulSoup


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

def chap2text(chap):
    blacklist = [   '[document]',   'noscript', 'header',   'html', 'meta', 'head','input', 'script',   ]
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

#from selenium.webdriver.chrome.options import Options
#options = Options()
#options.headless = True
# Start a Selenium driver 
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#service = Service(executable_path=r'/usr/local/bin/chromedriver')
#options = webdriver.ChromeOptions()
#options.add_argument('--headless')
#options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage')
#options = webdriver.FirefoxOptions()
#options.add_argument("--headless")
#options.add_argument("--disable-gpu")
#driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
#driver = webdriver.Chrome(service=service, options=options)
#time.sleep(3)
#driver.delete_all_cookies()
#driver_path='/usr/local/bin/chromedriver'
#driver = webdriver.Chrome(driver_path, options=options)

from itertools import islice
import pyperclip
import time


#opt = Options()
#opt.headless = True
#driver = webdriver.Firefox(options=opt)
#driver.get("https://deepl.com")



def get_output_textarea():
    output_box = driver.find_elements_by_class_name("lmt__inner_textarea_container")[1]
    return output_box.find_element_by_tag_name("textarea")

# Recipe from https://docs.python.org/2/library/itertools.html
def take(n, iterable):
    return list(islice(iterable, n))
#if __name__ == "__main__":



def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print ('Input file is "', inputfile)
   print ('Output file is "', outputfile)
   blacklist = [   '[document]',   'noscript', 'header',   'html', 'meta', 'head','input', 'script',   ]
   if ".epub" in inputfile:
    e = epub2text(inputfile)
    e2 = ''.join(e)
    e2b = e2.replace("et al.","et al ")
    e3 = splitkeep(e2b, ".")
   elif ".txt" in inputfile:
    e2 = open(inputfile,"r")
    e2a = e2.readlines()
    e2a2 = str(e2a)
    e2b = e2a2.replace("et al.","et al ")
    e3 = splitkeep(e2b, ".")
   ebookpl = open(outputfile,"a+")
   counter_file = open("counter.txt","r")
   counter_file2 = str(counter_file.readlines()).strip()
   counter_fileb = open("counterb.txt","a")
   time.sleep(6)
   counter = 0
   counter_internal = 1
   from selenium import webdriver
   from selenium.webdriver.common.by import By
   from selenium.webdriver.firefox.service import Service
   from webdriver_manager.firefox import GeckoDriverManager
   from selenium.webdriver.support.ui import WebDriverWait
   from selenium.webdriver.support import expected_conditions as EC
   options = webdriver.FirefoxOptions()
   options.add_argument("--headless")
   options.add_argument("--disable-gpu")
   driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
   time.sleep(3)
#  driver.delete_all_cookies()
   url = "https://www.deepl.com/pl/translator#{English}/{Polish}/"
   driver.get(url)
   time.sleep(5)

   for group in chunker(e3, 10):
       counter = counter + 1
       print("Licznik wynosi: "+str(counter))
       if counter_internal % 20 == 0:
          print("Reloading.")
          time.sleep(2)
          driver.close()
         #driver = webdriver.Chrome(driver_path, options=options)
         #driver = webdriver.Chrome(service=service, options=options)
          driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
          time.sleep(20)
          deepl_url = 'https://www.deepl.com/pl/translator#{English}/{Polish}/'
          driver.get(deepl_url)
          time.sleep(60)
       lines = ''.join(group)
       #print(counter_file2)
       cstring = "counter"+str(counter)+"end"
       #if cstring in counter_file2:
       # print("znaleziono"+cstring)
       # break 
       if cstring not in counter_file2:
        counter_internal = counter_internal + 1
        print("---- Nie Znaleziono licznika. Tłumaczę -----")
        area = driver.find_element(By.XPATH, "//div[@aria-labelledby='translation-source-heading']")
        area.send_keys(Keys.CONTROL + "a")
        area.send_keys(Keys.DELETE)
        time.sleep(5)
        area.send_keys(lines)
        time.sleep(15)
        out1 = driver.find_element(By.XPATH, "//div[@aria-labelledby='translation-target-heading']").text
        print(out1)
# Get content from clipboard
#       content = clipboard.paste()
        ebookpl.write(out1)
        counter_fileb.write("counter"+str(counter)+"end")
        os.system('cp counterb.txt counter.txt')
#       else:
#       counter_fileb.close()
   ebookpl.close()
   counter_fileb.close()

if __name__ == "__main__":
   main(sys.argv[1:])
