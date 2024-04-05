import os

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait



# @pytest.fixture(autouse = True)
# def setup(request, browser, url):
#         if browser == "Chrome":
#             driver = webdriver.Chrome()
#
#         elif browser == "Edge":
#             driver = webdriver.Edge()
#
#         # else:
#         #     print("Provide valid browser")
#
#         else:
#             pytest.skip("Unsupported browser: {}".format(browser))
#
#         driver.get(url)
#         driver.maximize_window()
#
#         request.cls.driver = driver
#         # request.cls.wait = wait
#         yield
#         driver.close()
#
#
# def pytest_addoption(parser):
#         parser.addoption("--browser")
#         parser.addoption("--url")
#
# @pytest.fixture(scope="class", autouse = True)
# def browser(request):
#     return request.config.getoption("--browser")
#
# @pytest.fixture(scope="class", autouse = True)
# def url(request):
#     return request.config.getoption("--url")


#
# @pytest.fixture(autouse = True)
# def setup(request, browser):
#         if browser == "Chrome":
#             driver = webdriver.Chrome()
#
#         elif browser == "Edge":
#             driver = webdriver.Edge()
#
#         # else:
#         #     print("Provide valid browser")
#
#         else:
#             pytest.skip("Unsupported browser: {}".format(browser))
#
#         driver.get("https://www.yatra.com/")
#         driver.maximize_window()
#
#         request.cls.driver = driver
#         # request.cls.wait = wait
#         yield
#         driver.close()
#
#
# def pytest_addoption(parser):
#         parser.addoption("--browser")
#
# @pytest.fixture(scope="class", autouse = True)
# def browser(request):
#     return request.config.getoption("--browser")



@pytest.fixture(autouse = True)
def setup(request):
    driver = webdriver.Chrome()
    # wait = WebDriverWait(driver, 20)
    driver.get("https://www.yatra.com/")
    driver.maximize_window()

    request.cls.driver = driver
    # request.cls.wait = wait
    yield
    driver.close()

#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extras", [])
#     if report.when == "call":
#         # always add url to report, specify the specific url,
#         extra.append(pytest_html.extras.url("http://www.rcvacademy.com/"))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#
#             # getting report directory
#             report_directory = os.path.dirname(item.config.option.htmlpath)
#             # file_name = str(int(round(time.time() * 1000))) + ".png"
#             # it is used to get the file name, as per the test case name
#             # this will give the png file will be as per the test case,
#             # say for example this test search flight test has failed the file name
#             # of the screenshot will be containing something similar to that, so this is around that
#             file_name = report.nodeid.replace("::","_")+".png"
#             # then the destination file, where exactly I want to keep my screenshot
#             # I am just joining the report directory which is the directory
#             # of the report and then the file name.
#             destinationFile = os.path.join(report_directory, file_name)
#             # and then saving the screenshot
#             driver.save_screenshot(destinationFile)
#             # adding html, adding a div tag within the report, and I am saying that
#             # add the screenshot there, with this width and height
#             if file_name:
#                 html ='<div><img src ="%s" alt="screenshot" style="width:300px;height=200px" '\
#                       'onclick = "window.open(this.src)" align="right"/></div>'%file_name
#             extra.append(pytest_html.extras.html(html))
#         report.extra =extra

# SCREENSHOT_FOLDER = "C:\\Users\\pmondal\\PycharmProjects\\pythonProject\\PythonSeleniumproject1\\TestFramework\\reports\\"
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         if hasattr(report, "wasxfail"):
#             # Add other extra information as needed
#             extra.append(pytest_html.extras.url("http://www.example.com"))
#             if report.failed:
#                 # Add screenshot only if the htmlpath is set
#                 html_path = item.config.option.htmlpath
#                 if html_path is not None:
#                     screenshot_folder = SCREENSHOT_FOLDER
#                     os.makedirs(screenshot_folder, exist_ok=True)
#                     screenshot_path = os.path.join(screenshot_folder, f"{item.nodeid.replace('::', '_')}.png")
#                     item.cls.driver.save_screenshot(screenshot_path)
#                     extra.append(pytest_html.extras.image(screenshot_path, "Screenshot"))
#     report.extra = extra
#
# # it will change the report tile, search title in guide document
# def pytest_html_report_title(report):
#     report.title = "RCV Academy Automation Report"

