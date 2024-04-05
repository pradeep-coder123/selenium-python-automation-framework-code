import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class baseDriver:
    def __init__(self, driver):
        self.driver = driver



    def page_scroll(self):

        pageLength = self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
        print("The page lenght in one scroll: ",pageLength)

        # pageLength = driver.execute_script("return document.body.scrollHeight;")
        print("Page length:", pageLength)

        match = False
        while(match == False):
            lastCount = pageLength
            print("lastpage length:", lastCount)
            print("Page length is are :", pageLength)
            time.sleep(2)
            lenOfPage = self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
            print("Page length is are :", pageLength)
            print("Page length is are :", lenOfPage)
            if lastCount == pageLength:
                match = True

        print("The page lenght in whole scroll: ",pageLength)
        time.sleep(4)



    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        list_of_elements  = wait.until(EC.presence_of_all_elements_located((locator_type,locator)))
        # print(len(list_of_elements))
        return list_of_elements


    def wait_until_element_is_clickable(self,locator_type,locator):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element



