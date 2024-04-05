import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from PythonSeleniumproject1.TestFramework.base.base_driver import baseDriver
from PythonSeleniumproject1.TestFramework.pages.search_flights_results_page import SearchFlightResults
from PythonSeleniumproject1.TestFramework.utilities.utils import Utils


class LaunchPage(baseDriver):
        log = Utils.custome_logger()
        def __init__(self,driver):
            super().__init__(driver)
            self.driver = driver
            # self.wait = wait


        #Locators
        DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
        GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
        GOING_TO_RESULT_LIST = "//div[@class='viewport']//div[1]/li"
        SELECT_DATE_FEILD = "//input[@id='BE_flight_origin_date']"
        ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD weekend']"
        SEARCH_BUTTON = "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']"


        def getDepartFromFiled(self):
            return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

        def getGoingToFiled(self):
            return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)

        def getGoingToResults(self):
            return self.wait_for_presence_of_all_elements(By.XPATH, self.GOING_TO_RESULT_LIST)

        def getDepartureDateField(self):
            return self.wait_until_element_is_clickable(By.XPATH, self.SELECT_DATE_FEILD)

        def getAllDatesField(self):
            return self.wait_until_element_is_clickable(By.XPATH, self.ALL_DATES)

        def getSearchButton(self):
            return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON)



        def enterDepartFromLocation(self, departLocation):
            time.sleep(4)
            self.getDepartFromFiled().click()
            time.sleep(4)
            self.getDepartFromFiled().send_keys(departLocation)
            time.sleep(4)
            self.getDepartFromFiled().send_keys(Keys.ENTER)
            time.sleep(4)


        def enterGoingToLocation(self,goingtolocation):
            self.getGoingToFiled().send_keys(goingtolocation)
            self.log.info("Typed text into going to field successfully")
            time.sleep(4)

            search_result = self.getGoingToResults()
            print(len(search_result))
            for result in search_result:
                if goingtolocation in result.text:
                    result.click()
                    break
            # time.sleep(4)

        def enterDepartureDate(self,depaturedate):

            self.getDepartureDateField().click()
            element = self.getAllDatesField().find_elements(By.XPATH, self.ALL_DATES)

            for date in element:
                # print(date.text)
                if date.get_attribute("data-date") == depaturedate:
                    date.click()
                    break



        def clickSearchFlightsButton(self):
          self.getSearchButton().click()
          time.sleep(10)


        def searchFlights(self, departlocation, goingtolocation, departuredate):
            self.enterDepartFromLocation(departlocation)
            self.enterGoingToLocation(goingtolocation)
            self.enterDepartureDate(departuredate)
            self.clickSearchFlightsButton()
            search_Flights_result = SearchFlightResults(self.driver) # making object of SF
            return search_Flights_result





        # def departfrom(self,departlocation):
        #     # depart_time = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
        #     depart_time = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='BE_flight_origin_city']")
        #
        #     depart_time.click()
        #     # time.sleep(4)
        #     depart_time.send_keys(departlocation)
        #     time.sleep(4)
        #     depart_time.send_keys(Keys.ENTER)
        #     time.sleep(4)


        # def goingto(self,goingtolocation):
        #     # goint_to = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']")))
        #     goint_to = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        #     goint_to.send_keys(goingtolocation)
        #
        #     time.sleep(4)
        #     # search_result = self.wait.until(
        #     #     EC.presence_of_all_elements_located((By.XPATH, "//div[@class='viewport']//div[1]/li")))
        #
        #     search_result = self.wait_for_presence_of_all_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        #     print(len(search_result))
        #     for result in search_result:
        #         if "New York (JFK)" in result.text:
        #             result.click()
        #             break
        #     # time.sleep(4)


        # def selectdate(self,depaturedate):
        #     # depart_date = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']")))
        #     depart_date = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='BE_flight_origin_date']")
        #     depart_date.click()
        #
        #     # driver.find_element(By.XPATH, "//td[@id='22/02/2024']").click()
        #     # time.sleep(4)
        #     # element = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD weekend']"))).find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class != 'inActiveTD weekend']")
        #
        #     element = self.wait_until_element_is_clickable(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD weekend']").find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class != 'inActiveTD weekend']")
        #
        #     # time.sleep(4)
        #     for date in element:
        #         # print(date.text)
        #         if date.get_attribute("data-date") == depaturedate:
        #             date.click()
        #             break


        # def clicksearch(self):
        #     self.driver.find_element(By.XPATH,"//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").click()
        #     time.sleep(10)