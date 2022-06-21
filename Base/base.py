import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseDriver():
    def __init__(self,driver):
        # super().__init__(driver)
        self.driver=driver

    def element_be_clickable(self,locator_type,locator_path):
        wait = WebDriverWait(self.driver, 40)
        return wait.until(EC.element_to_be_clickable((locator_type,locator_path)))
    def present_elements(self,locator_type,locator_path):
        wait = WebDriverWait(self.driver, 40)
        return wait.until(EC.presence_of_all_elements_located((locator_type,locator_path)))
    def windowScroll(self):
        pagelength = self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight); varlenght=0,document.body.scrollHeight;return 0,document.body.scrollHeight ")
        match = False
        time.sleep(4)
        while match == False:
            lastpage = pagelength
            pagelength = self.driver.execute_script(
                "window.scrollTo(0,document.body.scrollHeight); varlenght=0,document.body.scrollHeight;return 0,document.body.scrollHeight ")
            if pagelength == lastpage:
                match = True