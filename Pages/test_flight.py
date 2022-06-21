import logging
import time
import softest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Base.base import BaseDriver
from Utilities.Utils import utils
import logging
class launchpages(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        # self.wait=wait

    ut = utils()
    log = ut.customer_logging(logLevel=logging.DEBUG)
    Depart="//input[@id='BE_flight_origin_city']"
    goint="//input[@id='BE_flight_arrival_city']"
    deparDate="//input[@id='BE_flight_origin_date']"
    search_date="//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    all_filter="//p[@class='font-lightgrey bold'][contains(text(),'1') or contains(text(),'2') or contains(text(),'0')]"
    all_stop="//span[@class='dotted-borderbtm'][contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]"
    # def depart_from(self):
    #     dpr= self.element_be_clickable(By.XPATH,self.Depart)
    #     dpr.click()
    #     dpr.send_keys("Jaipur")
    #     dpr.send_keys(Keys.ENTER)
    # def Going_to(self):
    #     gointo=self.element_be_clickable(By.XPATH,self.goint)
    #     gointo.click()
    #     gointo.send_keys("Mumbai")
    #     gointo.send_keys(Keys.ENTER)
    # def departure_date(self):
    #     self.element_be_clickable(By.XPATH,self.deparDate).click()
    #     all_date=self.present_elements(By.XPATH,self.search_date)
    #     print("length is ",len(all_date))
    #     for date in all_date:
    #         if date.get_attribute("data-date")=="05/07/2022":
    #             print("datecheck",date.text)
    #             date.click()
    #
    #             time.sleep(4)
    #             break
    # def search_button(self):
    #     self.element_be_clickable(By.XPATH,"//input[@value='Search Flights']").click()

    def search_filter(self):
        allcheck=self.present_elements(By.XPATH,self.all_filter)
        # print("first stop",len(allcheck))
        self.log.debug(len(allcheck))
        filer = self.driver.find_element(By.XPATH,"//p[@class='font-lightgrey bold'][normalize-space()='1']")
        filer.click()
        time.sleep(4)
        # for st in allcheck:
        #     if st=='1':
        #         st.click()
        #         break
    def search_stop(self):
        all_stop=self.present_elements(By.XPATH,self.all_stop)
        # print("second stop",len(all_stop))
        self.log.debug(len(all_stop))

        self.ut.assertioncheck(all_stop,"1 Stop")




