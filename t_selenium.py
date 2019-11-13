'''
webdriver 3以上各浏览器需要对应的驱动程序

'''

from selenium import webdriver  # 导入库
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

browser = webdriver.Chrome()    # 声明浏览器
# chromedriver.exe如果没有放置在path中包含的目录中，则需要指定驱动位置：
# driver = webdriver.Chrome(executable_path="d:/Chrome/Application/chromedriver")

# browser = webdriver.Firefox()

url = 'https:www.baidu.com'
browser.get(url)                # 打开浏览器预设网址

# print(browser.page_source)      # 打印网页源代码

# 定位单一元素
# find_element_by_name
# find_element_by_id
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector
input_one = browser.find_element_by_id('qrcode')
input = browser.find_element_by_css_selector('#qrcode')

print(input.get_attribute('id'))
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)

# 定位元素集
# find_elements_by_name
# find_elements_by_id
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector
lis = browser.find_elements(By.CSS_SELECTOR,'.s_tab_inner a')

input = browser.find_element_by_css_selector('#kw')
input.send_keys('python 语言')
time.sleep(2)
input.clear()
input.send_keys('selenium 文档')
button = browser.find_element_by_css_selector('#su')
button.click()



url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()

browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')

browser.close()                 # 关闭浏览器