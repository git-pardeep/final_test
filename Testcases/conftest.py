from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.wait import WebDriverWait
import pytest


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://flight.yatra.com/air-search-ui/int2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DEL&originCountry=IN&destination=YTO&destinationCountry=CA&flight_depart_date=03/08/2022&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home&unqvaldesktop=1057754987652")
    # driver.get("https://www.yatra.com/")
    driver.maximize_window()
    # wait = WebDriverWait(driver, 10)
    request.cls.driver = driver
    # request.cls.wait=wait
    yield
    driver.quit()
