import logging
import pytest
import time

import softest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PythonSeleniumproject1.TestFramework.pages.search_flights_results_page import SearchFlightResults
from PythonSeleniumproject1.TestFramework.pages.yatra_launch_page import LaunchPage
from PythonSeleniumproject1.TestFramework.utilities.utils import Utils
# from ddt import ddt,data,unpack
from ddt import ddt,data,unpack,file_data

# business layer of my test case
@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.custome_logger()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()


    # @data(("New Delhi","JFK",'27/03/2024',"1 Stop") , ("BOM","JFK",'28/04/2024',"2 Stop"))
    # @unpack
    # @file_data("../testdata/testdata.json")
    # @file_data("../testdata/testyml.yaml")
    # @data(*Utils.read_data_from_excel("C:\\Users\\pmondal\\PycharmProjects\\pythonProject\\PythonSeleniumproject1\\TestFramework\\testdata\\tdataexcel.xlsx", "Sheet"))
    @data(*Utils.read_data_from_csv("C:\\Users\\pmondal\\PycharmProjects\\pythonProject\\PythonSeleniumproject1\\TestFramework\\testdata\\tdatacsv.csv"))
    @unpack
    def test_search_flights(self, goingfrom, goingto, date, stops):
        # Launching browser and opening the travel website
        # provide going from location
        # lp = LaunchPage(self.driver)
        seach_flight_result=self.lp.searchFlights(goingfrom, goingto, date)


        # lp.departfrom("New Delhi")
        # lp.enterDepartFromLocation("New Delhi")

        # Provide going to location
        # lp.enterGoingToLocation("New York")

        #To resolve syn issues
        # Select the departure date
        # lp.enterDepartureDate('27/03/2024')

        # Click on flight search button
        # lp.clickSearchFlightsButton()

        # To handle dynamic scroll
        self.lp.page_scroll()



        # Select the filter 1 stop
        # sf = SearchFlightResults(self.driver)
        seach_flight_result.filter_flights_by_stop(stops)






        # verify that the filtered resutls show flights having only 1 stop
        # allstops1 = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,
        #                                                                  "//span[contains(text(), 'Non Stop') or contains(text(), '1 Stop') or contains(text(), '2 Stop')]")))
        # print(len(allstops1))

        #sf.wait_for_presence_of_all_elements()
        # allstops1= lp.wait_for_presence_of_all_elements(By.XPATH,"//span[contains(text(), 'Non Stop') or contains(text(), '1 Stop') or contains(text(), '2 Stop')]")
        allstops1 = seach_flight_result.get_search_flight_results()



        # time.sleep(10)
        # allstops = driver.find_element(By.XPATH, "//span[contains(text(), 'Non Stop') or contains(text(), 'cont')]")
        # print(len(allstops1))
        self.log.info(len(allstops1))
        # time.sleep(10)
        # ut = Utils()
        self.ut.assertListitemText(allstops1,"1 Stop")

        # for stop in list:
        #     print("The text is:" + stop.text)
        #     assert stop.text == "1 Stop"
        #     print("assert pass")

# Launch the travel website
# provide going from location
# Provide going to location
# Select the departure date
# Clcik on flight search button
# Select the filter 1 stop
# verify that the filtered resutls show flights having only 1 stop



    # def test_search_flights_2_stop(self):
    #     seach_flight_result=self.lp.searchFlights("New Delhi","JFK",'30/03/2024')
    #     self.lp.page_scroll()
    #     seach_flight_result.filter_flights_by_stop("2 Stop")
    #     allstops1 = seach_flight_result.get_search_flight_results()
    #     self.ut.assertListitemText(allstops1,"2 Stop")

    # Adding the following block at the end of the script

pytest.main(["test_searchflights.py","--html=C:\\Users\\pmondal\\PycharmProjects\\pythonProject\\PythonSeleniumproject1\\TestFramework\\reports\\report.html", "--self-contained-html"])
# pytest.main(["--html=C:\\Users\\pmondal\\PycharmProjects\\pythonProject\\PythonSeleniumproject1\\TestFramework\\reports\\report.html"])