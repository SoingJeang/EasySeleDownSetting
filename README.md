# EasySeleDownSetting
An easily download option for selenium's chrome, firefox and ie

Use:
```

from selenium.webdriver import Ie
from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
#导入自己模块
from easyseleniumdownload.easyseleniumdownload import EasySeleniumDownload

if hasattr(sys, "frozen"):
    file_dir = os.path.dirname(sys.executable)
else:
    file_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

file_path = os.path.join(file_dir,"Chrome\Application\chromedriver.exe")
#设置下载路径（要模拟的路径）
esd = EasySeleniumDownload("C:\Loginer")
#获取已设置的路径
option = esd.generate_download_folder_capability_by_chrome()
driver = Chrome(executable_path=file_path, options=option)
driver.get('https://www.lanzous.com/i6u3mqh')
iframes = driver.find_elements_by_tag_name("iframe")
for iframe in iframes:
    driver.switch_to.frame(iframe)
    driver.find_element_by_partial_link_text("下载").click()
    driver.switch_to.default_content()
    
```
