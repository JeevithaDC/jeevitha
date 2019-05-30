
from selenium import webdriver
import time
#import pdb;pdb.set_trace()
browser = webdriver.Chrome()
browser.get('http:www.google.com')
inputElement = browser.find_element_by_name("q")
# type in the search
inputElement.send_keys("GOOGLE")

# submit the form (although google automatically searches now without submitting)
inputElement.submit()
#time.sleep(20)
list_links=browser.find_elements_by_tag_name('a')
count=0
for i in list_links:
    count=1+count
print count

